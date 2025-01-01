"""
Question 3 :
Write a function to find out the sum of first M terms of
the following series N + NN + NNN + …. up to M terms
    1. for example for M =3, and N = 5
    2. 5 + 55 + 555
Input : M =3, and N = 5
Output : 615 (5,55,555)

"""

def sum_of_first_m_term(N,M):
    sum = 0
    total = 0
    for i in range(M):
        sum =( sum * 10 ) + N
        print(sum)
        total+=sum
    print(total)

sum_of_first_m_term(5,3)

