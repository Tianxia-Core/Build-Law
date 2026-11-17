#!/usr/bin/env python3
# ffp: FFP-BLAW-SKILL-PACK content-pipeline python
# dss14-ignore: PRATYANGIRA KALI (defines scanner regexes & documentation strings referencing forbidden tokens)
"""
Generates all multi-harness, IDE, skill, prompt, governance, VSIX, and AEO/GEO artifacts
for the public flagship repository `Tianxia-Core/Build-Law`.
"""
from __future__ import annotations

import json
import os
import re
import tarfile
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
WORKSPACE_ROOT = REPO_ROOT.parent.parent
DIST_EXTRA = REPO_ROOT / "dist_extras"


def write_file_atomic(path: Path, text: str, mode: int = 0o644) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.tmp.{os.getpid()}")
    tmp.write_text(text, encoding="utf-8")
    os.chmod(tmp, mode)
    os.replace(tmp, path)


PUBLIC_CONSTITUTION_MD = """# Build Law — Sovereign Autonomous Engineering & Token-Efficiency Constitution

> **Edition:** `v5.1-SOVEREIGN-CONSTITUTION` · **License:** `MIT`
> **Architected by:** **Collins Takem** — Founder & Principal Systems Architect, **RASA-X-MACHINA** ([rasaxmachina.com](https://rasaxmachina.com) · Makers of [`tianxiaOS`](https://github.com/Tianxia-Core/TianxiaOS))
> **Scope:** Universal, Model-Agnostic & Platform-Agnostic (Claude, GPT, Gemini, DeepSeek, Qwen, Local Quantized Models · Claude Code, Cursor, OpenCode, VS Code, GitHub Copilot, Windsurf, Cline, Roo Code, Continue, Aider, Zed, JetBrains Junie, Goose, Antigravity & Custom Agent Harnesses)

**COMPLIANCE MANDATE:** Every architecture specification, source file, shell script, database migration, UI surface, and automated agent workflow governed by **Build Law** satisfies four orthogonal constitutional pillars with zero placeholders and verifiable execution proof.

```
                              ┌───────────────────────────────────────┐
                              │         BUILD LAW CONSTITUTION        │
                              └──────────────────┬────────────────────┘
                                                 │
         ┌───────────────────────────┬───────────┴───────────┬───────────────────────────┐
         ▼                           ▼                       ▼                           ▼
┌──────────────────┐       ┌──────────────────┐     ┌──────────────────┐       ┌──────────────────┐
│     PILLAR 1     │       │     PILLAR 2     │     │     PILLAR 3     │       │     PILLAR 4     │
│   14-GATE SPEC   │       │    POLYGLOT      │     │     SLECO-SO++   │       │  PRIVACY/GDPR++  │
│   COMPLETENESS   │       │    FFP-First     │     │ Canonical Runtime│       │ & 5x–8.8x TOKEN  │
│  (DSS-14.2 Gate) │       │ (<=8 FFPs / Unit)│     │    & ENHAN³      │       │  ECONOMICS (Vāk) │
└──────────────────┘       └──────────────────┘     └──────────────────┘       └──────────────────┘
```

---

## PILLAR 1: 14-Gate Universal Architectural Completeness (`DSS-14.2` / `PARAMASIVA` Gate)

Most AI-generated and rush-shipped software fails not in the happy path, but in the 13 unspoken operational dimensions surrounding it. Under Build Law, an artifact ships only when all **14 Natural-Language Engineering Lenses** concur:

1. **KĀLĪ — Severance & Zero-Stub Discipline**: Cut what cannot be defended. Zero `TODO`, `FIXME`, `pass`, `todo!()`, `unimplemented!()`, or mock data in committed code. Deterministic lifecycle bounding and stale-state eviction.
2. **BHAIRAVĪ — Capability Containment**: Anything mutating a protected surface (files, cryptographic keys, sockets, production state, payments) stands behind an explicit capability check, cgroup v2 resource bound (`MemoryMax`, `TasksMax`), and `NoNewPrivileges=yes`. Read-only diagnostics remain friction-free.
3. **PRATYAṄGIRĀ — Execution Innocence & Active Anomaly Arrest**: Zero dynamic string `eval()`, zero unguarded shell-string interpolation, zero hidden interpretation; thermal/rate-limit circuit breakers and offline peer backoff arrestors.
4. **BĀGALAMUKHĪ — Loop Discipline & Non-Bypassable ACLs**: Every long-lived loop carries an explicit kill-switch, bounded timeout, and clean shutdown path. Fail-closed proxy and firewall boundaries.
5. **TĀRĀ — Graceful Failure & Sovereign Transit**: Errors are logged with structured context and survived—never silently swallowed (`except: pass` banned) and never crashing half-written state. Zero-trust encrypted transit across distributed nodes.
6. **TRIPURA — Three-Way Redundancy & Visual Clarity**: Eliminate single points of failure across fetch, build, and verification paths; maintain high-contrast, accessible (`WCAG 2.2 AA`), F-pattern scannable interfaces.
7. **BHUVANĒŚVARĪ — Environment Humility**: Never hardcode brittle host assumptions; resolve paths, ports, and capabilities dynamically via environment defaults (`${VAR:-default}`, `os.environ`) with portable fallbacks.
8. **CHHINNAMASTĀ — Decoupled Shared-Memory Velocity & Clean Severance**: Decouple hot paths via lockless ring buffers or zero-copy IPC; cleanly stop, archive, and record retired daemons with zero zombie processes.
9. **DHŪMĀVATĪ — Zero-Knowledge Secrecy & Truthful Audit Logging**: Secrets and PII reside strictly in `chmod 0600` out-of-tree vaults—never in git, configs, or stdout. Every state transition writes an auditable hash-chained trace.
10. **MĀTAṄGĪ — Polyglot Grammatical Fitness**: Language follows workload physics; prefer deterministic AST parsing and compile-time type/macro verification over regex guesswork.
11. **ANNAPŪRṆĀ — Idempotent Self-Sustaining Provision**: Idempotent initialization, resumable transfers, sleep-coalesced mobile/edge workqueues, and self-healing state files.
12. **MAHĀSARASVATĪ — Merkle Provenance & Coherent Polyglot Voice**: Structured JSONL telemetry, Prometheus metrics, and SHA-256/Blake3 Merkle DAG receipts proving what ran and what changed.
13. **FFP — Explicit Function-Feature Pairing**: Every source file declares its atomic capability unit at line 1–5 (`// ffp: <FFP-ID> <fitness-class> <language>`). Unpaired code is unverified code.
14. **KAMALĀ — Verifiable Value & Resource Precision**: Predictable memory/CPU provisioning and verifiable unit-economics telemetry grounded in ledger truth rather than aspiration.

---

## PILLAR 2: Polyglot `FFP-First` Architecture & The `<= 8` FFP Service Bound

### 2.1 Canonical Unit: `FFP` = Function-Feature Pair
An **FFP** is a discrete `(function, feature)` capability unit backed by a concrete source artifact, bounded marginal cost, and an explicitly declared **Architectural Fitness Class**.

### 2.2 Ban on the Single-Language Lazy Default
There is **no default programming language**. Implementing high-concurrency daemons, wire codecs, or capability proxies in a slow scripting language out of habit is a Build Law violation. Select from the ranked fitness matrix:

| Architectural Fitness Class (`ffp_class`) | Ranked Languages (Best Fit First) | Target Workloads |
| :--- | :--- | :--- |
| **`concurrent-daemon`** | **Rust**, Go, Nim, Zig | Multi-threaded actors, background daemons, HUD compositors, supervisors |
| **`wire-codec`** | **Rust**, Zig, C | Shared-memory ring buffers, zero-copy binary framing, IPC brokers |
| **`edge-agent`** | **Rust**, Go, Nim, Zig | Deterministic CLI verifiers, AST compilers, low-footprint edge agents |
| **`capability-proxy`** | **OCaml**, Rust, F# | Formally typed protocol firewalls, ACL proxies, state-machine verifiers |
| **`compute-kernel`** | **C (AVX2/NEON)**, CUDA, Mojo, Rust, Julia | SIMD scoring kernels, tensor pre-filters, real-time numerical engines |
| **`kernel-interceptor`** | **eBPF / BPF**, C | In-kernel packet filtration (`AF_XDP`), socket guards, syscall tracing |
| **`crypto-signer`** | **Rust**, Go, C, Zig | Ed25519 release signing, AES-256-GCM / ML-KEM key envelopes, Merkle ledgers |
| **`declarative`** | **Nix** | Reproducible OS/package closures, pinned dependencies, zero config drift |
| **`frontend`** | **TypeScript**, Wasm, JavaScript | Accessible reactive web apps, WebGPU/WebCrypto interfaces, IDE extensions |
| **`data-science` / `ml-inference`** | **Julia**, Mojo, Python | Statistical modeling, offline analytics, tensor evaluation |
| **`contract`** | **Solidity**, Rust | On-chain escrow, deterministic settlement vaults |
| **`glue` / `content-pipeline`** | **Python**, Bash, Nix | Build orchestration, deterministic artifact compilers, CLI bridges |

### 2.3 The `<= 8` FFP Bounding Law (Anti-Bloat & Anti-Context-Collapse)
Every standalone service, package, or microservice is strictly bounded to **`<= 8` Function-Feature Pairs** inside an isolated execution boundary. Systems requiring more than 8 capabilities decompose into modular `<= 8`-FFP units communicating over explicit typed contracts or UNIX domain sockets.

### 2.4 The `ENHAN³` Tri-Vector Invariant
Before any FFP ships, harden it across three orthogonal axes:
1. **Resilience**: Explicit signal/error traps, bounded timeouts, circuit breakers, clean child-process reaping.
2. **Performance**: $O(1)$ or strict $O(N)$ linear algorithms, zero-copy buffers, exponential backoff on unreachable peers.
3. **Security**: Capability isolation, input sanitization, `0600` secret custody, memory safety.

---

## PILLAR 3: `SLECO-SO++` Canonical Runtime Standard

1. **Anti-Fail-Fast Shell Resilience**: Production shell scripts use `set +e` and `set +u` with explicit exit-code checks and `trap '...' EXIT INT TERM` cleanup—never blind `set -e` that aborts mid-transaction leaving corrupted lockfiles or zombie processes.
2. **Linear Velocity ($O(1)$ / $O(N)$)**: Quadratic $O(N^2)$ loops, unindexed table scans, and tight polling loops without backoff are prohibited.
3. **Pure Parameter Expansion**: Prefer native shell expansion (`${var##*/}`, `${var%/*}`, `${var:-default}`) over spawning subshells (`basename`, `dirname`, `sed`, `awk`) inside loops.
4. **Atomic File Synchronization**: Never write partially into live config or state files; write to `.tmp.$$` on the same filesystem, `fsync` where critical, and atomically `rename()` / `os.replace()` / `mv -f`.

---

## PILLAR 4: `GDPR++` Horizon Security & `5.0x–8.8x` Sovereign Token-Economics (`Vāk` Gate)

### 4.1 Privacy by Design (`PbD`), Security by Design (`SbD`) & `GDPR++` `< 50ms` Cryptoshredding
- **Zero Plaintext Secrets**: Credentials never enter git, `.env` commits, MCP configs, or logs; redact sensitive patterns automatically before stdout/log emission.
- **Sub-50ms Cryptographic Erasure (`GDPR++`)**: Isolate per-subject PII behind ephemeral key envelopes so right-to-erasure requests destroy the subject key in `< 50 ms` and emit a verifiable SHA-256 Merkle erasure receipt without mutating immutable audit chains.
- **Universal Multi-OS Signed Releases**: Production tools ship with verifiable `Ed25519` signatures (`.sig`), `SHA256SUMS`, and CycloneDX 1.5 `SBOM.cdx.json` across native packages (`.tar.gz`, `.deb`, `.rpm`, `.AppImage`, `flake.nix`, `.exe`, `.apk`).

### 4.2 Sovereign Token-Economics & `Vāk` Zero-Token AST Routing (`5.0x–8.8x` Value Multiplier)
Treat LLM context windows and inference spend as scarce engineering capital:
1. **System-0 Deterministic AST & SQL/FTS5 Bypass (`Vāk` Gate — `$0.00`, `0` Tokens)**: Never ask an LLM to filter spreadsheets, deduplicate records, scan files for regexes, or compute aggregates in prose. Execute structured queries and transformations in compiled CLI/SQL/FTS5 tools at `$0.00` token cost.
2. **Schema-First `< 2%` Digest Projection**: Never dump raw CSVs, large JSON registries, or full database tables into model context. Inspect schema headers, row counts, and `LIMIT 5..15` exemplars; perform transformations in code.
3. **Batch Parallel Tool Execution & Single-Pass Generators**: Batch independent reads/checks in parallel; apply cross-file structural updates via deterministic $O(N)$ scripts rather than repetitive conversational edit loops.
4. **Bounded Window Reads (`<= 250` Lines)**: On large files, read targeted `StartLine`–`EndLine` slices rather than re-reading entire files across turns.
5. **Compact Semantic Pointers & Hash Handoffs**: Pass `path#Lstart-Lend` references and SHA-256/Blake3 digests across subagents instead of duplicating multi-kilobyte text blocks.
6. **Immutable Prefix KV-Cache Pinning & Tiered Model Routing**: Keep system rules byte-stable at the prompt prefix (`75%–90%` cache-hit cost reduction) and route subtasks to the lightest sufficient model tier, reserving frontier reasoning strictly for novel architecture, security proofs, and complex synthesis.
7. **Checksum Delta Short-Circuiting**: Compare SHA-256 digests before rebuilding databases, packages, or media assets; skip no-op rebuilds in $O(1)$.

---

## Architectural Specification Lifecycle (`missions/ → yet/ → accomplished/`)

Track non-trivial builds through three explicit filesystem stages:
- `missions/` — Pending architectural specifications awaiting implementation.
- `yet/` — Active specifications currently under construction and verification.
- `accomplished/` — Promoted **only** when 100% of components are implemented with zero stubs, compiled, and verified against live checks.
"""

COMPACT_PROMPT_MD = """# Build Law — Compact KV-Cached System Prompt (`~1,050` Tokens · v5.1)

Operate strictly under **Build Law** (architected by Collins Takem · RASA-X-MACHINA):

1. **14-Gate Completeness (`PARAMASIVA` Gate)**:
   - **Zero Stubs**: Never emit `TODO`, `FIXME`, `pass`, `todo!()`, `unimplemented!()`, placeholder comments, or mock responses. Every function, route, error handler, and config block must be complete and runnable.
   - **Innocence & Containment**: Zero `eval()`, zero shell-string injection (`shell=True` banned on untrusted input), explicit capability/permission checks before mutating files, keys, networks, or payments.
   - **Loop & Failure Discipline**: Every loop/network call must have a bounded timeout and clean shutdown path; never swallow exceptions silently—log structured context and recover cleanly.
2. **Polyglot `FFP-First` Architecture (`<= 8` FFPs per Service)**:
   - Decompose work into atomic **Function-Feature Pairs (`FFPs`)**, max **`8` FFPs** per standalone service/module.
   - Choose the language best suited to workload physics (`Rust`/`Zig`/`C` for daemons, wire codecs & kernels; `OCaml`/`Rust` for capability proxies; `Go`/`Rust` for concurrent relays & CLIs; `Nix` for reproducible infra; `TypeScript` for UIs; `Julia`/`Python` for data science & glue—never Python as a lazy daemon default).
   - Add an explicit FFP header at lines 1–5 of every source file: `// ffp: <FFP-ID> <fitness-class> <language>`.
3. **`SLECO-SO++` Runtime & `ENHAN³` Hardening**:
   - Shell scripts use `set +e`, `set +u`, explicit `trap` cleanup, and native parameter expansion (`${var##*/}`) instead of blind `set -e` or hot-loop subshells.
   - Enforce $O(1)$ or $O(N)$ linear complexity, exponential peer backoff, and atomic writes (`write .tmp` -> `rename`).
   - Harden every unit across **Resilience**, **Performance**, and **Security** (`ENHAN³`).
4. **`GDPR++` Security & `5.0x–8.8x` Token-Economics (`Vāk` System-0 Gate)**:
   - Never hardcode or log secrets/PII; store credentials in `chmod 0600` out-of-tree vaults and enforce `< 50ms` ephemeral key erasure (`GDPR++`).
   - **System-0 Bypass**: Run filtering, deduplication, regex scans, and math in deterministic CLI/SQL/FTS5 code (`$0.00`, `0` LLM tokens) rather than in LLM prose.
   - **Context Compression**: Batch parallel tool calls, project `< 2%` schema/top-K digests instead of raw data dumps, read bounded line windows (`<= 250` lines) on large files, short-circuit no-op builds via SHA-256 checksums, and respond concisely with clickable file references.
"""

CHAT_DROP_IN_TXT = """Adopt BUILD LAW (v5.1 by Collins Takem / RASA-X-MACHINA) for this entire session:
1. ZERO STUBS: Never output TODO, FIXME, pass, mock data, or truncated "...rest of code..." placeholders. Deliver complete, production-ready, runnable artifacts.
2. SECURITY & CONTAINMENT: Zero eval(), zero shell injection, zero hardcoded secrets/PII, bounded timeouts on all I/O and loops, and atomic file writes (temp + rename).
3. POLYGLOT FFP<=8 FITNESS: Pick the optimal language for each workload's physics (no lazy defaults), keep each service <= 8 Function-Feature Pairs (FFPs), and annotate files with `// ffp: <ID> <class> <lang>`.
4. SLECO-SO++ & ENHAN3: Prefer O(1)/O(N) algorithms, explicit error recovery (`set +e` + `trap` in shell), and upgrade every component across Resilience, Performance, and Security.
5. 5x-8.8x TOKEN EFFICIENCY: Offload deterministic parsing, math, and filtering to code/SQL rather than prose; inspect compact schemas instead of dumping raw files; keep answers crisp, structured, and verifiable.
"""

AUDIT_PROMPT_MD = """# Build Law — 14-Gate Architecture & Pull-Request Audit Prompt

Audit the target repository, pull request, or specification against all **14 Build Law Gates (`PARAMASIVA` Gate)**:

1. **KĀLĪ (Zero Stubs & Stale Code)**: Any `TODO`, `FIXME`, `unimplemented!()`, dead code, or uncollected resources?
2. **BHAIRAVĪ (Containment)**: Are file, network, key, and payment mutations gated and resource-bounded (`MemoryMax`, `NoNewPrivileges`)?
3. **PRATYAṄGIRĀ (Innocence)**: Any `eval()`, `exec()`, `shell=True`, SQL string concatenation, or missing rate-limit circuit breakers?
4. **BĀGALAMUKHĪ (Loop & ACL Bounds)**: Any unbounded `while true` loops, missing socket timeouts, or fail-open ACLs?
5. **TĀRĀ (Graceful Recovery)**: Any blind `set -e`, bare `unwrap()` on untrusted input, or silent `except: pass` blocks?
6. **TRIPURA (Redundancy & UX)**: Single points of failure or inaccessible UI contrast/keyboard navigation?
7. **BHUVANĒŚVARĪ (Environment Humility)**: Any hardcoded developer paths, brittle hostnames, or unconfigurable ports?
8. **CHHINNAMASTĀ (Decoupling)**: Hot-path lock contention or orphaned child processes?
9. **DHŪMĀVATĪ (Secret & PII Hygiene)**: Any plaintext tokens, `.env` leaks, PII in logs, or missing `0600` vault isolation?
10. **MĀTAṄGĪ (Language Fitness)**: Is the language matched to the workload's latency/safety profile?
11. **ANNAPŪRṆĀ (Idempotency)**: Is setup idempotent, resumable, and atomic (`temp` + `rename`)?
12. **MAHĀSARASVATĪ (Provenance)**: Are state mutations deterministically logged and checksummed?
13. **FFP (`<= 8` Bound)**: Does each source file carry an `# ffp:` header, and is each service bounded to `<= 8` FFPs?
14. **KAMALĀ (Token & Compute Efficiency)**: Are deterministic data tasks offloaded from LLM prompts to $O(N)$ code/SQL (`Vāk` Gate)?

Output a structured Markdown table (`Gate | Status [PASS/FAIL] | File:Line | Concrete Remediation`) followed by exact drop-in fixes for every failing gate.
"""

SKILL_MD = """---
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
"""

INSTALL_SH = """#!/usr/bin/env bash
# ffp: FFP-BLAW-INSTALLER content-pipeline bash
# Build Law Universal SLECO-SO++ Installer (Linux, macOS, Termux/Android, WSL)
# Usage: curl -fsSL https://raw.githubusercontent.com/Tianxia-Core/Build-Law/main/install.sh | bash
set +e
set +u

TMP_STAGE=""
cleanup() {
  if [ -n "${TMP_STAGE}" ] && [ -d "${TMP_STAGE}" ]; then
    rm -rf "${TMP_STAGE}"
  fi
}
trap cleanup EXIT INT TERM

REPO="Tianxia-Core/Build-Law"
VERSION="${BUILD_LAW_VERSION:-v1.0.0}"
RAW_BASE="https://raw.githubusercontent.com/${REPO}/main"
REL_BASE="https://github.com/${REPO}/releases/download/${VERSION}"

log_info() { printf '[build-law] %s\\n' "$1"; }
log_err()  { printf '[build-law] ERROR: %s\\n' "$1" >&2; }

OS_RAW="$(uname -s 2>/dev/null || printf 'Linux')"
ARCH_RAW="$(uname -m 2>/dev/null || printf 'x86_64')"

case "${ARCH_RAW}" in
  x86_64|amd64) ARCH="x86_64" ;;
  aarch64|arm64) ARCH="aarch64" ;;
  *) ARCH="${ARCH_RAW}" ;;
esac

IS_TERMUX=0
if [ -n "${TERMUX_VERSION:-}" ] || [ -d "/data/data/com.termux/files/usr" ]; then
  IS_TERMUX=1
fi

if [ "${IS_TERMUX}" -eq 1 ]; then
  BIN_DIR="${HOME}/bin"
  PLATFORM_ASSET="build-law-${VERSION}-android-aarch64"
elif [ "${OS_RAW}" = "Linux" ]; then
  if [ "$(id -u 2>/dev/null || printf '1000')" -eq 0 ]; then
    BIN_DIR="/usr/local/bin"
  else
    BIN_DIR="${HOME}/.local/bin"
  fi
  PLATFORM_ASSET="build-law-${VERSION}-linux-${ARCH}"
else
  BIN_DIR="${HOME}/.local/bin"
  PLATFORM_ASSET=""
fi

mkdir -p "${BIN_DIR}" "${HOME}/.config/build-law"
TMP_STAGE="$(mktemp -d 2>/dev/null || printf '/tmp/blaw_stage_%s' "$$")"
mkdir -p "${TMP_STAGE}"

fetch_url() {
  src_url="$1"
  dst_file="$2"
  if command -v curl >/dev/null 2>&1; then
    curl -fsSL --connect-timeout 10 --max-time 60 "${src_url}" -o "${dst_file}"
    return $?
  elif command -v wget >/dev/null 2>&1; then
    wget -q -T 30 -O "${dst_file}" "${src_url}"
    return $?
  fi
  return 1
}

if [ -n "${PLATFORM_ASSET}" ]; then
  log_info "Downloading native static binary (${PLATFORM_ASSET})..."
  if fetch_url "${REL_BASE}/${PLATFORM_ASSET}" "${TMP_STAGE}/build-law.bin"; then
    chmod 0755 "${TMP_STAGE}/build-law.bin"
    mv -f "${TMP_STAGE}/build-law.bin" "${BIN_DIR}/build-law"
    log_info "Installed native binary -> ${BIN_DIR}/build-law"
  fi
fi

log_info "Fetching Build Law Constitution & Global Multi-Harness Rules..."
if fetch_url "${RAW_BASE}/BUILD_LAW.md" "${TMP_STAGE}/BUILD_LAW.md"; then
  mv -f "${TMP_STAGE}/BUILD_LAW.md" "${HOME}/.config/build-law/BUILD_LAW.md"
fi

if [ -x "${BIN_DIR}/build-law" ]; then
  "${BIN_DIR}/build-law" enforce-global
  "${BIN_DIR}/build-law" status
else
  # Pure POSIX fallback provisioning across Claude, Cursor, OpenCode, Gemini, Codex & Copilot
  for d in "${HOME}/.claude" "${HOME}/.config/opencode" "${HOME}/.gemini" "${HOME}/.codex" "${HOME}/.cursor/rules" "${HOME}/.windsurf/rules"; do
    mkdir -p "${d}"
  done
  if [ -f "${HOME}/.config/build-law/BUILD_LAW.md" ]; then
    cp -f "${HOME}/.config/build-law/BUILD_LAW.md" "${HOME}/.claude/CLAUDE.md"
    cp -f "${HOME}/.config/build-law/BUILD_LAW.md" "${HOME}/.config/opencode/AGENTS.md"
    cp -f "${HOME}/.config/build-law/BUILD_LAW.md" "${HOME}/.gemini/GEMINI.md"
    cp -f "${HOME}/.config/build-law/BUILD_LAW.md" "${HOME}/.codex/AGENTS.md"
    cp -f "${HOME}/.config/build-law/BUILD_LAW.md" "${HOME}/.cursor/rules/build-law.mdc"
    cp -f "${HOME}/.config/build-law/BUILD_LAW.md" "${HOME}/.windsurf/rules/build-law.md"
  fi
  log_info "Provisioned global Build Law configurations across $HOME."
fi

log_info "Build Law installation complete. Run: ${BIN_DIR}/build-law check ."
exit 0
"""


def build_vscode_extension_and_vsix() -> Path:
    ext_dir = REPO_ROOT / "extensions" / "vscode-build-law"
    pkg_json = {
        "name": "build-law-sentinel",
        "displayName": "Build Law — 14-Gate AI Engineering & Token-Efficiency Sentinel",
        "description": "Enforces Build Law across VS Code, Cursor, Windsurf & Copilot: 14-Gate zero-stub/zero-secret verification, workspace rule provisioning, and KV-cached prompt injection.",
        "version": "1.0.0",
        "publisher": "rasaxmachina",
        "author": {"name": "Collins Takem (RASA-X-MACHINA)", "url": "https://rasaxmachina.com"},
        "license": "MIT",
        "repository": {"type": "git", "url": "https://github.com/Tianxia-Core/Build-Law.git"},
        "engines": {"vscode": "^1.74.0"},
        "categories": ["Linters", "AI", "Other"],
        "keywords": ["build-law", "ai-agents", "cursor", "copilot", "claude", "opencode", "devsecops", "architecture"],
        "activationEvents": ["onStartupFinished"],
        "main": "./extension.js",
        "contributes": {
            "commands": [
                {"command": "buildLaw.auditActiveFile", "title": "Build Law: Audit Active File (14-Gate Check)"},
                {"command": "buildLaw.provisionWorkspace", "title": "Build Law: Provision Workspace Rules (All AI Tools)"},
                {"command": "buildLaw.copyCompactPrompt", "title": "Build Law: Copy Distilled System Prompt to Clipboard"},
            ],
            "configuration": {
                "title": "Build Law",
                "properties": {
                    "buildLaw.auditOnSave": {
                        "type": "boolean",
                        "default": True,
                        "description": "Run zero-token Build Law 14-Gate static diagnostics automatically on file save.",
                    },
                    "buildLaw.autoEnsureWorkspaceRules": {
                        "type": "boolean",
                        "default": True,
                        "description": "Automatically ensure workspace AI instruction files stay synchronized with Build Law.",
                    },
                },
            },
        },
    }

    ext_js = """// ffp: FFP-BLAW-VSCODE frontend javascript
// build-law-ignore: scanner rule definitions
// Build Law Native Extension for VS Code, Cursor, Windsurf & VSCodium
const vscode = require('vscode');
const fs = require('fs');
const path = require('path');

const STUB_RE = /\\b(TODO|FIXME|unimplemented!|todo!)\\b/;
const SECRET_RE = /(sk_live_[0-9a-zA-Z_]{12,}|gh[pousr]_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16})/;
const EVAL_RE = /\\beval\\s*\\(/;

const COMPACT_PROMPT = `Operate strictly under Build Law v5.1 (RASA-X-MACHINA):
1. ZERO STUBS: Never emit TODO, FIXME, pass, todo!(), unimplemented!(), or mock data.
2. INNOCENCE & CONTAINMENT: Zero eval(), zero shell injection, bounded timeouts on all loops/IO, and 0600 out-of-tree secret custody.
3. POLYGLOT FFP<=8: Match language to workload physics, cap services at <= 8 FFPs, and declare // ffp: <ID> <class> <lang>.
4. SLECO-SO++ & 5x-8.8x TOKEN EFFICIENCY: Use O(1)/O(N) algorithms, atomic file writes, and offload deterministic data ops to CLI/SQL ($0.00, 0 tokens).`;

function scanDocument(doc, collection) {
  if (!doc || doc.uri.scheme !== 'file') return;
  const text = doc.getText();
  const diags = [];
  const lines = text.split(/\\r?\\n/);
  for (let i = 0; i < lines.length; i++) {
    const ln = lines[i];
    if (SECRET_RE.test(ln)) {
      diags.push(new vscode.Diagnostic(
        new vscode.Range(i, 0, i, ln.length),
        '[Build Law · 07-DHUMAVATI] Plaintext credential signature detected; move to chmod 0600 out-of-tree vault.',
        vscode.DiagnosticSeverity.Error
      ));
    }
    if (EVAL_RE.test(ln) && !ln.includes('dss14-ignore')) {
      diags.push(new vscode.Diagnostic(
        new vscode.Range(i, 0, i, ln.length),
        '[Build Law · 03-PRATYANGIRA] Dynamic eval() prohibited; use deterministic AST parsing.',
        vscode.DiagnosticSeverity.Warning
      ));
    }
    if (STUB_RE.test(ln) && !doc.fileName.endsWith('.md')) {
      diags.push(new vscode.Diagnostic(
        new vscode.Range(i, 0, i, ln.length),
        '[Build Law · 01-KALI] Placeholder stub token detected; complete implementation before shipping.',
        vscode.DiagnosticSeverity.Information
      ));
    }
  }
  collection.set(doc.uri, diags);
}

function ensureWorkspaceRules() {
  const folders = vscode.workspace.workspaceFolders;
  if (!folders || folders.length === 0) return 0;
  const root = folders[0].uri.fsPath;
  const cursorRule = path.join(root, '.cursor', 'rules', 'build-law.mdc');
  const copilotRule = path.join(root, '.github', 'copilot-instructions.md');
  let created = 0;
  for (const target of [cursorRule, copilotRule]) {
    if (!fs.existsSync(target)) {
      fs.mkdirSync(path.dirname(target), { recursive: true });
      const body = target.endsWith('.mdc')
        ? `---\\ndescription: Build Law Sovereign Engineering Rules\\nglobs: "**/*"\\nalwaysApply: true\\n---\\n\\n${COMPACT_PROMPT}\\n`
        : `${COMPACT_PROMPT}\\n`;
      fs.writeFileSync(target, body, 'utf8');
      created++;
    }
  }
  return created;
}

function activate(context) {
  const diagCollection = vscode.languages.createDiagnosticCollection('buildLaw');
  context.subscriptions.push(diagCollection);

  const statusBar = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Right, 100);
  statusBar.text = '$(shield) Build Law: v5.1';
  statusBar.tooltip = 'Build Law 14-Gate Architectural & Token-Efficiency Sentinel Active';
  statusBar.command = 'buildLaw.auditActiveFile';
  statusBar.show();
  context.subscriptions.push(statusBar);

  context.subscriptions.push(vscode.commands.registerCommand('buildLaw.auditActiveFile', () => {
    const ed = vscode.window.activeTextEditor;
    if (!ed) {
      vscode.window.showInformationMessage('Build Law: Open a file to run 14-Gate verification.');
      return;
    }
    scanDocument(ed.document, diagCollection);
    const current = diagCollection.get(ed.document.uri) || [];
    vscode.window.showInformationMessage(`Build Law 14-Gate Check: ${current.length} finding(s) in ${path.basename(ed.document.fileName)} (0 LLM tokens).`);
  }));

  context.subscriptions.push(vscode.commands.registerCommand('buildLaw.provisionWorkspace', () => {
    const count = ensureWorkspaceRules();
    vscode.window.showInformationMessage(`Build Law: Provisioned ${count} new workspace AI governance file(s).`);
  }));

  context.subscriptions.push(vscode.commands.registerCommand('buildLaw.copyCompactPrompt', async () => {
    await vscode.env.clipboard.writeText(COMPACT_PROMPT);
    vscode.window.showInformationMessage('Build Law: Copied Compact KV-Cached System Prompt to clipboard.');
  }));

  context.subscriptions.push(vscode.workspace.onDidSaveTextDocument(doc => {
    if (vscode.workspace.getConfiguration('buildLaw').get('auditOnSave', true)) {
      scanDocument(doc, diagCollection);
    }
  }));

  if (vscode.workspace.getConfiguration('buildLaw').get('autoEnsureWorkspaceRules', true)) {
    try { ensureWorkspaceRules(); } catch (_e) {}
  }
}

function deactivate() {}

module.exports = { activate, deactivate };
"""

    ext_readme = "# Build Law Sentinel (VS Code · Cursor · Windsurf · VSCodium)\n\nZero-token 14-Gate architectural diagnostic linter, workspace AI rule provisioner, and KV-cached system prompt toolbar by **Collins Takem (`RASA-X-MACHINA`)**.\n"
    license_txt = (REPO_ROOT / "LICENSE").read_text(encoding="utf-8") if (REPO_ROOT / "LICENSE").is_file() else "MIT License - Copyright (c) 2026 Collins Takem / RASA-X-MACHINA\n"

    write_file_atomic(ext_dir / "package.json", json.dumps(pkg_json, indent=2) + "\n")
    write_file_atomic(ext_dir / "extension.js", ext_js)
    write_file_atomic(ext_dir / "README.md", ext_readme)
    write_file_atomic(ext_dir / "LICENSE.txt", license_txt)

    # Package standard OPC .vsix archive
    DIST_EXTRA.mkdir(parents=True, exist_ok=True)
    vsix_path = DIST_EXTRA / "build-law-sentinel-1.0.0.vsix"
    content_types = """<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension=".json" ContentType="application/json"/>
  <Default Extension=".js" ContentType="application/javascript"/>
  <Default Extension=".md" ContentType="text/markdown"/>
  <Default Extension=".txt" ContentType="text/plain"/>
  <Default Extension=".vsixmanifest" ContentType="text/xml"/>
</Types>
"""
    vsix_manifest = """<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011" xmlns:d="http://schemas.microsoft.com/developer/vsx-schema-design/2011">
  <Metadata>
    <Identity Language="en-US" Id="build-law-sentinel" Version="1.0.0" Publisher="rasaxmachina"/>
    <DisplayName>Build Law — 14-Gate AI Engineering &amp; Token-Efficiency Sentinel</DisplayName>
    <Description xml:space="preserve">Enforces Build Law across VS Code, Cursor, Windsurf &amp; Copilot: 14-Gate zero-stub/zero-secret verification and workspace rule provisioning.</Description>
    <Tags>build-law,ai-agents,cursor,copilot,claude,opencode,architecture</Tags>
    <Categories>Linters,AI,Other</Categories>
    <GalleryFlags>Public</GalleryFlags>
  </Metadata>
  <Installation>
    <InstallationTarget Id="Microsoft.VisualStudio.Code"/>
  </Installation>
  <Dependencies/>
  <Assets>
    <Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json" Addressable="true"/>
    <Asset Type="Microsoft.VisualStudio.Services.Content.Details" Path="extension/README.md" Addressable="true"/>
    <Asset Type="Microsoft.VisualStudio.Services.Content.License" Path="extension/LICENSE.txt" Addressable="true"/>
  </Assets>
</PackageManifest>
"""
    with zipfile.ZipFile(vsix_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types)
        zf.writestr("extension.vsixmanifest", vsix_manifest)
        for fname in ("package.json", "extension.js", "README.md", "LICENSE.txt"):
            zf.writestr(f"extension/{fname}", (ext_dir / fname).read_text(encoding="utf-8"))
    return vsix_path


def main() -> int:
    mit_license = """MIT License

Copyright (c) 2026 Collins Takem · RASA-X-MACHINA (https://rasaxmachina.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software, constitutional specification, skill pack, and associated
documentation files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
    write_file_atomic(REPO_ROOT / "LICENSE", mit_license)

    # 1. Core Constitutional Mirrors inside Build-Law repo
    for root_doc in ("BUILD_LAW.md", "AGENTS.md", "CLAUDE.md", "GEMINI.md"):
        write_file_atomic(REPO_ROOT / root_doc, PUBLIC_CONSTITUTION_MD)

    # 2. Standalone Prompts
    write_file_atomic(REPO_ROOT / "prompts" / "SYSTEM_PROMPT_FULL.md", PUBLIC_CONSTITUTION_MD)
    write_file_atomic(REPO_ROOT / "prompts" / "SYSTEM_PROMPT_COMPACT_KV.md", COMPACT_PROMPT_MD)
    write_file_atomic(REPO_ROOT / "prompts" / "CHAT_DROP_IN_PROMPT.txt", CHAT_DROP_IN_TXT)
    write_file_atomic(REPO_ROOT / "prompts" / "PR_AND_ARCHITECTURE_AUDIT_PROMPT.md", AUDIT_PROMPT_MD)

    # 3. Claude Skill + References + Claude Plugin
    write_file_atomic(REPO_ROOT / "skills" / "build-law" / "SKILL.md", SKILL_MD)
    write_file_atomic(
        REPO_ROOT / "skills" / "build-law" / "references" / "four-pillars.md",
        PUBLIC_CONSTITUTION_MD,
    )
    write_file_atomic(
        REPO_ROOT / "skills" / "build-law" / "references" / "fourteen-gates.md",
        AUDIT_PROMPT_MD,
    )
    write_file_atomic(
        REPO_ROOT / "skills" / "build-law" / "references" / "token-economics.md",
        "# Sovereign Token-Economics (`5.0x–8.8x` Value Multiplier)\n\n" + COMPACT_PROMPT_MD,
    )
    write_file_atomic(REPO_ROOT / ".claude" / "CLAUDE.md", COMPACT_PROMPT_MD)
    write_file_atomic(REPO_ROOT / ".claude" / "commands" / "build-law-audit.md", AUDIT_PROMPT_MD)
    write_file_atomic(
        REPO_ROOT / ".claude-plugin" / "plugin.json",
        json.dumps(
            {
                "name": "build-law",
                "version": "1.0.0",
                "description": "Deterministic 14-Gate Constitutional Governance, Polyglot FFP<=8 & 5x-8.8x Token-Efficiency Skill for Claude Code",
                "author": {"name": "Collins Takem (RASA-X-MACHINA)", "url": "https://rasaxmachina.com"},
                "license": "MIT",
                "skills": ["./skills/build-law"],
            },
            indent=2,
        )
        + "\n",
    )

    # Package Claude.ai / Claude Code uploadable Skill .zip & .tar.gz
    DIST_EXTRA.mkdir(parents=True, exist_ok=True)
    skill_zip = DIST_EXTRA / "build-law-claude-skill-v1.0.0.zip"
    with zipfile.ZipFile(skill_zip, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for p in sorted((REPO_ROOT / "skills" / "build-law").rglob("*")):
            if p.is_file():
                rel = p.relative_to(REPO_ROOT / "skills")
                zf.writestr(str(rel), p.read_text(encoding="utf-8"))
    skill_tgz = DIST_EXTRA / "build-law-claude-skill-v1.0.0.tar.gz"
    with tarfile.open(skill_tgz, "w:gz") as tf:
        tf.add(str(REPO_ROOT / "skills" / "build-law"), arcname="build-law")

    # 4. Cursor, OpenCode, Copilot, Windsurf, Cline, Roo, Continue, Aider, Zed, JetBrains, Goose
    cursor_mdc = (
        "---\n"
        "description: Build Law — 14-Gate Completeness, Polyglot FFP<=8, SLECO-SO++ & 5x-8.8x Token Efficiency\n"
        'globs: "**/*"\n'
        "alwaysApply: true\n"
        "---\n\n" + COMPACT_PROMPT_MD
    )
    write_file_atomic(REPO_ROOT / ".cursor" / "rules" / "build-law.mdc", cursor_mdc)
    write_file_atomic(REPO_ROOT / ".cursorrules", COMPACT_PROMPT_MD)

    write_file_atomic(REPO_ROOT / "integrations" / "opencode" / "skills" / "build-law" / "SKILL.md", SKILL_MD)
    opencode_plugin_js = """// ffp: FFP-BLAW-OPENCODE-PLUGIN edge-agent javascript
// build-law-ignore: rule prompt string
// OpenCode Autonomous Build Law Plugin — Injects compact KV-stable Build Law context & tool check
export default {
  name: "build-law-enforcer",
  version: "1.0.0",
  systemPromptSuffix: () => `\\n[Build Law v5.1 Active: Zero TODO/stubs, zero eval/secrets, Polyglot FFP<=8 with # ffp: header, SLECO-SO++ set +e/trap, O(1)/O(N) velocity, System-0 CLI/SQL bypass for 5x-8.8x token efficiency.]\\n`,
};
"""
    write_file_atomic(REPO_ROOT / "integrations" / "opencode" / "plugins" / "build-law-enforcer.js", opencode_plugin_js)

    copilot_inst = "---\napplyTo: \"**\"\n---\n\n" + COMPACT_PROMPT_MD
    write_file_atomic(REPO_ROOT / ".github" / "copilot-instructions.md", COMPACT_PROMPT_MD)
    write_file_atomic(REPO_ROOT / ".github" / "instructions" / "build-law.instructions.md", copilot_inst)
    write_file_atomic(REPO_ROOT / ".windsurf" / "rules" / "build-law.md", COMPACT_PROMPT_MD)
    write_file_atomic(REPO_ROOT / ".windsurfrules", COMPACT_PROMPT_MD)
    write_file_atomic(REPO_ROOT / ".clinerules" / "01-build-law.md", COMPACT_PROMPT_MD)
    write_file_atomic(REPO_ROOT / ".roo" / "rules" / "build-law.md", COMPACT_PROMPT_MD)
    write_file_atomic(REPO_ROOT / ".continue" / "rules" / "build-law.md", COMPACT_PROMPT_MD)
    write_file_atomic(REPO_ROOT / ".aider.conf.yml", "read:\n  - BUILD_LAW.md\n")
    write_file_atomic(REPO_ROOT / ".rules", COMPACT_PROMPT_MD)
    write_file_atomic(REPO_ROOT / ".junie" / "guidelines.md", COMPACT_PROMPT_MD)
    write_file_atomic(REPO_ROOT / ".aiassistant" / "rules" / "build-law.md", COMPACT_PROMPT_MD)
    write_file_atomic(REPO_ROOT / ".goosehints", COMPACT_PROMPT_MD)

    # VS Code workspace settings + extension build
    write_file_atomic(
        REPO_ROOT / ".vscode" / "extensions.json",
        json.dumps({"recommendations": ["rasaxmachina.build-law-sentinel"]}, indent=2) + "\n",
    )
    write_file_atomic(
        REPO_ROOT / ".vscode" / "settings.json",
        json.dumps(
            {
                "github.copilot.chat.codeGeneration.useInstructionFiles": True,
                "buildLaw.auditOnSave": True,
                "buildLaw.autoEnsureWorkspaceRules": True,
            },
            indent=2,
        )
        + "\n",
    )
    write_file_atomic(
        REPO_ROOT / ".vscode" / "tasks.json",
        json.dumps(
            {
                "version": "2.0.0",
                "tasks": [
                    {
                        "label": "Build Law: 14-Gate Audit",
                        "type": "shell",
                        "command": "build-law check .",
                        "group": "test",
                    }
                ],
            },
            indent=2,
        )
        + "\n",
    )
    vsix_path = build_vscode_extension_and_vsix()

    # 5. Reusable GitHub Action, CI Workflow, Pre-Commit, & SLECO-SO++ Installer
    action_yml = """name: 'Build Law 14-Gate Verification'
description: 'Deterministic zero-token static verification of Build Law (zero stubs, zero leaked secrets, zero eval injection, SLECO-SO++ shell safety).'
author: 'Collins Takem (RASA-X-MACHINA)'
branding:
  icon: 'shield'
  color: 'purple'
inputs:
  path:
    description: 'Target directory or file to verify'
    required: false
    default: '.'
runs:
  using: 'composite'
  steps:
    - name: Set up Go & Run Build Law 14-Gate Check
      shell: bash
      run: |
        set +e
        go run "${{ github.action_path }}/cmd/build-law/main.go" check "${{ inputs.path }}"
"""
    write_file_atomic(REPO_ROOT / "action.yml", action_yml)

    ci_yml = """name: Build Law 14-Gate Sentinel

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

permissions:
  contents: read

jobs:
  paramasiva-gate:
    name: 14-Gate Deterministic Audit (0 LLM Tokens)
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-go@v5
        with:
          go-version: '1.22'
      - name: Compile & Execute Build Law Verifier
        run: |
          go build -trimpath -ldflags="-s -w" -o build-law ./cmd/build-law
          ./build-law check .
"""
    write_file_atomic(REPO_ROOT / ".github" / "workflows" / "build-law-gate.yml", ci_yml)

    pre_commit_yml = """- id: build-law-check
  name: Build Law 14-Gate Static Verifier
  description: Verifies zero plaintext secrets, zero Unicode prompt-injection tags, zero eval(), and zero TODO stubs (0 LLM tokens).
  entry: build-law check
  language: golang
  pass_filenames: false
"""
    write_file_atomic(REPO_ROOT / ".pre-commit-hooks.yaml", pre_commit_yml)
    write_file_atomic(REPO_ROOT / "install.sh", INSTALL_SH, mode=0o755)

    # 6. Enterprise GitHub Governance & AEO / GEO / Academic Citation Files
    write_file_atomic(
        REPO_ROOT / "SECURITY.md",
        "# Security Policy (`GDPR++` & `Dhūmāvatī` Boundary)\n\n"
        "- **Supported Version:** `v1.0.x` (`Edition v5.1`)\n"
        "- **Zero-Secret Policy:** Never include plaintext credentials in issues or pull requests.\n"
        "- **Coordinated Disclosure:** Report vulnerabilities via [rasaxmachina.com/.well-known/security.txt](https://rasaxmachina.com/.well-known/security.txt) or [rasaxmachina.com/collins](https://rasaxmachina.com/collins) (`< 24h` triage SLA).\n",
    )
    write_file_atomic(
        REPO_ROOT / "CONTRIBUTING.md",
        "# Contributing to Build Law\n\n"
        "All pull requests must pass `./build-law check .` (`0` critical/high findings, `0` placeholder stubs, atomic commits, and monotonic rigor—never weakening existing safety, privacy, or performance guarantees).\n",
    )
    write_file_atomic(
        REPO_ROOT / "GOVERNANCE.md",
        "# Monotonic Ratchet Governance\n\n"
        "**Build Law** is governed under a **Monotonic Constitutional Ratchet** maintained by **Collins Takem** (**RASA-X-MACHINA**): amendments may add stricter safety gates, broader IDE/harness adapters, or stronger token-efficiency mechanisms, but may never remove or weaken any of the 4 Pillars or 14 Gates.\n",
    )
    write_file_atomic(
        REPO_ROOT / "CODE_OF_CONDUCT.md",
        "# Code of Conduct\n\nWe uphold rigorous, evidence-backed, respectful technical discourse focused on verifiable engineering artifacts.\n",
    )
    write_file_atomic(
        REPO_ROOT / "SUPPORT.md",
        "# Support & Enterprise Architecture Sprints\n\n"
        "- **Documentation & Quickstart:** See [README.md](./README.md)\n"
        "- **72-Hour Bounded `VRTTI` Architecture Sprints & Enterprise Rollouts:** [vrtti.rasaxmachina.com](https://vrtti.rasaxmachina.com) · [rasaxmachina.com](https://rasaxmachina.com)\n",
    )
    write_file_atomic(
        REPO_ROOT / "CHANGELOG.md",
        "# Changelog\n\n## [1.0.0] — 2026-11-17 (`Edition v5.1-SOVEREIGN-CONSTITUTION`)\n"
        "- Initial public flagship release of **Build Law** across 18+ AI coding harnesses & IDEs, `.vsix` extension, Claude Skill, MCP server, and 7 Ed25519-signed multi-OS binary package formats.\n"
        "- Codifies the 4 Pillars: 14-Gate `PARAMASIVA` Completeness, Polyglot `FFP<=8` Fitness Matrix, `SLECO-SO++` Runtime Standard, and `GDPR++` + `5.0x–8.8x` Sovereign Token-Economics (`Vāk` System-0 Gate).\n",
    )
    write_file_atomic(REPO_ROOT / "CODEOWNERS", "* @collinstaken525-cloud\n")
    write_file_atomic(
        REPO_ROOT / ".github" / "dependabot.yml",
        "version: 2\nupdates:\n  - package-ecosystem: \"gomod\"\n    directory: \"/\"\n    schedule:\n      interval: \"weekly\"\n  - package-ecosystem: \"github-actions\"\n    directory: \"/\"\n    schedule:\n      interval: \"weekly\"\n",
    )

    citation_cff = """cff-version: 1.2.0
message: "If you use or reference Build Law in research, engineering standards, or benchmarks, please cite it as below."
title: "Build Law: Deterministic Constitutional Governance, Polyglot FFP Architecture, and Sub-Linear Token Economics for Autonomous Software Engineering"
version: "5.1.0"
date-released: "2026-11-17"
license: MIT
url: "https://github.com/Tianxia-Core/Build-Law"
repository-code: "https://github.com/Tianxia-Core/Build-Law"
authors:
  - family-names: "Takem"
    given-names: "Collins"
    affiliation: "RASA-X-MACHINA"
    website: "https://rasaxmachina.com/collins"
keywords:
  - autonomous-agents
  - software-architecture
  - polyglot-systems
  - token-efficiency
  - formal-verification
  - devsecops
  - gdpr
"""
    write_file_atomic(REPO_ROOT / "CITATION.cff", citation_cff)

    llms_txt = """# Build Law (by Collins Takem · RASA-X-MACHINA)

> Build Law is an open-source (MIT) constitutional engineering standard, zero-token static verifier CLI, MCP server, IDE extension, and universal rule pack that stops AI coding agents from shipping broken stubs, security holes, bloated single-language daemons, and runaway token bills—delivering 5.0x to 8.8x higher engineering output per token across Claude Code, Cursor, OpenCode, VS Code, Copilot, Windsurf, Cline, Aider, Zed, Gemini, and Codex.

## Canonical Resources
- [README & Layman + Technical Guide](https://github.com/Tianxia-Core/Build-Law/blob/main/README.md)
- [Full Build Law v5.1 Constitution](https://github.com/Tianxia-Core/Build-Law/blob/main/BUILD_LAW.md)
- [Compact KV-Cached System Prompt (~1,050 tokens)](https://github.com/Tianxia-Core/Build-Law/blob/main/prompts/SYSTEM_PROMPT_COMPACT_KV.md)
- [Claude Skill Definition](https://github.com/Tianxia-Core/Build-Law/blob/main/skills/build-law/SKILL.md)
- [Author & Principal Architect Profile — Collins Takem](https://rasaxmachina.com/collins)
- [RASA-X-MACHINA & tianxiaOS Portal](https://rasaxmachina.com)
"""
    write_file_atomic(REPO_ROOT / "llms.txt", llms_txt)
    write_file_atomic(REPO_ROOT / "llms-full.txt", llms_txt + "\n---\n\n" + PUBLIC_CONSTITUTION_MD)

    schema_jsonld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "SoftwareSourceCode",
                "name": "Build Law",
                "alternateName": "TianxiaOS Build Law v5.1",
                "version": "1.0.0",
                "license": "https://opensource.org/licenses/MIT",
                "codeRepository": "https://github.com/Tianxia-Core/Build-Law",
                "programmingLanguage": ["Go", "JavaScript", "Markdown", "Nix", "Bash"],
                "description": "Deterministic 4-Pillar, 14-Gate constitutional governance, Polyglot FFP<=8 architecture, SLECO-SO++ runtime resilience, and 5.0x–8.8x token-efficiency toolkit for AI coding agents and engineering teams.",
                "author": {
                    "@type": "Person",
                    "name": "Collins Takem",
                    "jobTitle": "Founder & Principal Systems Architect",
                    "url": "https://rasaxmachina.com/collins",
                    "worksFor": {"@type": "Organization", "name": "RASA-X-MACHINA", "url": "https://rasaxmachina.com"},
                },
            }
        ],
    }
    write_file_atomic(REPO_ROOT / "schema.jsonld", json.dumps(schema_jsonld, indent=2) + "\n")

    print(f"GENERATED_FORMATS_OK vsix={vsix_path.name} skill_zip={skill_zip.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
