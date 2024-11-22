n_term = 7

fibonacci_serire = [0,1]

for i in range(2,n_term):
    next_term = fibonacci_serire[i - 1] + fibonacci_serire[i-2]
    fibonacci_serire.append(next_term)
    
    print("fibonacci series:",fibonacci_serire)