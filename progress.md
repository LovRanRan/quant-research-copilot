# Project 3 · quant-research-copilot — Progress Tracker

> 单文件进度板 — Dashboard + Roadmap + Logs + Repo 蓝图 + Hand-write 规矩 + Tool Inventory
> 维护方式：每完成一个 sub-step，在 Dashboard 更新 Current，在 Logs 追加一行
> Owner: Haichuan · Start: 2026-04-22 · Target: 2026-05-14 (Week 5–8)

---

## 📊 Dashboard

| Field | Value |
|-------|-------|
| **Current Stage** | `Stage 1 · Scaffolding + DESIGN.md v0` |
| **Current Sub-step** | `1.3 — DESIGN.md v0.1 draft (Claude drafts, Haichuan fills key fields)` |
| **Stage 1 Progress** | 🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜ 9 / 10 micro-steps |
| **Overall Progress** | 🟦⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ 0 / 13 stages |
| **Blocker** | none |
| **Last Activity** | 2026-04-22 · **Stage 1.2 closed**. All 3 MCP skeletons at parity — `FastMCP('mcp-sec-edgar')` / `FastMCP('mcp-fred-macro')` / `FastMCP('mcp-backtest')` all smoke-check green. Three subpackage trees, uv workspace aligned, LICENSE/CI/boilerplate identical across all. |
| **Working Mode** | HAND-WRITE (Claude drafts DESIGN.md; Haichuan fills AgentState schema and tool signatures) |
| **Next Action** | Claude proposes DESIGN.md v0.1 outline → Haichuan approves/edits scope → Claude drafts → Haichuan fills key fields + reviews. |

---

## 🗺️ Roadmap（13 Stage · 按流程推进，不绑日期）

### Stage 1 — Scaffolding + DESIGN.md v0 🟧 in progress
- [ ] 1.1 主 repo 骨架（`projects/quant-research-copilot/`）
  - [x] 1.1.a `uv init --package` + 顶层目录（src/ eval/ tests/ configs/ scripts/ mcp-servers/）✅ 2026-04-22
  - [x] 1.1.b Option B · 标准 src-layout，所有 `__init__.py` 就位 ✅ 2026-04-22
  - [x] 1.1.c `.gitignore` + `.env.example` ✅ 2026-04-22
  - [x] 1.1.d `git init` + GitHub public repo + first push ✅ 2026-04-22
- [ ] 1.2 mcp-servers/ subdirs + 3 MCP skeletons
  - [x] 1.2.a `mcp-servers/mcp-sec-edgar/` ✅ 2026-04-22 (uv workspace auto-enabled, see ADR-003)
  - [ ] 1.2.b `mcp-servers/mcp-fred-macro/` (same shape)
  - [ ] 1.2.c `mcp-servers/mcp-backtest/` (same shape)
- [ ] 1.3 DESIGN.md v0.1 起草（Claude 起草，Haichuan 填 AgentState schema）

### Stage 2 — mcp-sec-edgar 独立 repo 开源 ⬜
- [ ] 2.1 FastMCP 骨架 + pytest + ruff + GitHub Actions CI
- [ ] 2.2 Tool `get_index_constituents(index, as_of_date)` + `constituents://{index}/{date}` resource
- [ ] 2.3 Rate limit middleware（10 req/s + User-Agent 强制） + SQLite cache
- [ ] 2.4 IndexRegistry 抽象（默认 SP500Index，预留 Russell1000/Nasdaq100）
- [ ] 2.5 Tool `search_filings(ticker, form_type, limit)`
- [ ] 2.6 Tool `get_filing_section(accession_number, section)` + strategy pattern 预留
- [ ] 2.7 MCP Inspector 全量验证（3 tools + 1 resource）
- [ ] 2.8 pytest ≥ 10（rate limit / cache hit / bad ticker / empty filing）
- [ ] 2.9 README + MIT LICENSE + push GitHub public

### Stage 3 — mcp-fred-macro 独立 repo 开源 ⬜
- [ ] 3.1 FastMCP 骨架 + CI
- [ ] 3.2 Tool `search_series(keyword, limit)` / `get_series(series_id, start, end)` / `align_series(series_ids[], start, end, freq)`
- [ ] 3.3 Resource `meta://{series_id}`
- [ ] 3.4 Parquet 本地缓存（hash key）+ ResamplePolicy 抽象
- [ ] 3.5 MCP Inspector 验证 + pytest ≥ 8
- [ ] 3.6 README + LICENSE + push GitHub

### Stage 4 — mcp-backtest 独立 repo 开源 + 3 repo 提 registry PR ⬜
- [ ] 4.1 FastMCP 骨架 + CI + Strategy Protocol 设计
- [ ] 4.2 Tool `list_strategies()` + `run_backtest(strategy, universe, start, end, params)` MVP
- [ ] 4.3 MomentumStrategy(lookback=12, skip=1)（Jegadeesh & Titman 1993）
- [ ] 4.4 yfinance Parquet cache（ticker-start-end 切片）
- [ ] 4.5 Tool `get_backtest_result(run_id)` + `result://{run_id}` resource
- [ ] 4.6 指标：sharpe / max_dd / CAGR / yearly_pnl（对齐 QuantConnect ±0.2）
- [ ] 4.7 pytest ≥ 12
- [ ] 4.8 README + LICENSE + extensibility note + push
- [ ] 4.9 **3 个 server 一起提交 `modelcontextprotocol/servers` community registry PR**

### Stage 5 — LangGraph Supervisor + 3 sub-agent 骨架 ⬜
- [ ] 5.1 `AgentState` TypedDict（query / paper_id / plan / messages / market_data / backtest_result / macro_context / memo_draft / next_agent）
- [ ] 5.2 4 个空节点（supervisor / research_reader / market_analyst / memo_writer）
- [ ] 5.3 Supervisor 条件边（按 next_agent 分发）+ routing prompt v1（few-shot 3 条）
- [ ] 5.4 `langgraph dev` 跑 no-op 流程

### Stage 6 — 接 MCP 第 1 批（sec-edgar + fred-macro → market_analyst）⬜
- [ ] 6.1 `langchain-mcp-adapters` 挂载两个 server（stdio transport 本地）
- [ ] 6.2 tool binding 给 market_analyst
- [ ] 6.3 smoke test："SP500 成分 + 2020–2024 Fed Funds Rate" 全链路
- [ ] 6.4 调 routing prompt（观察误路由）

### Stage 7 — 接 MCP 第 2 批 + 记录 baseline 数据 ⭐关键 ⬜
- [ ] 7.1 backtest → market_analyst / arxiv → research_reader / tavily → all sub-agent 兜底
- [ ] 7.2 端到端跑 "arxiv 2408.xxxxx → momentum 验证 → 宏观解读 → memo" 示例
- [ ] 7.3 **记录第一轮 baseline：路由决策 / 总延迟 / tokens / 成本 USD**（面试最值钱的数字）

### Stage 8 — Reflection self-check in memo_writer ⬜
- [ ] 8.1 generate → grade（事实核查 / 引用对齐 / 关键数字来源）→ rewrite，最多 2 轮
- [ ] 8.2 复用 Project 2 finrag-copilot faithfulness grading 模板
- [ ] 8.3 5 条样本验证 iteration 0 vs iteration 1 改写生效

### Stage 9 — LangSmith 全链路 tracing ⬜
- [ ] 9.1 env vars 打开 tracing + graph 所有节点 + tool call 可见
- [ ] 9.2 自定义 metadata（agent_name / tool_name / mcp_server / tokens_in/out / latency_ms / cost_usd）
- [ ] 9.3 3 类 query 验证（纯回测 / 纯论文 / 混合研究）

### Stage 10 — DESIGN.md v1.0 终稿 + 8 Failure Mode ⬜
- [ ] 10.1 DESIGN.md v0.1 → v1.0（加 baseline 数据 / 完整 IO contract / 架构图定稿）
- [ ] 10.2 8 种 Failure Mode + 每种 1 行处理策略

### Stage 11 — 韧性层（retry/backoff/fallback + HITL）Week 7 硬事 #1 ⬜
- [ ] 11.1 按 Stage 10 的 8 failure mode 落地三层韧性
- [ ] 11.2 langgraph retry_policy + cache_policy + Command API
- [ ] 11.3 HITL interrupt（长 backtest / 模糊 query）

### Stage 12 — 40 任务 × 3 架构严肃 Eval Week 7 硬事 #2 ⭐差异化支柱 ⬜
- [ ] 12.1 40 条 quant research 任务标注（含 ground truth + reference memo）
- [ ] 12.2 Supervisor / ReAct / Swarm 三架构各跑一遍
- [ ] 12.3 产出 4 张图（routing / accuracy / cost / latency）

### Stage 13 — 生产化 Week 8 ⬜
- [ ] 13.1 FastAPI gateway
- [ ] 13.2 Docker Compose（5 MCP server 编排）
- [ ] 13.3 GitHub Actions CI/CD
- [ ] 13.4 Dashboard（baseline vs eval 对比）
- [ ] 13.5 README 主 repo（4-repo 架构图）
- [ ] 13.6 Demo video
- [ ] 13.7 双语博客（中文 + 英文各一篇）

---

## 📁 Repo 目录蓝图

**主 repo** — `ai-agent-prep/projects/quant-research-copilot/`

```
quant-research-copilot/
├── src/
│   ├── agents/                      # supervisor + 3 sub-agent
│   │   ├── __init__.py
│   │   ├── supervisor.py
│   │   ├── research_reader.py
│   │   ├── market_analyst.py
│   │   └── memo_writer.py
│   ├── graph/
│   │   ├── __init__.py
│   │   ├── state.py                 # AgentState TypedDict
│   │   └── build_graph.py
│   ├── mcp_clients/                 # langchain-mcp-adapters 挂载层
│   │   ├── __init__.py
│   │   └── registry.py
│   └── __init__.py
├── eval/                            # Stage 12 用
│   ├── tasks.jsonl
│   ├── runners/
│   └── metrics.py
├── tests/
├── configs/
│   └── settings.py
├── scripts/
├── mcp-servers/                     # ⚠ 注意：嵌套位置，开源时需单独 push
│   ├── mcp-sec-edgar/               # 独立 public repo（git subtree 或单独 push）
│   ├── mcp-fred-macro/
│   └── mcp-backtest/
├── DESIGN.md                        # Stage 1.3 起草
├── README.md
├── progress.md                      # ← 本文件
├── project3_mapping.md              # MCP 概念 → 项目映射（已完成）
├── pyproject.toml
├── .env.example
└── .gitignore
```

**3 个 MCP 独立 repo 统一模板**（以 `mcp-sec-edgar/` 为例）：

```
mcp-sec-edgar/
├── src/mcp_sec_edgar/
│   ├── __init__.py
│   ├── server.py                    # FastMCP 入口
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── get_index_constituents.py
│   │   ├── search_filings.py
│   │   └── get_filing_section.py
│   ├── resources/
│   │   ├── __init__.py
│   │   └── constituents.py
│   ├── registries/                  # ⭐ 可扩展性插槽
│   │   ├── __init__.py
│   │   └── index_registry.py        # IndexRegistry protocol + SP500Index
│   ├── cache/
│   │   ├── __init__.py
│   │   └── db.py                    # SQLite 层
│   └── middleware/
│       ├── __init__.py
│       └── rate_limit.py
├── tests/
│   ├── __init__.py
│   ├── test_tools.py
│   └── test_cache.py
├── .github/workflows/ci.yml
├── pyproject.toml
├── README.md
├── LICENSE                          # MIT
├── .env.example                     # SEC_USER_AGENT=email+app-name
└── .gitignore
```

> `mcp-fred-macro/` 的区别：`tools/` 换成 `search_series/get_series/align_series.py`；`registries/` 换成 `resample_policy.py`；`cache/` 换成 Parquet（不是 SQLite）。
> `mcp-backtest/` 的区别：`tools/` 换成 `run_backtest/get_backtest_result.py`；`registries/` 换成 `strategy.py`（Strategy Protocol + MomentumStrategy）；`cache/` 换成 yfinance Parquet。

---

## ⚠ 架构决策记录（ADR）

### ADR-001 · MCP server 嵌在主 repo 的 `mcp-servers/` 子目录
- **Date**: 2026-04-22
- **Context**: 本来 Day 28 原方案是 `ai-agent-prep/mcp-servers/`（和 projects/ 平级），用户选择嵌在 `projects/quant-research-copilot/mcp-servers/`。
- **Risk**: 每个 MCP server 必须独立 public GitHub repo（开源要求 + community registry 提交要求）。嵌套会导致 `git push` 默认只 push 整个主 repo。
- **Mitigation**:
  - Option A：每个 MCP server 子目录单独 `git init` + `git remote add`，**不**作为主 repo 的子目录提交（靠 `.gitignore` 排除 `mcp-servers/`）。主 repo 引用通过 `pip install -e ./mcp-servers/mcp-sec-edgar` 或绝对路径。
  - Option B：用 `git subtree split` 定期把子目录 push 到独立 GitHub repo。
  - **推荐 Option A** — 更简单，符合"3 个独立 repo"的开源语义。
- **Decision pending**：Stage 1.2 开工时确认。

### ADR-002 · Git 策略：单主 repo + 到时 `git subtree split`
- **Date**: 2026-04-22
- **Context**: Stage 1.1.d 要建 GitHub repo + push。mcp-servers/ 子目录未来必须以独立 public repo 开源。
- **Decision**: 今天先把整个 `quant-research-copilot/` 作为**单一主 repo** push 到 GitHub（包含 mcp-servers/ 子目录的历史）。等某个 MCP server 完成（Stage 2/3/4），再用 `git subtree split --prefix=mcp-servers/mcp-sec-edgar main -b sec-edgar-standalone` 把子目录的历史拆到独立分支，然后 push 到**另一个** public GitHub repo（`mcp-sec-edgar`）。
- **Why**: 今天就能 push 不被 Option A（每个子目录单独 git init）的 path 问题卡住；未来 3 个 MCP server 开源时的 `subtree split` 是一次性操作，不影响主 repo 开发节奏。
- **Risk**: 主 repo commit 里会包含 mcp-servers/ 的早期半成品代码；`subtree split` 出来的独立 repo 会包含这些"史前"commit。可以接受（开源前可以 rebase 清理）。

### ADR-004 · Root project declares the 3 MCPs as workspace dependencies
- **Date**: 2026-04-22
- **Context**: After 1.2.c, running `uv run python -c "import mcp_sec_edgar, mcp_fred_macro, mcp_backtest; ..."` from the workspace root failed with `ModuleNotFoundError`. Root cause: `uv sync` at the root only installs the root package's deps — workspace members aren't auto-installed unless (a) the root depends on them, or (b) you pass `--all-packages`. Each individual smoke check passed because running `uv run` *inside* a member dir syncs that specific member.
- **Decision**: Declare the 3 self-authored MCPs as `dependencies` of the root `quant-research-copilot` package, resolved via `[tool.uv.sources]` with `workspace = true`.
- **Why**:
  - Semantically accurate — the supervisor's runtime does require these MCPs (launched as stdio subprocesses by `langchain-mcp-adapters`); the binaries/modules must live in the same venv.
  - `uv sync` at root "just works" for every dev, no flag-memory burden.
  - Makes `uv run pytest` at root able to import across packages if needed (e.g. integration tests that spin up an MCP in-process).
- **Consequence**: Root `pyproject.toml` now has 3 deps + a `[tool.uv.sources]` block. When any MCP is eventually split out via `git subtree split`, the extracted repo is unaffected (source entries only apply at the workspace root).

### ADR-003 · Keep uv workspace (parent `[tool.uv.workspace]`)
- **Date**: 2026-04-22
- **Context**: `uv init --package mcp-sec-edgar` inside `mcp-servers/` auto-added a `[tool.uv.workspace]` block to the parent `pyproject.toml` listing the new sub-project as a member.
- **Decision**: Keep it.
- **Why**:
  - Single lockfile + shared cache + faster `uv sync` during development
  - Each sub-project's own `pyproject.toml` is already self-sufficient (standalone `[project]` with its own deps)
  - Future `git subtree split` to produce standalone open-source repos will naturally drop the parent workspace block — sub-repos stay clean
- **Consequence**: When adding 1.2.b and 1.2.c (fred-macro, backtest), uv will auto-append them to the workspace `members` list. That's expected and desired.

---

## ✅ Hand-write 规矩（Project 3 生效）

| 类型 | 谁来写 |
|------|--------|
| Python 代码（FastMCP / LangGraph / tool / adapter） | **Haichuan** |
| 测试代码（pytest） | **Haichuan** |
| YAML / Dockerfile / Docker Compose | **Haichuan** |
| pyproject.toml / .env.example / .gitignore | **Haichuan**（Claude 给结构清单） |
| 目录 mkdir/touch 命令 | **Haichuan** 执行（Claude 给蓝图） |
| DESIGN.md / README / 博客草稿 | **Claude 起草**，Haichuan review + 关键字段（AgentState schema / tool 签名）自己填 |
| eval 任务标注 / baseline 数据 | **Haichuan** |
| 架构图 Mermaid | **Claude 起草**，Haichuan 改 |

**Code review 三档**：
- 🟢 过 — 一句话 kudos
- 🟡 有问题 — 指问题 + 方向，**不给代码**
- 🔴 卡 >15 min 且精准描述 — 允许 <10 行最小修复示例 + 解释

**反 hand-write 的信号**（Claude 会拒绝）：
- "帮我写 xxx 这个 tool"
- "给我整个 yyy 的完整代码"
- "我不知道怎么开始，你写个例子"

---

## 🧰 Tool Inventory（5 MCP server · tool / resource / prompt 清单）

| # | Server | 状态 | Tools | Resources | Prompts | Extensibility |
|---|--------|------|-------|-----------|---------|---------------|
| 1 | **mcp-sec-edgar**（自写） | ⬜ | `list_tickers(index)` / `search_filings(ticker, form_type, limit)` / `get_filing_section(accession, section)` | `constituents://{index}/{date}` | — | `IndexRegistry` protocol |
| 2 | **mcp-fred-macro**（自写） | ⬜ | `search_series(keyword, limit)` / `get_series(series_id, start, end)` / `align_series(ids[], start, end, freq)` | `meta://{series_id}` | — | `ResamplePolicy` |
| 3 | **mcp-backtest**（自写） | ⬜ | `list_strategies()` / `run_backtest(strategy, universe, start, end, params)` / `get_backtest_result(run_id)` | `result://{run_id}` | — | `Strategy` Protocol |
| 4 | arxiv-mcp（社区） | ⬜ | `search_arxiv(query)` / `download_paper(arxiv_id)` | — | — | — |
| 5 | tavily-mcp（社区） | ⬜ | `tavily_search(query, max_results)` | — | — | — |

### Sub-agent ↔ MCP 绑定计划
- `research_reader` → arxiv-mcp + mcp-sec-edgar + tavily-mcp（新闻）
- `market_analyst` → mcp-fred-macro + mcp-backtest + tavily-mcp（宏观兜底）
- `memo_writer` → 不直接调 MCP（读 AgentState 合成 memo）
- `supervisor` → 不调 MCP（纯路由）

---

## 📝 Logs

| Timestamp | Stage | Event |
|-----------|-------|-------|
| 2026-04-22 | — | Project 3 正式开工。确认 hand-write mode 应用。13 Stage 路线图建立。进度板 `progress.md` 创建。 |
| 2026-04-22 | 1 | Stage 1 进入 in_progress。决议 `mcp-servers/` 嵌在主 repo 下（ADR-001）。 |
| 2026-04-22 10:17 | 1.1.a | ✅ `uv init --package` 成功（生成 pyproject.toml + .python-version + README.md 占位）。7 个顶层目录建好（src/ eval/ tests/ configs/ scripts/ mcp-servers/ + uv 自动包目录）。 |
| 2026-04-22 | 1.1.b | ✅ 选 Option B 标准 src-layout。agents/graph/mcp_clients 移入 `src/quant_research_copilot/`。所有 `__init__.py` 就位（4 src + tests + eval + eval/runners + configs）。 |
| 2026-04-22 | 1.1.c | ✅ `.gitignore` + `.env.example` created. Language switched to English from this point. |
| 2026-04-22 | 1.1.d | ✅ `git init` + first commit + GitHub public repo + push. Main repo is now remote-tracked. |
| 2026-04-22 | 1.2.a | ✅ `mcp-sec-edgar/` skeleton complete (13 files, 5 sub-packages). uv auto-added `[tool.uv.workspace]` to parent pyproject.toml; kept per ADR-003. |
| 2026-04-22 | 1.2.b | ⚠ Cleanup: stray `mcp-servers/src/mcp_fred_macro/{cache,registries,resources,tools}/` created by wrong-CWD `mkdir` — removed via `rmdir` bottom-up. Glob miss (empty dirs invisible to Glob) logged as a lesson. |
| 2026-04-22 | 1.2.b | ✅ `mcp-fred-macro/` skeleton re-created at correct path. `diff` against sec-edgar file list shows only package-name swap. Boilerplate files done: `.env.example` (7 lines), `LICENSE` (copied from sec-edgar, identical), `.github/workflows/ci.yml` (29 lines, standalone-repo style, identical for both packages). Remaining: `server.py` + `tests/test_smoke.py` (hand-write). |
| 2026-04-22 | 1.2.b | ✅ **DONE**. `server.py` hand-written (docstring + `FastMCP(name=...)` + `@mcp.tool def ping() -> dict[str, str]` returning `{"status": "ok", "server": mcp.name}` + `main()` + entrypoint guard). `__init__.py` re-exports `main`. `uv add fastmcp` → fastmcp 3.2.4. Smoke check ✅ (`FastMCP('mcp-fred-macro')` instance printed). Lesson learned: editable install can get half-broken after `uv add` — recover via `uv sync --reinstall-package`. |
| 2026-04-22 | 1.2.c | ✅ **DONE**. `mcp-backtest` scaffolded end-to-end: `uv init --package`, 4 subpackage dirs (no middleware — yfinance needs no rate-limit), LICENSE + CI copied from fred-macro (identical templates), `.env.example` commented-only (no required secrets), `server.py` + `__init__.py` written in same five-section shape as fred-macro. `uv add fastmcp` + smoke check ✅ `FastMCP('mcp-backtest')`. Workspace `members` now lists all 3 MCPs. |
| 2026-04-22 | 1.2.a (parity) | ✅ **DONE**. `mcp-sec-edgar/server.py` + `__init__.py` rewritten to same ping-stub shape as fred-macro/backtest. Smoke check ✅ `FastMCP('mcp-sec-edgar')`. |
| 2026-04-22 | 1.2 (final) | ⚠→✅ Triple-import test from workspace root initially failed (`ModuleNotFoundError`). Root cause: root project didn't declare MCPs as deps, so `uv sync` at root skipped them. Fix: ADR-004 — add 3 MCPs as `dependencies` + `[tool.uv.sources]` with `workspace = true`. After `uv sync`, triple import ✅ all three `main` functions printed. **Stage 1.2 fully closed.** |

---

## 🎯 下一步（由 Claude 给 → Haichuan 执行 → 回来报完成）

**Next micro-step: 1.3** — DESIGN.md v0.1 draft. Claude proposes an outline first (sections + purpose of each), Haichuan confirms/edits scope, then Claude drafts. Haichuan hand-writes: (a) `AgentState` TypedDict fields, (b) tool signatures for the 3 self-authored MCPs. Claude drafts everything else.
