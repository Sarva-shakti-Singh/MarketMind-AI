#!/usr/bin/env bash
set -e
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv .venv
fi
source .venv/bin/activate
echo "Installing dependencies..."
pip install -q -r requirements.txt
echo "Starting AI Marketing Automation Dashboard..."
streamlit run app.py
