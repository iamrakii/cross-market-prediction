@echo off
REM ============================================================
REM STREAMLIT CLOUD DEPLOYMENT HELPER
REM ============================================================
REM This script helps you deploy to Streamlit Cloud for a free public URL
REM ============================================================

echo.
echo ============================================================
echo   STREAMLIT CLOUD DEPLOYMENT GUIDE
echo ============================================================
echo.

echo To get a free custom URL for your app:
echo.
echo Step 1: Create GitHub Account
echo   - Go to: https://github.com
echo   - Sign up with email
echo.

echo Step 2: Create a New Repository
echo   - Name it: cross-market-prediction
echo   - Make it PUBLIC
echo   - Add README and .gitignore
echo.

echo Step 3: Upload Your Files
echo   Option A - Using GitHub Web:
echo     - Go to your repository
echo     - Click "Add file" > "Upload files"
echo     - Upload: streamlit_app.py, requirements.txt, project.py
echo.
echo   Option B - Using Git Command (Advanced):
echo     - git init
echo     - git add .
echo     - git commit -m "Initial commit"
echo     - git remote add origin https://github.com/YOUR_USERNAME/cross-market-prediction.git
echo     - git branch -M main
echo     - git push -u origin main
echo.

echo Step 4: Deploy on Streamlit Cloud
echo   - Go to: https://share.streamlit.io/
echo   - Click "Deploy an app"
echo   - Connect GitHub account
echo   - Select your repository
echo   - Select branch: main
echo   - Select file: streamlit_app.py
echo   - Click "Deploy!"
echo.

echo Step 5: Share Your Public URL
echo   - Streamlit will give you a URL like:
echo   - https://your-username-cross-market-prediction.streamlit.app/
echo   - Share this URL with anyone!
echo.

echo ============================================================
echo   ALTERNATIVE: Use NGROK for Quick Temporary URL
echo ============================================================
echo.

echo To use Ngrok (temporary public URL, no setup needed):
echo.
echo 1. Install pyngrok:
echo    pip install pyngrok
echo.

echo 2. Run this command in another terminal:
echo    streamlit run streamlit_app.py
echo.

echo 3. Run this Python script to get public URL:
echo.

REM Create a Python script to help with ngrok
(
echo import subprocess
echo import time
echo from pyngrok import ngrok
echo.
echo # Start ngrok tunnel
echo public_url = ngrok.connect(8501^)
echo print(f"\n{'='*60^}\n"^)
echo print(f"Your PUBLIC URL: {public_url^}"^)
echo print(f"\n{'='*60^}\n"^)
echo print("Keep this terminal open while using your app."^)
echo print("Share this URL with anyone to let them access your app!"^)
echo print("\nPress Ctrl+C to stop."^)
echo.
echo try:
echo     ngrok_process = ngrok.get_ngrok_process(^)
echo     ngrok_process.proc.wait(^)
echo except KeyboardInterrupt:
echo     print("\nStopping ngrok..."^)
echo     ngrok.kill(^)
) > ngrok_setup.py

echo 4. Run: python ngrok_setup.py
echo.

echo.
echo ============================================================
echo   QUICK COMPARISON
echo ============================================================
echo.
echo Option              | Free | Setup Time | URL Example
echo ==================  | ==== | ========== | =======================
echo Localhost (Current) | Yes  | 0 min      | localhost:8501
echo Ngrok              | Yes  | 2 min      | https://abc123.ngrok.io
echo Streamlit Cloud    | Yes  | 15 min     | myapp.streamlit.app
echo Heroku             | ~    | 30 min     | myapp.herokuapp.com
echo Render             | Yes  | 30 min     | myapp.onrender.com
echo Custom Domain      | No   | 1-2 hrs    | myapp.com
echo.

echo ============================================================
pause
