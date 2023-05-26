def maximum_operations(N, A):
    operations = 0

    while all(num % 2 == 0 for num in A):
        A = [num // 2 for num in A]
        operations += 1

    return operations


# Example usage
N = int(input("Enter the number of elements: "))
A_str = input("Enter the elements separated by spaces: ")
A = list(map(int, A_str.split()))

max_ops = maximum_operations(N, A)
print("Maximum possible operations:", max_ops)