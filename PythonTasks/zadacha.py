s = 'aaaabbсaafffffdAAAAaaaaAAaaaaas'
#'a4b2с1a2'

temp = s[0]
counter = 0
res = ""
for i in range(0, len(s)):
    if temp == s[i]:
        counter += 1
    if temp != s[i]:
         res += s[i-1]
         res += str(counter)
         temp = s[i]
         counter = 1
res += temp
res += str(counter)
print(res)