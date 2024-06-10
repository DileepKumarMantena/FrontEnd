import asyncio

async def find_duplicates(list_elements):
    s = set()
    duplicates = set()
    for i in list_elements:
        if i in s:
            duplicates.add(i)
        else:
            s.add(i)
        # Simulate asynchronous behavior
        await asyncio.sleep(0)  
    return duplicates

async def main():
    size = int(input("Enter the number of elements: "))
    list1 = [input(f"Enter list element {i+1}: ") for i in range(size)]
    print("The list of elements is:", list1)

    # Asynchronously find duplicates
    result = await find_duplicates(list1)
    print(result)

# Run the main function in the event loop
asyncio.run(main())
