这里是一份 Pandoc 实战速查表 (Cheat Sheet)。

### 1\. 核心语法 (Core)

基本逻辑：`pandoc [输入文件] [参数] -o [输出文件]`

| 标志 | 全称 | 作用 |
| :--- | :--- | :--- |
| `-o` | `--output` | 指定输出文件名 (根据后缀自动推断格式) |
| `-f` / `-r` | `--from` / `--read` | 指定输入格式 (通常可省略，自动检测) |
| `-t` / `-w` | `--to` / `--write` | 指定输出格式 (通常可省略，自动检测) |
| `-s` | `--standalone` | 生成完整文档 (包含 head/body)，转 HTML/LaTeX 必加 |

-----

### 2\. 办公文档转换 (Office)

#### Markdown 转 Word (最常用)

```bash
# 基础转换
pandoc report.md -o report.docx

# 进阶：使用自定义样式模板 (先改好一个 ref.docx 的样式)
pandoc report.md --reference-doc=ref.docx -o report.docx
```

#### Word 转 Markdown (逆向提取)

```bash
# 基础转换
pandoc source.docx -f docx -t markdown -o source.md

# 进阶：提取 Word 中的图片到本地 media 文件夹
pandoc source.docx -t markdown --extract-media=./media -o source.md
```

-----

### 3\. PDF 生成 (解决中文乱码)

**注意**：必须安装 LaTeX 环境 (如 TeXLive/MacTeX/MiKTeX)。

```bash
# 标准中文 PDF 生成命令
pandoc input.md -o output.pdf \
  --pdf-engine=xelatex \
  -V CJKmainfont="PingFang SC" \
  -V mainfont="Times New Roman" \
  -V geometry:margin=1in \
  --toc

# Windows 用户字体改为: "Microsoft YaHei" 或 "SimSun"
# macOS 用户字体改为: "PingFang SC" 或 "Songti SC"
```

  * `--pdf-engine=xelatex`: 处理 UTF-8 字符的关键引擎。
  * `-V`: 传入 LaTeX 变量。
  * `--toc`: 自动生成目录 (Table of Contents)。

-----

### 4\. 网页与幻灯片 (Web & Slides)

#### 生成单页 HTML (内嵌 CSS/JS/图片)

用于发送给别人直接用浏览器打开查看。

```bash
pandoc input.md -s --embed-resources --metadata title="我的文档" -o output.html
```

#### 生成 Reveal.js 幻灯片

```bash
# 使用 -t revealjs
pandoc slides.md -t revealjs -s -o slides.html -V theme=solarized
```

  * Markdown 分页符：使用 `---` (水平线) 分隔 PPT 页。

-----

### 5\. 学术与引用 (Academic)

需要 `.bib` 文件 (BibTeX) 和 `.csl` 文件 (引用格式，可选)。

```bash
pandoc paper.md -o paper.pdf \
  --pdf-engine=xelatex \
  --citeproc \
  --bibliography=refs.bib \
  --csl=ieee.csl
```

  * `--citeproc`: 启用引文处理 (旧版用 `--filter pandoc-citeproc`)。

-----

### 6\. 实战小技巧 (Tips)

#### 多文件合并

```bash
# 按顺序将三个章节合并为一个 Word 文档
pandoc chapter1.md chapter2.md chapter3.md -o book.docx
```

#### 支持 LaTeX 数学公式 (转 Web)

```bash
# 使用 MathJax 渲染公式
pandoc math.md -s --mathjax -o math.html
```

#### 常用 YAML Header (写在 MD 文件头部)

```yaml
---
title: "项目开发文档"
author: "张三"
date: "2023-10-27"
output:
  docx:
    reference-doc: template.docx
  pdf:
    latex-engine: xelatex
---
```

### 7\. 自动化配置 (Defaults File)

对于复杂的参数，不要每次都在命令行敲。创建一个 `defaults.yaml` 文件：

**文件：defaults.yaml**

```yaml
input-files:
  - chapter1.md
  - chapter2.md
output-file: result.pdf
pdf-engine: xelatex
variables:
  CJKmainfont: "PingFang SC"
  geometry:
    - top=2cm
    - left=2cm
toc: true
```

**执行命令：**

```bash
pandoc -d defaults.yaml
```

