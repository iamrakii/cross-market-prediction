"""
Streamlit Web App with Custom Domain/URL Configuration
This file shows how to set up custom URLs for your application
"""

# ============================================================
# OPTION 1: LOCAL DEVELOPMENT (Current Setup)
# ============================================================
"""
Current Setup:
URL: http://localhost:8501

To change the port, run:
streamlit run streamlit_app.py --server.port 8502
"""

# ============================================================
# OPTION 2: NGROK (Temporary Public URL)
# ============================================================
"""
Installation:
pip install pyngrok

Usage in Python:
from pyngrok import ngrok

public_url = ngrok.connect(8501)
print(f"Your public URL: {public_url}")

Then run your Streamlit app normally in another terminal:
streamlit run streamlit_app.py

Your app will be accessible via the public URL provided by ngrok.
It's temporary but free and easy to set up.
"""

# ============================================================
# OPTION 3: STREAMLIT CLOUD (Free Hosting)
# ============================================================
"""
Steps to deploy on Streamlit Cloud:

1. Push your code to GitHub:
   - Create a GitHub repository
   - Push streamlit_app.py to the repo
   - Requirements: requirements.txt file

2. Go to: https://share.streamlit.io/

3. Click "Deploy an app"

4. Connect your GitHub account

5. Select your repository and streamlit_app.py file

6. You'll get a public URL like:
   https://your-username-app-name.streamlit.app/

Your app will be live and shareable!
"""

# ============================================================
# OPTION 4: HEROKU (Free/Paid Hosting)
# ============================================================
"""
Steps to deploy on Heroku:

1. Create Heroku account at https://www.heroku.com

2. Install Heroku CLI

3. Create these files in your project:
   
   a) Procfile (no extension):
   web: streamlit run streamlit_app.py
   
   b) requirements.txt:
   streamlit==1.28.0
   pandas==2.0.0
   plotly==5.17.0
   numpy==1.24.0
   torch==2.1.0
   networkx==3.2
   yfinance==0.2.32
   scikit-learn==1.3.2
   scipy==1.11.4
   statsmodels==0.14.0
   seaborn==0.12.2
   matplotlib==3.8.2

4. Set config file:
   heroku config:set PYTHONUNBUFFERED=1

5. Deploy:
   heroku create your-app-name
   git push heroku main

6. Your URL will be:
   https://your-app-name.herokuapp.com/
"""

# ============================================================
# OPTION 5: RENDER (Free Hosting Alternative)
# ============================================================
"""
Steps to deploy on Render:

1. Go to: https://render.com

2. Sign up with GitHub

3. Click "New +" and select "Web Service"

4. Connect your GitHub repository

5. Settings:
   - Name: your-app-name
   - Environment: Python 3
   - Build Command: pip install -r requirements.txt
   - Start Command: streamlit run streamlit_app.py

6. Your URL will be:
   https://your-app-name.onrender.com/
"""

# ============================================================
# OPTION 6: CUSTOM DOMAIN (Domain + Hosting)
# ============================================================
"""
For a completely custom domain like:
https://prediction.yourdomain.com

Steps:

1. Buy a domain (Godaddy, Namecheap, etc.)
   Cost: ~$10-15/year

2. Choose a hosting provider:
   - Streamlit Cloud (free)
   - Heroku (free/paid)
   - AWS (paid)
   - Google Cloud (paid)
   - Azure (paid)

3. Point domain to hosting provider's nameservers

4. Configure DNS records as per hosting provider

5. Your app becomes accessible via your custom URL
"""

# ============================================================
# RECOMMENDED SETUP FOR YOU
# ============================================================
"""
EASIEST: Streamlit Cloud (RECOMMENDED)
- Free hosting
- Automatic deployment from GitHub
- Live URL in minutes
- Perfect for portfolio/demonstration

STEPS:
1. Create GitHub account (if not done)
2. Create a public repository
3. Push your files:
   - streamlit_app.py
   - requirements.txt
   - Any CSV/data files
4. Go to share.streamlit.io
5. Deploy by selecting your repo
6. Share the public URL

Example Result:
https://cross-market-prediction.streamlit.app/
"""

print(__doc__)
