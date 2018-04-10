import imaplib
import email
import re
import os

password = os.environ['password']
e_mail = os.environ['e_mail']

m = imaplib.IMAP4_SSL("imap.gmail.com",993)
#m.login("email@gmail.com","pass")
m.login(e_mail,password)
m.list()
m.select()
#(retcode,messages)=m.search(None,'(UNSEEN)')
test = m.fetch(2,'(RFC822)')
ola=str(test)
#ola.split()[5]
typ, data = m.fetch(3,'(RFC822)')
msg = email.message_from_string(data[0][1])
#typ, data = m.fetch(3,'(RFC822)')
#typ, data = m.store(3,'-FLAGS','\\Seen')
oi = str(msg)
pi = oi.split()
save_dado = []
for line in pi:
    if 'Devops' in line:
        print line
        data=pi[2:5]
        data=str(data)
        data=re.sub("['',\[\]]", "", data)
        data=re.sub(" ", "-" , data)
        print data

        
