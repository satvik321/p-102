import os 
import shutil

from_dir="C:/Users/drsba/Downloads"
to_dir = "C:/Users/drsba/Downloads/example"

listOfFiles=os.listdir(from_dir)
#print(listOfFiles)

for fileName in listOfFiles:
    name,ext= os.path.splitext(fileName)
    #print(name)
    print(ext)
    if ext =="":
        continue
    if ext in[".txt",".doc", ".docx", ".pdf"]:
      path1=from_dir+"/"+fileName
      path2=to_dir+"/"+"docFile"
      path3=to_dir+"/"+"docFile"+"/"+fileName
      
      if os.path.exists(path2):
         print("moving"+fileName)
         shutil.move(path1,path3)

      else:
         os.makedirs(path2)
         print("moving"+fileName)
         shutil.move(path1,path3)
         
