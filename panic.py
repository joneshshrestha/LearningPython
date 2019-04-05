phrase = "Don't Panic!"
plist = list(phrase)
print(phrase)
print(plist)
for i in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")
plist.insert(3, plist.pop())
plist.insert(2, plist.pop(4))
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
 
