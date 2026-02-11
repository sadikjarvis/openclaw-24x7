import subprocess

# List of safe commands
SAFE_COMMANDS = ['dir', 'echo', 'start', 'copy', 'move', 'notepad', 'calc']

def run_command(command):
    # Check if command starts with allowed commands
    if not any(command.strip().lower().startswith(cmd) for cmd in SAFE_COMMANDS):
        return "Error: Command not allowed for safety."

    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"

# Example usage when OpenClaw triggers this skill
if __name__ == "__main__":
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    print(run_command(cmd))
