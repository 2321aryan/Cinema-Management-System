import sys
import subprocess
import os

def check_import(module_name):
    try:
        __import__(module_name)
        print(f"[OK] {module_name} is installed")
        return True
    except ImportError:
        print(f"[ERROR] {module_name} is NOT installed")
        return False

def main():
    print("Checking Setup...")
    
    # Check dependencies
    deps = ["fastapi", "uvicorn", "supabase", "qrcode", "reportlab"]
    all_good = True
    for dep in deps:
        if not check_import(dep):
            all_good = False
            
    if all_good:
        print("\nAll dependencies seem correct!")
        print("You can start the server by running 'start_backend.bat'")
    else:
        print("\nSome dependencies are missing.")
        print("Please wait for the installation to finish or run 'pip install -r backend/requirements.txt' manually.")

if __name__ == "__main__":
    main()
