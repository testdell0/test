# uv Installation Manual (Windows PowerShell)

## 1. Launch PowerShell
1. Open the **Start Menu** and search for **“PowerShell”**.  
2. Select **Windows PowerShell** to launch it.  
   - The prompt should look like `PS C:\Users\<username>>`.  
   - Administrator privileges are **not required** to install uv. You can run it with a regular user account.

---

## 2. Install uv
Run the following command in PowerShell:

```powershell
Invoke-RestMethod https://astral.sh/uv/install.ps1 | Invoke-Expression
```

If successful, you will see output like this:

```
Downloading uv 0.8.15 (x86_64-pc-windows-msvc)
Installing to C:\Users\<username>\.local\bin
  uv.exe
  uvx.exe
  uvw.exe
everything's installed!

To add C:\Users\<username>\.local\bin to your PATH, either restart your shell or run:

    set Path=C:\Users\<username>\.local\bin;%Path%   (cmd)
    $env:Path = "C:\Users\<username>\.local\bin;$env:Path"   (powershell)
```

---

## 3. Configure PATH
The installation location is:

```
C:\Users\<username>\.local\bin
```

### Temporarily add to PATH (valid for the current session only)
```powershell
$env:Path = "C:\Users\<username>\.local\bin;$env:Path"
```

### Permanently add to PATH
1. In Windows Search, type **“Environment Variables”** → Open **“Edit the system environment variables”**  
2. Click **“Environment Variables…”**  
3. Under **User variables**, select `Path` → Edit  
4. Add a new entry:  
   ```
   C:\Users\<username>\.local\bin
   ```
5. Click OK → OK, then restart PowerShell

---

## 4. Verify Installation
```powershell
uv --version
```

Example:

```
uv 0.8.15 (8473ecba1 2025-09-03)
```
