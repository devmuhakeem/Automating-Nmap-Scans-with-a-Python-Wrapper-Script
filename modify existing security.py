
import subprocess

def run_nmap():
    target = input("Enter the target IP or domain: ")
    scan_type = input("Enter the scan type (for example, -sS, -sV, -A): ")

    print("Running nmap...")

    log_file = "nmap_scan_log.txt"

    print(f"Logging scan results to {log_file}...")

    with open(log_file, "w") as output:
        subprocess.call(
            ["nmap", scan_type, target],
            stdout=output
        )

    print("Scan completed!")
    print(f"Results saved to {log_file}.")

if __name__ == "__main__":
    run_nmap()
