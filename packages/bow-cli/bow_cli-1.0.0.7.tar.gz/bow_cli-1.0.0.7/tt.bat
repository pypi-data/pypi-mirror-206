@echo off
hatch build
hatch publish
pip uninstall bow-cli
