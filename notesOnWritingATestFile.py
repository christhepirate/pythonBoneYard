#!bin/bin/python3
#notes on writing a test file

#variable = open("filename","w")
#filemodes
#r=read
#w=write
#a=append
#r+=readand write
myFile = open("testfile.txt","w")#writes a new file object called "testfile.txt"
myFile.write("Hello World\n")
myFile.write("Test, Test\n")
myFile.write("Oh behest")
#Closes the file
myFile.close()

#opens and reads the file
myFile = open("testfile.txt","r")#read the new file object called "testfile.txt"
print(myFile.read())
myFile.close()

myFile = open("testfile.txt","r")#read the new file object called "testfile.txt"
print(myFile.read(5))#Prints out the first 5 characters of the "testfile.txt"
myFile.close()

myFile = open("testfile.txt","r")#read the new file object called "testfile.txt"
for line in myFile:
    if line.startswith("T"):
        print(line, end='')#the end='' part is a print option to not include a new line after the print statment. this is necisarry because 'line' also prints a new line
myFile.close()

#read file using a WITH statement
with open("testfile.txt", "r") as myFile:
    print(myFile.read())
