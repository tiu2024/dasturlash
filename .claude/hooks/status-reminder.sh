#!/usr/bin/env bash
# PreToolUse hook (Bash): before Claude runs `git commit`, check status.md.
# If status.md has no changes, ask the teacher to approve the commit and
# remind Claude to update status.md. Never blocks on its own.

input=$(cat)
case "$input" in
  *"git commit"*) ;;
  *) exit 0 ;;
esac

cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}" || exit 0

if git diff --quiet -- status.md && git diff --cached --quiet -- status.md; then
  cat <<'JSON'
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"status.md is not updated in this commit. Approve if the status does not change; reject to have Claude update status.md first.","additionalContext":"Reminder: status.md has no changes. If this work changes the project state, update status.md and include it in the commit."}}
JSON
fi
exit 0
