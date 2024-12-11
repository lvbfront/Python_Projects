import imapclient

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)


#log in

res_email = "lvb999997@gmail.com"
pas = input(str("the pass: "))
imapObj.login(res_email, pas)

#print all fo;ders
import pprint
pprint.pprint(imapObj.list_folders())

#select fo;der
imapObj.select_folder('INBOX', readonly=True)

#search in folder
uid = imapObj.search(['ALL'])
#print(uid)


res_msg = imapObj.fetch(uid, ['BODY[]'])
#pprint.pprint(res_msg) 270

import pyzmail

msg = pyzmail.PyzMessage.factory(res_msg[270][b'BODY[]'])
print(msg.get_subject())
print(msg.get_addresses('from'))
print(msg.get_addresses('to'))
print(msg.get_filename())

#get the msg bode
print(msg.text_part.get_payload().decode(msg.text_part.charset))