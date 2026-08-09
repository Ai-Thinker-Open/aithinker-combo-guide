[![English](https://img.shields.io/badge/English-Document-green)](ARCHITECTURE.md)

# 架构说明

## 总览

项目使用一套 reStructuredText 源文件和 gettext 翻译目录，发布同一个 Sphinx 站点的中文与英文版本。

```text
.readthedocs.yaml
        |
        +--> docs/requirements.txt
        |
        +--> sphinx-intl --> source/locale/en/LC_MESSAGES/*.po --> *.mo
        |
        +--> source/conf.py + source/index.rst
                           |
                           +--> instruction
                           +--> command-set
                           +--> command-examples
                           |
                           +--> 中英文 HTML、LaTeX、EPUB、HTML ZIP
```

## 组件职责

- `source/index.rst`：维护顶层导航。
- `source/docs/`：维护中文源内容，分为使用入门、命令参考和命令示例。
- `source/locale/en/LC_MESSAGES/`：维护英文 gettext 目录；每个源 `.rst` 都有对应的 `.po` 和已编译 `.mo`。
- `source/_static/` 以及文档同级图片：保存文档引用的静态资源。
- `source/conf.py`：默认选择 `zh_CN`，并通过 `READTHEDOCS_LANGUAGE` 或 `-D language=en` 构建英文站点。
- `.readthedocs.yaml`：连接 Read the Docs 托管构建，并请求全部支持的输出格式。

## 翻译流程

1. 维护者修改中文 `.rst` 源文档。
2. Sphinx 将可翻译内容提取为 gettext 模板。
3. `sphinx-intl` 更新英文 `.po` 文件。
4. 翻译人员补全 `msgstr`。
5. `sphinx-intl build` 将 `.po` 编译为 `.mo`。
6. Sphinx 使用同一文档树并指定 `language=en`，生成英文站点。

## 依赖设计

为兼容托管环境的 Python 3.8，Sphinx 固定为 4.5；`sphinxcontrib-*` 也固定到兼容 Sphinx 4 的版本。这样全新安装时不会误选要求 Sphinx 5 以上版本的新扩展。

## 维护约束

- 保持 `.rst`、`.po` 和 `.mo` 的路径一一对应。
- 修改导航、链接、替换项或翻译后，必须在“警告视为错误”的模式下同时构建两种语言。
- 文档成功渲染不等于命令已在某个固件或硬件版本上验证通过。
