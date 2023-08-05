import os
import argparse

from otoe.dialogs import ensure_ready
from otoe.obsidian import ObsidianParser


def main():
    ensure_ready()
    md_dir = os.getenv('MD_DIR')
    if not md_dir:
        raise ValueError('MD_DIR not set')

    parser = argparse.ArgumentParser(description='Parse Obsidian markdown files')
    parser.add_argument(
        '--per-project',
        action='store_true',
        help='Generate a yaml file per project',
        default=True,
    )
    args = parser.parse_args()
    obsidian_parser = ObsidianParser(md_dir, args.per_project)
    matches = obsidian_parser.generate_matches()
    obsidian_parser.write_yamls(matches)
