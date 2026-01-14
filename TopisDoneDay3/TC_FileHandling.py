file=open("test.txt","r")
content=file.readline()
content1=file.readlines()
print(content)
print(content1)
file.close()

file=open("test.txt","a")
file.write(" new line is added to the file")
file.close()

file=open("test.txt","w")
file.write(" this is my write example")
file.close()