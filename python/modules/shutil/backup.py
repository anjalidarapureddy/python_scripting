import shutil
from datetime import datetime

name = f"backup_{datetime.now().strftime('%d-%m')}"

shutil.make_archive(name, "gztar", ".")# name is the output name, gztar is format type, . is the it takes backup of the current directory

print("backup created")
