import subprocess
import argparse
import os
import shutil


def run_command(command, cwd=None):
    result = subprocess.run(command, shell=True, cwd=cwd)
    if result.returncode != 0:
        print(f"Error executing {command}")
        exit(result.returncode)


def make_html(version, lang):
    print(f"Building HTML documentation for version {version}, language: {lang} ...")
    if version:
        os.environ['SIFLI_DOC_VERSION'] = version
    run_command(f'sphinx-build -M html source/{lang} build/{lang} -D language={lang} -j 8')


def main(version, lang):
    make_html(version, lang)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate documentation for specified board.')
    parser.add_argument('--lang', choices=['en', 'zh_CN'], default='zh_CN', help='Specify language(en or zh_CN)')
    parser.add_argument('--version', type=str, help='Specify version')
    args = parser.parse_args()

    main(args.version, args.lang)