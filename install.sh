#!/usr/bin/env bash
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

log_info() { printf '[build-law] %s\n' "$1"; }
log_err()  { printf '[build-law] ERROR: %s\n' "$1" >&2; }

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
