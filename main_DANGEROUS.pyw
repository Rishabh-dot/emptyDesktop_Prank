import os, shutil, getpass
 
#Finding Username
uname = getpass.getuser()

# Deleting
dir = 'C:/Users/'+uname+'/Desktop'
for files in os.listdir(dir):
    path = os.path.join(dir, files)
    try:
        shutil.rmtree(path)
    except OSError:
        os.remove(path)