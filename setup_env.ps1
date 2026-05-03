$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$venvPath = Join-Path $projectRoot '.venv'
$venvPython = Join-Path $venvPath 'Scripts\python.exe'
$requirementsPath = Join-Path $projectRoot 'requirements.txt'

function Get-TempDriveLetter {
    $candidates = 'T','U','V','W','X','Y','Z'
    foreach ($letter in $candidates) {
        if (-not (Test-Path -LiteralPath "$letter`:\")) {
            return $letter
        }
    }

    throw "Nao foi possivel encontrar uma letra de unidade livre para encurtar o caminho do projeto."
}

function Get-CompatiblePython {
    $pyCommand = Get-Command py -ErrorAction SilentlyContinue
    if ($pyCommand) {
        & $pyCommand.Source -3.12 --version *> $null
        if ($LASTEXITCODE -eq 0) {
            return @($pyCommand.Source, '-3.12')
        }

        & $pyCommand.Source -3.11 --version *> $null
        if ($LASTEXITCODE -eq 0) {
            return @($pyCommand.Source, '-3.11')
        }
    }

    $pythonCommand = Get-Command python -ErrorAction SilentlyContinue
    if ($pythonCommand) {
        $versionText = & $pythonCommand.Source --version 2>&1
        if ($versionText -match 'Python\s+(\d+)\.(\d+)') {
            $major = [int]$matches[1]
            $minor = [int]$matches[2]
            if ($major -eq 3 -and ($minor -eq 11 -or $minor -eq 12)) {
                return @($pythonCommand.Source)
            }
        }
    }

    throw "Python compativel nao encontrado. Este projeto requer Python 3.11 ou 3.12 por causa das dependencias do notebook com CNN."
}

function Install-ProjectDependencies {
    param(
        [string]$PythonExe,
        [string]$RequirementsFile
    )

    Write-Host "Atualizando ferramentas de instalacao..." -ForegroundColor Cyan
    & $PythonExe -m pip install --upgrade pip setuptools wheel
    if ($LASTEXITCODE -ne 0) {
        throw "Falha ao atualizar pip/setuptools/wheel."
    }

    Write-Host "Instalando dependencias do projeto..." -ForegroundColor Cyan
    & $PythonExe -m pip install -r $RequirementsFile
    if ($LASTEXITCODE -ne 0) {
        throw "Falha ao instalar as dependencias do projeto."
    }
}

if (-not (Test-Path -LiteralPath $venvPython)) {
    $basePython = Get-CompatiblePython
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

try {
    Install-ProjectDependencies -PythonExe $venvPython -RequirementsFile $requirementsPath
}
catch {
    Write-Host "Instalacao direta falhou. Tentando novamente com caminho encurtado..." -ForegroundColor Yellow

    $driveLetter = Get-TempDriveLetter
    $shortProjectRoot = "$driveLetter`:\"
    $shortDrive = "$driveLetter`:"
    $shortVenvPython = "${shortProjectRoot}.venv\Scripts\python.exe"
    $shortRequirements = "${shortProjectRoot}requirements.txt"

    try {
        subst $shortDrive $projectRoot
        if ($LASTEXITCODE -ne 0) {
            throw "Falha ao criar a unidade temporaria para encurtar o caminho do projeto."
        }

        Install-ProjectDependencies -PythonExe $shortVenvPython -RequirementsFile $shortRequirements
    }
    finally {
        subst $shortDrive /d | Out-Null
    }
}

Write-Host ""
Write-Host "Ambiente configurado com sucesso." -ForegroundColor Green
Write-Host "Agora basta abrir os notebooks no VS Code ou Jupyter e executar as celulas." -ForegroundColor Green
