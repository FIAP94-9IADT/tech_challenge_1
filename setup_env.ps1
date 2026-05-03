$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$venvPath = Join-Path $projectRoot '.venv'
$venvPython = Join-Path $venvPath 'Scripts\python.exe'

function Get-TempDriveLetter {
    $candidates = 'T','U','V','W','X','Y','Z'
    foreach ($letter in $candidates) {
        if (-not (Test-Path -LiteralPath "$letter`:\")) {
            return $letter
        }
    }

    throw "Nao foi possivel encontrar uma letra de unidade livre para encurtar o caminho do projeto."
}

function Get-BasePython {
    $pythonCommand = Get-Command python -ErrorAction SilentlyContinue
    if ($pythonCommand) {
        return @($pythonCommand.Source)
    }

    $pyCommand = Get-Command py -ErrorAction SilentlyContinue
    if ($pyCommand) {
        return @($pyCommand.Source)
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

    Write-Host "Atualizando ferramentas de instalacao..." -ForegroundColor Cyan
    & $shortVenvPython -m pip install --upgrade pip setuptools wheel
    if ($LASTEXITCODE -ne 0) {
        throw "Falha ao atualizar pip/setuptools/wheel."
    }

    Write-Host "Instalando dependencias do projeto..." -ForegroundColor Cyan
    & $shortVenvPython -m pip install -r $shortRequirements
    if ($LASTEXITCODE -ne 0) {
        throw "Falha ao instalar as dependencias do projeto."
    }
}
finally {
    subst $shortDrive /d | Out-Null
}

Write-Host ""
Write-Host "Ambiente configurado com sucesso." -ForegroundColor Green
Write-Host "Agora basta abrir os notebooks no VS Code ou Jupyter e executar as celulas." -ForegroundColor Green