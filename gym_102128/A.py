m = int(input())
n = int(input())
offers = []
for i in range(n):
    offers.append(input().split(" "))
for j in range(int(len(offers)/3)):
    offers[j] = [f for f in offers[j+1:j+3]]
print(offers)