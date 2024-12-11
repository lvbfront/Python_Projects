import ezgmail
#need to cd to emails
print(ezgmail.EMAIL_ADDRESS)

#ezgmail.send('lvb999997@gmail.com', 'test msg2', 'this is a test for sending siiii', 'logo.png')

#get unread mgss
unreadMsg = ezgmail.unread()
#print(ezgmail.summary(unreadMsg))


#print the msg info

# print(len(unreadMsg))
# print(unreadMsg[0])
# print(unreadMsg[0].messages[0]) #the first msg if you want the response write 1
# print(unreadMsg[0].messages[0].subject)
# print(unreadMsg[0].messages[0].body)
# print(unreadMsg[0].messages[0].timestamp)
# print(unreadMsg[0].messages[0].sender)
# print(unreadMsg[0].messages[0].recipient)

#get last msgs
recentMsg = ezgmail.recent()
print(len(recentMsg))


recentMsg = ezgmail.recent(maxResults=50)
print(len(recentMsg))

#search a msg by topic
resultSearch = ezgmail.search('BinDawood')
print(len(resultSearch))
print(resultSearch[0])