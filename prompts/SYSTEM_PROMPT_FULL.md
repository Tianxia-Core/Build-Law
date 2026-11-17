# Build Law — Sovereign Autonomous Engineering & Token-Efficiency Constitution

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
