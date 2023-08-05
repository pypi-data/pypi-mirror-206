import yaml
from typing import Optional, Union
from collections import defaultdict
from pathlib import Path

from otoe.parsers import MarkDownParser
from otoe.exceptions import (
    OtoeFileNotFoundError,
    OtoeNoMatchesError,
)


class ObsidianParser:
    """
    Parse Obsidian markdown files
    md_dir: directory where the markdown files are located
    md_dir can also contain directories with markdown files
    """

    def __init__(
        self,
        md_dir: Union[str, Path],
        target_dir: Optional[Union[str, Path]] = None,
        per_project: bool = True,
    ):
        self.md_dir_path = Path(md_dir)
        self.check_md_dir()

        if not target_dir:
            target_dir = self.md_dir_path / 'yamls'
        self.target_dir_path = Path(target_dir)
        self.check_target_dir()
        self.target_dir_path.mkdir()

        self.parser = MarkDownParser
        self.per_project = per_project

    def check_md_dir(self):
        if not self.md_dir_path.exists():
            raise OtoeFileNotFoundError(f'Directory {self.md_dir_path} does not exist')

    def check_target_dir(self):
        if self.target_dir_path.exists():
            raise FileExistsError(f'Directory {self.target_dir_path} already exists')

    def get_md_files(self) -> dict[str, list[Path]]:
        files_by_dir = defaultdict(list)
        for file in self.md_dir_path.iterdir():
            print(file)
            if file.is_dir():
                files = [f for f in file.iterdir() if f.is_file() and f.suffix == '.md']
                if files:
                    files_by_dir[file.name] = files
            elif file.suffix == '.md':
                files_by_dir['base'].append(file)
        return files_by_dir

    def parse_md_file(self, file: Path) -> dict:
        return self.parser(file).parse()

    def generate_matches(self) -> dict:
        matches = defaultdict(list)
        files_by_dir = self.get_md_files()
        for dir_name, files in files_by_dir.items():
            for file in files:
                try:
                    match = self.parse_md_file(file)
                    matches[dir_name].append(match)
                except Exception as e:
                    print(f'Skipping file {file.name} due to the error: {e}')
        if not matches:
            raise OtoeNoMatchesError(
                f'Cannot construct any match from {self.md_dir_path}'
            )
        return matches

    def write_yamls(self, matches: dict[str, list[dict]]):
        matches_to_write: dict[str, list[dict]] = (
            matches
            if self.per_project
            else {
                'base': [
                    match
                    for project_matches in matches.values()
                    for match in project_matches
                ]
            }
        )

        for file_name, project_matches in matches_to_write.items():
            file_path = self.target_dir_path / f'{file_name}.yml'
            with open(file_path, 'w') as f:
                yaml.dump(
                    {'matches': project_matches},
                    f,
                    encoding='utf-8',
                    allow_unicode=True,
                )
            print(f'Written {len(project_matches)} matches to {file_name}.yaml')
            print(f'File {file_path} written')

