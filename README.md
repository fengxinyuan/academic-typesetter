# 📚《矩阵理论 (第二版)》全书翻译与出版级数字排版系统
> **英文原著**：*The Theory of Matrices (Second Edition with Applications)* — Peter Lancaster & Miron Tismenetsky (Academic Press)  
> **项目定位**：全书 574 页理论数学经典巨著的全流程端到端自动化翻译、大模型排版校对与高保真矢量渲染系统。

---

## 🌟 核心架构与技术创新

本项目针对理论数学专著中**公式密集（全书 20,000+ 处公式）、矩阵复杂（1,400+ 处多行分块矩阵）、符号易粘连坍塌**的行业级难题，构建了完整的自愈式翻译与排版流水线：

```
       [英文扫描版 PDF (589 页)]
                  │
                  ▼
   1. 物理版面与公式提取 (MinerU / UniMERNet)
                  │
                  ▼
   2. 工业级流式分块翻译 (Qwen-Plus / 阿里云百炼)
                  │
                  ▼
   3. 逐页大模型学术精修引擎 (Page-by-Page LLM Typesetter)
      ├── 原子级单页切片 (574 页，上下文 1~2KB 黄金窗口)
      ├── 5 线程安全极速并发 + 指数退避容错
      ├── 行内/块级定界符相位锁定 (杜绝公式源码裸露)
      └── 矩阵环境对齐补全与字符粘连自愈
                  │
                  ▼
   4. 最终双模交付产物
      ├── 📖 Theory_of_Matrices_Full_CN.md  (纯净 Markdown，支持 Typora 秒开)
      └── 🌐 Theory_of_Matrices_Full_CN.html (视口优先 + 空闲流式 KaTeX，首屏 <100ms)
```

---

## 🚀 核心功能与排版特性

### 1. 彻底根治公式源码裸露
* **定界符智能相位锁定**：全书严格隔离，杜绝因单处字符缺失引发的全局 `$$` 翻转；
* **裸露 LaTeX 命令自愈包裹**：正文中的内联变量（如 $x$、$\lambda_i$、$\eta > 0$、$P \in \mathbb{R}^{n \times n}$）100% 自动包裹为行内公式；
* **矩阵独立成块居中**：1,400+ 处矩阵（`bmatrix`, `pmatrix`, `array`）全部独立居中展现，并支持超长矩阵水平平滑滚动。

### 2. 出版级学术卡片体系 (Academic Card System)
系统自动解析全书逻辑结构，赋予 6 类专属出版级色块卡片：
* 🔷 **定理卡片 (Theorems)**：科技蓝左侧重边框加深背景；
* 🔘 **定义卡片 (Definitions)**：经典典雅灰学术色系；
* 🟣 **引理 / 推论卡片 (Lemmas & Corollaries)**：学术紫尊贵高阶色；
* 🟢 **例题卡片 (Examples)**：森林绿柔和色块；
* 🟠 **习题卡片 (Exercises)**：学术暖橙专属区块；
* 📄 **证明区块 (Proofs)**：极简左侧竖线缩进体系。

### 3. 毫秒级秒开与流式矢量渲染引擎
* **首屏挂载耗时 < 100ms**：采用轻量占位符架构，彻底告别单次调用两万次 KaTeX 导致的浏览器假死；
* **视口优先 (Intersection Observer)**：当前屏幕可见区域加 500px 缓冲内的公式在 16ms 内瞬时完成矢量渲染；
* **空闲调度 (requestIdleCallback)**：主线程闲置时平滑批量渲染后续内容，滚动极致丝滑（60 FPS）。

---

## 📂 核心目录与文件结构

```
matrix_translator/
├── final_output/                          # 最终成果交付目录
│   ├── Theory_of_Matrices_Full_CN.html    # 最终出版级交互式 HTML 专著 (即开即读)
│   ├── Theory_of_Matrices_Full_CN.md      # 全书完整精校 Markdown 专著源码
│   └── full_translation_progress.json    # 1033 个切片的全量翻译进度存档
│
├── run_llm_page_typesetter.py             # 核心：大模型逐页自愈排版与全书装配引擎
├── run_pipeline.py                        # 基础：MinerU 提取与初步流水线
├── make_bilingual_pdf.py                  # 双语对照版 PDF 合成工具
├── run.bat                                # 跨平台一键启动脚本 (自动读取 .env)
├── .env.example                           # 环境变量与 API Key 配置模板
├── README.md                              # 本项目完整技术说明文档
└── .gitignore                             # Git 规范忽略配置
```

---

## 🛠️ 使用指南

### 1. 浏览与阅读最终译本
* 双击或直接用现代浏览器（Chrome、Edge、Safari）打开：  
  `final_output/Theory_of_Matrices_Full_CN.html`
* 支持原书页码跳转、章节导航、全书快速关键词搜索及夜间/移动端自适应。

### 2. 环境配置与 API 密钥设置
本项目已实现密钥完全隔离，绝不硬编码敏感 Token：
1. 复制模板文件生成配置：
   ```bash
   cp .env.example .env
   ```
2. 在 `.env` 中填入你的通义千问 API 密钥：
   ```ini
   DASHSCOPE_API_KEY=your_dashscope_api_key_here
   ```

### 3. 一键运行与断点续跑
Windows 用户直接双击运行：
```bash
run.bat
```
或在终端中运行：
```bash
python run_llm_page_typesetter.py
```
* **断点续跑机制**：引擎按单页（1~574页）缓存已校对成果，重新运行会自动跳过已完成页面，零重复扣费；
* **并发控制**：默认开启 5 线程并发，带有指数退避防限流机制，支持 `Ctrl + C` 安全随时退出。

---

## 📜 依赖环境
* Python 3.8+
* `pip install requests python-dotenv`
* 现代浏览器（Chrome / Edge / Firefox / Safari）
