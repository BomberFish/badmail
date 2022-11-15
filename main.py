#importing pip like this will fail in the future, should be replaced.
for n in range(1):
        try:
           import pip
        except ImportError as missing:
            print("You don't have pip. Exiting...")
            exit()

#install package function
def install(package):
    pip.main(['install', package])

#mail module checker & install
for n in range(1):
        try:
           import yagmail
        except ImportError as missing:
            if input("You don't have the yagmail module. Install it now? [Y/n]").lower() == "y":	
               install(missing.name)
               print("Please run the program again for changes to apply.")
               exit()
            else:
               print("Abort.")
               exit()


authfile = open("auth.txt", "r") 
authlines = authfile.readlines()
mail = yagmail.SMTP(authlines[0], authlines[1])

#TODO: multiple recipients
recipient = str(input("enter recipient> "))

subject = str(input("enter subject> "))

#TODO: multiple lines
content=str(input("enter text> "))

#TODO: multiple attachmets
doAttach=str(input("add an attachment? (y/N)> "))
if doAttach == "y":
   attachment=input("enter name of file (MUST BE IN CURRENT DIRECTORY!!)> ")
else:
   attachment=0

mail.send(to=recipient, subject=subject, contents=content, attachments=attachment)
print("sent!")