#check the disk usage and then send alert if it exceeds >80

import subprocess

def disk_usage():
    result=subprocess.run(["df", "-h"], capture_output=True, text=True)
    # here it captures both stdout and stderr and also text is for it returns in a text format instead of bytes

    lines = result.stdout.splitlines()

    for line in lines[1:]:
        parts = line.split()
        usage = parts[4]

        if int(usage.strip("%")) > 20:
            print(f"[Alert]: High disk usage- {line}")


disk_usage()
