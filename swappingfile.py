def swapfiledata():
    file1name= input("enter the first file name : ")
    file2name= input("enter the second file name : ")

    with open(file1name,'r')as a:
        data_a=a.read()
    a.close()    
    with open(file2name,'r')as b:
        data_b=b.read()
    b.close()    

    with open(file1name,'w')as a:
        a.write(data_b)
    with open(file2name,'w')as b:
        b.write(data_a)

swapfiledata()