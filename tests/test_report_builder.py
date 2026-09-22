import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))

from build_compliance_report import build_report, load_events, load_inventory


class ReportBuilderTests(unittest.TestCase):
    def test_loads_sample_inputs(self):
        inventory = load_inventory(ROOT / 'data/synthetic-sensitive-inventory.csv')
        events = load_events(ROOT / 'data/sample-dlp-events.json')
        self.assertEqual(len(inventory), 5)
        self.assertEqual(len(events), 5)

    def test_report_contains_key_sections(self):
        inventory = load_inventory(ROOT / 'data/synthetic-sensitive-inventory.csv')
        events = load_events(ROOT / 'data/sample-dlp-events.json')
        report = build_report(inventory, events)
        self.assertIn('## Summary', report)
        self.assertIn('High-risk locations: 3', report)
        self.assertIn('Events needing follow-up: 2', report)
        self.assertIn('DLP-1001', report)
        self.assertIn('Finance Contracts; owner: Finance Operations', report)

    def test_empty_followup_queue_is_reported(self):
        inventory = [{
            'risk_rating': 'Low',
            'location_id': 'LOC-X',
            'repository': 'Public',
            'workload': 'SharePoint',
            'data_type': 'Public template',
        }]
        events = [{
            'event_id': 'DLP-X',
            'location_id': 'LOC-X',
            'severity': 'low',
            'action': 'audit_only',
            'status': 'no_action',
            'sensitive_info_type': 'Public template',
            'workload': 'SharePoint',
        }]
        report = build_report(inventory, events)
        self.assertIn('No unresolved synthetic events.', report)

    def test_followup_with_missing_inventory_keeps_safe_placeholder(self):
        inventory = []
        events = [{
            'event_id': 'DLP-MISSING',
            'location_id': 'LOC-MISSING',
            'severity': 'high',
            'action': 'block_external_share',
            'status': 'needs_owner_review',
            'sensitive_info_type': 'Client contract',
            'workload': 'SharePoint',
        }]

        report = build_report(inventory, events)

        self.assertIn('Unknown repository; owner: Unassigned owner', report)


if __name__ == '__main__':
    unittest.main()
