# DLP review workflow

## 1. Confirm scope

- List workloads covered by the policy.
- Confirm owner groups for each high-risk location.
- Record policy mode before changing enforcement.

## 2. Review findings

- Sort events by severity and action.
- Check whether high-severity events were blocked, encrypted, or only audited.
- Mark events that need owner review or policy tuning.

## 3. Tune controls

- Keep low-confidence matches in monitor mode until reviewed.
- Move confirmed high-risk sharing paths toward block or encryption actions.
- Add user notification text that explains the business reason for the block.

## 4. Capture evidence

Record:

- policy name,
- rule name,
- event identifier,
- action taken,
- owner decision,
- review date,
- next action.

Do not record protected content values in the evidence note.

## 5. Report status

Produce a short report with totals, high-risk locations, unresolved findings, and policy changes proposed for the next review window.
