#Toomas Silmberg
#21.11.22
#kt emaili kontroll
import re

#salvestab faili
f= open("tekst.txt","w+")


#küsib emaili
email = (input("Lisage email: "))

#tükledab emaili
enimi = email.split(".")[0]
server = re.findall(r"[\w']+", email)[2]
domeen = email.split(".")[2]

#kontrollib emaili ja väljastab vastuse
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check(email):
    if(re.fullmatch(regex, email)):
        f.write(f"Tere {enimi}, sinu email on {server} serveris ja domeeniks on sul {domeen}")
    else:
        f.write("See pole korrektne email")
check(email)


f.close()
