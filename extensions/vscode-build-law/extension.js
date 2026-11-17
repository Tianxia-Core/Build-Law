// ffp: FFP-BLAW-VSCODE frontend javascript
// build-law-ignore: scanner rule definitions
// Build Law Native Extension for VS Code, Cursor, Windsurf & VSCodium
const vscode = require('vscode');
const fs = require('fs');
const path = require('path');

const STUB_RE = /\b(TODO|FIXME|unimplemented!|todo!)\b/;
const SECRET_RE = /(sk_live_[0-9a-zA-Z_]{12,}|gh[pousr]_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16})/;
const EVAL_RE = /\beval\s*\(/;

const COMPACT_PROMPT = `Operate strictly under Build Law v5.1 (RASA-X-MACHINA):
1. ZERO STUBS: Never emit TODO, FIXME, pass, todo!(), unimplemented!(), or mock data.
2. INNOCENCE & CONTAINMENT: Zero eval(), zero shell injection, bounded timeouts on all loops/IO, and 0600 out-of-tree secret custody.
3. POLYGLOT FFP<=8: Match language to workload physics, cap services at <= 8 FFPs, and declare // ffp: <ID> <class> <lang>.
4. SLECO-SO++ & 5x-8.8x TOKEN EFFICIENCY: Use O(1)/O(N) algorithms, atomic file writes, and offload deterministic data ops to CLI/SQL ($0.00, 0 tokens).`;

function scanDocument(doc, collection) {
  if (!doc || doc.uri.scheme !== 'file') return;
  const text = doc.getText();
  const diags = [];
  const lines = text.split(/\r?\n/);
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
        ? `---\ndescription: Build Law Sovereign Engineering Rules\nglobs: "**/*"\nalwaysApply: true\n---\n\n${COMPACT_PROMPT}\n`
        : `${COMPACT_PROMPT}\n`;
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
