param(
    [Parameter(Mandatory = $true)]
    [string]$PolicyPath
)

if (-not (Test-Path -LiteralPath $PolicyPath)) {
    Write-Error "Policy file not found: $PolicyPath"
    exit 1
}

$policy = Get-Content -LiteralPath $PolicyPath -Raw | ConvertFrom-Json
$findings = @()

if (-not $policy.policyName) { $findings += "Missing policyName" }
if (-not $policy.mode) { $findings += "Missing mode" }
if (-not $policy.workloads -or $policy.workloads.Count -eq 0) { $findings += "No workloads configured" }
if (-not $policy.rules -or $policy.rules.Count -eq 0) { $findings += "No rules configured" }

foreach ($rule in $policy.rules) {
    if (-not $rule.name) { $findings += "A rule is missing a name" }
    if (-not $rule.sensitiveInfoTypes -or $rule.sensitiveInfoTypes.Count -eq 0) { $findings += "Rule '$($rule.name)' has no sensitive information types" }
    if (-not $rule.actions -or $rule.actions.Count -eq 0) { $findings += "Rule '$($rule.name)' has no actions" }
    if (-not $rule.severity) { $findings += "Rule '$($rule.name)' has no severity" }
}

if ($findings.Count -gt 0) {
    Write-Host "DLP policy readiness failed"
    $findings | ForEach-Object { Write-Host "- $_" }
    exit 1
}

Write-Host "DLP policy readiness passed: $($policy.rules.Count) rules across $($policy.workloads.Count) workloads."
