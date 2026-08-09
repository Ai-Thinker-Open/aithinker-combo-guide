[![English](https://img.shields.io/badge/English-Document-green)](CODE_ENTRY.md)

# 代码与文档入口

本仓库是文档项目，不是固件 SDK。它的运行产物是由 Sphinx 生成的文档站点，因此下面的“入口”指文档构建入口和页面导航入口。

## 主要入口

- `source/index.rst`：Sphinx 根文档，也是站点首页。
- `source/conf.py`：配置主题、默认语言、gettext 翻译目录、链接检查和 LaTeX 输出。
- `.readthedocs.yaml`：托管构建入口；指定 Python 3.8、安装 `docs/requirements.txt`，并在 Sphinx 构建前编译英文翻译。
- `docs/requirements.txt`：保存可复现的构建依赖版本。

## 内容入口

`source/index.rst` 中的根 `toctree` 将读者引导到三组内容：

1. `source/docs/instruction/index.rst`：产品介绍、硬件连接、固件下载和错误码。
2. `source/docs/command-set/index.rst`：AT 命令参考。
3. `source/docs/command-examples/index.rst`：AT 命令实际示例。

## 本地构建入口

在仓库根目录安装锁定依赖、编译翻译目录，再调用 Sphinx：

```powershell
python -m pip install -r docs\requirements.txt
sphinx-intl build -l en -d source\locale
sphinx-build -W --keep-going -b html source build\html\zh
sphinx-build -W --keep-going -b html -D language=en source build\html\en
```

生成的入口页面分别是 `build/html/zh/index.html` 和 `build/html/en/index.html`。

## 验证边界

本仓库说明 AT 固件行为，但不包含固件实现和设备测试框架。因此入口审查验证的是文档构建及导航路径，不代表已在真实硬件上执行 AT 命令。
