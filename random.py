import math

# Implementing our own random number generator using the linear congruent method
def generate_random_numbers( a, c, M, r1, ri_array, no_of_randoms ):
 
    ri_array[0] = r1
 
    for i in range(no_of_randoms - 1):
        ri_array[i + 1] = ( a * ri_array[i] + c ) % M
 
if __name__ == '__main__':
    
    # With (a, c, M, r1) = (57, 1, 256, 10), determining the period (how many numbers are generated before the sequence repeats)
    print("\n-------------------------------------------------")
    a = 57
    c = 1
    r1 = 256
    M = 10
    
    no_of_randoms = 15
    print("Let us generate a sequence of ", no_of_randoms, " random numbers.")
    
    ri_array = [0] * no_of_randoms
 
    generate_random_numbers(a, c, M, r1, ri_array, no_of_randoms)

    print("Sequence: ", ri_array)
    print("As can be seen from the generated sequence,")
    print("5 numbers were generated before the sequence repeated.")
        
    # Testing our random-number generator for k = 1, 3, 7 and N = 100, 10000, 100000
    print("\n-------------------------------------------------")
    ks = [1, 3, 7]
    Ns = [100, 10000, 100000]
    
    for k in ks:
        for N in Ns:
            M = N
            r1 = math.sqrt(M)
            a = math.sqrt(r1 + 19)
            c = 1
            
            ri_array = [0] * N
            generate_random_numbers(a, c, M, r1, ri_array, N)
            xi_array = [ float(ri / M) for ri in ri_array] # so that they range in [0,1]
            
            xik_sum = 0
            for i in range(N):
                xik_sum += xi_array[i] ** k
                
            result = math.sqrt(N) * abs( 1/N * xik_sum - 1/(k+1) )
            print("k = ", k, "| N = ", N, "\t| Result = ", result, "\n"  )
            
    print("As can be seen, the results are indeed in the order of 1.")
            
    #  We can determine the near-neighbor correlation in our random sequence by taking sums of products for small k
    print("\n-------------------------------------------------")
    N = 81
    k = 2
    
    a = 4
    c = 1
    r1 = 9
    M = N
    
    print("Let us generate a sequence of ", N, " random numbers between 0 & 1,\nand compute the given expression.\n")
    
    ri_array = [0] * N
    generate_random_numbers(a, c, M, r1, ri_array, N)
    xi_array = [ float(ri / M) for ri in ri_array] # so that they range in [0,1]
    
    xi_xik_sum = 0
    for i in range(N - k):
        xi_xik_sum += xi_array[i] * xi_array[i+k]
    
    result = 1/N * xi_xik_sum
    print("Result = ", result )
    
    print("\nThis value is indeed close to 0.25, meaning that my")
    print("generator produces independent random numbers.")
