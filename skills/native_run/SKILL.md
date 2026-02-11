# Native Run

## Description
A very simple skill that runs an arbitrary Windows shell command and returns the stdout/stderr.

## Trigger
Message starts with `Run command:`

## Safety
Only the commands you literally type are executed.  
Feel free to add a whitelist or log‑file if you want extra safety.

## Quick example