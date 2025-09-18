# How to build the document

## Install toolchain
1. Install Python 3.x
1. Execute `pip install -r requirements.txt` in command line under the `docs` folder. It would install all modules needed by the document building
1. Execute `pip install https://github.com/OpenSiFli/shibuya-sifli/releases/download/2024.12.21%2Bsifli.2/shibuya-2024.12.21+sifli.2-py3-none-any.whl`

## Build the document
```shell
python generate_docs.py --lang zh_CN --version latest
```


