// ffp: FFP-BLAW-TEST edge-agent go
package main

import (
	"os"
	"path/filepath"
	"testing"
)

func TestAuditPathAndCleanroomDetection(t *testing.T) {
	tmp := t.TempDir()
	good := "// ffp: FFP-DEMO edge-agent go\npackage demo\nfunc Ready() int { return 42 }\n"
	if err := os.WriteFile(filepath.Join(tmp, "demo.go"), []byte(good), 0o600); err != nil {
		t.Fatal(err)
	}
	rep := auditPath(tmp, true)
	if !rep.OK || rep.FilesScanned != 1 || rep.FFPHeadersFound != 1 || rep.LLMTokensSpent != 0 {
		t.Fatalf("unexpected clean audit report: %+v", rep)
	}
}
