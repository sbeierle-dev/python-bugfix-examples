def average(numbers):
    if not numbers:
        return None

    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


data = []
result = average(data)

if result is None:
    print("No data provided.")
else:
    print("Average:", result)
