@echo off
cd /d "%~dp0"
if not exist "_site\index.html" (
  echo The site has not been built yet. See PERSONAL_SITE_GUIDE.md.
  pause
  exit /b 1
)
echo Open http://127.0.0.1:4000/ in your browser.
echo Keep this window open while reviewing. Press Ctrl+C to stop.
python scripts\preview-server.py
pause
