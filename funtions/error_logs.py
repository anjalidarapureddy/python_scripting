def read_logs(file):
    with open(file) as f:
        for line in f:
            yield line

def filter_logs(error):
    for log in logs:
        if "ERROR" in log:
            yield log

def analysis(file):
    total = 0
    error = 0
    logs = read_logs(file)
    for log in logs:
        total += 1
        if "ERROR" in log:
            error += 1
            print(f"[Error found] {log.strip()}")

    print("\nsummary:")
    print(f"total logs: {total}")
    print(f"error logs: {error}")

analysis("logs.txt")
