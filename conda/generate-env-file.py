# -*- coding: utf-8 -*-
# Generate file environment

# import argparse
# import sys
# import re
# from pathlib import Path


# def parse_argument():

#     parser = argparse.ArgumentParser(
#         description="Convert Template to Conda Environment File"
#     )

#     # Optional Argument
#     parser.add_argument("-t", "--template", help="path to template")
#     parser.add_argument("-d", "--directory", help="path to directory")
#     parser.add_argument("-py", "--python-version", help="python version")
#     parser.add_argument("-nv", "--name-environment", help="name of enviroment")
#     parser.add_argument(
#         "-pc",
#         "--path-conda",
#         default=Path(r"C:\Miniconda3\envs"),
#         help="path of conda environment",
#     )
#     parser.add_argument("-pv", "--path-environment", help="full path of environment")
#     return parser.parse_args()


# def run_no_argument(path_cwd):

#     for file in path_cwd.glob("*-template.yml"):
#         print(f":: FOUND TEMPLATE: {file.name}")
#         name_template = file.stem.split("-template")[0]
#         with open(file, "r") as file_template:
#             python_ver = re.findall("python=(.+)", file_template.read())[0]
#         print(python_ver)

#     ...


# def run_with_argument():
#     ...


# def main():
#     current_path = Path(".")
#     print(f"CURRENT WORKING DIRECTORY: {current_path.absolute()}")

#     args = parse_argument()
#     if len(sys.argv) == 1:  # if no argument given
#         run_no_argument(current_path)
#     if len(sys.argv) != 1:
#         print(args)


# if __name__ == "__main__":
#     main()

from pathlib import Path
import re


def main():
    CURRENT_PATH = Path(".")
    print(f"CURRENT WORKING DIRECTORY: {CURRENT_PATH.absolute()}")

    PYTHON_VER = ["3.7", "3.8"]

    TEMPLATE_PATTERN = "*-template*"
    TEMPLATE_SPLIT = "-template"
    CONDA_PATH = Path(r"C:\Miniconda3\envs")

    SUBS_NAME_ENV = "\{name_environment\}"
    SUBS_PATH_ENV = "\{path_environment\}"
    SUBS_PYTHON_VER = "\{python_version\}"

    for python_version in PYTHON_VER:
        for file in CURRENT_PATH.glob(TEMPLATE_PATTERN):
            print(f":: FOUND TEMPLATE {file.name}")
            name_template = file.stem[1:].split(TEMPLATE_SPLIT)[0]

            # var to subs
            name_environment = f'{name_template}{python_version.replace(".","")}'
            path_environment = CONDA_PATH / name_environment
            file_path = CURRENT_PATH / f"{name_environment}.yml"

            dict_subs = {
                SUBS_NAME_ENV: name_environment,
                SUBS_PATH_ENV: str(path_environment.absolute()).replace("\\", "\\\\"),
                SUBS_PYTHON_VER: python_version,
            }

            with open(file, "r") as input:
                data = input.read()

            # print(data)

            # replace
            for key, value in dict_subs.items():
                data = re.sub(key, value, data)

            # print(data)
            print(f":: CREATING ENVIRONMENT FILE: {file_path.name}")
            with open(file_path, "w") as output:
                output.write(data)


if __name__ == "__main__":
    main()
