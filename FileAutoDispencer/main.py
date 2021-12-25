# from _typeshed import FileDescriptor
import os
from datetime import*



def file_dispencer(path,thresh,base=True):

    if os.path.isdir(path):
        for i in os.listdir(path):
            file_dispencer(path+"/"+i,thresh,False)

        if(not base) and (len(os.listdir(path))==0):
            os.rmdir(path)

        return 


    mod=os.path.getatime(path)

    if thresh>mod:

        os.remove(path)



threshold=(datetime.now()-timedelta(minutes=1)).timestamp()

file_dispencer("files",threshold)