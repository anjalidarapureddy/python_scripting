# Try to create a file called sub_process.txt and then add content in it like a description through scrips
import os

load_data="""
sub-process allows python to 
run system commands (Linux commands, Docker, kubectl, git, etc.) and interact with them
Run deployments (kubectl apply)
Build images (docker build)
Check system status (df -h, ps)
Automate pipelines
"""

# now i prepared the data
#next i create a empty file and load the data

with open("sub_process.txt", "w") as f:
    f.write(load_data)

