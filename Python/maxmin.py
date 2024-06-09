def min_max(list1):
    min_el=min(list1)
    max_el=max(list1)
    return min_el,max_el

num_elements = int(input("Enter the number of elements: "))
max_min_numbers = [input(f"Enter list elements {i+1}: ") for i in range(num_elements )]
print('The min and max elements are ',min_max(max_min_numbers))
