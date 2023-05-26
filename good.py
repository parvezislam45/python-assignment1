def min_elements_to_remove(N, sequence):
    freq_counts = {}
    for num in sequence:
        freq_counts[num] = freq_counts.get(num, 0) + 1
    
    removal_count = 0
    for num, count in freq_counts.items():
        if count > num:
            removal_count += count - num
    
    return removal_count

# Read the input
N = int(input())
sequence = list(map(int, input().split()))

# Call the function and print the result
min_removals = min_elements_to_remove(N, sequence)
print(min_removals)