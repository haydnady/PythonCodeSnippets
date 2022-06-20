
def freq_count(list_: list, number: int) -> list:
    dict_ = {}
    level = -1

    for char in str(list_):  # Note list to string
        if char.isdigit():
            if int(char) == number:
                dict_[level] += 1
        elif char == "[":
            level += 1
            if level not in dict_:
                dict_[level] = 0  # Initialize key for this level in dictionary
        elif char == "]":
            level -= 1

    # Using list comprehension to convert dictionary to list
    # print([[k, v] for k, v in dict_.items()])
    return [[k, v] for k, v in dict_.items()]


if __name__ == "__main__":
    # Tests
    solution = freq_count([1, 4, 4, [1, 1, [1, 2, 1, 1]]], 1)
    expected = [[0, 1], [1, 2], [2, 3]]
    print("✔ Passed!" if solution == expected else "❌ Failed.")

    solution = freq_count([1, 5, 5, [5, [1, 2, 1, 1], 5, 5], 5, [5]], 5)
    expected = [[0, 3], [1, 4], [2, 0]]
    print("✔ Passed!" if solution == expected else "❌ Failed.")
    
    solution = freq_count([1, [2], 1, [[2]], 1, [[[2]]], 1, [[[[2]]]]], 2)
    expected = [[0, 0], [1, 1], [2, 1], [3, 1], [4, 1]]
    print("✔ Passed!" if solution == expected else "❌ Failed.")