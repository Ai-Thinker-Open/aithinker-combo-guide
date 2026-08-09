[![English](https://img.shields.io/badge/English-Document-green)](VALIDATION.md)

# 验证证据

验证在临时副本和全新创建的虚拟环境中执行。证据绑定到实现提交 `340b8943106bdc3c248f40748ee817c08ceba881`。

## 环境

- Windows 主机，Python 3.12.13。
- Sphinx 4.5.0，以及 `docs/requirements.txt` 中锁定的全部依赖。
- 使用全新依赖安装，没有复用仓库内的既有虚拟环境。

## 结果

| 检查项 | 结果 |
| --- | --- |
| 源文件与翻译目录对应 | 26 个 `.rst`、26 个 `.po`、26 个 `.mo` |
| 翻译覆盖率 | 当前 1,425 条消息都有非空翻译；缺失 0、模糊翻译 0、UTF-8 BOM 文件 0 |
| 翻译目录编译 | 26 个目录全部通过，0 警告 |
| 中文 HTML 严格构建 | 通过，28 个页面，0 警告/错误 |
| 英文 HTML 严格构建 | 通过，28 个页面，0 警告/错误 |
| LaTeX 源文件严格构建 | 通过，生成 1 个 `.tex`，0 警告/错误，无 GIF 引用 |
| 链接严格检查 | 通过，0 警告/错误 |

严格构建使用 `-W --keep-going`，因此任何 Sphinx 警告都会使命令失败。

## 复现方法

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r docs\requirements.txt
.\.venv\Scripts\sphinx-intl build -l en -d source\locale
.\.venv\Scripts\sphinx-build -W --keep-going -b html source build\html\zh
.\.venv\Scripts\sphinx-build -W --keep-going -b html -D language=en source build\html\en
.\.venv\Scripts\sphinx-build -W --keep-going -b latex source build\latex
.\.venv\Scripts\sphinx-build -W --keep-going -b linkcheck source build\linkcheck
.\.venv\Scripts\python tools\validate_repository.py
```

## 明确边界

- Windows 主机和 WSL 都没有 XeLaTeX，因此已验证 Sphinx 生成的 LaTeX 源文件，但没有生成最终 PDF 文件。
- 没有可用的实体模组和固件镜像，未执行 AT 命令和硬件操作步骤。
- `source/conf.py` 仅针对三个由站点生成的首页卡片 HTML 路径和硬件引脚文字 `RX:PA0` 设置了链接检查忽略项；其他受检链接全部通过。

详细命令记录位于 `validation-logs/Sphinx-validation.log`。
