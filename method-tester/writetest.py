file=open("presets.txt","r+")
a=file.readlines()
if a==[]:
    print("empty")
file.close()

file=open("presets.txt","w")
file.writelines("\n abc")
# file.close()

# file=open("presets.txt","w")
file.writelines("\n abc")
file.close()

file=open("presets.txt","r+")
print(file.read())

file.close()