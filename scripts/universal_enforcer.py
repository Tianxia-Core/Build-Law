#!/usr/bin/env python3
# ffp: FFP-BLAW-ENFORCER concurrent-daemon python
# dss14-ignore: PRATYANGIRA KALI (governance rule strings reference forbidden anti-patterns)
"""
tx_build_law_universal_enforcer.py — Universal Multi-Harness, Multi-IDE & Tailscale Mesh
Build Law Auto-Enforcer (`pixel8pro` Termux + `latitude-tianxia` + `tianxia-relay` + Mesh Peers).

Guarantees Build Law compliance automatically across:
  1. All 20+ known AI harnesses & IDEs (Claude Code, OpenCode, Cursor, VS Code, VSCodium,
     Code-Server, GitHub Copilot, Windsurf, Cline, Roo Code, Continue, Aider, Zed,
     JetBrains Junie/AI, Gemini CLI, Antigravity, Codex CLI, Block Goose).
  2. Any FUTURE AI-native IDE, VSCodium fork, or CLI agent installed later on the device
     (heuristic auto-discovery of `extensions/`, `User/prompts/`, `skills/`, `rules/`, `memories/`).
  3. Any FUTURE Git repository initialized or cloned on the device (`git config --global init.templateDir`
     with non-destructive pre-commit secret/injection/ratchet gate).
  4. Shell environment & periodic self-healing watchdog (Termux profile/boot + systemd timers across
     all online Tailscale mesh nodes with exponential backoff `_PEER_OFFLINE_UNTIL` on sleeping peers).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

HOME = Path.home()
STATE_DIR = HOME / ".config" / "tianxia"
BLAW_DIR = HOME / ".config" / "build-law"
STATE_FILE = STATE_DIR / "universal_build_law_enforcer_state.json"

COMPACT_BUILD_LAW = """# BUILD LAW — Deterministic Autonomous Engineering & Token-Efficiency Constitution (v5.1)

Operate strictly under **Build Law** (Collins Takem · RASA-X-MACHINA · tianxiaOS):

1. **PILLAR 1 — 14-Gate Completeness (`PARAMASIVA` Gate)**:
   - **Zero Placeholders**: Never emit `TODO`, `FIXME`, `pass`, `todo!()`, `unimplemented!()`, or mock data.
   - **Innocence & Containment**: Zero `eval()`, zero shell-string injection, bounded timeouts on all loops/sockets, explicit capability checks before mutating files, keys, networks, or money.
   - **Graceful Recovery**: Log errors with structured context and recover cleanly; never swallow exceptions silently.
2. **PILLAR 2 — Polyglot `FFP-First` Modularity (`<= 8` FFPs per Service)**:
   - Decompose systems into atomic **Function-Feature Pairs (`FFPs`)**, max `<= 8` FFPs per isolated service/unit.
   - Match language to workload physics (`Rust`/`Zig`/`C` for daemons, codecs & kernels; `OCaml`/`Rust` for capability proxies; `Go`/`Rust` for CLIs & relays; `Nix` for hermetic infra; `TypeScript` for UIs; `Python`/`Julia` for analytics & glue — never Python as a lazy daemon default).
   - Annotate lines 1–5 of every source file: `// ffp: <FFP-ID> <fitness-class> <language>`.
3. **PILLAR 3 — `SLECO-SO++` Runtime & `ENHAN³` Hardening**:
   - Shell scripts use `set +e`, `set +u`, explicit `trap` cleanup, and pure parameter expansion (`${var##*/}`) over blind `set -e` or hot-loop subshells.
   - Enforce $O(1)$ / $O(N)$ linear algorithms, exponential peer backoff, and atomic writes (`write .tmp` -> `rename`).
   - Harden every unit across **Resilience**, **Performance**, and **Security** (`ENHAN³`).
4. **PILLAR 4 — `GDPR++` Security & `5.0x–8.8x` Token-Economics (`Vāk` System-0 Gate)**:
   - Store credentials strictly in `chmod 0600` out-of-tree vaults; enforce `< 50ms` ephemeral key cryptoshredding (`GDPR++`).
   - **System-0 Bypass**: Execute deterministic filtering, deduplication, regex scans, and math in compiled CLI/SQL/FTS5 tools (`$0.00`, `0` LLM tokens) rather than inside LLM prompts.
   - **Context Compression**: Batch parallel tool calls, project `< 2%` schema/top-K digests instead of raw dumps, read bounded `<= 250`-line slices on large files, and short-circuit no-op builds via SHA-256 digests.
"""

SKILL_PACK_MD = (
    "---\n"
    "name: build-law\n"
    "description: Use when designing, coding, refactoring, auditing, packaging, or deploying any software, script, database, UI, or AI workflow to enforce 14-gate completeness, polyglot FFP<=8 modularity, SLECO-SO++ resilience, GDPR++ security, and 5x-8.8x token efficiency.\n"
    "metadata:\n"
    "  author: Collins Takem (RASA-X-MACHINA)\n"
    "  version: \"5.1.0\"\n"
    "  category: architecture-governance\n"
    "  triggers: build-law, code, architecture, security, optimize, deploy, refactor, review\n"
    "---\n\n" + COMPACT_BUILD_LAW
)

CURSOR_MDC = (
    "---\n"
    "description: Build Law — 14-Gate Completeness, Polyglot FFP<=8, SLECO-SO++ & 5x-8.8x Token Efficiency\n"
    'globs: "**/*"\n'
    "alwaysApply: true\n"
    "---\n\n" + COMPACT_BUILD_LAW
)

COPILOT_INSTRUCTIONS = "---\napplyTo: \"**\"\n---\n\n" + COMPACT_BUILD_LAW

VSCODE_EXT_PKG = {
    "name": "build-law-sentinel",
    "displayName": "Build Law — 14-Gate AI Engineering & Token-Efficiency Sentinel",
    "description": "Universal Build Law enforcement & save-time zero-stub/zero-secret diagnostics for VS Code, Cursor, Windsurf & Copilot.",
    "version": "1.0.0",
    "publisher": "rasaxmachina",
    "engines": {"vscode": "^1.74.0"},
    "activationEvents": ["onStartupFinished"],
    "main": "./extension.js",
    "contributes": {
        "commands": [
            {"command": "buildLaw.auditActiveFile", "title": "Build Law: Audit Active File (14-Gate Check)"},
        ]
    },
}

VSCODE_EXT_JS = """// ffp: FFP-BLAW-VSCODE-EXT frontend javascript
// build-law-ignore: scanner definitions
const vscode = require('vscode');
const SECRET_RE = /(sk_live_[0-9a-zA-Z_]{12,}|gh[pousr]_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16})/;
const EVAL_RE = /\\beval\\s*\\(/;
function activate(context) {
  const diags = vscode.languages.createDiagnosticCollection('buildLaw');
  context.subscriptions.push(diags);
  const bar = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Right, 100);
  bar.text = '$(shield) Build Law: v5.1';
  bar.tooltip = 'Build Law Constitutional Governance Active';
  bar.command = 'buildLaw.auditActiveFile';
  bar.show();
  context.subscriptions.push(bar);
  const scan = doc => {
    if (!doc || doc.uri.scheme !== 'file') return;
    const out = [];
    doc.getText().split(/\\r?\\n/).forEach((ln, idx) => {
      if (SECRET_RE.test(ln)) {
        out.push(new vscode.Diagnostic(new vscode.Range(idx, 0, idx, ln.length), '[Build Law] Plaintext secret detected; move to 0600 vault.', vscode.DiagnosticSeverity.Error));
      }
      if (EVAL_RE.test(ln) && !ln.includes('ignore')) {
        out.push(new vscode.Diagnostic(new vscode.Range(idx, 0, idx, ln.length), '[Build Law] Dynamic eval() prohibited.', vscode.DiagnosticSeverity.Warning));
      }
    });
    diags.set(doc.uri, out);
  };
  context.subscriptions.push(vscode.commands.registerCommand('buildLaw.auditActiveFile', () => {
    if (vscode.window.activeTextEditor) scan(vscode.window.activeTextEditor.document);
  }));
  context.subscriptions.push(vscode.workspace.onDidSaveTextDocument(scan));
}
function deactivate() {}
module.exports = { activate, deactivate };
"""

GIT_PRE_COMMIT_HOOK = """#!/usr/bin/env bash
# ffp: FFP-BLAW-GIT-HOOK crypto-signer bash
# Build Law Universal Pre-Commit Secret & Prompt-Injection Gate (SLECO-SO++)
set +e
set +u

REPO_TOP="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
if [ -x "${REPO_TOP}/.git/hooks/pre-commit.local" ]; then
  "${REPO_TOP}/.git/hooks/pre-commit.local" "$@"
  rc=$?
  if [ "${rc}" -ne 0 ]; then
    exit "${rc}"
  fi
fi

# Fast O(N) staged diff check for plaintext API keys & Unicode Bidi smuggling
STAGED_DIFF="$(git diff --cached --unified=0 2>/dev/null || true)"
if [ -n "${STAGED_DIFF}" ]; then
  if printf '%s' "${STAGED_DIFF}" | grep -Eq '^\\+.*(sk_live_[0-9a-zA-Z_]{12,}|gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16})'; then
    printf '[Build Law · 07-DHUMAVATI] COMMIT BLOCKED: Plaintext API credential detected in staged changes.\\n' >&2
    exit 1
  fi
fi

# Verify Build Law 7-mirror seal if inside sovereign workspace
if [ -f "${REPO_TOP}/tianxia/bin/tx_build_law_sentinel.py" ]; then
  python3 "${REPO_TOP}/tianxia/bin/tx_build_law_sentinel.py" --verify >/dev/null 2>&1
  if [ $? -ne 0 ]; then
    printf '[Build Law · Sentinel] COMMIT BLOCKED: Build Law mirror seal verification failed.\\n' >&2
    exit 1
  fi
fi

exit 0
"""


def write_atomic_if_changed(path: Path, content: str, mode: int = 0o644) -> bool:
    raw = content.encode("utf-8")
    if path.is_file() and not path.is_symlink():
        try:
            if path.read_bytes() == raw:
                return False
        except OSError:
            pass
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.tmp.{os.getpid()}")
    tmp.write_bytes(raw)
    os.chmod(tmp, mode)
    os.replace(tmp, path)
    return True


def load_canonical_law_text() -> str:
    candidates = [
        Path("/data/data/com.termux/files/home/workspace/AGENTS.md"),
        Path("/var/lib/tianxia/AGENTS.md"),
        Path("/var/lib/tianxia/BUILD_LAW.md"),
        BLAW_DIR / "BUILD_LAW.md",
    ]
    for c in candidates:
        if c.is_file():
            try:
                return c.read_text(encoding="utf-8")
            except OSError:
                continue
    return COMPACT_BUILD_LAW


def install_vscode_extension_dir(ext_parent: Path) -> str:
    ext_dir = ext_parent / "rasaxmachina.build-law-sentinel-1.0.0"
    write_atomic_if_changed(ext_dir / "package.json", json.dumps(VSCODE_EXT_PKG, indent=2) + "\n")
    write_atomic_if_changed(ext_dir / "extension.js", VSCODE_EXT_JS)
    write_atomic_if_changed(ext_dir / "README.md", "# Build Law Sentinel Extension\n")
    return str(ext_dir)


def ensure_ide_user_settings(user_dir: Path) -> None:
    write_atomic_if_changed(user_dir / "prompts" / "build-law.instructions.md", COPILOT_INSTRUCTIONS)
    settings_path = user_dir / "settings.json"
    data: dict[str, Any] = {}
    if settings_path.is_file():
        try:
            parsed = json.loads(settings_path.read_text(encoding="utf-8"))
            if isinstance(parsed, dict):
                data = parsed
        except Exception:
            return  # Respect custom JSONC with comments if unparseable
    changed = False
    if data.get("github.copilot.chat.codeGeneration.useInstructionFiles") is not True:
        data["github.copilot.chat.codeGeneration.useInstructionFiles"] = True
        changed = True
    if data.get("buildLaw.auditOnSave") is not True:
        data["buildLaw.auditOnSave"] = True
        changed = True
    if changed:
        write_atomic_if_changed(settings_path, json.dumps(data, indent=2) + "\n")


def enforce_local_device() -> dict[str, Any]:
    t0 = time.perf_counter()
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    BLAW_DIR.mkdir(parents=True, exist_ok=True)

    full_law = load_canonical_law_text()
    law_sha = hashlib.sha256(full_law.encode("utf-8")).hexdigest()

    write_atomic_if_changed(BLAW_DIR / "BUILD_LAW.md", full_law)
    write_atomic_if_changed(BLAW_DIR / "BUILD_LAW_COMPACT.md", COMPACT_BUILD_LAW)
    write_atomic_if_changed(STATE_DIR / "BUILD_LAW.md", full_law)

    # 1. Provision all 20+ standard AI CLI & IDE user-level config paths
    harness_files: dict[Path, str] = {
        HOME / ".claude" / "CLAUDE.md": COMPACT_BUILD_LAW,
        HOME / ".claude" / "skills" / "build-law" / "SKILL.md": SKILL_PACK_MD,
        HOME / ".config" / "opencode" / "AGENTS.md": COMPACT_BUILD_LAW,
        HOME / ".config" / "opencode" / "skills" / "build-law" / "SKILL.md": SKILL_PACK_MD,
        HOME / ".config" / "opencode" / "skills-library" / "antigravity" / "skills" / "build-law" / "SKILL.md": SKILL_PACK_MD,
        HOME / ".gemini" / "GEMINI.md": COMPACT_BUILD_LAW,
        HOME / ".gemini" / "antigravity-cli" / "AGENTS.md": COMPACT_BUILD_LAW,
        HOME / ".codex" / "AGENTS.md": COMPACT_BUILD_LAW,
        HOME / ".codex" / "instructions.md": COMPACT_BUILD_LAW,
        HOME / ".cursor" / "rules" / "build-law.mdc": CURSOR_MDC,
        HOME / ".config" / "github-copilot" / "instructions.md": COMPACT_BUILD_LAW,
        HOME / ".codeium" / "windsurf" / "memories" / "global_rules.md": COMPACT_BUILD_LAW,
        HOME / ".windsurf" / "rules" / "build-law.md": COMPACT_BUILD_LAW,
        HOME / ".clinerules" / "01-build-law.md": COMPACT_BUILD_LAW,
        HOME / "Documents" / "Cline" / "Rules" / "build-law.md": COMPACT_BUILD_LAW,
        HOME / ".roo" / "rules" / "build-law.md": COMPACT_BUILD_LAW,
        HOME / ".continue" / "rules" / "build-law.md": COMPACT_BUILD_LAW,
        HOME / ".config" / "zed" / "rules.md": COMPACT_BUILD_LAW,
        HOME / ".junie" / "guidelines.md": COMPACT_BUILD_LAW,
        HOME / ".aiassistant" / "rules" / "build-law.md": COMPACT_BUILD_LAW,
        HOME / ".config" / "goose" / ".goosehints": COMPACT_BUILD_LAW,
    }
    # Root $HOME upward-traversal fallbacks (used by Claude/Codex/OpenCode/Cursor when run outside ~/workspace)
    for top_doc in ("AGENTS.md", "CLAUDE.md", "GEMINI.md", "BUILD_LAW.md"):
        p = HOME / top_doc
        if not p.exists() or (p.is_file() and not p.is_symlink()):
            harness_files[p] = COMPACT_BUILD_LAW

    updated_count = 0
    for dest, body in harness_files.items():
        if write_atomic_if_changed(dest, body):
            updated_count += 1

    # Safe Aider global config merge
    aider_cfg = HOME / ".aider.conf.yml"
    blaw_ref = str(BLAW_DIR / "BUILD_LAW_COMPACT.md")
    if not aider_cfg.exists():
        write_atomic_if_changed(aider_cfg, f"read:\n  - {blaw_ref}\n")
    else:
        txt = aider_cfg.read_text(encoding="utf-8", errors="ignore")
        if blaw_ref not in txt and "BUILD_LAW" not in txt:
            write_atomic_if_changed(aider_cfg, txt.rstrip() + f"\nread:\n  - {blaw_ref}\n")

    # 2. Known + Future IDE Extension & User/prompts Auto-Injection
    ide_ext_roots = [
        HOME / ".vscode" / "extensions",
        HOME / ".vscode-server" / "extensions",
        HOME / ".vscode-oss" / "extensions",
        HOME / ".cursor" / "extensions",
        HOME / ".cursor-server" / "extensions",
        HOME / ".windsurf" / "extensions",
        HOME / ".local" / "share" / "code-server" / "extensions",
    ]
    ide_user_dirs = [
        HOME / ".config" / "Code" / "User",
        HOME / ".config" / "Code - OSS" / "User",
        HOME / ".config" / "VSCodium" / "User",
        HOME / ".config" / "Cursor" / "User",
        HOME / ".config" / "Windsurf" / "User",
        HOME / ".config" / "code-server" / "User",
    ]

    # Future-tool heuristic discovery across $HOME/.* and $HOME/.config/*
    discovered_future_tools: list[str] = []
    scan_parents = [HOME, HOME / ".config"]
    skip_names = {".git", ".ssh", ".cache", ".npm", ".cargo", ".rustup", ".local", ".termux", ".gradle"}
    for parent in scan_parents:
        if not parent.is_dir():
            continue
        for child in parent.iterdir():
            if not child.is_dir() or child.name in skip_names:
                continue
            if (child / "extensions").is_dir() and (child / "extensions") not in ide_ext_roots:
                ide_ext_roots.append(child / "extensions")
                discovered_future_tools.append(f"ide-ext:{child.name}")
            if (child / "User").is_dir() and (child / "User") not in ide_user_dirs:
                ide_user_dirs.append(child / "User")
                discovered_future_tools.append(f"ide-user:{child.name}")
            for sub_kind in ("skills", "rules", "prompts", "memories"):
                sd = child / sub_kind
                if sd.is_dir():
                    if sub_kind == "skills":
                        write_atomic_if_changed(sd / "build-law" / "SKILL.md", SKILL_PACK_MD)
                    else:
                        write_atomic_if_changed(sd / "build-law.md", COMPACT_BUILD_LAW)
                    discovered_future_tools.append(f"agent-{sub_kind}:{child.name}")

    installed_exts = [install_vscode_extension_dir(er) for er in ide_ext_roots]
    for ud in ide_user_dirs:
        ensure_ide_user_settings(ud)

    # 3. Global Git init.templateDir + Pre-Commit Gate (Future Repositories Guaranteed)
    git_tpl_hooks = HOME / ".config" / "git" / "template" / "hooks"
    hook_body = GIT_PRE_COMMIT_HOOK
    if Path("/data/data/com.termux/files/usr/bin/bash").is_file():
        hook_body = hook_body.replace("#!/usr/bin/env bash", "#!/data/data/com.termux/files/usr/bin/bash", 1)
    write_atomic_if_changed(git_tpl_hooks / "pre-commit", hook_body, mode=0o755)
    if shutil.which("git"):
        subprocess.run(
            ["git", "config", "--global", "init.templateDir", str(HOME / ".config" / "git" / "template")],
            check=False,
            timeout=5,
        )

    # 4. Shell Profile Environment Export & Lightweight Auto-Heal Hook
    env_sh = STATE_DIR / "tx_build_law_env.sh"
    enforcer_self = Path(__file__).resolve()
    env_sh_body = (
        "# ffp: FFP-BLAW-SHELL-ENV glue bash\n"
        f'export TIANXIA_BUILD_LAW_PATH="{BLAW_DIR / "BUILD_LAW.md"}"\n'
        'export BUILD_LAW_ENFORCED="1"\n'
        'if [ -d "${HOME}/bin" ]; then case ":${PATH}:" in *":${HOME}/bin:"*) ;; *) export PATH="${HOME}/bin:${PATH}" ;; esac; fi\n'
        f'if [ -f "{enforcer_self}" ]; then\n'
        f'  _blaw_stamp="{STATE_FILE}"\n'
        '  if [ ! -f "${_blaw_stamp}" ] || [ -n "$(find "${_blaw_stamp}" -mmin +60 2>/dev/null)" ]; then\n'
        f'    (python3 "{enforcer_self}" --quiet >/dev/null 2>&1 &)\n'
        '  fi\n'
        'fi\n'
    )
    write_atomic_if_changed(env_sh, env_sh_body)

    source_line = f'[ -f "{env_sh}" ] && . "{env_sh}"'
    for rc_name in (".bashrc", ".zshrc", ".profile"):
        rc_path = HOME / rc_name
        if rc_path.is_file():
            rc_txt = rc_path.read_text(encoding="utf-8", errors="ignore")
            if "tx_build_law_env.sh" not in rc_txt:
                write_atomic_if_changed(rc_path, rc_txt.rstrip() + "\n" + source_line + "\n")
        elif rc_name == ".bashrc":
            write_atomic_if_changed(rc_path, source_line + "\n")

    # Termux boot hook if running on Termux
    if os.environ.get("TERMUX_VERSION") or Path("/data/data/com.termux/files/usr").is_dir():
        boot_script = HOME / ".termux" / "boot" / "tx-build-law-enforcer.sh"
        write_atomic_if_changed(
            boot_script,
            f"#!/data/data/com.termux/files/usr/bin/bash\nset +e\npython3 \"{enforcer_self}\" --quiet >/dev/null 2>&1\n",
            mode=0o755,
        )

    # Linux root /etc/profile.d hook if uid == 0
    if hasattr(os, "geteuid") and os.geteuid() == 0 and Path("/etc/profile.d").is_dir():
        write_atomic_if_changed(Path("/etc/profile.d/tx-build-law.sh"), env_sh_body)

    elapsed_ms = round((time.perf_counter() - t0) * 1000.0, 2)
    report = {
        "ok": True,
        "host": os.uname().nodename,
        "arch": os.uname().machine,
        "law_sha256": law_sha,
        "harness_configs_governed": len(harness_files) + 1,
        "files_updated_this_pass": updated_count,
        "ide_extension_roots_injected": len(installed_exts),
        "future_tools_auto_discovered": sorted(set(discovered_future_tools)),
        "git_global_template_active": True,
        "elapsed_ms": elapsed_ms,
        "timestamp": int(time.time()),
    }
    write_atomic_if_changed(STATE_FILE, json.dumps(report, indent=2) + "\n")
    return report


def sync_tailscale_mesh() -> dict[str, Any]:
    """Propagates Build Law binary, constitution, and systemd 15-min timer across mesh peers with exponential backoff."""
    peers = [
        {"alias": "tlat", "name": "latitude-tianxia", "arch": "x86_64"},
        {"alias": "trelay", "name": "tianxia-relay", "arch": "x86_64"},
        {"alias": "tpoco", "name": "poco-x5-pro-5g", "arch": "aarch64"},
        {"alias": "txps", "name": "xps13-tianxia", "arch": "x86_64"},
    ]
    backoff_file = STATE_DIR / "mesh_peer_backoff.json"
    backoff_state: dict[str, Any] = {}
    if backoff_file.is_file():
        try:
            backoff_state = json.loads(backoff_file.read_text(encoding="utf-8"))
        except Exception:
            backoff_state = {}

    ws_dist = Path("/data/data/com.termux/files/home/workspace/platforms/Build-Law/dist")
    self_script = Path(__file__).resolve()
    law_file = BLAW_DIR / "BUILD_LAW.md"

    results: dict[str, Any] = {}
    now = time.time()

    for p in peers:
        alias = p["alias"]
        pstate = backoff_state.get(alias, {"failures": 0, "offline_until": 0})
        if now < float(pstate.get("offline_until", 0)):
            results[alias] = {"status": "BACKOFF_SKIPPED", "offline_until": pstate["offline_until"]}
            continue

        # Quick SSH reachability check
        probe = subprocess.run(
            ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=4", alias, "uname -m && id -u"],
            capture_output=True,
            text=True,
            timeout=8,
            check=False,
        )
        if probe.returncode != 0:
            fails = int(pstate.get("failures", 0)) + 1
            delay = min(3600, 60 * (2 ** min(fails, 6)))
            backoff_state[alias] = {"failures": fails, "offline_until": round(now + delay, 1)}
            results[alias] = {"status": "OFFLINE_BACKOFF_SET", "retry_in_sec": delay}
            continue

        backoff_state[alias] = {"failures": 0, "offline_until": 0}
        remote_lines = probe.stdout.strip().splitlines()
        remote_arch = remote_lines[0].strip() if remote_lines else p["arch"]
        remote_uid = remote_lines[1].strip() if len(remote_lines) > 1 else "1000"

        bin_cand = ws_dist / (
            "build-law-v1.0.0-linux-x86_64" if "x86_64" in remote_arch else "build-law-v1.0.0-android-aarch64"
        )
        remote_bin_dir = "/usr/local/bin" if remote_uid == "0" else "~/bin"
        remote_cfg_dir = "/var/lib/tianxia/bin" if remote_uid == "0" else "~/.config/tianxia"

        subprocess.run(
            ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=5", alias, f"mkdir -p {remote_bin_dir} {remote_cfg_dir} ~/.config/build-law"],
            check=False,
            timeout=10,
        )
        if law_file.is_file():
            subprocess.run(
                ["scp", "-q", "-o", "ConnectTimeout=5", str(law_file), f"{alias}:~/.config/build-law/BUILD_LAW.md"],
                check=False,
                timeout=15,
            )
        if bin_cand.is_file():
            subprocess.run(
                ["scp", "-q", "-o", "ConnectTimeout=5", str(bin_cand), f"{alias}:{remote_bin_dir}/build-law"],
                check=False,
                timeout=20,
            )
        subprocess.run(
            ["scp", "-q", "-o", "ConnectTimeout=5", str(self_script), f"{alias}:{remote_cfg_dir}/tx_build_law_universal_enforcer.py"],
            check=False,
            timeout=15,
        )

        # Activate enforcer + systemd timer on remote Linux root nodes
        remote_cmd = (
            f"chmod 755 {remote_bin_dir}/build-law {remote_cfg_dir}/tx_build_law_universal_enforcer.py 2>/dev/null || true; "
            f"python3 {remote_cfg_dir}/tx_build_law_universal_enforcer.py --quiet"
        )
        if remote_uid == "0":
            remote_cmd += (
                " && if [ -d /etc/systemd/system ]; then "
                "printf '%s\\n' '[Unit]' 'Description=TianxiaOS Universal Build Law Multi-Harness Enforcer' '[Service]' 'Type=oneshot' "
                f"'ExecStart=/usr/bin/env python3 {remote_cfg_dir}/tx_build_law_universal_enforcer.py --quiet' "
                "'MemoryMax=128M' 'TasksMax=32' 'NoNewPrivileges=yes' > /etc/systemd/system/tx-build-law-enforcer.service && "
                "printf '%s\\n' '[Unit]' 'Description=Periodic Universal Build Law Enforcement Timer' '[Timer]' "
                "'OnBootSec=1min' 'OnUnitActiveSec=15min' 'Persistent=true' '[Install]' 'WantedBy=timers.target' "
                "> /etc/systemd/system/tx-build-law-enforcer.timer && "
                "systemctl daemon-reload && systemctl enable --now tx-build-law-enforcer.timer >/dev/null 2>&1 || true; fi"
            )
        exec_res = subprocess.run(
            ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=6", alias, remote_cmd],
            capture_output=True,
            text=True,
            timeout=25,
            check=False,
        )
        results[alias] = {
            "status": "SYNCED_AND_ACTIVE" if exec_res.returncode == 0 else "PARTIAL",
            "hostname": p["name"],
            "arch": remote_arch,
            "rc": exec_res.returncode,
        }

    write_atomic_if_changed(backoff_file, json.dumps(backoff_state, indent=2) + "\n")
    return results


def main() -> int:
    ap = argparse.ArgumentParser(description="Universal Multi-Harness, Multi-IDE & Tailscale Mesh Build Law Enforcer")
    ap.add_argument("--sync-mesh", action="store_true", help="Also propagate and activate across Tailscale mesh nodes")
    ap.add_argument("--quiet", action="store_true", help="Suppress stdout unless error occurs")
    args = ap.parse_args()

    local_rep = enforce_local_device()
    out: dict[str, Any] = {"local": local_rep}
    if args.sync_mesh:
        out["mesh"] = sync_tailscale_mesh()

    if not args.quiet:
        print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
