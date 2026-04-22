# MCP → Project 3 (quant-research-copilot) 映射

> 学完课程后填。目标：把每个 MCP 概念落到 Project 3 的具体实现上。
> **Pivoted 2026-04-17**: 从原 "DevOps Intelligence Agent" 方向整体转向 `quant-research-copilot`。

## Project 3 架构回顾

- **Product:** 量化研究副驾驶 — 输入一个 ticker 或主题，输出带引用的研究备忘（research memo）
- **1 个 Supervisor Agent** — LangGraph `create_supervisor` 路由用户 query 到 3 个 sub-agent
- **3 个 Sub-agents:**
  - `research_reader` — 读 SEC 文件 + arxiv 论文
  - `market_analyst` — 读 FRED 宏观 + 价格 + backtest
  - `memo_writer` — 合成带引用的研究备忘
- **5 个 MCP servers（3 自写 + 2 社区）:**
  - 自写 #1 `mcp-sec-edgar` — SEC EDGAR 10-K/10-Q/8-K（`IndexRegistry` 抽象：SP500 默认 + Russell1000/自定义扩展位）
  - 自写 #2 `mcp-fred-macro` — FRED macro series（`ResamplePolicy` 抽象：daily/weekly/monthly + 自定义规则）
  - 自写 #3 `mcp-backtest` — vectorbt 动量回测（`Strategy` Protocol：momentum MVP + mean-reversion/pairs 预留）
  - 社区 #4 `arxiv-mcp` — 学术论文检索
  - 社区 #5 `tavily-mcp` — 新闻 / 宏观 web search
- **时间：** Week 5–8（2026-04-17 → 2026-05-14）
- **三轴差异化：** ① 自写 3 个 MCP server 并发社区 registry ② 40-task eval + Supervisor/ReAct/Swarm 三架构对比 ③ 量化金融 niche 领域

## 概念映射表

| MCP 概念 | 在 Project 3 中怎么用 | 哪个 sub-agent 用到 |
|---------|---------------------|-------------------|
| Tools (model-controlled) | `get_filings(ticker, form_type)` / `get_series(series_id, resample)` / `run_backtest(strategy, universe, params)` — LLM 自主决定何时调用 | 全部 3 个 sub-agent |
| Resources (app-controlled) | 把 SP500 constituents、FRED 关键 series 白名单作为 resource 暴露 — Supervisor 启动时一次性加载到 context | Supervisor 层 |
| Prompts (user-controlled) | `/daily-briefing`、`/ticker-report` 作为 slash-prompt 暴露给前端 — 用户显式触发固定 prompt 模板 | memo_writer |
| Inspector | 写每个 server 的 MVP 后，先用 Inspector（MCP 版 Postman）跑一遍 list_tools/call_tool/read_resource，再接 LangGraph | 开发期全部 |
| Transport（stdio vs HTTP） | 本地开发 stdio；Docker Compose / Railway 部署切 HTTP(Streamable HTTP)；5 个 server 都支持双模 | 部署层 |

## 5 个 MCP server 选型决策

| Server | 官方/社区/自写 | 暴露的关键 tool/resource/prompt | 接给哪个 sub-agent |
|--------|-----------|-------------------------------|-----------------|
| 1. mcp-sec-edgar | **自写** | **Tools:** `list_tickers(index)`, `get_filings(ticker, form_type, n)`, `get_section(filing_id, section)` · **Resources:** `indexes/sp500.json` · **Ext:** `IndexRegistry` | research_reader |
| 2. mcp-fred-macro | **自写** | **Tools:** `get_series(series_id, start, end, resample)`, `list_series()` · **Resources:** `series/whitelist.json`（CPI/UNRATE/FEDFUNDS 等）· **Ext:** `ResamplePolicy` | market_analyst |
| 3. mcp-backtest | **自写** | **Tools:** `run_backtest(strategy, universe, params)` · **Resources:** `strategies/registry.json` · **Ext:** `Strategy` Protocol | market_analyst |
| 4. arxiv-mcp | 社区 | **Tools:** `search_arxiv(query)`, `download_paper(arxiv_id)` | research_reader |
| 5. tavily-mcp | 社区 | **Tools:** `tavily_search(query, max_results)` | research_reader（新闻）/ market_analyst（宏观 fallback）|

## Extensibility 抽象预留（每个自写 server 必做）

- `mcp-sec-edgar`：`IndexRegistry` protocol，默认实现 `SP500Index`；未来可注册 `Russell1000Index` / `CustomTickerListIndex`
- `mcp-fred-macro`：`ResamplePolicy` strategy，默认 `PandasResamplePolicy('M')`；预留自定义 rule
- `mcp-backtest`：`Strategy` Protocol，默认 `MomentumStrategy(lookback=12, holding=1)`（Jegadeesh & Titman 1993）；预留 `MeanReversionStrategy` / `PairsTradingStrategy` slot

## 风险 & 待解决问题

- SEC EDGAR 对 User-Agent 要求严格（email + app-name），server 必须允许注入
- FRED API 限速 120 req/min，需要内建限速 + LRU cache
- vectorbt 对大 universe 内存开销不小，MVP 先限 SP500 + 月频；HITL interrupt 在长 backtest 时触发人工审核
- MCP 社区 registry PR review 周期可能 > 1 周，Week 8 结尾的"registry 合并确认"如滑档则降级为"PR 已提交 + 截图进 README"
- Resume 同期展示 3 个独立 repo + 1 个主 repo 可能让 recruiter 眼花 → README 一开始就放 4-repo 架构图
