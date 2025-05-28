numbers = [1, 2, 3, 4, 5]

print(numbers[0])

numbers[2] = 10
print(numbers[2])

print(numbers)

def reverse_list(lst):
    return lst[::-1]

reversed_numbers = reverse_list(numbers)
print("Reversed list:", reversed_numbers)
