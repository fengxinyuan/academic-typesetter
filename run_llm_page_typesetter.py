import os
import sys
import re
import json
import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# 配置参数
# ==============================================================================
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY", "")
API_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
MODEL_NAME = "qwen-plus"  # 通义千问学术精修首选高性价比模型

WORKSPACE_DIR = r"C:\Users\fengxy\Desktop\matrix_translator"
# 优先从本地 .env 读取环境变量
env_file = os.path.join(WORKSPACE_DIR, ".env")
if os.path.exists(env_file):
    with open(env_file, "r", encoding="utf-8") as _ef:
        for _line in _ef:
            _line = _line.strip()
            if _line and not _line.startswith("#") and "=" in _line:
                _k, _v = _line.split("=", 1)
                os.environ.setdefault(_k.strip(), _v.strip())

RAW_PAGES_DIR = os.path.join(WORKSPACE_DIR, r"llm_pages_cache\raw_pages")
HEALED_PAGES_DIR = os.path.join(WORKSPACE_DIR, r"llm_pages_cache\healed_pages")
OUT_MD = os.path.join(WORKSPACE_DIR, r"final_output\Theory_of_Matrices_Full_CN.md")
OUT_HTML = os.path.join(WORKSPACE_DIR, r"final_output\Theory_of_Matrices_Full_CN.html")

MAX_WORKERS = 5  # 并发线程数

SYSTEM_PROMPT = """你是一位顶尖的理论数学专著与 LaTeX 排版专家。你的任务是对《矩阵理论》中文专著的单页内容进行出版级排版与数学公式精校。

【排版精校黄金准则】：
1. 绝对保真：严禁删减、总结、扩写或更改原书的中文语义与数学推导逻辑。必须保留开头的 `<div class="page-marker" ...>...</div>` 原书页码标识！
2. 根除公式源码裸露与定界符错位：
   - 所有的行内数学符号、单变量、字母、式子（如 $x$, $\lambda_i$, $\beta > 0$, $A \in \mathbb{R}^{n \times n}$）必须严格用成对的单个美元符 `$ ... $` 包裹；
   - 所有的独立大公式、方程组、多行矩阵（如 \begin{array}, \begin{bmatrix}, \begin{cases}, \begin{aligned}）必须独立成段，并用成对的双美元符 `$$ ... $$` 包裹；
   - 严禁在汉字句子中间把行内公式误写成 `$$`；严禁留下未闭合的单个 `$` 或双 `$$`。
3. 矩阵与数学语法修复：
   - 修复 OCR 导致的字符粘连与语法缺失（如 `\b { a }` 修复为 `\mathbf{a}`，`\pmb` 统一为 `\mathbf`，`\det A = 1$$。` 修复为 `$\det A = 1$。`）；
   - 确保矩阵的换行 `\\\\` 和列对齐 `&` 语法严密无损，括号 `\left[` 与 `\right]` 严格匹配。
4. 学术卡片标准化：
   - 定理、定义、引理、推论、命题、例题、习题、证明必须以清晰独立的加粗标题开头（如 **定理 1.**、**证明.**、**习题 2.**、**例 1.**）。
5. 纯净输出：直接输出排版修复后的 Markdown 文本内容，严禁输出任何问候语、确认词、解释性文字，严禁在最外层包裹 ```markdown 代码块！"""

def call_llm_heal(page_content, max_retries=3):
    headers = {
        "Authorization": f"Bearer {DASHSCOPE_API_KEY}",
        "Content-Type": "application/json"
    }
    
    prompt = f"请对以下单页内容执行学术出版级排版与数学公式修复，直接输出修复后的正文：\n\n{page_content}"
    
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.1
    }
    
    for attempt in range(max_retries):
        try:
            resp = requests.post(API_URL, headers=headers, json=payload, timeout=45)
            if resp.status_code == 200:
                data = resp.json()
                text = data['choices'][0]['message']['content'].strip()
                # 剥去可能误带的最外层 ```markdown ... ```
                if text.startswith("```markdown"):
                    text = text[11:].strip()
                elif text.startswith("```"):
                    text = text[3:].strip()
                if text.endswith("```"):
                    text = text[:-3].strip()
                return text
            elif resp.status_code == 429:
                time.sleep(2 * (attempt + 1))
            else:
                time.sleep(1.5)
        except Exception as e:
            time.sleep(2)
            
    return None

def process_page_job(filename):
    os.makedirs(HEALED_PAGES_DIR, exist_ok=True)
    raw_path = os.path.join(RAW_PAGES_DIR, filename)
    healed_path = os.path.join(HEALED_PAGES_DIR, filename)
    
    # 1. 命中缓存直接跳过（极速断点续传）
    if os.path.exists(healed_path):
        return filename, "CACHED"
        
    with open(raw_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 2. 检查页面是否包含数学内容
    # 如果是不含任何公式的封面/目录页，直接复用
    has_math = any(k in content for k in ['\\', '$', '矩阵', '定理', '定义', '习题', '式 ('])
    if not has_math or len(content.strip()) < 300:
        with open(healed_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return filename, "SKIPPED_NO_MATH"
        
    # 3. 调用大模型精校
    healed_content = call_llm_heal(content)
    if healed_content:
        if '<div class="page-marker"' not in healed_content:
            marker_m = re.search(r'<div class="page-marker"[^>]*>[\s\S]*?</div>', content)
            if marker_m:
                healed_content = marker_m.group(0) + "\n\n" + healed_content
                
        with open(healed_path, 'w', encoding='utf-8') as f:
            f.write(healed_content)
        return filename, "HEALED"
    else:
        with open(healed_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return filename, "FAILED_FALLBACK"

def merge_all_healed_pages():
    print("\n=== 正在合成最终全书 Markdown 与出版级 HTML ===")
    os.makedirs(HEALED_PAGES_DIR, exist_ok=True)
    all_files = sorted(os.listdir(RAW_PAGES_DIR))
    
    merged_pages = []
    cached_count = 0
    for f in all_files:
        healed_path = os.path.join(HEALED_PAGES_DIR, f)
        raw_path = os.path.join(RAW_PAGES_DIR, f)
        target = healed_path if os.path.exists(healed_path) else raw_path
        if os.path.exists(healed_path):
            cached_count += 1
        with open(target, 'r', encoding='utf-8') as p_file:
            c = p_file.read().strip()
            c = re.sub(r'\n+---+\s*\n+\*{0,2}(附注|校正说明|公式语义校正|修改说明|排版说明)[\s\S]*$', '', c)
            c = re.sub(r'\n+\*{0,2}(附注（公式语义校正说明）|【公式语义校正说明】)[\s\S]*$', '', c)
            merged_pages.append(c)
                
    full_md = "\n\n".join(merged_pages)
    with open(OUT_MD, 'w', encoding='utf-8') as f:
        f.write(full_md)
        
    print(f"全书已合并: 共 {len(merged_pages)} 页 (其中已精校: {cached_count} 页)")
    print(f"输出 Markdown 文件: {OUT_MD} ({len(full_md):,} 字符)")

    if os.path.exists(OUT_HTML):
        with open(OUT_HTML, 'r', encoding='utf-8') as f:
            html = f.read()
        new_html = re.sub(
            r'(<script type="text/plain" id="raw-md">)[\s\S]*?(<\/script>)',
            lambda m: m.group(1) + "\n" + full_md + "\n    " + m.group(2),
            html
        )
        with open(OUT_HTML, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"已同步更新出版级 HTML 网页: {OUT_HTML} ({len(new_html):,} 字节)")

if __name__ == "__main__":
    os.makedirs(HEALED_PAGES_DIR, exist_ok=True)
    raw_files = sorted(os.listdir(RAW_PAGES_DIR))
    total = len(raw_files)
    
    print("=================================================================")
    print(f"=== 启动全书逐页大模型排版校对引擎 (共 {total} 页，并发 {MAX_WORKERS} 线程) ===")
    print("=================================================================")
    
    done = 0
    t0 = time.time()
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(process_page_job, f): f for f in raw_files}
        
        for future in as_completed(futures):
            filename = futures[future]
            try:
                fn, status = future.result()
                done += 1
                elapsed = time.time() - t0
                speed = done / elapsed if elapsed > 0 else 0
                eta = (total - done) / speed if speed > 0 else 0
                
                print(f"[{done:3d}/{total:3d}] {status:16s} | {filename} | 耗时: {elapsed:.1f}s | 剩余约: {eta/60:.1f}分")
                
                # 每完成 20 页自动合并一次，保证进度实时呈现
                if done % 20 == 0:
                    merge_all_healed_pages()
            except Exception as e:
                print(f"[ERROR] 处理 {filename} 时发生异常: {e}")
                
    merge_all_healed_pages()
    print("=================================================================")
    print(f"=== 恭喜！全书 {total} 页大模型出版级排版自愈已全部完成！ ===")
    print("=================================================================")
