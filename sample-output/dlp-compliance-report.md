# DLP compliance review report

Generated from synthetic sample data. No tenant or client data is included.

## Summary

- Data locations reviewed: 5
- DLP events reviewed: 5
- High-risk locations: 3
- Events needing follow-up: 2

## Risk rating by location

- High: 3
- Low: 1
- Medium: 1

## Event severity

- high: 3
- low: 1
- medium: 1

## Actions observed

- audit_only: 2
- block_external_share: 1
- encrypt_and_notify: 1
- notify_user_and_block: 1

## High-risk locations

- LOC-001: Finance Contracts (SharePoint, Client contract)
- LOC-002: Executive Working Files (OneDrive, Passport number)
- LOC-003: Tax Correspondence (Exchange, Tax identifier)

## Follow-up queue

- DLP-1001: needs_owner_review for Client contract in SharePoint (Finance Contracts; owner: Finance Operations)
- DLP-1003: needs_policy_tuning for Tax identifier in Exchange (Tax Correspondence; owner: Tax Advisory)

## Recommended next actions

- Confirm owners for each high-risk location.
- Review monitor-only rules before moving them to blocking mode.
- Keep evidence metadata-only and avoid copying protected content into tickets.
