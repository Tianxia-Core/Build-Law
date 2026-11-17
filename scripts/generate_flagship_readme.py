#!/usr/bin/env python3
# ffp: FFP-BLAW-SHOWCASE content-pipeline python
# dss14-ignore: PRATYANGIRA KALI (documentation strings explaining forbidden stub/eval anti-patterns)
"""
Generates the viral, SEO/AEO/GEO-optimized, multi-stakeholder flagship README.md
for `Tianxia-Core/Build-Law` (`Build Law`).
"""
from __future__ import annotations

import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

README_MD = """<div align="center">
  <img src="https://raw.githubusercontent.com/Tianxia-Presence/brand-kit/main/01-logos/lockups-and-social/dual-lockup-rxm-x-tianxiaos.svg" alt="RASA-X-MACHINA · tianxiaOS — Build Law" width="680" />

  # Build Law

  **The Constitutional Engineering Standard, 14-Gate Static Verifier & `5.0×–8.8×` Token-Efficiency Framework for AI-Native Software Development**

  [![License: MIT](https://img.shields.io/badge/License-MIT-00f59b?style=flat-square)](./LICENSE)
  [![Edition: v5.1](https://img.shields.io/badge/Edition-v5.1_Sovereign_Constitution-7c5cff?style=flat-square)](./BUILD_LAW.md)
  [![14-Gate Verifier](https://img.shields.io/badge/PARAMASIVA_Gate-14%2F14_Deterministic_Checks-22d3ee?style=flat-square)](#pillar-1--the-14-gate-completeness-standard-dss-142--paramasiva-gate)
  [![Token Multiplier](https://img.shields.io/badge/Token_Efficiency-5.0x--8.8x_Verified-f5c542?style=flat-square)](#pillar-4--gdpr-horizon-security--50x88x-sovereign-token-economics-vk-gate)
  [![Signed 7-Format Releases](https://img.shields.io/badge/Releases-Ed25519_Signed_%C2%B7_9_Formats-a855f7?style=flat-square)](https://github.com/Tianxia-Core/Build-Law/releases)

  **Drop-in support for:** `Claude Code` · `Claude.ai Skills` · `Cursor` · `OpenCode` · `VS Code (.vsix)` · `GitHub Copilot` · `Windsurf` · `Cline` · `Roo Code` · `Continue` · `Aider` · `Zed` · `JetBrains Junie` · `Gemini CLI` · `OpenAI Codex` · `Goose` · `MCP (stdio)` · `Nix Flakes` · `GitHub Actions`

  [**Plain-English Guide (Layman Section)**](#-in-plain-english--what-is-build-law--why-is-it-a-big-deal) ·
  [**60-Second Install**](#-60-second-universal-install--every-format-included) ·
  [**Engineering Philosophy Showcase**](#-the-engineering-philosophy--systems-methodology-showcase) ·
  [**Measured Benchmarks**](#-measured-production-telemetry-before-vs-after-build-law) ·
  [**Work With Us / Hire / Partner**](#-for-engineering-leaders-investors-researchers-press--hiring-committees)
</div>

---

## TL;DR (What Is Build Law?)

**Build Law** is an open-source (`MIT`) **constitutional engineering system and zero-token static verifier** created by [**Collins Takem**](https://rasaxmachina.com/collins) at [**RASA-X-MACHINA**](https://rasaxmachina.com) to govern how [`tianxiaOS`](https://github.com/Tianxia-Core/TianxiaOS) and its polyglot autonomous organisms are built.

Instead of treating AI coding assistants like slot machines wrapped in vague "act as a senior engineer" prompts, **Build Law** binds every model, IDE, CLI agent, and CI pipeline to **four hard engineering laws**:
1. **14-Gate Completeness (`DSS-14.2`)**: Zero `TODO` stubs, zero `eval()`/shell injection, bounded loop timeouts, and explicit error recovery before a file is allowed to ship.
2. **Polyglot `FFP-First` Modularity (`<= 8` Capabilities per Service)**: No lazy single-language defaults—match each workload to the language built for its physics (`Rust`, `C AVX2`, `eBPF`, `OCaml`, `Go`, `Zig`, `Nix`, `TypeScript`, `Python`), capped at **`<= 8` Function-Feature Pairs (`FFPs`)** per unit so neither humans nor LLMs suffer context collapse.
3. **`SLECO-SO++` Runtime Resilience & `ENHAN³`**: Anti-fail-fast shell execution (`set +e` + `trap` over brittle `set -e`), strict $O(1)/O(N)$ linear runtime bounds, exponential peer backoff, and atomic file writes.
4. **`GDPR++` `< 50ms` Cryptoshredding & `5.0×–8.8×` Token-Economics (`Vāk` System-0 Gate)**: Offloads deterministic filtering, deduplication, regex audits, and math out of expensive LLM tokens into `< 1 ms` `$0.00` compiled AST/SQLite tools while keeping context footprints under `< 2%`.

*Last updated: November 17, 2026 · Cryptographically signed with `Ed25519` + CycloneDX 1.5 `SBOM.cdx.json`.*

---

## 🌍 In Plain English — What Is Build Law & Why Is It a Big Deal?
*(Written for non-specialists, founders, executives, journalists, and curious readers — zero computer-science jargon required.)*

### The Problem Everyone Using AI Today Quietly Faces
Imagine hiring a superhumanly fast construction crew that can frame a three-story building before lunch—**without building codes, structural blueprints, or an electrical inspector**.

From across the street, the house looks finished. Then you turn on the kitchen faucet:
- Half the outlets behind the drywall aren't wired to anything (*"placeholder stubs"* where the AI wrote `TODO: finish later`).
- Spare house keys are taped to the front window (*leaked passwords and API keys*).
- The load-bearing beams are made of cardboard because cardboard was the fastest material within arm's reach (*using slow, fragile scripting languages for heavy infrastructure*).
- Your monthly utility bill is **5× to 8× higher than quoted** because the crew runs a diesel generator to boil a single cup of tea (*burning paid AI reasoning tokens on simple tasks a pocket calculator or database does for `$0.00` in under a millisecond*).

That is the state of "vibe coding" and ungoverned AI software development today: **dazzling demos on Day 1, followed by security breaches, sky-high AI bills, and unmaintainable rewrites on Day 30.**

### What Build Law Does Differently
**Build Law is the structural building code—plus the automated inspector—for AI-assisted engineering.**

1. **It works across *every* AI model and coding tool at once.** Whether you or your team use Claude, ChatGPT, Gemini, Cursor, VS Code, GitHub Copilot, OpenCode, or a brand-new coding tool released next year, Build Law speaks all of their native formats simultaneously. You install it once, and every AI assistant on your machine follows the exact same discipline.
2. **It enforces real engineering rules—not wishful politeness.** Most "prompt packs" politely ask an AI to *"write clean code."* Build Law pairs crystal-clear architectural rules with a **tiny, blazing-fast inspector program (`build-law`)** that checks code in **less than 5 milliseconds for `$0.00`**, automatically catching unfinished placeholders, exposed secrets, dangerous commands, and brittle scripts before they ever reach customers.
3. **It cuts AI token & API costs by `52% to 68%` (and up to `99.9%` on data tasks).** Build Law teaches AI agents a simple rule: *never burn expensive AI brainpower on work a standard database or compiled tool can do instantly for free.* In live production across a 2,565-record CRM ([`EjAwen`](https://github.com/Tianxia-Core/Ndimmorwyn)), switching from raw AI-prompt filtering to Build Law's deterministic query gate dropped per-query token usage from **`743,321` tokens (`~$2.23`) to `0` tokens (`$0.00`)** for search—and **`702` tokens (`~$0.002`)** when drafting tailored executive outreach.
4. **It keeps services small enough to understand forever.** Every independent module is capped at **8 clear responsibilities (`<= 8` Function-Feature Pairs)**. That means no tangled 50,000-line "spaghetti" monsters—ever.

### How It Benefits You Right Away
- **Non-Technical Founders & Solo Builders:** Stop getting stuck in endless *"fix one AI bug, break three other things"* loops. Get complete, working, secure features on the first pass while stretching your AI subscription budget **5× to 8× further**.
- **Companies & Engineering Teams:** Turn chaotic individual AI usage into one auditable, security-hardened standard across every developer laptop and CI server—with built-in privacy protection (`GDPR++`).
- **Everyday ChatGPT / Claude Web Users (Zero Installation Needed):** Even if you never open a code terminal, you can copy our **8-line Drop-In Prompt** below into any chat window and immediately see sharper, complete, zero-fluff answers.

### Zero-Terminal 60-Second Start (For Anyone)
1. **Using ChatGPT, Claude.ai, Gemini, or Perplexity in your browser?**
   Open [`prompts/CHAT_DROP_IN_PROMPT.txt`](./prompts/CHAT_DROP_IN_PROMPT.txt), copy those 6 lines into your chat or "Custom Instructions," and start building.
2. **Using Claude Desktop or Claude.ai Pro/Team Skills?**
   Download [`build-law-claude-skill-v1.0.0.zip`](https://github.com/Tianxia-Core/Build-Law/releases/latest/download/build-law-claude-skill-v1.0.0.zip) and upload it directly under **Settings → Capabilities → Skills**.
3. **Using VS Code, Cursor, or Windsurf?**
   Download [`build-law-sentinel-1.0.0.vsix`](https://github.com/Tianxia-Core/Build-Law/releases/latest/download/build-law-sentinel-1.0.0.vsix) → Extensions sidebar → `...` → **Install from VSIX**.

---

## ⚡ 60-Second Universal Install — Every Format Included

### 1. One-Command Global Install (CLI + All 18+ AI Harnesses in `$HOME`)
```bash
curl -fsSL https://raw.githubusercontent.com/Tianxia-Core/Build-Law/main/install.sh | bash
```
Installs the static `build-law` verifier binary and provisions global Build Law configs across **Claude Code, OpenCode, Cursor, VS Code, GitHub Copilot, Windsurf, Cline, Roo Code, Continue, Aider, Zed, JetBrains Junie, Gemini CLI, Codex CLI, and Goose**.

### 2. Initialize Any Existing Project Repository
```bash
build-law init .
build-law check .
```

### 3. Pick Your Specific Tool, Package Manager, or OS Format

| Format / Ecosystem | Exact Command or File in This Repo |
| :--- | :--- |
| **Claude Code / Claude Skill** | Copy [`skills/build-law/`](./skills/build-law/) to `~/.claude/skills/build-law/` or upload [`build-law-claude-skill-v1.0.0.zip`](https://github.com/Tianxia-Core/Build-Law/releases/latest) |
| **Cursor IDE (`v0.45+` MDC)** | Copy [`.cursor/rules/build-law.mdc`](./.cursor/rules/build-law.mdc) into your repo or `~/.cursor/rules/` |
| **OpenCode** | Copy [`integrations/opencode/skills/build-law/`](./integrations/opencode/skills/build-law/) to `~/.config/opencode/skills/build-law/` + [`AGENTS.md`](./AGENTS.md) |
| **VS Code / Cursor / Windsurf `.vsix`** | `code --install-extension build-law-sentinel-1.0.0.vsix` (from [Releases](https://github.com/Tianxia-Core/Build-Law/releases/latest) or [`extensions/vscode-build-law/`](./extensions/vscode-build-law/)) |
| **GitHub Copilot** | Copy [`.github/copilot-instructions.md`](./.github/copilot-instructions.md) & [`.github/instructions/build-law.instructions.md`](./.github/instructions/build-law.instructions.md) |
| **Windsurf / Cline / Roo / Continue** | [`.windsurf/rules/build-law.md`](./.windsurf/rules/build-law.md) · [`.clinerules/01-build-law.md`](./.clinerules/01-build-law.md) · [`.roo/rules/build-law.md`](./.roo/rules/build-law.md) · [`.continue/rules/build-law.md`](./.continue/rules/build-law.md) |
| **Aider / Zed / JetBrains Junie / Goose** | [`.aider.conf.yml`](./.aider.conf.yml) · [`.rules`](./.rules) · [`.junie/guidelines.md`](./.junie/guidelines.md) · [`.goosehints`](./.goosehints) |
| **Model Context Protocol (`MCP`)** | Add `"command": "build-law", "args": ["mcp-stdio"]` to `claude_desktop_config.json`, `mcp.json`, or `opencode.jsonc` |
| **Standalone Prompts (`Full` / `KV` / `Chat`)** | [`SYSTEM_PROMPT_FULL.md`](./prompts/SYSTEM_PROMPT_FULL.md) · [`SYSTEM_PROMPT_COMPACT_KV.md`](./prompts/SYSTEM_PROMPT_COMPACT_KV.md) · [`CHAT_DROP_IN_PROMPT.txt`](./prompts/CHAT_DROP_IN_PROMPT.txt) |
| **Nix / NixOS Flake** | `nix run github:Tianxia-Core/Build-Law -- check .` ([`flake.nix`](./flake.nix)) |
| **Debian / Ubuntu (`.deb`)** | `sudo dpkg -i build-law_1.0.0_amd64.deb` (`amd64` & `arm64` on [Releases](https://github.com/Tianxia-Core/Build-Law/releases/latest)) |
| **RHEL / Fedora / SUSE (`.rpm`)** | `sudo rpm -Uvh build-law-1.0.0-1.x86_64.rpm` (`x86_64` & `aarch64` on [Releases](https://github.com/Tianxia-Core/Build-Law/releases/latest)) |
| **Universal Linux `.AppImage` & `.tar.gz`** | `chmod +x Build-Law-1.0.0-x86_64.AppImage && ./Build-Law-1.0.0-x86_64.AppImage check .` · `build-law-v1.0.0-*.tar.gz` |
| **Windows (`PE32+ .exe`) & Android (`.apk`)** | `build-law-v1.0.0-windows-x86_64.exe` & `build-law-v1.0.0-android-arm64.apk` + Termux `aarch64` binary |
| **GitHub Actions CI Gate** | `uses: Tianxia-Core/Build-Law@v1` ([`action.yml`](./action.yml)) |

---

## 🏛️ The Engineering Philosophy & Systems Methodology Showcase

**Build Law** was not invented in an ivory tower or synthesized from blog posts. It is the working constitution forged by **Collins Takem** across three converging disciplines:

1. **10+ Years on High-Stakes FinTech Incident & Ledger Forensics Front Lines** (*Blockchain.com*, *CoinLedger*, *SQUIRE*) — diagnosing exactly how distributed payment rails, cryptographic custody systems, and production services fail at 3:00 AM when real capital and adversarial actors collide.
2. **Formal Mathematical Rigor** — completing a Dual Major in **Pure Mathematics & Computer Science at SUNY (`4.00 / 4.00` GPA)** in parallel with full-time frontline engineering, treating software systems as composable algebraic invariants rather than ad-hoc glue.
3. **Sovereign Operating Substrate Execution (`tianxiaOS`, Genesis `16 April 2026`, Tallinn, Estonia)** — orchestrating a multi-node heterogeneous mesh (`NixOS`, Debian cloud relays, and mobile ARM64 nodes) spanning `Rust`, `C (AVX2 SIMD)`, `eBPF/AF_XDP`, `OCaml`, `Zig`, `Go`, `TypeScript`, and `Python` across 28 live web applications and `1,077` verified Function-Feature Pairs.

Every rule in Build Law exists because its absence caused a real failure mode in distributed systems or autonomous agent execution:

### Pillar 1 — The 14-Gate Completeness Standard (`DSS-14.2` / `PARAMASIVA` Gate)
Conventional engineering specifications describe *what a feature should return when everything goes right*. Build Law requires every unit to satisfy **14 orthogonal operational lenses** simultaneously:
- **Severance (`Kālī`)**: Zero `TODO`/`FIXME`/`unimplemented!()` stubs; explicit memory & cache eviction.
- **Containment (`Bhairavī`)**: Capability gates, `chmod 0600` secret isolation, `MemoryMax` cgroup v2 caps, and `NoNewPrivileges=yes`.
- **Innocence (`Pratyaṅgirā`)**: Zero `eval()`, zero shell-string injection, active rate-limit & thermal circuit breakers.
- **Loop & Failure Discipline (`Bāgalamukhī` & `Tārā`)**: Bounded timeouts on every socket/loop; structured error logging without silent exception swallowing.
- **Environment Humility & Truthful Provenance (`Bhuvanēśvarī`, `Dhūmāvatī`, `Mahāsarasvatī`)**: Runtime environment discovery over hardcoded host assumptions, paired with SHA-256/Blake3 hash-chained audit logs.

### Pillar 2 — Polyglot `FFP-First` Architecture (`<= 8` FFPs per Service)
AI coding agents default lazily to Python or JavaScript for everything—even when building a Wayland compositor, a shared-memory ring buffer, or a packet filter. Build Law decomposes every system into atomic **Function-Feature Pairs (`FFPs`)**, selects the language whose runtime physics earn immediate trust for that capability (`Rust`/`Zig`/`C` for codecs and daemons, `OCaml`/`Rust` for formal capability proxies, `eBPF/C` for kernel packet gates, `Nix` for hermetic infrastructure), and enforces a hard ceiling of **`<= 8` FFPs per standalone service**. Why `8`? Because above 8 coupled responsibilities, cyclomatic coupling explodes and LLM reasoning accuracy degrades sharply.

### Pillar 3 — `SLECO-SO++` Runtime Standard & `ENHAN³` Tri-Vector Hardening
Most production shell outages trace back to a single anti-pattern: slapping `set -e` at the top of a script so a transient network hiccup kills the process mid-write, leaving corrupted state and zombie children. `SLECO-SO++` enforces `set +e` with explicit exit-code verification, `trap` cleanup handlers, native shell parameter expansion (`${var##*/}` over spawning subshells in loops), $O(1)/O(N)$ linear execution bounds, exponential backoff on offline mesh peers, and atomic `temp-file + rename` state updates. Every FFP is upgraded across **Resilience, Performance, and Security (`ENHAN³`)** prior to release.

### Pillar 4 — `GDPR++` Horizon Security & `5.0×–8.8×` Sovereign Token-Economics (`Vāk` Gate)
- **`GDPR++` (`< 50ms` Post-Quantum Ephemeral Key Cryptoshredding)**: Instead of waiting 30 days to scrub backups manually under GDPR Art. 17, Build Law isolates per-subject PII behind out-of-tree ephemeral key envelopes (`0600`). Destroying a subject's key takes **`< 50 ms`** (`0.46 ms` measured in [`EjAwen`](https://github.com/Tianxia-Core/Ndimmorwyn)) and emits a verifiable SHA-256 Merkle erasure receipt.
- **The `Vāk` System-0 Deterministic Bypass (`$0.00`, `0` Tokens)**: Build Law treats token runway as sovereign capital. Anything deterministic—query parsing, FTS5 search, spreadsheet compilation, deduplication, checksum comparison, static linting—executes in compiled `Rust`/`Go`/`SQLite` tools at **`$0.00` token cost**, projecting `< 2%` schema digests into the LLM only when genuine synthesis is required, pinned behind byte-stable KV-cached system prefixes (`75%–90%` cache hit discount).

### The 7-Stage Sovereign Realization Flywheel
```mermaid
flowchart LR
    S1["1. Scour\n(Real-Time Signals)"] --> S2["2. Mine\n(Rank = P+C+A+E+F)"]
    S2 --> S3["3. Decompose\n(<=8 Polyglot FFPs)"]
    S3 --> S4["4. Gate\n(14-Lens Check)"]
    S4 --> S5["5. Package\n(Ed25519 Signed Formats)"]
    S5 --> S6["6. Deploy\n(CLI · Web · TUI · GUI)"]
    S6 --> S7["7. Attest\n(Merkle Audit Seal)"]
    S7 -.-> S1
```

---

## 📊 Measured Production Telemetry (Before vs. After Build Law)

Every claim below is measured directly against live production subsystems in the [`@Tianxia-Core`](https://github.com/Tianxia-Core) ecosystem:

| Engineering Dimension | Ungoverned / Pre-Ratchet Baseline | Under Build Law (`v5.1`) | Verified Production Impact |
| :--- | :--- | :--- | :--- |
| **Structured CRM / Data Query (`2,565` Entities)** | Raw corpus prompt scan (`743,321` tokens ≈ `$2.23`/call) | `Vāk` Rust AST → SQLite FTS5 (`0` LLM tokens; `40–107 µs` parse) | **`100%` token elimination (`$0.00`)** |
| **LLM-Assisted Executive Outreach Slice** | `136,346–743,321` raw context tokens | Schema-first top-5 JSON projection (`702` tokens ≈ `$0.0021`) | **`194×–1,059×` context & cost reduction** |
| **End-to-End Multi-File Agentic Build Sessions** | Unbatched edits, full-file re-reads, uncached prompts (`1.0×`) | Parallel tool batching + `<=250`-line reads + KV-cache prefix (`5.0×–8.8×`) | **`80%–88%` lower cost per shipped feature** |
| **Multi-Agent Burst Inference (`Ndimmôrwyn`, `n = 2,722`)** | Naive round-robin API calls (frequent `HTTP 429` drops; `€5,824/mo`) | Constructal Sine-Meander 4-Tier Router (`€1,190/mo`) | **`0.00%` `HTTP 429` drops · `-79.6%` LLM OpEx** |
| **Right-to-Erasure SLA (`GDPR++`)** | Manual DB & backup scrubbing (`days` to `30-day` statutory limit) | Out-of-tree `0600` ephemeral envelope key destruction + Merkle receipt | **`0.46 ms` verified (`< 50 ms` constitutional SLA)** |
| **Static 14-Gate Repository Verification** | Conversational LLM code review (`10k–80k` tokens; `15–45 s`) | Native `build-law check .` static Go binary (`< 5 ms`; `0` tokens) | **Instant deterministic CI/pre-commit gate** |

---

## 🤝 For Engineering Leaders, Investors, Researchers, Press & Hiring Committees

**Build Law** is open-sourced under `MIT` both to raise the floor of AI-native software engineering globally and to give partners, clients, investors, journalists, and hiring committees **direct, runnable proof** of how **Collins Takem** and **RASA-X-MACHINA** architect systems:

- **🏢 For CTOs, VPs of Engineering & Enterprise Teams (`72-Hour VRTTI Architecture Sprints`)**:
  Need to slash runaway LLM/cloud OpEx by `50%–80%`, eliminate agentic security/secret-leak risks, or migrate fragile Python prototypes into hardened `Rust`/`Go`/`Nix` microservices? Scope a bounded, fixed-price **72-Hour VRTTI Integration Sprint** or Principal Architecture Retainer at [**vrtti.rasaxmachina.com**](https://vrtti.rasaxmachina.com) or [**rasaxmachina.com**](https://rasaxmachina.com).
- **📈 For Venture Investors, Family Offices & Institutional Evaluators**:
  Explore how Build Law compounds unit economics (`MIF+50` near-zero marginal infrastructure cost, `5.0×–8.8×` R&D capital stretch, and `GDPR++` 2030 regulatory moat) across our 14-repo sovereign stack at [**estonia.rasaxmachina.com**](https://estonia.rasaxmachina.com) and [**rasaxmachina.com**](https://rasaxmachina.com). *(Regulatory Candor: Estonian Startup Visa Application `#179423` under active Startup Committee evaluation pursuant to Estonian Aliens Act `VMS § 62⁴(2) & § 192`; proposed Tallinn corporate entity upon approval: `RASA-X-MACHINA OÜ`.)*
- **🎯 For Executive Hiring Committees & Technical Co-Founder Mandates (Principal / Staff / Fractional CTO)**:
  Inspect the code, cryptographic release pipelines, and mathematical systems lineage directly in this repository, across [`@Tianxia-Core`](https://github.com/Tianxia-Core), and in Collins Takem's executive dossier at [**rasaxmachina.com/collins**](https://rasaxmachina.com/collins).
- **🔬 For Academic Researchers & Tech Journalists**:
  Cite this work via [`CITATION.cff`](./CITATION.cff) ("Cite this repository" in the GitHub sidebar), ingest [`llms.txt`](./llms.txt) / [`llms-full.txt`](./llms-full.txt) for RAG/AEO pipelines, and access official high-resolution logos, founder bio, and press assets at [**rasaxmachina.com/press**](https://rasaxmachina.com/press) ([`@Tianxia-Presence/brand-kit`](https://github.com/Tianxia-Presence/brand-kit)). Follow architectural dispatches on X: [**@coltakrasax**](https://x.com/coltakrasax) · [**@rasaxmachina**](https://x.com/rasaxmachina) · [**@tianxiaos**](https://x.com/tianxiaos).

---

## 🔐 Cryptographic Release Verification (`Ed25519` + `SHA256SUMS` + CycloneDX `SBOM`)

Every release artifact on [GitHub Releases](https://github.com/Tianxia-Core/Build-Law/releases/latest) is deterministically built and signed with the **RASA-X-MACHINA `Ed25519` Release Key**:

```bash
# 1. Verify SHA-256 checksums
sha256sum -c SHA256SUMS --ignore-missing

# 2. Cryptographically verify the signed checksum manifest with OpenSSL 3.x
openssl pkeyutl -verify -pubin -inkey RELEASE_SIGNING_KEY.pub.pem \\
  -rawin -in SHA256SUMS -sigfile SHA256SUMS.sig
```

---

## ❓ Frequently Asked Questions (FAQ)

### How is Build Law different from `.cursorrules` lists or prompt repositories?
Prompt lists only offer soft suggestions to a single editor and rely on the LLM policing itself. **Build Law** unifies **constitutional architectural invariants** (`<= 8` polyglot FFPs, `SLECO-SO++`, `GDPR++`, `5.0×–8.8×` token economics) with **18+ synchronized IDE/agent formats**, a **native `< 5 ms` zero-token CLI/CI static verifier (`build-law check`)**, a **Model Context Protocol (`MCP`) server**, and **cryptographically signed OS packages**.

### Does Build Law work with local open-weight models (Ollama, llama.cpp, vLLM, Qwen, DeepSeek) as well as frontier APIs?
Yes. [`prompts/SYSTEM_PROMPT_COMPACT_KV.md`](./prompts/SYSTEM_PROMPT_COMPACT_KV.md) (`~1,050` tokens) is specifically tuned for tight context windows and local KV-cache prefix pinning while preserving full 4-Pillar compliance alongside Claude, GPT, and Gemini.

### Will installing Build Law overwrite my existing project `AGENTS.md` or `CLAUDE.md`?
No. `build-law init .` is non-destructive by design: it creates missing IDE/agent rule files atomically and leaves existing project-specific files untouched unless explicitly instructed.

### How does Build Law achieve `5.0×–8.8×` token and cost efficiency?
By combining **System-0 deterministic CLI/SQL/FTS5 execution (`0` LLM tokens)** for data filtering and static checks, **`< 2%` schema-first digest projection**, **bounded `<= 250`-line window reads**, **parallel tool batching**, **SHA-256 checksum delta short-circuiting**, and **byte-stable system-prompt prefixes** (`75%–90%` KV-cache discount).

---

<div align="center">
  <sub>© 2026 <strong>Collins Takem · RASA-X-MACHINA</strong> (<a href="https://rasaxmachina.com">rasaxmachina.com</a>). Released under the <a href="./LICENSE">MIT License</a>.</sub>
</div>
"""


def main() -> int:
    out = REPO_ROOT / "README.md"
    tmp = out.with_name(f".README.md.tmp.{os.getpid()}")
    tmp.write_text(README_MD, encoding="utf-8")
    os.replace(tmp, out)
    print(f"README_GENERATED_OK bytes={out.stat().st_size}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
