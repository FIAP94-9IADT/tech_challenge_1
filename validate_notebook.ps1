$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$venvPython = Join-Path $projectRoot '.venv\Scripts\python.exe'

if (-not (Test-Path -LiteralPath $venvPython)) {
    Write-Host "Ambiente virtual nao encontrado em '.venv'." -ForegroundColor Yellow
    Write-Host "Execute primeiro: powershell -ExecutionPolicy Bypass -File .\setup_env.ps1" -ForegroundColor Yellow
    exit 1
}

$env:MPLBACKEND = 'Agg'
$env:MPLCONFIGDIR = Join-Path $projectRoot '.mplconfig'
$env:LOKY_MAX_CPU_COUNT = '1'

New-Item -ItemType Directory -Force -Path $env:MPLCONFIGDIR | Out-Null

@'
import os
import nbformat
from IPython.display import display

notebook_path = 'tech_challenge_breast_cancer.ipynb'
nb = nbformat.read(notebook_path, as_version=4)
ctx = {'display': display, '__name__': '__main__'}

executed = 0
for idx, cell in enumerate(nb.cells, start=1):
    if cell.cell_type != 'code':
        continue
    source = cell.source.strip()
    if not source:
        continue
    print(f'Running cell {idx}...')
    exec(compile(source, f'<cell {idx}>', 'exec'), ctx)
    executed += 1

print(f'Executed {executed} code cells successfully.')
'@ | & $venvPython -
