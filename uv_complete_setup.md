================================================================================
COMPLETE UV PACKAGE MANAGER SETUP GUIDE
For Windows 11 Corporate Environment (No Admin Access Required)
================================================================================

TABLE OF CONTENTS
-----------------
1. Prerequisites Check
2. Corporate Proxy Configuration
3. Install UV Package Manager
4. Configure PATH Environment Variable
5. Verify UV Installation
6. Create Virtual Environment
7. Install Packages and Use UV
8. Troubleshooting Guide

================================================================================

STEP 1: PREREQUISITES CHECK
================================================================================

Before starting, ensure you have:
- Windows 11 system
- PowerShell access (no admin rights needed)
- Internet connection (or corporate proxy details)
- Your Windows username (will be auto-detected)

To check your username:
  1. Press Win + R
  2. Type: cmd
  3. Type: echo %USERNAME%
  4. Note down your username

================================================================================

STEP 2: CORPORATE PROXY CONFIGURATION (If Applicable)
================================================================================

If you're behind a corporate firewall/proxy:

2.1. Find your proxy settings:
     - Ask your IT department, OR
     - Open Internet Explorer/Edge → Settings → Internet Options
       → Connections → LAN Settings
     - Note the proxy address and port

2.2. Open PowerShell:
     - Press Win + S
     - Search "PowerShell"
     - Click "Windows PowerShell"

2.3. Set proxy environment variables:
     Copy and paste these commands (replace with your proxy details):

     $env:HTTP_PROXY  = "http://your-proxy-address:port"
     $env:HTTPS_PROXY = "http://your-proxy-address:port"
     $env:NO_PROXY    = "localhost,127.0.0.1,::1,.your-company.com"
     $env:http_proxy  = $env:HTTP_PROXY
     $env:https_proxy = $env:HTTPS_PROXY
     $env:no_proxy    = $env:NO_PROXY

     Example (Honda corporate network):
     $env:HTTP_PROXY  = "http://10.249.24.17:3128"
     $env:HTTPS_PROXY = "http://10.249.24.17:3128"
     $env:NO_PROXY    = "localhost,127.0.0.1,::1,.honda.com"

2.4. (Optional) If you encounter TLS/SSL errors:
     $env:UV_NATIVE_TLS = "1"

================================================================================

STEP 3: INSTALL UV PACKAGE MANAGER
================================================================================

3.1. In the same PowerShell window, run this command:

     Invoke-RestMethod https://astral.sh/uv/install.ps1 | Invoke-Expression

3.2. Wait for installation to complete. You should see output like:

     Downloading uv 0.8.15 (x86_64-pc-windows-msvc)
     Installing to C:\Users\<your-username>\.local\bin
       uv.exe
       uvx.exe
       uvw.exe
     everything's installed!

3.3. Note the installation path shown in the output:
     C:\Users\<your-username>\.local\bin

================================================================================

STEP 4: CONFIGURE PATH ENVIRONMENT VARIABLE
================================================================================

OPTION A: Using Windows GUI (Recommended - Permanent)
------------------------------------------------------

4A.1. Press Win + R to open Run dialog

4A.2. Type: rundll32.exe sysdm.cpl,EditEnvironmentVariables

4A.3. Press Enter (no admin needed - this opens USER variables)

4A.4. In the "User variables" section (top half):
      - Find and click on "Path"
      - Click "Edit..." button

4A.5. Click "New" button

4A.6. Add this path (replace <your-username> with your actual username):
      C:\Users\<your-username>\.local\bin

      Example:
      C:\Users\john.smith\.local\bin

4A.7. Click OK → OK to save

4A.8. CLOSE ALL PowerShell windows


OPTION B: Using PowerShell (Permanent)
---------------------------------------

4B.1. Open PowerShell

4B.2. Run this command (copy all lines together):

      $uvPath = "C:\Users\$env:USERNAME\.local\bin"
      $currentPath = [Environment]::GetEnvironmentVariable("Path", "User")
      if ($currentPath -notlike "*$uvPath*") {
          $newPath = "$uvPath;$currentPath"
          [Environment]::SetEnvironmentVariable("Path", $newPath, "User")
          Write-Host "PATH updated successfully!"
      } else {
          Write-Host "UV path already in PATH"
      }

4B.3. CLOSE ALL PowerShell windows


OPTION C: Using Batch File (Automated)
---------------------------------------

4C.1. Create a new text file named: setup_uv_path.bat

4C.2. Copy the batch file content provided separately

4C.3. Double-click the setup_uv_path.bat file

4C.4. Follow on-screen instructions

4C.5. CLOSE ALL PowerShell windows

================================================================================

STEP 5: VERIFY UV INSTALLATION
================================================================================

5.1. Open a NEW PowerShell window (important - must be new!)
     - Press Win + S
     - Search "PowerShell"
     - Click "Windows PowerShell"

5.2. Run this command:
     uv --version

5.3. Expected output:
     uv 0.8.15 (8473ecba1 2025-09-03)

     If you see the version number: SUCCESS! ✓
     If you see "command not found": Go to Troubleshooting section

================================================================================

STEP 6: CREATE VIRTUAL ENVIRONMENT
================================================================================

6.1. Navigate to your project folder:
     cd C:\path\to\your\project

     Or create a new project folder:
     mkdir C:\Users\<your-username>\Documents\my_project
     cd C:\Users\<your-username>\Documents\my_project

6.2. (If needed) Set proxy again in this new PowerShell session:
     $env:HTTP_PROXY  = "http://your-proxy-address:port"
     $env:HTTPS_PROXY = "http://your-proxy-address:port"

6.3. Create virtual environment with Python 3.13:
     uv venv --python 3.13

     Note: A folder named .venv will be created

6.4. Activate the virtual environment:
     . .\.venv\Scripts\Activate.ps1

     You should see (.venv) appear at the start of your prompt:
     (.venv) PS C:\Users\username\Documents\my_project>

6.5. Install ipykernel (for Jupyter support):
     uv add ipykernel

6.6. RESTART PowerShell or VSCode after first activation

6.7. Activate environment again after restart:
     . .\.venv\Scripts\Activate.ps1

================================================================================

STEP 7: INSTALL PACKAGES AND USE UV
================================================================================

Common UV Commands (Use these instead of pip):
-----------------------------------------------

Install a package:
  uv add pandas

Install multiple packages:
  uv add numpy pandas matplotlib

Install a specific version:
  uv add requests==2.31.0

Remove a package:
  uv remove pandas

List installed packages:
  uv pip list

Run Python in the virtual environment:
  uv run python script.py

Install from requirements.txt:
  uv pip install -r requirements.txt


Register Jupyter Kernel (Optional):
------------------------------------

For Jupyter Lab/Notebook integration:
  uv run python -m ipykernel install --user --name myproj-3.13 --display-name "Python 3.13 (myproj)"

================================================================================

STEP 8: TROUBLESHOOTING GUIDE
================================================================================

PROBLEM: "uv : The term 'uv' is not recognized"
SOLUTION:
  1. Verify UV is installed:
     Test-Path "C:\Users\$env:USERNAME\.local\bin\uv.exe"
     
     If False: Reinstall UV (go back to Step 3)
     If True: Continue below

  2. Check if PATH is set correctly:
     $env:Path -split ';' | Select-String "\.local\\bin"
     
     If no result: Go back to Step 4 and configure PATH again

  3. Restart PowerShell completely (close all windows, open new one)

  4. Try temporary PATH (for testing):
     $env:Path = "C:\Users\$env:USERNAME\.local\bin;$env:Path"
     uv --version


PROBLEM: SSL/TLS Certificate Errors
SOLUTION:
  $env:UV_NATIVE_TLS = "1"
  OR ask IT for corporate certificate configuration


PROBLEM: Proxy Connection Errors
SOLUTION:
  1. Verify proxy settings with IT department
  2. Test proxy:
     curl -x http://proxy:port http://google.com
  3. Set proxy again with correct address
  4. Try with NO_PROXY settings adjusted


PROBLEM: Permission Denied Errors
SOLUTION:
  1. Never use admin/elevated PowerShell
  2. All UV operations work with regular user account
  3. Check if antivirus is blocking - ask IT to whitelist .local\bin


PROBLEM: Python Version Not Found
SOLUTION:
  uv venv --python 3.12  (try different version)
  OR
  uv python install 3.13  (install Python via UV)


PROBLEM: Cannot Activate Virtual Environment
SOLUTION:
  1. Check execution policy:
     Get-ExecutionPolicy
  
  2. If "Restricted", set for current user:
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  
  3. Then activate again:
     . .\.venv\Scripts\Activate.ps1

================================================================================

QUICK REFERENCE CARD
================================================================================

Setup Commands:
  Install UV:        Invoke-RestMethod https://astral.sh/uv/install.ps1 | Invoke-Expression
  Check version:     uv --version

Virtual Environment:
  Create:            uv venv --python 3.13
  Activate:          . .\.venv\Scripts\Activate.ps1
  Deactivate:        deactivate

Package Management:
  Install:           uv add <package>
  Remove:            uv remove <package>
  List:              uv pip list
  Run:               uv run python script.py

Proxy Setup:
  $env:HTTP_PROXY  = "http://proxy:port"
  $env:HTTPS_PROXY = "http://proxy:port"

Installation Path:
  C:\Users\<your-username>\.local\bin

================================================================================

SUMMARY CHECKLIST
================================================================================

□ Step 1: Checked prerequisites and noted username
□ Step 2: Configured corporate proxy (if needed)
□ Step 3: Installed UV package manager
□ Step 4: Added UV to PATH environment variable
□ Step 5: Verified UV installation (uv --version works)
□ Step 6: Created and activated virtual environment
□ Step 7: Installed packages using uv add
□ Step 8: Bookmarked troubleshooting section

================================================================================

SUPPORT RESOURCES
================================================================================

Official Documentation:
  - UV Documentation: https://docs.astral.sh/uv/
  - Python Downloads: https://www.python.org/downloads/
  - Jupyter Lab: https://jupyter.org/

Corporate IT Support:
  - Contact your IT Help Desk for:
    • Proxy settings and port numbers
    • Certificate issues
    • Firewall exceptions
    • Domain-specific configurations

================================================================================
END OF GUIDE
================================================================================

Last Updated: November 2024
Version: 1.0
For: Windows 11 Corporate Environment (No Admin Access)
