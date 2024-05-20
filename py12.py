import os
import shutil


yol=os.getcwd()
try:
    os.mkdir("Example")
    os.chdir(yol+"/Example")
    os.mkdir("Example2")
except FileExistsError :
    print("Bu qovluq artiq yaradilib !!")


#----------------------------Birinci hisse----------------------------------------------

os.chdir(yol)
for file in os.listdir():
    if not os.path.isdir(file) and not file.endswith(".py"):
        shutil.move(file,yol+"\\Example\\Example2\\{}".format(file.split("\\")[-1]))




#----------------------------İkinci hisse----------------------------------------------
"""
os.chdir(yol+"\\Example\\Example2")
for file in os.listdir():
    if file.endswith(".txt"):
        shutil.move(file,yol+"\\Example\\{}".format(file.split("\\")[-1]))
"""
