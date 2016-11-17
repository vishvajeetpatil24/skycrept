
# Strings

katrina = "Nude Pics"
print(katrina)
print('India is my country')
print("Go to hell")
print("This is my mother's childhood home")
print('This is my mother\'s childhood home')
print("Use \"\\'\" mark for apostrophe")

katrina = katrina + " Ah those what an masterpiece"
print(katrina)
aish = "Nude "
print(aish * 5)
print("C:\Windows\Program Files\\nude Saver\\")
#Reading the last five characters in katrina
print(katrina[-5:])
#Divide strings in blocks of same size n when length is m*n and m is integer then the value
note = "I am an Indian Boy".encode("UTF-8")
oblist = list(zip(*[iter(note.decode("UTF-8"))]*3))
print(''.join(oblist[1]))
