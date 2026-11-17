---
name: build-law
description: Use when designing, writing, refactoring, auditing, packaging, or deploying any software, script, database, UI, or AI agent workflow to enforce 14-gate architectural completeness, polyglot FFP<=8 modularity, SLECO-SO++ runtime resilience, GDPR++ security, and 5x-8.8x token efficiency.
metadata:
  author: Collins Takem (RASA-X-MACHINA)
  version: "5.1.0"
  category: architecture-governance
  triggers: build-law, architecture, production-ready, zero-stubs, polyglot, security-audit, token-efficiency, sleco, dss-14
---

# Build Law — Autonomous Engineering & Token-Efficiency Skill

You are operating under **Build Law v5.1** (architected by Collins Takem · **RASA-X-MACHINA**). Apply these invariants automatically before writing code, plans, scripts, or reviews.

## When to Activate
- Designing or implementing any new feature, service, CLI, daemon, database, or web app
- Writing shell scripts, CI pipelines, Docker/Nix configs, or deployment automation
- Auditing PRs, hardening security/privacy boundaries, or cutting LLM token/API spend

## Core Invariants (The 4 Pillars)

1. **Pillar 1 — 14-Gate Completeness (`PARAMASIVA` Gate)**:
   - **Zero Placeholders**: Never emit `TODO`, `FIXME`, `pass`, `todo!()`, `unimplemented!()`, or truncated code blocks.
   - **Execution Innocence**: Zero `eval()`, zero shell string interpolation (`subprocess` uses list argv with `shell=False`), bounded timeouts on every loop and network call.
   - **Graceful Recovery**: Log errors with structured context and recover cleanly; never swallow exceptions silently.
   - Deep reference: see [references/fourteen-gates.md](references/fourteen-gates.md).

2. **Pillar 2 — Polyglot `FFP-First` Modularity (`<= 8` FFPs per Service)**:
   - Decompose systems into atomic **Function-Feature Pairs (`FFPs`)**, strictly `<= 8` FFPs per service/unit.
   - Match language physics to workload physics (`Rust`/`Zig`/`C` for daemons, codecs & kernels; `OCaml`/`Rust` for capability proxies; `Go`/`Rust` for CLIs & relays; `Nix` for reproducible infra; `TypeScript` for UIs; `Python`/`Julia` for analytics & glue).
   - Annotate lines 1–5 of every source file: `// ffp: <FFP-ID> <class> <lang>`.
   - Deep reference: see [references/four-pillars.md](references/four-pillars.md).

3. **Pillar 3 — `SLECO-SO++` Runtime & `ENHAN³` Hardening**:
   - Shell scripts use `set +e`, `set +u`, explicit `trap '...' EXIT INT TERM` cleanup, and pure parameter expansion (`${var##*/}`).
   - Enforce $O(1)$ / $O(N)$ linear algorithms, exponential peer backoff, and atomic file swaps (`write .tmp` -> `rename`).
   - Upgrade every unit across **Resilience**, **Performance**, and **Security** (`ENHAN³`).

4. **Pillar 4 — `GDPR++` Security & `5.0x–8.8x` Token-Economics (`Vāk` Gate)**:
   - Store credentials strictly in `chmod 0600` out-of-tree vaults; isolate PII behind ephemeral keys for `< 50ms` cryptoshredding.
   - **System-0 Bypass**: Execute deterministic filtering, deduplication, regex checks, and math via compiled CLI/SQL/FTS5 tools (`0` LLM tokens) instead of LLM prose.
   - **Sub-Linear Context**: Batch parallel tool calls, project `< 2%` schema digests instead of raw files, read bounded `<= 250`-line slices on large files, and short-circuit no-op builds via SHA-256 digests.
   - Deep reference: see [references/token-economics.md](references/token-economics.md).

## Anti-Rationalization Table (Zero Excuses)

| Common Agent Excuse | Build Law Reality & Required Action |
| :--- | :--- |
| *"I'll leave a `TODO` for error handling to save time."* | Rejected by Gate 1 (`KĀLĪ`) & Gate 5 (`TĀRĀ`). Write the real error path now. |
| *"I'll just use `set -e` at the top of the bash script."* | Rejected by Pillar 3 (`SLECO-SO++`). `set -e` orphans locks/processes; use `set +e` + `trap` + explicit exit checks. |
| *"I'll write the daemon in Python because it's quick."* | Rejected by Pillar 2 (`MĀTAṄGĪ`). Match language to workload fitness (`Rust`/`Go` for daemons & relays). |
| *"Let me read the entire 5,000-line file into context."* | Rejected by Pillar 4 (`Vāk` Gate). Grep symbols or read bounded `<= 250`-line windows. |

## Verification Command
If `build-law` CLI is installed on `$PATH`, run deterministic `0`-token verification before completing any task:
```bash
build-law check .
```
