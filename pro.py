import os
import shutil
from_dir="C:/Users/vipin kumar/Downloads"
to_dir="C:/Users/vipin kumar/OneDrive/Desktop/whj/112-pro"
listOfFiles = os.listdir(from_dir)
print(listOfFiles)
for file_name in listOfFiles:
    name,ext=os.path.splitext(file_name)
    print(name)
    print(ext)