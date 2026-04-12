import subprocess

result = subprocess.run(
    ["docker", "logs", "silly_buck"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

print("STDOUT:")
print(result.stdout)

print("STDERR:")
print(result.stderr)

print("RETURN CODE:", result.returncode)
