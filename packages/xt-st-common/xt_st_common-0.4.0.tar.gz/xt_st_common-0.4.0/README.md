# XT-STREAMLIT - 0.4.0

This repo contains all of the common Streamlit code used by the Exploration Toolkit and CMR's Discovery Program.

## `xt-st-common` - Common Framework for XT's Streamlit apps

### Getting Started

This project recommends using [nox](https://nox.thea.codes/) as a tool for managing test environments and running scripts

In your base python environment
``` bash
pip install pipx # Pipx is a tool for installing python tools globally
pipx install nox # Installs nox as a global tool
pipx inject nox nox-poetry # Injects nox-poetry into the pipx venv that nox uses
```
