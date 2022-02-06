def identify_first_duplicate(num_list):
    length = len(num_list)
    freq = []
    for i in range(length):
        if i not in freq:
            freq.append(num_list[i])
        else:
            return num_list[i]

    return "No duplicate elements found"


print(identify_first_duplicate([1, 2, 3, 2, 1]))