# `docs.sifl.com/projects`文档模板

## Install toolchain
1. Install Python 3.x
1. Execute `pip install -r requirements.txt` in command line. It would install all modules needed by the document building except theme.
1. Execute `pip install https://github.com/OpenSiFli/shibuya-sifli/releases/download/2024.12.21%2Bsifli.2/shibuya-2024.12.21+sifli.2-py3-none-any.whl` to install theme

## Build the document
```shell
python generate_docs.py --lang zh_CN --version latest
```

`--lang`配置生成文档的语言，`zh_CN`为中文，`en`为英文，缺省为中文。`--version`配置版本号, 不配置则为`latest`。CI编译时会自动获取标签作为版本号

双击`build/zh_CN/html/index.html`可以打开生成的中文文档。

点击[链接]((https://docs.sifli.com/projects/doc-template/latest/zh_CN/index.html))浏览网站效果


## 定制
### 项目名称
项目配置文件位于`source/en/conf.py`和`source/zh_CN/conf.py`，分别对应英文版和中文版

把`conf.py`里的`project`变量值由`foo`改为实际项目的名字即可修改项目名称

### 部署的网站路径
文件`.github\workflows\build-docs.yml`为github的`Actions`配置文件，修改其中`PROJ_NAME`环境变量即可修改文档的部署地址，如把`PROJ_NAME`由`doc-template`改为`test-doc`，部署的文档网址就是`docs.sifli.com/projects/test-doc`，包含版本号和语言的网站路径为
`docs.sifli.com/projects/test-doc/latest/en`和`docs.sifli.com/projects/test-doc/latest/zh_CN`

提交后会自动触发文档的编译，没有标签的节点会以`latest`版本编译，有标签的节点则以标签名称为版本号编译。

### 版本号
根目录下的`version.json`为版本号列表，在其中添加需要在版本下拉框中选择的版本号，同时还支持分支的最新节点版本，由`"type": "branch"`来指定，类似主分支的latest版本，他表示某个分支的最新版本。

如果不需要版本选择框，可以把`conf.py`里`html_context`字典中的`versions`变量删除

### 多语言
如果不需要配置选择语言，可以把`conf.py`里`html_context`字典中的`languages`变量删除