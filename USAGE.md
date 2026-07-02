# Combo-AT Guide 仓库使用说明

> 本文档面向**不熟悉 Sphinx / Read the Docs** 的研发同事，用于讲解本仓库的结构、日常维护方式与中英文发布流程。
> 建议配合本地预览实际操作一遍。

---

## 目录

1. [这个仓库是做什么的](#1-这个仓库是做什么的)
2. [先搞懂 5 个核心概念](#2-先搞懂-5-个核心概念)
3. [目录结构说明](#3-目录结构说明)
4. [站点导航与文档分类](#4-站点导航与文档分类)
5. [文档怎么写](#5-文档怎么写)
6. [新增或修改文档的完整流程](#6-新增或修改文档的完整流程)
7. [英文翻译怎么维护](#7-英文翻译怎么维护)
8. [本地环境搭建与预览](#8-本地环境搭建与预览)
9. [Read the Docs 线上发布](#9-read-the-docs-线上发布)
10. [常见问题排查](#10-常见问题排查)
11. [术语表](#11-术语表)

---

## 1. 这个仓库是做什么的

本仓库是 **安信可 Combo-AT 固件官方文档** 的源码，最终发布为在线网站：

- 介绍 Combo-AT 是什么、如何连接硬件、如何下载与烧录固件
- 提供完整的 **AT 命令集** 参考（基础、Wi-Fi、TCP/IP、MQTT、BLE 等）
- 提供 **AT 命令示例**（配网、OTA、HTTP、MQTT、蓝牙等实操场景）
- 支持 **中文 + 英文** 两个语言版本

### 用一句话理解技术栈

| 组件 | 作用 | 类比 |
| --- | --- | --- |
| **`.rst` 文件** | 文档正文（中文源稿） | Word 文档 |
| **Sphinx** | 把 `.rst` 转成 HTML / PDF | 排版 + 发布工具 |
| **`.po` / `.mo` 文件** | 英文翻译词典 | 中英对照表 |
| **Read the Docs (RTD)** | 云端自动构建并托管网站 | 自动部署平台 |

**你只需要会编辑 `.rst` 和 `.po`，其余构建、部署大多可自动化。**

---

## 2. 先搞懂 5 个核心概念

### 2.1 源语言 vs 翻译语言

- **源语言（中文）**：所有正文写在 `source/docs/**/*.rst` 里，**只维护这一份中文源稿**
- **英文**：不单独维护一套英文 `.rst`，而是维护 `source/locale/en/LC_MESSAGES/**/*.po` 里的 `msgstr`

```
中文源稿 (.rst)  ──gettext 提取──▶  .po 里的 msgid（中文）
                                        │
                                   研发填写 msgstr（英文）
                                        │
                                   编译为 .mo
                                        │
英文站点构建 ◀──────────────────────────┘
```

### 2.2 `.rst` 是什么

ReStructuredText（reST）是 Sphinx 使用的标记语言，类似 Markdown，但语法略有不同。

常见写法：

```rst
章节标题
========

小节标题
--------

``行内代码 / AT 指令``

**加粗**

`链接文字 <https://example.com>`__

.. code-block:: none

   AT+GMR

.. list-table::
   :header-rows: 1

   * - 参数
     - 说明
   * - <ssid>
     - Wi-Fi 名称
```

### 2.3 `.po` 和 `.mo` 是什么

| 文件 | 谁编辑 | 作用 |
| --- | --- | --- |
| `.po` | **人工编辑** | 翻译源文件，含 `msgid`（中文）和 `msgstr`（英文） |
| `.mo` | **机器生成** | `.po` 编译后的二进制，**Sphinx 构建英文站时实际读取的文件** |

> **重要：** 只改 `.po` 不改 `.mo`，英文站可能仍显示旧内容或中文。
> 改完 `.po` 后必须执行 `sphinx-intl build -l en -d source\locale`。

### 2.4 一份 `conf.py` 服务两个语言

`source/conf.py` 通过环境变量 `READTHEDOCS_LANGUAGE` 决定构建哪种语言：

| 环境 | `language` | 读什么内容 |
| --- | --- | --- |
| 未设置（本地默认） | `zh_CN` | 直接读 `.rst` 中文 |
| RTD 中文项目 | `zh_CN` | 直接读 `.rst` 中文 |
| RTD 英文项目 | `en` | 读 `.rst` + `locale/en/**/*.mo` 译文 |

### 2.5 线上是「一个仓库 + 两个 RTD 项目」

- **中文 RTD 项目**：Language = `Simplified Chinese (zh_CN)`
- **英文 RTD 项目**：Language = `English (en)`，导入**同一个 Git 仓库**
- 在主项目里把英文项目 **关联为 Translation**，RTD 会自动提供语言切换

---

## 3. 目录结构说明

```
aithinker-combo-guide/
│
├─ source/                          ← 【文档源目录，日常主要改这里】
│  ├─ conf.py                         Sphinx 配置（语言、主题、i18n、LaTeX）
│  ├─ index.rst                       网站首页（三大入口导航）
│  │
│  ├─ docs/                           【中文正文，按模块分子目录】
│  │  ├─ instruction/                 快速入门（Combo-AT 介绍、硬件连接、固件下载等）
│  │  ├─ command-set/                 AT 命令集（基础、Wi-Fi、TCP/IP、MQTT、BLE 等）
│  │  └─ command-examples/            AT 命令示例（配网、OTA、HTTP、MQTT 等）
│  │
│  ├─ _static/                        图片、Logo、CSS 等静态资源
│  ├─ _templates/                     HTML 模板（一般不用动）
│  │
│  └─ locale/                         【英文翻译文件】
│     └─ en/LC_MESSAGES/              与 docs/ 目录一一对应的 .po / .mo
│        ├─ index.po                  首页翻译
│        └─ docs/.../*.po             各页面翻译
│
├─ docs/requirements.txt              Python 构建依赖（RTD 也用这份）
├─ .readthedocs.yaml                  RTD 云端构建配置
├─ README.md                          仓库简介（快速入口）
└─ USAGE.md                           本文档（详细使用说明）
```

### 3.1 `.rst` 与 `.po` 的对应关系

每个 `source/docs/xxx/yyy.rst` 对应一个翻译文件：

```
source/docs/command-set/Wi-Fi_AT_Commands.rst
    ↕ 一一对应
source/locale/en/LC_MESSAGES/docs/command-set/Wi-Fi_AT_Commands.po
source/locale/en/LC_MESSAGES/docs/command-set/Wi-Fi_AT_Commands.mo
```

当前仓库共有 **25 个** `.rst` 文档 + **1 个** 首页 `index.rst`，对应 **26 个** `.po` 文件。

### 3.2 不要提交到 Git 的内容

已在 `.gitignore` 中忽略：

| 路径/模式 | 说明 |
| --- | --- |
| `build/` | 本地构建输出 |

`.mo` 文件建议由 RTD 构建前自动编译，或本地 `sphinx-intl build` 生成；是否提交 `.mo` 由团队约定（见第 9 节）。

---

## 4. 站点导航与文档分类

### 4.1 首页三大模块

首页 `source/index.rst` 提供三个入口：

| 入口 | 目录 | 说明 |
| --- | --- | --- |
| 快速入门 | `docs/instruction/` | Combo-AT 介绍、硬件连接、固件下载与差异说明 |
| AT 命令集 | `docs/command-set/` | 各类 AT 指令参考手册 |
| AT 命令示例 | `docs/command-examples/` | 典型场景的命令用法演示 |

### 4.2 AT 命令集子目录

`docs/command-set/` 包含：

| 文件 | 内容 |
| --- | --- |
| `AT_Basic_Commands.rst` | 基础 AT 命令 |
| `Wi-Fi_AT_Commands.rst` | Wi-Fi 相关命令 |
| `TCP-IP_AT_Commands.rst` | TCP/IP 相关命令 |
| `HTTP_AT_Commands.rst` | HTTP 相关命令 |
| `MQTT_AT_Commands.rst` | MQTT 相关命令 |
| `BLE_AT_Commands.rst` | 蓝牙低功耗命令 |
| `SNTP_AT_Commands.rst` | SNTP 时间同步命令 |
| `Driver_AT_Commands.rst` | 驱动相关命令 |
| `Granwin_AT_Commands.rst` | 广云物联平台命令 |

### 4.3 AT 命令示例子目录

`docs/command-examples/` 包含：

| 文件 | 内容 |
| --- | --- |
| `Netconfig_AT_Examples.rst` | 配网示例（SmartConfig、Airkiss、Blufi 等） |
| `OTA_AT_Examples.rst` | OTA 升级示例 |
| `TCP-IP_AT_Examples.rst` | TCP/UDP 通信示例 |
| `MQTT_AT_Examples.rst` | MQTT 连接与发布示例 |
| `http_at_examples.rst` | HTTP 请求示例 |
| `bluetooth_le_at_examples.rst` | 蓝牙 LE 通信示例 |
| `granwin_at_examples.rst` | 广云物联平台对接示例 |
| `sleep_at_examples.rst` | 休眠模式示例 |

### 4.4 快速入门子目录

`docs/instruction/` 包含：

| 文件 | 内容 |
| --- | --- |
| `Aithinker_combo-AT.rst` | Combo-AT 固件介绍 |
| `Hardware_connection.rst` | 硬件连接说明 |
| `other/firmware_download.rst` | 固件下载 |
| `other/firmware_differences.rst` | 固件差异说明 |
| `other/error_code_.rst` | AT 命令错误码 |

---

## 5. 文档怎么写

### 5.1 AT 命令参考页常见结构

命令集页面通常包含命令说明、参数表格与示例：

```rst
AT+WJAP：连接 AP
-----------------

设置命令
~~~~~~~~

**命令：**

.. code-block:: none

   AT+WJAP=<ssid>,<password>

**响应：**

.. code-block:: none

   OK

**参数：**

.. list-table::
   :header-rows: 1

   * - 参数
     - 说明
   * - <ssid>
     - Wi-Fi 名称
   * - <password>
     - Wi-Fi 密码
```

### 5.2 常用 reST 语法速查

| 效果 | 写法 |
| --- | --- |
| 行内代码 / 型号 / AT 指令 | ``AT+GMR`` |
| 加粗 | `**加粗文字**` |
| 外链 | `` `链接文字 <https://url>`__ `` |
| 代码块 | `.. code-block:: none` 下一行起缩进 |
| 图片 | `.. figure:: _static/xxx.png` |
| 文档内链接 | `` :doc:`../instruction/other/error_code_` `` |

### 5.3 动图 GIF 与 PDF 兼容

LaTeX/PDF 引擎**不支持 GIF**。本仓库已采用按格式分流引用：

```rst
.. only:: format_html

   .. figure:: ../../_static/example.gif
      :scale: 50 %

.. only:: format_latex

   .. figure:: ../../_static/example.png
      :scale: 50 %
```

- HTML / EPUB：显示 GIF 动图
- PDF：使用同名 PNG（首帧）
- 新增 GIF 时须同时生成 PNG，可用 Pillow 转换首帧

### 5.4 写作注意事项

1. **AT 命令格式保持一致**：命令名、参数占位符（`<ssid>`）不要随意改动
2. **型号、URL、AT 指令**：保持原文，英文翻译时也通常原样保留
3. **不要随意改已有标题**：改标题会导致 `.po` 里 `msgid` 变化，原有英文翻译会失效
4. **图片放 `_static/`**：引用路径写相对路径如 `../../_static/图片名.png`
5. **错误码引用**：使用 `:doc:` 链接到 `error_code_.rst`

---

## 6. 新增或修改文档的完整流程

以下以「在 `command-set/` 下修改 Wi-Fi 命令说明」为例。

### 步骤 1：编辑中文源稿

打开 `source/docs/command-set/Wi-Fi_AT_Commands.rst`，修改或新增内容。

### 步骤 2：本地预览中文效果

```powershell
cd D:\GitHub\aithinker-combo-guide
sphinx-build -b html source build\html
# 浏览器打开 build\html\docs\command-set\Wi-Fi_AT_Commands.html
```

### 步骤 3：更新英文翻译模板

中文源稿变更后，需要刷新 `.po` 文件：

```powershell
sphinx-build -b gettext source build\gettext
sphinx-intl update -p build\gettext -l en -d source\locale
Remove-Item -Recurse -Force build\gettext
```

此时对应 `.po` 会出现新的空 `msgstr` 条目（已有译文因 `gettext_uuid = True` 会保留）。

### 步骤 4：填写英文翻译

用文本编辑器打开对应 `.po`，找到新增条目：

```po
msgid "Wi-Fi 相关 AT 命令"
msgstr ""          ← 在这里填写英文
```

填写示例：

```po
msgid "Wi-Fi 相关 AT 命令"
msgstr "Wi-Fi AT Commands"
```

**翻译规范：**

- 保留 reST 标记、URL、型号、AT 命令字符串
- `msgstr` 不要留空
- `PO-Revision-Date` 使用完整格式：`2026-07-02 00:00+0800`（缺少时分会导致 Sphinx 警告）

### 步骤 5：编译 `.mo` 文件

```powershell
sphinx-intl build -l en -d source\locale
```

### 步骤 6：预览英文效果

```powershell
sphinx-build -b html -D language=en source build\html\en
# 浏览器打开 build\html\en\docs\command-set\Wi-Fi_AT_Commands.html
```

### 步骤 7：提交 Git

```powershell
git add source/docs/command-set/Wi-Fi_AT_Commands.rst
git add source/locale/en/LC_MESSAGES/docs/command-set/Wi-Fi_AT_Commands.po
git commit -m "docs(Wi-Fi): 更新 Wi-Fi AT 命令说明及英文翻译"
git push
```

推送后 RTD 会自动重新构建中英文两个项目。

### 流程图（总览）

```
编辑 .rst（中文）
      │
      ▼
本地预览中文 build\html
      │
      ▼
sphinx-intl update          → 刷新 .po
      │
      ▼
编辑 .po 填写 msgstr（英文）
      │
      ▼
sphinx-intl build -l en     → 生成 .mo
      │
      ▼
本地预览英文 build\html\en
      │
      ▼
git commit & push           → RTD 自动部署
```

---

## 7. 英文翻译怎么维护

### 7.1 `.po` 文件结构说明

```po
#: ../../source/docs/xxx.rst:行号 唯一ID
msgid "中文原文（从 .rst 自动提取）"
msgstr "English translation（人工填写）"
```

- **`msgid`**：不要手动改，由 Sphinx 从 `.rst` 提取
- **`msgstr`**：填英文；留空则英文站显示中文

### 7.2 何时需要更新 `.po`

| 操作 | 是否需要 update |
| --- | --- |
| 新增或修改中文内容 | ✅ 需要 |
| 只改英文翻译 | ❌ 直接改 msgstr 即可 |
| 删除内容 | ✅ update 后 obsolete 条目可清理 |

### 7.3 新增整页文档时

若新建了 `source/docs/新目录/新文件.rst`：

1. 确保已被某个 `index.rst` 的 `toctree` 引用（否则不会出现在导航）
2. 执行 `sphinx-intl update` 自动生成对应 `.po`
3. 翻译并 `sphinx-intl build -l en -d source\locale`

---

## 8. 本地环境搭建与预览

### 8.1 环境要求

- **Python 3.8+**（与 RTD 线上一致，推荐 3.8）
- **Windows**（本仓库命令示例使用 PowerShell）

### 8.2 一次性安装依赖

```powershell
cd D:\GitHub\aithinker-combo-guide
pip install -r docs/requirements.txt
```

主要依赖：

| 包 | 用途 |
| --- | --- |
| Sphinx | 文档构建 |
| sphinx-rtd-theme | 网站主题（与 RTD 线上一致） |
| myst-parser | Markdown 支持（本仓库主要用 .rst） |
| sphinx-intl | 翻译文件管理 |

### 8.3 常用构建命令

```powershell
# 中文 HTML
sphinx-build -b html source build\html

# 编译 .mo + 英文 HTML
sphinx-intl build -l en -d source\locale
sphinx-build -b html -D language=en source build\html\en

# 模拟 RTD 英文项目（环境变量方式）
$env:READTHEDOCS_LANGUAGE='en'
sphinx-build -b html source build\html_en_test
Remove-Item env:READTHEDOCS_LANGUAGE

# LaTeX / PDF 源（验证 GIF 未进入 PDF）
sphinx-build -b latex source build\latex
Select-String -Path build\latex\*.tex -Pattern "\.gif"   # 期望：无输出
```

构建完成后用浏览器打开：

| 语言 | 路径 |
| --- | --- |
| 中文 | `build\html\index.html` |
| 英文 | `build\html\en\index.html` |

### 8.4 更新翻译模板（中文源稿变更后）

```powershell
sphinx-build -b gettext source build\gettext
sphinx-intl update -p build\gettext -l en -d source\locale
Remove-Item -Recurse -Force build\gettext
sphinx-intl build -l en -d source\locale
```

---

## 9. Read the Docs 线上发布

### 9.1 架构说明

```
GitHub 仓库 (aithinker-combo-guide)
        │
        ├─▶ RTD 项目 A（中文，Language = zh_CN）
        │       构建 URL: /zh-cn/latest/
        │
        └─▶ RTD 项目 B（英文，Language = en）
                构建 URL: /en/latest/
                读取 locale/en/*.mo 显示英文
```

两个项目导入**同一个仓库**，通过 **Translations 关联** 后，页面右下角会出现语言切换。

### 9.2 首次配置 checklist

**中文主项目：**

1. RTD 导入 GitHub 仓库
2. `Admin → Settings → Language` → **Simplified Chinese (zh_CN)**
3. 确认使用 `.readthedocs.yaml` 配置

**英文项目：**

1. `Dashboard → Add project` → 导入**同一仓库**
2. `Admin → Settings → Language` → **English (en)**
3. 回到**中文主项目** → `Admin → Translations → Add translation` → 选择英文项目

### 9.3 `.readthedocs.yaml` 关键配置说明

```yaml
formats: all                   # 产出 PDF / EPUB / HTMLZIP

build:
  os: ubuntu-22.04
  tools:
    python: "3.8"

sphinx:
  configuration: source/conf.py

python:
  install:
    - requirements: docs/requirements.txt
```

**英文构建前编译 `.mo`（已配置）：**

RTD 不会自动把 `.po` 编译为 `.mo`，`.readthedocs.yaml` 已在 `build.jobs.pre_build` 中执行：

```yaml
build:
  jobs:
    pre_build:
      - sphinx-intl build -l en -d source/locale
```

该步骤在 `pip install` 之后、Sphinx 构建之前运行，中英文两个 RTD 项目均会执行（对中文项目无副作用）。

### 9.4 日常发布

**正常流程：改完代码 → `git push` → RTD 自动构建**，无需手动点构建（Webhook 已配置时）。

可在 RTD 项目页查看 Build 日志排查失败原因。

### 9.5 关于 PDF

本仓库已启用 PDF 构建（`formats: all`），并做了以下适配：

- 使用 `xelatex` 引擎 + `xeCJK` 支持中文
- GIF 动图在 PDF 中替换为同名 PNG 首帧（见第 5.3 节）
- 本地可用 `sphinx-build -b latex` 验证 `.tex` 中不含 `.gif` 引用

---

## 10. 常见问题排查

### Q1：英文站仍显示中文

| 可能原因 | 解决方法 |
| --- | --- |
| 只改了 `.po` 没编译 `.mo` | 执行 `sphinx-intl build -l en -d source\locale` |
| `msgstr` 为空 | 打开对应 `.po` 填写英文 |
| RTD 英文项目 Language 未设为 `en` | 检查 RTD Admin → Settings |
| RTD 未执行 pre-build 编译 | 在 `.readthedocs.yaml` 添加 `sphinx-intl build` |

### Q2：构建报 `time data '2026-07-02' does not match format`

`.po` 文件头 `PO-Revision-Date` 格式不正确，须包含时分：

```
PO-Revision-Date: 2026-07-02 00:00+0800
```

不能写成 `PO-Revision-Date: 2026-07-02`。

### Q3：RTD PDF 构建失败（GIF 相关）

日志出现 `Error: /undefined in GIF89a` 或 Ghostscript 错误，说明 PDF 仍引用了 GIF：

1. 为 GIF 生成同名 PNG（首帧）
2. 在 `.rst` 中用 `.. only:: format_html` / `.. only:: format_latex` 分流引用
3. 本地验证：`Select-String -Path build\latex\*.tex -Pattern "\.gif"` 应无输出

### Q4：新增了 `.rst` 但导航里看不到

检查是否被父级 `index.rst` 的 `toctree` 引用：

```rst
.. toctree::
   :maxdepth: 1
   :glob:

   *
```

### Q5：构建有很多 WARNING 但成功了

部分历史页面存在标题下划线长度、重复锚点等警告，**通常不影响 HTML 发布**。若出现 **ERROR**（红色），则需要修复后再发布。

### Q6：`unsupported theme option 'display_version'`

新版 `sphinx-rtd-theme` 已移除 `display_version` 选项，可从 `conf.py` 的 `html_theme_options` 中删除（不影响功能）。

---

## 11. 术语表

| 术语 | 解释 |
| --- | --- |
| **Combo-AT** | 安信可自研 Combo 固件 AT 指令集 |
| **Sphinx** | Python 文档生成工具，把 `.rst` 转成 HTML / PDF |
| **reST / RST** | reStructuredText，Sphinx 使用的标记语言 |
| **Read the Docs (RTD)** | 免费文档托管平台，连接 Git 自动构建 |
| **gettext / i18n** | 国际化机制，实现多语言 |
| **`.pot`** | 翻译模板（从 `.rst` 提取，一般不提交 Git） |
| **`.po`** | 翻译编辑文件（人工维护） |
| **`.mo`** | 编译后的翻译文件（构建时读取） |
| **msgid** | `.po` 中的源语言字符串（中文） |
| **msgstr** | `.po` 中的译文（英文） |
| **toctree** | Sphinx 目录树指令，控制左侧导航 |
| **sphinx-intl** | Sphinx 国际化辅助工具 |
| **READTHEDOCS_LANGUAGE** | RTD 注入的环境变量，值为 `en` 或 `zh_CN` 等 |
