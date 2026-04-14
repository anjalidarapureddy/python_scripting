import shutil

total, used, free = shutil.disk_usage("/")

print(f"Free space: {free} bytes")

free_gb = free / (1024 ** 3)
print(f"free space : {free_gb}GB")

