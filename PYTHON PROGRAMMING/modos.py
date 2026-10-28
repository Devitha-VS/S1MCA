import os
print("current directory:",os.getcwd())
print("Files:",os.listdir())
os.mkdir("TestFolder")
print("Directory created")
print("path exists:",os.path.exists("TestFolder"))
print("Is directory:",os.path.isdir("TestFolder"))
print("is file:",os.path.isfile("sample.txt"))
