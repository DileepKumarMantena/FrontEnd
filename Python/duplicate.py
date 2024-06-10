def duplicate(list_elements):
    s=set()
    duplicates=set()
    for i in list_elements:
            if i in s:
                  duplicates.add(i)
            else :
                  s.add(i)
                  

    return duplicates


size= int(input("Enter the number of elements: "))
list1 = [input(f"Enter list elements {i+1}: ") for i in range(size)]
print("The list of elements is:", list1)

result=duplicate(list1)
print(result)