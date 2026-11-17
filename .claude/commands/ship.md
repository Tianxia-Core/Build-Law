---
description: Group dirty changes by domain, run 14-Gate Build Law pre-flight check, commit explicit pathspecs, push branch, open PR, and queue auto-squash-merge ($0.00, 0 LLM tokens).
---

Execute the deterministic Build Law commit, push, PR & auto-merge dispatcher:

```bash
tx-ship --execute $ARGUMENTS
```

If `tx-ship` reports held findings or CI failures, inspect the specific flagged line(s) and remediate before re-running.
