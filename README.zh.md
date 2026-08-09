[![English](https://img.shields.io/badge/English-README-green)](README.md)

# Combo-AT Guide

安信可 **Combo-AT 固件** 官方文档站点，基于 [Sphinx](https://www.sphinx-doc.org/) + [sphinx-rtd-theme](https://sphinx-rtd-theme.readthedocs.io/) 构建，托管于 [Read the Docs](https://readthedocs.org/)。

文档涵盖 Combo-AT 指令说明、硬件连接、固件下载与 AT 命令示例，支持 **中英文双语**：以简体中文为源语言（`source/docs/**/*.rst`），英文通过 `.po` 翻译文件（`source/locale/en/`）生成，采用 RTD 官方「单仓库 + 双项目关联」方案。

---

## 快速开始

```powershell
# 1. 安装依赖（一次性）
pip install -r docs/requirements.txt

# 2. 编译英文翻译并构建预览
sphinx-intl build -l en -d source\locale
sphinx-build -b html source build\html
sphinx-build -b html -D language=en source build\html\en

# 3. 浏览器打开
#    中文：build\html\index.html
#    英文：build\html\en\index.html
```

---

## 详细使用说明

**给部门同事的内部培训文档（推荐从这里开始）：**

👉 **[USAGE.zh.md](./USAGE.zh.md)** — 含目录结构、文档写作规范、翻译流程、RTD 部署、PDF 构建、常见问题排查等完整说明。

---

## 目录结构（简表）

```
aithinker-combo-guide/
├─ source/
│  ├─ conf.py                 # Sphinx 配置（i18n、主题、LaTeX）
│  ├─ index.rst               # 网站首页
│  ├─ docs/                   # 中文正文（.rst）
│  │  ├─ instruction/         # 快速入门
│  │  ├─ command-set/         # AT 命令集
│  │  └─ command-examples/    # AT 命令示例
│  ├─ _static/                # 图片等静态资源（含 GIF/PNG）
│  └─ locale/en/LC_MESSAGES/  # 英文翻译（.po / .mo）
├─ docs/requirements.txt      # Python 构建依赖
├─ .readthedocs.yaml          # RTD 构建配置
├─ README.md                  # 英文快速入口
├─ README.zh.md               # 本文件（中文快速入口）
├─ USAGE.md                   # 英文详细使用说明
└─ USAGE.zh.md                # 中文详细使用说明（培训用）
```

---

## 日常维护（四步）

```
1. 编辑 source/docs/.../*.rst（中文）
2. 更新 .po → 填写英文 msgstr → sphinx-intl build -l en -d source\locale
3. 本地预览中英文 HTML（可选验证 PDF：sphinx-build -b latex source build\latex）
4. git commit & push → RTD 自动部署
```

---

## Read the Docs 部署要点

| 项目 | Language 设置 |
|------|---------------|
| 中文主项目 | Simplified Chinese (zh_CN) |
| 英文项目（同一仓库） | English (en) |

在主项目 `Admin → Translations` 中关联英文项目后，站点右下角会出现语言切换。

> **PDF 构建**：`.readthedocs.yaml` 已启用 `formats: all`。动图 GIF 在 HTML 中保留，PDF 使用同名 PNG（首帧），详见 [USAGE.zh.md](./USAGE.zh.md)。

## 技术证据

- [代码入口](docs/CODE_ENTRY.zh.md)
- [架构说明](docs/ARCHITECTURE.zh.md)
- [验证记录](docs/VALIDATION.zh.md)

---

## 联系我们

1. 样品购买：<https://anxinke.taobao.com>
2. 样品资料：<https://docs.ai-thinker.com>
3. 商务合作：0755-29162996
4. 公司地址：深圳市宝安区西乡固戍华丰智慧创新港 C 栋 403~405、408~410
