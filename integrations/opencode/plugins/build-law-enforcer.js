// ffp: FFP-BLAW-OPENCODE-PLUGIN edge-agent javascript
// build-law-ignore: rule prompt string
// OpenCode Autonomous Build Law Plugin — Injects compact KV-stable Build Law context & tool check
export default {
  name: "build-law-enforcer",
  version: "1.0.0",
  systemPromptSuffix: () => `\n[Build Law v5.1 Active: Zero TODO/stubs, zero eval/secrets, Polyglot FFP<=8 with # ffp: header, SLECO-SO++ set +e/trap, O(1)/O(N) velocity, System-0 CLI/SQL bypass for 5x-8.8x token efficiency.]\n`,
};
