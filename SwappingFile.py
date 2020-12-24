def SwapFileData():
    fileName=input("Enter your file name:")
    f=open(fileName,"r")
    for line in f:
        data_a=line.read()
        f.write(data_b)
    nameofFile=input("Enter your file name:")
    fi=open(nameofFile,"r")
    for line in fi:
        data_b=line.read()
        fi.write(data_a)
SwapFileData()