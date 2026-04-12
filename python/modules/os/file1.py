import os

# get the current directory
structure = os.getcwd()
print(structure)

#list of files
print(os.listdir("."))

# create a .env file
#the below variable is not the comment its the multi-line string
env_content = """ 
DB_HOST=localhost
DB_NAME=dev
DB_USER=admin
DB_PASS=secret123
PORT=8080

"""
with open(".env", "w") as f: ## with used to close the file automatically after operation completes, it creates an empty file
    f.write(env_content) #it loads the data

print(os.path.exists(".env"))
print(os.path.isfile(".env"))



