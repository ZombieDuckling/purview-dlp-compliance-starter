#!/usr/bin/env python3
import argparse
import csv
import json
from collections import Counter
from pathlib import Path


def load_inventory(path):
    with open(path, newline='', encoding='utf-8') as handle:
        return list(csv.DictReader(handle))


def load_events(path):
    with open(path, encoding='utf-8') as handle:
        data = json.load(handle)
    return data.get('events', [])


def build_report(inventory, events):
    risk_counts = Counter(row['risk_rating'] for row in inventory)
    event_severity = Counter(event['severity'] for event in events)
    action_counts = Counter(event['action'] for event in events)
    high_locations = [row for row in inventory if row['risk_rating'].lower() == 'high']
    inventory_by_location = {row['location_id']: row for row in inventory}
    unresolved = [event for event in events if event['status'] in {'needs_owner_review', 'needs_policy_tuning'}]

    lines = []
    lines.append('# DLP compliance review report')
    lines.append('')
    lines.append('Generated from synthetic sample data. No tenant or client data is included.')
    lines.append('')
    lines.append('## Summary')
    lines.append('')
    lines.append(f'- Data locations reviewed: {len(inventory)}')
    lines.append(f'- DLP events reviewed: {len(events)}')
    lines.append(f'- High-risk locations: {len(high_locations)}')
    lines.append(f'- Events needing follow-up: {len(unresolved)}')
    lines.append('')
    lines.append('## Risk rating by location')
    lines.append('')
    for rating, count in sorted(risk_counts.items()):
        lines.append(f'- {rating}: {count}')
    lines.append('')
    lines.append('## Event severity')
    lines.append('')
    for severity, count in sorted(event_severity.items()):
        lines.append(f'- {severity}: {count}')
    lines.append('')
    lines.append('## Actions observed')
    lines.append('')
    for action, count in sorted(action_counts.items()):
        lines.append(f'- {action}: {count}')
    lines.append('')
    lines.append('## High-risk locations')
    lines.append('')
    for row in high_locations:
        lines.append(f"- {row['location_id']}: {row['repository']} ({row['workload']}, {row['data_type']})")
    lines.append('')
    lines.append('## Follow-up queue')
    lines.append('')
    if unresolved:
        for event in unresolved:
            location = inventory_by_location.get(event['location_id'], {})
            owner = location.get('owner_group', 'Unassigned owner')
            repository = location.get('repository', 'Unknown repository')
            lines.append(
                f"- {event['event_id']}: {event['status']} for {event['sensitive_info_type']} "
                f"in {event['workload']} ({repository}; owner: {owner})"
            )
    else:
        lines.append('- No unresolved synthetic events.')
    lines.append('')
    lines.append('## Recommended next actions')
    lines.append('')
    lines.append('- Confirm owners for each high-risk location.')
    lines.append('- Review monitor-only rules before moving them to blocking mode.')
    lines.append('- Keep evidence metadata-only and avoid copying protected content into tickets.')
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description='Build a synthetic DLP compliance report.')
    parser.add_argument('--inventory', required=True)
    parser.add_argument('--events', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    inventory = load_inventory(args.inventory)
    events = load_events(args.events)
    report = build_report(inventory, events)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding='utf-8')
    print(f'Wrote {output_path} with {len(inventory)} locations and {len(events)} events.')


if __name__ == '__main__':
    main()
