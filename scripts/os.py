import os

# os is allows to interact with files and folders, read env variables, perform os level operations

file = os.getcwd() #currentworkingdirectory
print(file)

file2 = os.listdir(".") #listdirectory
print(file2)

os.rmdir("os_dir") #remove dir

os.mkdir("os_dir") #create directory

os.makedirs("var/lib/html", exist_ok=True) #nested directories


db_pass = os.getenv("DB_PASSWORD")
print(db_pass)
