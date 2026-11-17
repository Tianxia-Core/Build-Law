# Build Law — 14-Gate Architecture & Pull-Request Audit Prompt

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
