"""
Quick NGROK Setup - Get a Public URL in 2 Minutes
No server needed, just run this file!
"""

import subprocess
import sys
import time

def install_ngrok():
    """Install pyngrok if not already installed"""
    try:
        import pyngrok
        print("✓ pyngrok already installed")
        return True
    except ImportError:
        print("Installing pyngrok...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyngrok", "-q"])
        print("✓ pyngrok installed successfully")
        return True

def setup_ngrok():
    """Setup and display ngrok public URL"""
    from pyngrok import ngrok
    
    print("\n" + "="*70)
    print("STARTING NGROK TUNNEL".center(70))
    print("="*70 + "\n")
    
    try:
        # Create ngrok tunnel to port 8501
        public_url = ngrok.connect(8501)
        
        print("="*70)
        print("✓ SUCCESS! YOUR PUBLIC URL IS READY:".center(70))
        print("="*70)
        print(f"\n  {public_url}\n")
        print("="*70)
        print("\nIMPORTANT INSTRUCTIONS:".center(70))
        print("="*70)
        print("""
1. KEEP THIS WINDOW OPEN - Your URL only works while this runs

2. Open another terminal and start your Streamlit app:
   .venv\\Scripts\\python.exe -m streamlit run streamlit_app.py

3. Then open the URL above in your browser

4. Share the URL with anyone - they can access your app!

5. Press Ctrl+C in THIS window to stop and close the tunnel

⚠️  NOTE: This is a TEMPORARY URL (free tier lasts 2 hours)
           For permanent URL, use Streamlit Cloud (see guide)
""")
        
        # Keep the tunnel running
        print("\nWaiting for Streamlit app... (press Ctrl+C to stop)")
        ngrok_process = ngrok.get_ngrok_process()
        ngrok_process.proc.wait()
        
    except KeyboardInterrupt:
        print("\n\n" + "="*70)
        print("STOPPING NGROK TUNNEL".center(70))
        print("="*70)
        ngrok.kill()
        print("✓ Ngrok stopped. Your URL is no longer accessible.")

if __name__ == "__main__":
    print("\n" + "="*70)
    print("NGROK PUBLIC URL SETUP".center(70))
    print("="*70)
    print("\nThis tool creates a PUBLIC URL for your Streamlit app")
    print("Perfect for sharing and testing!\n")
    
    # Install ngrok
    if install_ngrok():
        # Setup tunnel
        setup_ngrok()
