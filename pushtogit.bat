@echo off
title GitHub Auto-Sync
color 0A
echo [STATUS] Scanning for changes...

:: 1. Add all new files and changes
git add .

:: 2. Save with a timestamp (No manual naming needed)
git commit -m "Auto-update: %date% %time%"

:: 3. Upload to GitHub
git push

echo.
echo [SUCCESS] Files uploaded. Cloudflare is now deploying your site.
timeout /t 5