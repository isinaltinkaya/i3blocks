#!/usr/bin/python

import imaplib

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('YOUR_MAIL_ADDRESS@gmail.com', 'YOUR_PASSWORD')
mail.list()
mail.select()
mcount = len(mail.search(None,'UnSeen')[1][0].split())

print(mcount)
print(mcount)

if int(mcount) > 10:
    print("#C70039")
elif int(mcount) > 5:
    print("#FF5733")
elif int(mcount) > 0:
    print("#FFC300")
elif int(mcount) == 0:
    print("#FFFFFF")
