$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$venvPython = Join-Path $projectRoot '.venv\Scripts\python.exe'

if (-not (Test-Path -LiteralPath $venvPython)) {
    Write-Host "Ambiente virtual nao encontrado em '.venv'." -ForegroundColor Yellow
    Write-Host "Execute primeiro: powershell -ExecutionPolicy Bypass -File .\setup_env.ps1" -ForegroundColor Yellow
    exit 1
}

$env:JUPYTER_CONFIG_DIR = Join-Path $projectRoot '.jupyter_config'
$env:JUPYTER_DATA_DIR = Join-Path $projectRoot '.jupyter_local'
$env:JUPYTER_PATH = Join-Path $env:JUPYTER_DATA_DIR 'share\jupyter'
$env:IPYTHONDIR = Join-Path $projectRoot '.ipython_local'
$env:MPLCONFIGDIR = Join-Path $projectRoot '.mplconfig'

New-Item -ItemType Directory -Force -Path `
    $env:JUPYTER_CONFIG_DIR, `
    $env:JUPYTER_DATA_DIR, `
    $env:IPYTHONDIR, `
    $env:MPLCONFIGDIR | Out-Null

& $venvPython -m notebook tech_challenge_breast_cancer.ipynb
