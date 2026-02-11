import subprocess, json

def handler(args):
    cmd=args.get("cmd","")
    if not cmd:
        return {"error":"Missing 'cmd' argument"}
    res=subprocess.run(cmd,shell=True,capture_output=True,text=True)
    return {
        "stdout":res.stdout,
        "stderr":res.stderr,
        "returncode":res.returncode
    }
