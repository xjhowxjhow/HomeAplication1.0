
import os
import sys
from time import sleep

class update(object):
    def __init__(self):
        
        diretorio = os.getcwd() 
        num = diretorio.rfind("\\") + 1
        os.chdir(diretorio[:num]) 
        print(diretorio)
        
        if (os.path.exists(''+diretorio+'\HomeApp.exe')):
            sleep(2)
            os.remove(''+diretorio+'\HomeApp.exe')
            old_file = os.path.join(diretorio, "HomeAppold.exe")
            new_file = os.path.join(diretorio, "HomeApp.exe")
            os.rename(old_file, new_file)
            print('Update Sucess')
            
        else:
            pass
    

update()
