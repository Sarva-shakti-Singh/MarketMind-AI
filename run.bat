@echo off
if not exist .venv (
  echo Creating virtual environment...
  python -m venv .venv
)
call .venv\Scripts\activate
echo Installing dependencies...
pip install -q -r requirements.txt
echo Starting AI Marketing Automation Dashboard...
streamlit run app.py
