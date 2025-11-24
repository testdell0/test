# venv Installation Manual (Windows PowerShell)

This document explains how to create a Python virtual environment (venv) using **uv**,  
and how to set it up for use with tools such as **Jupyter**.  
Target environment: **Windows PowerShell**

---

## 0. Proxy Configuration

In a corporate network environment, set up the following proxy configuration **before** installing.  
(Example: run these in PowerShell)

```powershell
$env:HTTP_PROXY  = "http://10.249.24.17:3128"
$env:HTTPS_PROXY = "http://10.249.24.17:3128"
$env:NO_PROXY    = "localhost,127.0.0.1,::1,.honda.com"
$env:http_proxy  = $env:HTTP_PROXY
$env:https_proxy = $env:HTTPS_PROXY
$env:no_proxy    = $env:NO_PROXY

# Optional: skip TLS verification errors if needed
$env:UV_NATIVE_TLS = "1"
```
---

## 1. Create a Virtual Environment (venv)

Create a virtual environment using **Python 3.13**.

```powershell
uv venv --python 3.13
```

A folder named `.venv` will be created in your project directory.  
If you want to specify the folder name manually, run:

```powershell
uv venv --python 3.13 .venv
```

---

## 2. Activate the Virtual Environment

Activate the `.venv` environment you just created.

```powershell
. .\.venv\Scripts\Activate.ps1
```

When activation is successful, your PowerShell prompt will show  
`(.venv)` at the beginning — this indicates the virtual environment is active.

---

## 3. Install ipykernel

To use this environment in Jupyter Notebook or JupyterLab, install `ipykernel`.

```powershell
uv add ipykernel
```

The `uv add` command automatically creates a `pyproject.toml`  
and manages dependencies at high speed — it can be used as a replacement for `pip install`.

---

## 4. Restart PowerShell / VSCode

**Important!**  
After activating the environment, close PowerShell (or restart VSCode entirely).  
This ensures environment variables and paths are applied correctly.

After restarting, activate the virtual environment again:

```powershell
. .\.venv\Scripts\Activate.ps1
```

---

## 5. (Optional) Register Jupyter Kernel

Make the virtual environment available as a kernel in Jupyter Lab / Notebook.

```powershell
uv run python -m ipykernel install --user --name myproj-3.13 --display-name "Python 3.13 (myproj)"
```

Alternatively, you can select the interpreter directly from **VSCode’s UI**.

---

## Summary

| Step | Command Example | Description |
|------|------------------|-------------|
| 0 | Proxy setup (optional) | Configure proxy if on corporate network |
| 1 | `uv venv --python 3.13` | Create a virtual environment |
| 2 | `. .\.venv\Scripts\Activate.ps1` | Activate the environment |
| 3 | `uv add ipykernel` | Install Jupyter kernel |
| 4 | Restart VSCode / PowerShell | Apply environment variables |
| 5 | `uv run python -m ipykernel install ...` | Register kernel for Jupyter |

---

## References

- [uv Documentation](https://docs.astral.sh/uv/)
- [Python Downloads](https://www.python.org/downloads/)
- [JupyterLab](https://jupyter.org/)