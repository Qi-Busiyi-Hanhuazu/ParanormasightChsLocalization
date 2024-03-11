$Helper = "tools/bin/Release/net8.0/ParanormasightChsLocalizationHelper.exe"

# Build and run the CLI
if (-not(Test-Path -Path $Helper -PathType "Leaf")) {
  Push-Location "tools"
  dotnet restore
  dotnet build -c "Release"
  Pop-Location
}

& $Helper

Copy-Item "README.md" "out/patch/Windows/README.md"
Copy-Item "LICENSE" "out/patch/Windows/LICENSE"
Compress-Archive -Path out/patch/Windows/* -DestinationPath "out/patch-windows-text.zip" -Force

Copy-Item "README.md" "out/patch/Switch/README.md"
Copy-Item "LICENSE" "out/patch/Switch/LICENSE"
Compress-Archive -Path "out/patch/Switch/*" -DestinationPath "out/patch-switch-text.zip" -Force