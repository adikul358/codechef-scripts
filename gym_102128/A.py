def max_amount(offers):
    global m
    final = 0
    # print("Offer:", offers)
    if offers[0][0] > m and offers[1][0] > m:
        final = 0
    elif offers[0][0] >= m:
        if offers[1][1] > m:
            final = (offers[1][2]/100)*m
        else:
            final = (offers[1][2]/100)*offers[1][1]
    elif offers[1][0] > m:
        if offers[0][1] >= m:
            final = (offers[0][2]/100)*m
        else:
            final = (offers[0][2]/100)*offers[0][1]
    else:
        m1 = m if offers[0][1] >= m else offers[0][1]
        m2 = m if offers[1][1] >= m else offers[1][1]
        coeffs = [m1*offers[0][2]/100, m2*offers[1][2]/100]
        print(coeffs)
    print('{0:.9f}'.format(final+m)) 

m = int(input())
n = int(input())
offers = []
for i in range(n):
    temp = list(map(int, input().split(" ")))
    temp = [[i for i in temp[:3]], [i for i in temp[3:]]]
    offers.append(temp)

for i in offers:
    max_amount(i)