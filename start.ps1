Write-Host "Stopping old servers..."

Get-Process node -ErrorAction SilentlyContinue | Stop-Process -Force
Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force

Start-Sleep -Seconds 2

Write-Host "Starting CyberApply Backend..."

Start-Process powershell `
    -ArgumentList "-NoExit", "-Command", "cd E:\wow\backend; .\venv\Scripts\Activate.ps1; uvicorn app.main:app --reload"


Start-Sleep -Seconds 3


Write-Host "Starting CyberApply Frontend..."

Start-Process powershell `
    -ArgumentList "-NoExit", "-Command", "cd E:\wow\frontend; npm run dev"


Write-Host "CyberApply started!"