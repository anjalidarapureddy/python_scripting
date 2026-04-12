import os
# find all .log files. here we use .txt files

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root,file))
