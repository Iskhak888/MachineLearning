types = ['H','S','C','D']
card = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
lst = []
lst2 = []
a = 0


for i in types:
    for j in card:
        lst.append(i + j)


print(len(lst))
for i in range (50):
	for j in range(i+1,51):
		lst2.append(lst[i] + lst[j])
		a+=1
print(lst2)
print(a)





lst = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
lst1 = []
c = 0

for i in range(len(lst)):
    lst1.append(lst[i] + lst[i])

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        lst1.append(lst[i] + lst[j])
        
print(lst1)
print(len(lst1))


