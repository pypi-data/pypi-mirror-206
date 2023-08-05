@echo off
hatch build
hatch publish
pip uninstall bow-cli
pip install bow-cli==1.0.0.3
