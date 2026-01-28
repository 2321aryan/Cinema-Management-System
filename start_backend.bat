@echo off
cd backend
echo Installing dependencies...
pip install -r requirements.txt
echo Starting server...
uvicorn main:app --reload --host 0.0.0.0 --port 8000
pause
