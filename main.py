import math
import re

import tqdm as tqdm

FILE_SIZE_UNITS = ('B', 'KB', 'MB', 'GB')  # decimal ones, not binary ones (i.e., not the ones with -bi like mebibytes)

REPO_FILE_SIZES_FILE_PATH = 'oppd-dataset-file-sizes.txt'  # file generated with `git lfs ls-files -s > <output-file>` after LFS repo was cloned (NB: you only need LFS pointer files to compute sizes of actual LFS files)
FOLDER = 'DATA/images_plants'  # folder inside LFS repo to compute size of. Set to '' for computing entire repo size.
OUTPUT_UNIT_BASE_POWER = 2  # set to 2 for outputting size in KiB/MiB/GiB and to 10 for KB/MB/GB
assert OUTPUT_UNIT_BASE_POWER in (2, 10)


def get_size_bytes(lines: list) -> int:
    total_size_in_bytes: int = 0
    for line in tqdm.tqdm(lines):
        file_size_string = re.findall(r'\(.*?\)', line)[-1]
        file_size, size_unit = file_size_string[1:-1].split()
        file_size: float = float(file_size)
        file_size_in_bytes: int = file_size * 1000 ** FILE_SIZE_UNITS.index(size_unit)
        total_size_in_bytes += file_size_in_bytes
    return total_size_in_bytes


def read_lines(file_path: str, folder: str = None) -> list:
    """
    Reads lines from a given file produced by `git lfs ls-files -s > <output-file>`. If a folder name is given,
    only keeps the lines that correspond to that folder.
    """
    with open(file_path) as f:
        lines = f.read().split('\n')
    if lines[-1] == '':
        lines = lines[:-1]
    if folder is not None and folder != '':
        lines = [line for line in lines if line.split(' ')[2].startswith(folder)]
        if not lines:
            raise Exception(f"no lines for folder '{folder}' found")
    return lines


def main():
    total_size_in_bytes = get_size_bytes(read_lines(REPO_FILE_SIZES_FILE_PATH, FOLDER))
    filler = 'repo' if FOLDER == '' else f"folder '{FOLDER}'"
    # print out repo/folder size with optimal file size unit
    powers_and_units = ((30, 'GiB'), (20, 'MiB'), (10, 'KiB')) if OUTPUT_UNIT_BASE_POWER == 2 else ((9, 'GB'), (6, 'MB'), (3, 'KB'))
    for power, unit in powers_and_units:
        total_size = total_size_in_bytes / OUTPUT_UNIT_BASE_POWER ** power
        if math.floor(total_size) != 0:
            output_unit = unit
            break
    print(f'total {filler} size:', round(total_size, 2), output_unit)


if __name__ == '__main__':
    main()
