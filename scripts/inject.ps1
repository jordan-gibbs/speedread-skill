# Bundle a markdown report into a self-contained SpeedRead reader page.
param(
    [Parameter(Mandatory = $true)][string]$Markdown,
    [string]$Template = (Join-Path (Split-Path $PSScriptRoot -Parent) 'reader.html'),
    [string]$Output,
    [switch]$Open
)

if (-not $Output) {
    $Output = ($Markdown -replace '\.md$', '') + '.speedread.html'
}

# Escape closing script tags so a code sample can't truncate the page;
# the reader reverses this on load.
$md = (Get-Content $Markdown -Raw) -replace '</script', '<\/script'
$tpl = Get-Content $Template -Raw

if (([regex]::Matches($tpl, [regex]::Escape('%%SPEEDREAD_CONTENT%%'))).Count -ne 1) {
    Write-Error "template $Template is missing the %%SPEEDREAD_CONTENT%% sentinel"
    exit 1
}

$tpl.Replace('%%SPEEDREAD_CONTENT%%', $md) | Set-Content $Output -Encoding utf8
Write-Output $Output

if ($Open) { Start-Process $Output }
