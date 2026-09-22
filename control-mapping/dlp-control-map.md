# DLP control map

## Control objectives

- Identify regulated or contract-sensitive data before external sharing.
- Reduce accidental disclosure through blocking, notification, and business justification.
- Keep enough evidence for compliance review without exposing the content itself.
- Separate monitor-only rules from rules that block or encrypt content.

## Mapping

| Control area | Sample policy rule | Evidence produced | Review question |
| --- | --- | --- | --- |
| Client contracts | Block external sharing of client contracts | Incident record and owner notification | Was external sharing stopped or approved by an owner? |
| Identity documents | Protect passport and travel identity data | User notification and block event | Was the user coached and was the share blocked? |
| Tax records | Review tax identifier movement | Encryption action and compliance notification | Did the message need external release? |
| Commercial proposals | Monitor commercial proposal sharing | Audit event | Should this rule stay monitor-only or move to block mode? |

## Evidence handling

Do not copy protected content into tickets or reports. Record metadata, rule name, owner, action, decision, and the minimum context needed for review.
