@echo off
rem OpenClaw Gateway (v2026.2.3-1)
set PATH=C:\Users\Md Sadik Laskar\AppData\Roaming\npm;C:\Program Files\nodejs\;C:\ProgramData\chocolatey\bin;C:\Program Files\Git\cmd;C:\Users\Md Sadik Laskar\AppData\Local\Programs\Python\Python310\Scripts\;C:\Users\Md Sadik Laskar\AppData\Local\Programs\Python\Python310\;C:\Users\Md Sadik Laskar\AppData\Local\Programs\Python\Python311\Scripts\;C:\Users\Md Sadik Laskar\AppData\Local\Programs\Python\Python311\;C:\Users\Md Sadik Laskar\AppData\Local\Programs\Python\Python313\Scripts\;C:\Users\Md Sadik Laskar\AppData\Local\Programs\Python\Python313\;C:\Users\Md Sadik Laskar\AppData\Local\Programs\Python\Launcher\;C:\Users\Md Sadik Laskar\AppData\Local\Microsoft\WindowsApps;C:\Users\Md Sadik Laskar\AppData\Local\Programs\Ollama
set OPENCLAW_GATEWAY_PORT=18789
set OPENCLAW_GATEWAY_TOKEN=272d22dec98da63a3362c6dc0a9c0eebf2aa9ed96d21775d
set OPENCLAW_SYSTEMD_UNIT=openclaw-gateway.service
set OPENCLAW_SERVICE_MARKER=openclaw
set OPENCLAW_SERVICE_KIND=gateway
set OPENCLAW_SERVICE_VERSION=2026.2.3-1
"C:\Program Files\nodejs\node.exe" "C:\Users\Md Sadik Laskar\AppData\Roaming\npm\node_modules\openclaw\dist\index.js" gateway --port 18789
