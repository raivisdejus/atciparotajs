#!/bin/bash
set -e
pip install pyinstaller
pyinstaller --onefile --name atciparotajs atciparotajs/__main__.py
echo "Binary built at dist/atciparotajs"
