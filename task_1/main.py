import argparse
from pathlib import Path
import shutil
from random import random
import re


def parse_args():
    default_source_path = Path("task_1/dest")

    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True, help="Path to the source dir")
    parser.add_argument("--dest", type=Path, default=default_source_path, help="Path to the destination dir")

    return parser.parse_args()

def count_similar_files(dir_path: Path, file_name: str) -> int:
    try:
        counter = 0
        index_pattern = r"\(\d\)"

        for path in dir_path.iterdir():
            current_file_name = path.parts[-1]
            file_name_without_index = re.sub(index_pattern, "", current_file_name)

            if file_name == file_name_without_index:
                counter += 1

        return counter
    except (FileNotFoundError, PermissionError):
        return random() * 100


def move_file_to_folder(
    dest_path: Path,
    folder_name: str,
    file_path: Path
) -> None:
    try:
        if not folder_name:
            folder_name = "files_without_extension"

        dir_path = Path(dest_path) / folder_name
        dir_path.mkdir(parents=True, exist_ok=True)

        file_name = file_path.parts[-1]
        copy_file_path = dir_path / file_name

        if copy_file_path.exists():
            file_index = count_similar_files(dir_path, file_name)
            copy_file_path = dir_path / f"({file_index}){file_name}"

        shutil.copy2(
            file_path,
            copy_file_path
        )
    except FileNotFoundError:
        print(f"The following dest folder path '{dest_path}' is not exists, pls check your input")
        return
    except NotADirectoryError:
        print(f"The following source path '{dest_path}' is not a directory, pls check your input")
        return 
    except PermissionError:
        print(f"Access is denied to the following dest path '{dest_path}'")


def sort_files_by_extension(source_path: Path, dest_path: Path) -> None:
    try:
        for path in source_path.iterdir():
            if path.is_dir():
                sort_files_by_extension(path, dest_path)
            elif path.is_file():
                file_extension = path.suffix[1:]
                move_file_to_folder(dest_path, file_extension, path)
    except FileNotFoundError:
        print(f"The following source path '{source_path}' is not exists, pls check your input")
        return
    except NotADirectoryError:
        print(f"The following source path '{source_path}' is not a directory, pls check your input")
        return 
    except PermissionError:
        print(f"Access is denied to the following source path '{source_path}'")
        return


if __name__ == "__main__":
    args = parse_args()
    source_path = args.source
    dest_path = args.dest

    sort_files_by_extension(source_path, dest_path)