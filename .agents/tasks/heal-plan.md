# Implementation Plan — Extend `heal_formulas.js` to fix post-page-100 formula/layout errors

Scope: extend the existing repair script `c:/Users/fengxy/Desktop/matrix_translator/heal_formulas.js`.
Append new fix passes **immediately before** the existing `fs.writeFileSync(MD, text, 'utf8');` line (i.e. after Fix 11, before the write + HTML-regeneration tail). Do NOT rewrite the script, do NOT touch the write/HTML-swap tail or the `countErrors` function except to reuse `countErrors` from the temp verifier. This is a single-file, single-script, local task — no decomposition.

---

## Findings from exploration (ground truth — the plan is built on these, not on the brief's stale numbers)

Verified by reading the real files and running throwaway Node diagnostics (now deleted):

- `Theory_of_Matrices_Full_CN.md`: 29,672 lines, ~1.75 MB.
- **Standalone `$$`-on-own-line count = 3768 → already EVEN.** The brief said 3773/odd; the file has since drifted (prior heal runs changed it). So pass (A) is now mostly a *safety / regression-guard* pass: on the current file it should find few or zero orphans, but it must still run so a future re-run with fresh OCR stays balanced. The plan keeps (A) but its success bar is "parity stays EVEN", not "fixes 6 known orphans".
- **Current KaTeX errors = 197 / 17,868 tokens** (measured with the script's own `countErrors` extraction + installed `katex`). The brief's "186" is stale. **New baseline to beat: 197.**
- **Current naked display-formula lines = 1331** (brief said ~1266 — stale). **New baseline to beat: 1331.**
- **Qualifying naked display RUNS = 1330**, of which **152 end with a `\tag{...}`** (strong display signal) and **0 contain a run of ≥8 CJK chars** — so on current data pass (B)'s run detector would not swallow any prose. Guard (C) is still mandatory for safety / future OCR.
- There are **34 naked `\begin{array}` openers that do NOT close on the same line.** BUT inspection (e.g. .md line 6038) shows most are *shattered nested-fence* artifacts (a `$$ \begin{array}{r}{ y_1 = ` opener, then a nested `$$\left[...\end{array}$$`, then ` \right] `, then `$$`). Those belong to the **existing Fix 2 stitcher**, not to pass (B). Pass (B) must only wrap runs that sit cleanly OUTSIDE any `$$` block; it must not try to repair nested-fence corruption.
- The user's `\operatorname{rank}\operatorname{diag}\left[ \text{...} \right]` example now lives at **.md line 2805, already inside a `$$` block but structurally corrupt**: `\operatorname{rank} \operatorname{diag}\left[ A _ { 1 1  , A _ { 2 2 } , \ldots , A _ { k k } ] = \sum ... .} \right] = \sum_{i=1}^k \operatorname{rank} A_i.` — braces scrambled, a stray `]` and `.}` buried mid-expression, plus a duplicated tail. A prior Fix-4 pass already stripped the `\text{}` wrapper but left this wreck. The literal `\text{...}`-wrapping-subscripts form and the `\tag{0].}` form from the brief **no longer exist anywhere in the .md** (grepped: 0 matches). So pass (D) is a *targeted repair of this specific corrupt line* plus *defensive regexes* for the two patterns in case they reappear — not a hunt for strings that are already gone.
- Env reality: **`katex` was NOT installed** (no `node_modules`, no `package.json`). I installed `katex@0.16.11` with `npm install katex --no-save` so diagnostics could run. The coder step MUST ensure `katex` is importable before running the script (`npm ls katex` or re-install `--no-save`), otherwise `require('katex')` throws. Node v24 + npm 12 are available.
- Backups `Theory_of_Matrices_Full_CN.md.bak2` / `.html.bak2` exist in `final_output/` — a manual safety net, but make a fresh copy before the first run anyway (step 1).

Out-of-scope corruption observed but NOT covered by A–D (note for the record, do not fix here): inline-`$` mismatches on prose lines, e.g. `则$Y ( \zeta )$\zeta = 0$B亦连续。` (.md ~19534) and dangling `其中$` (.md ~25788). These flip inline-math state within a single prose line and are a different class; leave them unless a later task asks.

---

## Shared conventions for all appended passes

- Operate on the single in-memory `text` string, consistent with the existing script.
- Normalize line splitting on `/\r?\n/`; when rejoining, use `\n` (the existing tail already writes `\n`-joined text — the file is LF).
- **JS gotcha (call out in a code comment):** in `String.prototype.replace`, a replacement **string** turns `$$` into a single literal `$` (and `$1`, `$&` etc. are special). **Any pass whose output must literally contain `$$` MUST use a function replacer** (return the string from a callback), never a string literal with `$$` in it. Passes A, B, and D-for-line-2805 all emit `$$` and therefore must build their output in code and either assign to the array / return from a function replacer — not via `.replace(re, '...$$...')`.
- Define reusable predicates once, near the top of the appended block:
  - `isFence = l => l.trim() === '$$';`
  - `isPageMarker = l => /<div class="page-marker"/.test(l);`
  - `isHeading = l => /^#{1,6}\s/.test(l);`
  - `cjkRun8 = /[\u4e00-\u9fa5]{8,}/;`  (a run of ≥8 CJK = prose)
  - `cjk2 = /[\u4e00-\u9fa5]{2,}/;`      (matches the tail's own prose test)

---

- [ ] 1. Back up the two output files before any edit, so a bad heal run is recoverable.
      Files: none edited — copy `final_output/Theory_of_Matrices_Full_CN.md` → `...md.bak3` and `...html` → `...html.bak3`.
      Verify: both `.bak3` files exist (`Test-Path`); the originals are unchanged byte-for-byte vs. the copies.

- [ ] 2. Confirm `katex` is importable so the script's tail (`require('katex')`) and the verifier run.
      Files: none (environment check); if missing, run `npm install katex --no-save --no-audit --no-fund` in `c:/Users/fengxy/Desktop/matrix_translator`.
      Verify: `node -e "require('katex');console.log('ok')"` prints `ok`.

- [ ] 3. Append **Pass A — balance/close orphaned `$$` fences** just before `fs.writeFileSync(MD, ...)`.
      What: split `text` into lines; walk them tracking an `inBlock` boolean toggled by every `isFence(line)`. While `inBlock === true`, if the current line is NOT a fence and is clearly non-math — `isPageMarker(line) || isHeading(line) || cjkRun8.test(line)` — splice a closing `$$` line (plus a preserved blank line) immediately before that non-math line, and set `inBlock = false`. Rejoin with `\n`. Build the output as an array (function/array construction), never a string-literal replace, per the `$$` gotcha. This is primarily a regression guard — current parity is already EVEN, so expect 0 insertions today.
      Files: `heal_formulas.js` (appended block).
      Verify: run the temp verifier (step 8) → standalone-`$$` parity is EVEN and KaTeX errors ≤ 197 (no regression). On current data, naked count and errors should be unchanged by A alone.

- [ ] 4. Append **Pass B — wrap naked display-formula runs** (depends on Pass A having normalized fence state; run B after A).
      What: re-split into lines; walk with an `inBlock` toggle. Group maximal **contiguous non-blank runs** that lie entirely OUTSIDE any `$$` block. Skip a run if ANY of its lines contains `$`. A run **qualifies as display LaTeX** when any line: (a) starts (after optional whitespace) with one of `\pmb \boldsymbol \mathfrak \mathcal \mathbf \operatorname \operatorname* \left \frac \sum \prod \int \det`, or `\begin{array|bmatrix|pmatrix|matrix|cases}`, or `{ \pmb` / `{ \boldsymbol` / `{ \mathfrak` / `{ \mathcal` / `{ \mathbf`; OR (b) contains `\begin{array}` or `\end{array}`; OR (c) has TeX structure = contains `_ {` or `^ {` AND a `\command` AND one of `= \triangleq \leq \geq \in`. AND the trimmed joined run length `> 10`. Wrap the WHOLE qualifying run in ONE block: a line `$$`, the run lines verbatim, a line `$$`, with a blank line kept before and after. A multi-line `\begin{array}` run becomes ONE block, not one per line. Build output via array construction (the inserted `$$` lines must be real, per the gotcha).
      Files: `heal_formulas.js` (appended block, after Pass A).
      Verify: temp verifier → naked display-formula lines drop sharply from 1331 toward ~0; KaTeX errors ≤ 197 and ideally lower; standalone-`$$` parity stays EVEN. Spot-check that .md line ~4804 (`{ \mathfrak { f } } = [ \beta ...`) and .md ~15597 (`Z _ { k j } = ... \tag{9}`) are now fenced.

- [ ] 5. Append **Guard C — never wrap or swallow Chinese prose** (implemented as explicit conditions inside Pass B, not a separate pass).
      What: inside Pass B's run loop, before wrapping, reject the run if any line matches `cjkRun8` OR if the run contains a CJK run of ≥2 chars that is not inside `\text{...}` / `\operatorname{...}` (be conservative: if a run mixes CJK with math and you cannot cleanly tell, LEAVE IT UNWRAPPED). Document in a comment: a false negative (an un-wrapped formula) is acceptable; swallowing a paragraph into math is not. Current data has 0 CJK-contaminated qualifying runs, so this guard should exclude 0 today — it exists to stay safe on re-runs.
      Files: `heal_formulas.js` (conditions within the Pass B block).
      Verify: temp verifier reports 0 newly-created `$$` blocks whose body matches `cjk2` beyond those the tail already treats as prose; manually confirm no `page-marker`/heading/prose line was absorbed (diff `.md` vs `.md.bak3` and eyeball that inserted `$$` only ever hug formula runs).

- [ ] 6. Append **Pass D — targeted OCR fixes for the two user-reported cases** (the *delta* only; Fix 4/Fix 10 already run earlier).
      What:
      (i) Repair the specific corrupt line at .md ~2805 by matching its stable signature with a function replacer and emitting the correct math:
      target regex (anchored on the recognizable fragments) e.g. `/\\operatorname\{rank\}\s*\\operatorname\{diag\}\\left\[[\s\S]*?\\right\]\s*=\s*\\sum_\{i=1\}\^k \\operatorname\{rank\} A_i\./`
      replace (function replacer) with the intended expression:
      `\operatorname{rank} \operatorname{diag}[ A_{11}, A_{22}, \ldots, A_{kk} ] = \sum_{i=1}^{k} \operatorname{rank} A_{ii}.`
      (ii) Defensive, general regexes for the two brief patterns in case fresh OCR reintroduces them (they are absent now, so these are no-ops today but cheap insurance):
      - bracket-leaked tag: `text = text.replace(/\\tag\{([^}\]]*)\][^}]*\}/g, (m, t) => '\\tag{' + t.trim() + '}')` — collapses `\tag{0].}` → `\tag{0}` (function replacer; note Fix 5 already has a similar `\tag{..][..}` rule — add this ONLY if it catches cases Fix 5's `/\\tag\{([^}]*?)\][^}]*\}/` misses, i.e. verify against the file first and keep just the delta).
      - `\text{}` wrapping subscripted math: `text = text.replace(/\\text\s*\{([^{}]*?[_^]\s*\{[\s\S]*?)\}/g, '$1')` — unwrap. This overlaps Fix 4's second rule; add ONLY the portion Fix 4 misses (e.g. `\text{...}` containing `\left[`/`\operatorname` with subscripts). Confirm by grep before adding.
      Files: `heal_formulas.js` (appended block).
      Verify: temp verifier → the token for the (former) line-2805 block renders without a KaTeX error (overall errors ≤ post-step-4 count); grep confirms no `\tag{...]...}` and no `\text{...subscript...}` remain.

- [ ] 7. Decide pass ordering and finalize placement.
      What: in the appended block, run **D(i) line-2805 repair → A → B(+C guard) → D(ii) defensive** — i.e. fix the known in-block wreck first, then balance fences, then wrap naked runs on the now-clean fence state, then the cheap defensive sweeps. All of this sits strictly between Fix 11 and `fs.writeFileSync(MD, text, 'utf8');`. Do not alter the HTML-swap tail or `countErrors`.
      Files: `heal_formulas.js`.
      Verify: `node heal_formulas.js` runs clean (exit 0) and prints `HTML regenerated from healed markdown.` and a final `KaTeX errors AFTER:` line.

- [ ] 8. Add a TEMPORARY verifier, run it, record results, then delete it.
      What: create `_verify_tmp.js` in the project root that re-reads the healed `.md` and replicates the HTML's extraction + the script's `countErrors`: replace `$$([\s\S]*?)$$` blocks (if body matches `[\u4e00-\u9fa5]{2,}` treat as prose and skip; else block-math token, `displayMode:true`), then replace `$([^$\n\r\u4e00-\u9fa5]+?)$` as inline tokens (`displayMode:false`), render each with `katex.renderToString(content, { displayMode, throwOnError: true, strict: false })`, count failures. ALSO report: standalone-`$$` parity (must be EVEN) and remaining naked display-formula line count (reuse Pass B's predicate). This mirrors the exact logic in `heal_formulas.js` `countErrors` so numbers are comparable.
      Files: create then delete `c:/Users/fengxy/Desktop/matrix_translator/_verify_tmp.js`.
      Verify: `node _verify_tmp.js` prints KaTeX errors **< 197** (baseline), naked display lines **far below 1331** (target near 0), parity **EVEN**. Then delete the temp file. Grep-only checks do NOT count as verification — the KaTeX render pass is the gate.

- [ ] 9. Final build/render check and cleanup.
      What: run `node heal_formulas.js` once more to confirm idempotence (a second run should not increase errors or flip parity), confirm the HTML was regenerated (its embedded `id="raw-md"` block now matches the healed `.md`). Remove any stray temp files; leave `.bak3` backups in place.
      Files: none (verification only).
      Verify: second `node heal_formulas.js` reports KaTeX errors ≤ the first run's post-heal count and no new parity/naked regressions; open the HTML `raw-md` region and confirm the user's examples (`\mathfrak{f}` run, `\operatorname{rank}\operatorname{diag}` line) now sit in valid `$$` blocks.

---

## Baselines (verified today) and success criteria

| Metric | Baseline (now) | Brief's stale value | Target after heal |
|---|---|---|---|
| KaTeX render errors | **197** / 17,868 | 186 | strictly < 197, ideally well below |
| Standalone `$$` parity | EVEN (3768) | odd (3773) | stays EVEN |
| Naked display-formula lines | **1331** | ~1266 | near 0 (large reduction) |

If any pass cannot drive its metric the right direction without risking prose, prefer the safe no-op and record the shortfall in the step output rather than swallowing text. A larger-than-expected residual naked count is acceptable and safe; a swallowed paragraph is not.

## Assumptions / gaps (made explicit rather than stalling)
- The brief's exact strings (`\tag{0].}`, `\text{A_{11},...}` wrapping) are gone from the current `.md`; pass (D) therefore targets the one surviving corrupt line (.md ~2805) literally and keeps the two general patterns as defensive no-ops. If the coder finds the literal forms resurfaced in a fresh OCR pass, the defensive regexes already cover them.
- Inline-`$` mismatch corruption on prose lines (≥19534, ≥25788) is a separate class and intentionally left for a future task; it is not in the A–D scope.
- `katex` must be present at run time; the plan installs it `--no-save` so no `package.json`/lockfile is introduced into this Python-centric repo.
