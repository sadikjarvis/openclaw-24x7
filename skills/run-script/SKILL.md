# run-script

## Description

Simple skill that runs a local shell command and returns stdout/stderr/return‑code.

## Usage

```bash
runScript "<command>"
```

Example:

```bash
runScript "python - <<'PY'
print('Hello')
PY"
```

The returned JSON contains `stdout`, `stderr`, and `returncode`.
