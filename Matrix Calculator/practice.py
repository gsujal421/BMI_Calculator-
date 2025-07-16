import numpy as np

def calculator(A, B, choice):
    if choice == '1':
        return A + B
    elif choice == '2':
        return A - B
    elif choice == '3':
        return A @ B  
    else:
        return 'Invalid choice'

while True:
    print("\nMatrix Calculator Menu:")
    print("1. Add two matrices")
    print("2. Subtract two matrices")
    print("3. Matrix Multiplication") 
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    if choice == '4':
        print("Exiting")
        break

    print("Enter elements of Matrix A :")
    A = list(map(int, input().split()))
    print("Enter elements of Matrix B :")
    B = list(map(int, input().split()))
    A=(np.array(A))
    B=(np.array(B))
    result=calculator(A,B,choice)
    print('Result =',result)