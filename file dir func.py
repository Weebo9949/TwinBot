import glob 


#filedir needs to take on argument of what folder to look at, must handle right now at least
#jpg and py directories


def filedirlist(datatype):
    if datatype == "jpg":
        filedirs = glob.glob("C:/Users/Luke/Desktop/HAMBURGERJPG/*.jpg")
        return(filedirs)
    if datatype == "py":
        filedirs = glob.glob("C:/Users/Luke/Desktop/HAMBUGERPY/*.py")
        return(filedirs)
    else:
        return("error invalid datatype")
    
def filedirpath(filename, datatype):
    dirlist = filedirlist(datatype)
    for i in dirlist:
        if filename in i:
            return(i)
        else:
            pass
    return("error no such file")
filename = input("file name")
datatype = input("data type")

outdir = filedirpath(filename, datatype)

        
print(outdir)