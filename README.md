# Purview DLP Compliance Starter

A small review kit for Microsoft Purview Data Loss Prevention work. It uses synthetic records and policy examples to show how a security engineer can turn compliance requirements into reviewable controls, runbooks, and evidence.

This repository is safe for public review. It contains no tenant exports, client records, secrets, or production identifiers.

## What this demonstrates for the VAT IT role

- Microsoft Purview DLP policy structure and control mapping.
- Handling of regulated data types such as financial records, passport numbers, tax identifiers, and client contract files.
- Evidence-first compliance reporting from structured sample data.
- PowerShell review workflow for policy readiness checks.
- GitHub Actions validation for repeatable quality checks.

## Repository contents

- `policies/purview-dlp-policy-starter.json`: sample DLP policy package with safe placeholders.
- `data/synthetic-sensitive-inventory.csv`: synthetic data locations and risk ratings.
- `data/sample-dlp-events.json`: synthetic DLP events used for report generation.
- `control-mapping/dlp-control-map.md`: mapping from policy intent to operational checks.
- `runbooks/dlp-review-workflow.md`: review workflow for triage, tuning, and evidence capture.
- `scripts/Test-DlpPolicyReadiness.ps1`: PowerShell readiness checks for a policy JSON file.
- `tools/build_compliance_report.py`: builds a markdown report from the synthetic data.
- `tests/`: validation and unit tests.

## Quick start

```bash
python3 tools/build_compliance_report.py \
  --inventory data/synthetic-sensitive-inventory.csv \
  --events data/sample-dlp-events.json \
  --output sample-output/dlp-compliance-report.md

python3 tests/validate_project.py
python3 -m unittest discover -s tests
```

Optional PowerShell check:

```powershell
pwsh -File scripts/Test-DlpPolicyReadiness.ps1 -PolicyPath policies/purview-dlp-policy-starter.json
```

## Sample report

A generated report is included at `sample-output/dlp-compliance-report.md`. It summarizes:

- monitored data locations,
- synthetic event totals,
- high-risk repositories,
- owner context for events needing follow-up,
- policy readiness checks,
- recommended next actions.

## Safety model

- All data is synthetic.
- Policy identifiers use example names only.
- The scripts do not connect to Microsoft 365, Microsoft Graph, Exchange Online, SharePoint, or a tenant.
- The PowerShell script reads local JSON and returns readiness findings.
- The Python tool reads local files and writes a local report.

## Skills covered

- Microsoft Purview DLP concepts.
- Data classification and control mapping.
- Security operations reporting.
- Compliance evidence handling.
- PowerShell and Python automation.
- CI-backed validation.
