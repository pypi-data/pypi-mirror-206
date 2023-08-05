import yaml
from pathlib import Path
from typing import Union
from otoe.exceptions import (
    OtoeFileNotFoundError,
    OtoeEmptyMarkdownError,
    OtoeEmptyYamlError,
    OtoeValueError,
)
from otoe.config import TRIGGER, SEPARATOR


class MarkDownParser:
    def __init__(self, file: Union[str, Path]):
        file_path = Path(file)
        if not file_path.exists():
            raise OtoeFileNotFoundError(f'File {file} not found')
        self.file_path = file_path
        self.data: str = self.load()

    def load(self):
        with open(self.file_path, 'r') as f:
            data = f.read()
        return data

    def parse_md_part(self, replace_text: str):
        parsed_text = replace_text.strip()
        if not parsed_text:
            raise OtoeEmptyMarkdownError(
                f'File {self.file_path} has empty markdown part'
            )
        return parsed_text

    def parse_yaml_part(self, yaml_str: str) -> dict:
        yaml_str = yaml_str.replace('\t', ' ' * 4).strip()

        if not yaml_str:
            raise OtoeEmptyYamlError(f'File {self.file_path} has empty yaml part')
        print(yaml_str)
        yaml_dict = yaml.load(yaml_str, Loader=yaml.FullLoader)
        if TRIGGER not in yaml_dict:
            raise OtoeValueError(f'File {self.file_path} has no trigger')
        return yaml_dict

    def parse(self):
        splitted_data = self.data.split(SEPARATOR)
        if len(splitted_data) > 2:
            splitted_data = [SEPARATOR.join(splitted_data[:-1]), splitted_data[-1]]
        elif len(splitted_data) < 2:
            raise OtoeValueError(f'File {self.file_path} has no separator')
        replace_text = splitted_data[0]
        yaml_text = splitted_data[1]
        match = self.parse_yaml_part(yaml_text)
        match['replace'] = self.parse_md_part(replace_text)
        return match
