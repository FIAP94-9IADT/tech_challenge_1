$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$venvPath = Join-Path $projectRoot '.venv'
$venvPython = Join-Path $venvPath 'Scripts\python.exe'

function Get-BasePython {
    $pyCommand = Get-Command py -ErrorAction SilentlyContinue
    if ($pyCommand) {
        return @($pyCommand.Source, '-3.11')
    }

    $pythonCommand = Get-Command python -ErrorAction SilentlyContinue
    if ($pythonCommand) {
        return @($pythonCommand.Source)
    }

    throw "Python nao encontrado. Instale o Python 3.11+ e tente novamente."
}

if (-not (Test-Path -LiteralPath $venvPython)) {
    $basePython = Get-BasePython
    Write-Host "Criando ambiente virtual em '.venv'..." -ForegroundColor Cyan
    if ($basePython.Length -gt 1) {
        & $basePython[0] $basePython[1] -m venv $venvPath
    }
    else {
        & $basePython[0] -m venv $venvPath
    }
    if ($LASTEXITCODE -ne 0) {
        throw "Falha ao criar o ambiente virtual."
    }
}

Write-Host "Atualizando ferramentas de instalacao..." -ForegroundColor Cyan
& $venvPython -m pip install --upgrade pip setuptools wheel
if ($LASTEXITCODE -ne 0) {
    throw "Falha ao atualizar pip/setuptools/wheel."
}

Write-Host "Instalando dependencias do projeto..." -ForegroundColor Cyan
& $venvPython -m pip install -r (Join-Path $projectRoot 'requirements.txt')
if ($LASTEXITCODE -ne 0) {
    throw "Falha ao instalar as dependencias do projeto."
}

Write-Host ""
Write-Host "Ambiente configurado com sucesso." -ForegroundColor Green
Write-Host "Para abrir o notebook:" -ForegroundColor Green
Write-Host "powershell -ExecutionPolicy Bypass -File .\start_notebook.ps1"
Write-Host ""
Write-Host "Para validar o notebook:" -ForegroundColor Green
Write-Host "powershell -ExecutionPolicy Bypass -File .\validate_notebook.ps1"
