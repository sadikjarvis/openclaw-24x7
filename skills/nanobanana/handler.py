from openclaw import native_run

def run(args):
    prompt = args.get("message") or args.get("prompt") or "Hello Nano Banana"
    # Call your existing nano_banana.py script via NativeRun
    return native_run.run_command(f'python "C:\\Users\\Md Sadik Laskar\\.openclaw\\workspace\\nano_banana.py" "{prompt}"')
