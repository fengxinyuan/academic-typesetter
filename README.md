# 📚 Academic Typesetter: 通用学术文献智能翻译与出版级数字排版系统

> **定位**：面向学术论文（ArXiv / IEEE / Nature 等）、教材专著、技术报告的端到端自动化翻译、大模型排版校对、高保真双语阅读与出版级 PDF 导出系统。  
> **旗舰标杆成果**：全书 574 页理论数学经典巨著 *《The Theory of Matrices (Second Edition)》* 864 页出版级中文全译本与双语对照系统。

---

## 🌟 核心架构与技术创新

本项目针对学术文献中**公式密集、矩阵复杂、符号易粘连坍塌、跨页连锁雪崩**等行业级痛点，构建了完全解耦、模块化的自愈式排版流水线：

```
                    [ 任意学术 PDF / 论文 / 专著 / 技术报告 ]
                                       │
                                       ▼
  【阶段 1: 统一版面提取 (MinerU / UniMERNet)】
   - 提取段落、双栏结构、表格、数学公式与高保真矢量切图
                                       │
                                       ▼
  【阶段 2: 工业级公式哨兵防篡改 (Sentinel Protection)】
   - 抽取 LaTeX 公式为纯 ASCII 哨兵占位符 (MATHxZZZ)
   - 彻底杜绝大模型在翻译时篡改变量、漏下划线或注入中文符号
                                       │
                                       ▼
  【阶段 3: 多模型并发学术翻译与自愈排版 (LLM Core)】
   - 支持 Qwen-Plus、DeepSeek、GPT-4o 等主流大模型
   - 注入 8 类学术卡片（定理、定义、算法、例题、证明、习题、引理、备注）
   - 单页词法边界隔离，断点原子落盘存档，随时秒级续跑
                                       │
                                       ▼
  【阶段 4: 四维出版级多模态产物导出 (Exporters)】
   ├── 📖 纯净 Markdown (支持 Typora / Obsidian 知识库)
   ├── 🌐 交互式 HTML 专著 (自包含 KaTeX 矢量渲染，支持夜间模式与原图回退)
   ├── 🪟 中英双语对照阅读器 (左右分屏联动同步滚动，点击即查原文)
   └── 📑 出版级矢量 PDF (基于无头 Chrome / Edge 高清渲染，带完整大纲书签)
```

---

## 📂 项目模块化目录架构

```
academic-typesetter/
├── core/                                # 核心可复用引擎库
│   ├── config.py                        # 统一配置中心 (动态探测系统注册表、字体库与模型)
│   ├── sentinel.py                      # 工业级公式哨兵隔离与定界符零丢失自愈算法
│   ├── mineru.py                        # MinerU 云端与本地数据装配驱动器
│   ├── translator.py                    # 学术翻译引擎 (多模型/多语言/术语表/断点续传)
│   ├── typesetter.py                    # 出版级排版与学术卡片注入器
│   └── exporter.py                      # Markdown / HTML / 双语阅读器 / 矢量 PDF 导出器
│
├── web/                                 # 🌟 可视化 Web 双语排版工作台
│   ├── index.html                       # 极简双语拖拽交互工作台 (支持在线预览与一键下载)
│   └── server.py                        # FastAPI 轻量级 Web 调度后端
│
├── main.py                              # 统一命令行调度入口 (CLI)
├── run.bat                              # 跨平台一键启动脚本
├── .env.example                         # 环境变量与 API 密钥模板
└── output/                              # 文档处理产物归档根目录 (动态按输入文件名生成)
```

---

## 🚀 快速上手与使用指南

### 1. 环境配置与 API Key 设置
复制模板文件并填写您的 API 密钥：
```bash
cp .env.example .env
```
在 `.env` 中填入你的通义千问或 MinerU 密钥（系统支持完全隔离，绝不硬编码 Token）：
```ini
DASHSCOPE_API_KEY=your_dashscope_api_key_here
MINERU_TOKEN=your_mineru_token_here
```

### 2. 启动可视化 Web 双语工作台 (推荐)
借鉴现代学术工具交互设计，一键启动本地工作台：
```bash
python main.py serve
```
浏览器打开 `http://127.0.0.1:8000`，直接拖入 PDF 或 Markdown，实时查看翻译进度、双语分屏联动阅读并一键下载 PDF/HTML/MD。

### 3. 命令行一键批量处理 (CLI)
```bash
# 任务 A：端到端处理任意学术论文 (自动提取 + 翻译 + 卡片排版 + 导出 PDF/HTML/MD)
python main.py process my_paper.pdf

# 任务 B：生成中英双语分屏对照阅读器
python main.py bilingual my_paper.pdf

# 任务 C：仅对已有 Markdown 执行数学排版自愈与学术卡片注入 (不翻译)
python main.py typeset draft.md

# 任务 D：检查当前系统的浏览器路径、中文字体与可用模型
python main.py info
```

---

## 🛠️ 核心优化特性 (无硬编码规范)

* **浏览器路径动态定位**：全面弃用硬编码盘符路径，在 Windows 下优先通过操作系统注册表 `winreg` 检索 `chrome.exe` / `msedge.exe` 的官方 App Paths，兼顾环境变量 `BROWSER_PATH` 与 Linux/macOS 动态探测；
* **字体库自适应探测**：动态检索 `%WINDIR%\Fonts` 及系统字体池，优先采用系统原生微软雅黑（`msyh.ttc`）、思源黑体（`Noto Sans SC`）等高质量 CJK 字体；
* **任务流全泛化**：根据传入文件名自动在 `output/<文件名>/` 建立独立工作流，绝不相互干扰或硬编码单本书名。
