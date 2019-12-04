def check_revenue(index, price):
    global custs
    eligible_custs = custs-index
    return eligible_custs*price

cust_list = []
max_revenue = 0

for i in range(int(input())):
    cust_list.append(int(input()))

cust_list.sort()
custs = len(cust_list)

for i in range(custs):
    r = check_revenue(i, cust_list[i])
    if r > max_revenue:
        max_revenue = r

print(max_revenue)