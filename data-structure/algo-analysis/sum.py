#Analysis of algorithms 

# case 1

def sum1(n):
    final_sum = 0
    for x in range(n + 1):
        final_sum += x
        
    return final_sum

case1 = sum1(10)


# case2

def sum2(n):
    return (n*(n+1))/2

case2 = sum2(10)

print("case1", case1)    
print("case2", case2)    