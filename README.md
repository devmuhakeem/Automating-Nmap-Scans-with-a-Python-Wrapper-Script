# Automating Nmap Scans with a Python Wrapper Script

A hands-on lab writing a Python script that wraps Nmap: prompting for a target and scan type, running the scan via `subprocess`, and automatically logging results to a file instead of just printing them to the terminal.

## Scenario
Using Nmap directly means retyping the full command correctly every time and manually redirecting output if you want a persistent record. This lab built a small Python wrapper to standardize that workflow: take input, run the scan, log the results.

## What I did

### Built the script (`nmap_scanning_script.py`)
```python
import subprocess

def run_nmap():
    target = input("Enter the target IP or domain: ")
    scan_type = input("Enter the scan type (for example, -sS, -sV, -A): ")

    print("Running nmap...")
    subprocess.call(["nmap", scan_type, target])

    log_file = "nmap_scan_log.txt"
    print(f"Logging scan results to {log_file}...")
    subprocess.call(["nmap", scan_type, target], stdout=open(log_file, "w"))

if __name__ == "__main__":
    run_nmap()
```

- `subprocess` is what lets Python invoke Nmap, a separate external command-line tool, programmatically
- Wrapping the logic in a function (`run_nmap`) keeps it organized and reusable
- Prompting for `target` and `scan_type` via `input()` rather than hardcoding either makes the script reusable against any target/scan type without editing code
- `subprocess.call()` takes arguments as a list (not a concatenated string) — a safer pattern that avoids shell-interpretation issues
- `stdout=open(log_file, "w")` redirects scan output to a persistent file instead of letting it only print to the terminal
- The `if __name__ == "__main__":` guard ensures `run_nmap()` only fires when the script is run directly, not if it's ever imported elsewhere

### Tested the script
- Ran `python3 nmap_scanning_script.py`
- Entered `scanme.nmap.org` (the Nmap project's own official, authorized test target) and selected a scan type (`-sS`, `-sV`, or `-A`)
- Confirmed completion, then ran `ls` to verify both the script and `nmap_scan_log.txt` existed
- Ran `cat nmap_scan_log.txt` to confirm the logged scan results matched what Nmap would normally print directly to the terminal

## Key takeaways
- Wrapping a command-line tool in a script standardizes its invocation, reducing the chance of a repeated manual typo or inconsistency across runs
- Passing arguments as a list to `subprocess.call()`, rather than building a single command string, is a real security practice that avoids a category of shell-interpretation issues
- Logging output to a file is what actually makes scan results useful afterward — terminal output alone is effectively disposable once the window closes or scrolls away
- This script is a deliberate starting point: a fixed log filename means repeated runs overwrite each other, and a more developed version might accept CLI arguments or generate timestamped log files per run
- The pattern (wrap, standardize input, log output persistently) generalizes well beyond Nmap — it's a reusable template for automating any command-line security tool

## Tools
Python 3, `subprocess` (standard library), Nmap, Kali Linux, nano

---
*Completed as an IBM hands-on lab, run against scanme.nmap.org, the Nmap project's officially authorized public test target.*
