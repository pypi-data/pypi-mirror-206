# Copyright (C) 2023 twyleg
import argparse
import glob
import os.path
import pathlib

from pathlib import Path
from ausbildungsnachweise_utils import processor

FILE_DIR = Path().absolute()
INPUT_DIR = "resources"
INPUT_SUFFIX = ".xml"
OUTPUT_DIR = "output"
OUTPUT_SUFFIX = ".pdf"


def start():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", nargs='?', default=INPUT_DIR)
    parser.add_argument("output_dir", nargs='?', default=OUTPUT_DIR)
    args = parser.parse_args()

    print(Path().absolute())
    print(Path(__file__).parent)

    if Path(FILE_DIR, args.input_dir).is_dir() and Path(FILE_DIR, args.output_dir).is_dir():
        get_new_files(args.input_dir, args.output_dir)


def get_new_files(input_dir, output_dir):
    input_files = set((f.stem for f in Path(FILE_DIR, input_dir).glob("*" + INPUT_SUFFIX) if f.is_file()))
    output_files = set((f.stem for f in Path(FILE_DIR, output_dir).glob("*" + OUTPUT_SUFFIX) if f.is_file()))

    for i in input_files:
        exist = False
        for o in output_files:
            if i == o:
                exist = True
                compare_m_time(input_dir, output_dir, i, o)
                break

        if not exist:
            create_documents(input_dir, output_dir, set_file_extensions(i))


def compare_m_time(input_dir, output_dir, input_file, output_file):
    input_file_path = Path(FILE_DIR, input_dir, input_file + INPUT_SUFFIX)
    output_file_path = Path(FILE_DIR, output_dir, output_file + OUTPUT_SUFFIX)

    if os.path.getmtime(input_file_path) > os.path.getmtime(output_file_path):
        create_documents(input_dir, output_dir, set_file_extensions(input_file))


def set_file_extensions(input_file):
    file_names = (input_file + INPUT_SUFFIX, input_file + '.docx', input_file + OUTPUT_SUFFIX, input_file + '_signed.pdf')
    return file_names


def create_documents(input_dir, output_dir, file_name):
    processor.fill_template(FILE_DIR / input_dir / file_name[0], FILE_DIR / output_dir / file_name[1])

    processor.convert_docx_to_pdf(FILE_DIR / output_dir / file_name[1], FILE_DIR / str(output_dir + '/'))

    processor.sign_pdf(FILE_DIR / output_dir / file_name[2], FILE_DIR / output_dir / file_name[3])


if __name__ == "__main__":
    start()
