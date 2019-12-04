from itertools import combinations
n = input()
s = {}
r = input().split(' ')
for i in range(int(n)):
	r[i] = int(r[i])
	try:
		s[r[i]] += 1
	except:
		s[r[i]] = 1
p = combinations([i for i in s],2)
p = list(p)
rev = 0
for i in p:
	rev += abs(i[0]-i[1])*s[i[0]]*s[i[1]]
print(rev)