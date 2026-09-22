#!/usr/bin/env python3
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

required_paths = [
    'README.md',
    'LICENSE',
    'policies/purview-dlp-policy-starter.json',
    'data/synthetic-sensitive-inventory.csv',
    'data/sample-dlp-events.json',
    'control-mapping/dlp-control-map.md',
    'runbooks/dlp-review-workflow.md',
    'scripts/Test-DlpPolicyReadiness.ps1',
    'tools/build_compliance_report.py',
    '.github/workflows/validate.yml',
]

for rel in required_paths:
    path = ROOT / rel
    if not path.exists():
        raise SystemExit(f'Missing required file: {rel}')

policy = json.loads((ROOT / 'policies/purview-dlp-policy-starter.json').read_text(encoding='utf-8'))
if policy.get('mode') not in {'TestWithNotifications', 'AuditOnly', 'Enforce'}:
    raise SystemExit('Unexpected policy mode')
if len(policy.get('rules', [])) < 4:
    raise SystemExit('Expected at least four policy rules')
for rule in policy['rules']:
    for key in ['name', 'sensitiveInfoTypes', 'locations', 'actions', 'severity']:
        if not rule.get(key):
            raise SystemExit(f'Rule missing {key}: {rule}')

with open(ROOT / 'data/synthetic-sensitive-inventory.csv', newline='', encoding='utf-8') as handle:
    rows = list(csv.DictReader(handle))
if len(rows) < 5:
    raise SystemExit('Expected at least five inventory rows')
if not any(row['risk_rating'] == 'High' for row in rows):
    raise SystemExit('Expected at least one high-risk inventory row')

events = json.loads((ROOT / 'data/sample-dlp-events.json').read_text(encoding='utf-8')).get('events', [])
if len(events) < 5:
    raise SystemExit('Expected at least five sample events')
if not any(event['status'] == 'needs_owner_review' for event in events):
    raise SystemExit('Expected an owner review sample event')

for path in ROOT.rglob('*'):
    if path.is_file() and path.name != '.git' and '.git' not in path.parts:
        text = path.read_text(encoding='utf-8', errors='ignore')
        if chr(8212) in text:
            raise SystemExit(f'Forbidden dash character found in {path.relative_to(ROOT)}')
        forbidden = ['A' + 'I Powered', 'Revolu' + 'tionary', 'Cutting ' + 'Edge', 'Sea' + 'mless']
        for word in forbidden:
            if word in text:
                raise SystemExit(f'Forbidden phrase {word!r} found in {path.relative_to(ROOT)}')

print(f'Validation passed: {len(policy["rules"])} rules, {len(rows)} inventory rows, {len(events)} events.')
