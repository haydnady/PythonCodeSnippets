
def freq_count(list_: list, number: int) -> list:
    dict_ = {}
    solution = []
    level = -1

    for char in str(list_):
        if char.isdigit():
            if int(char) == number:
                print("---------------", dict_[level])
                dict_[level] += 1
        elif char == "[":
            level += 1
            dict_[level] = 0  # Initialize key for this level in dictionary
        elif char == "]":
            level -= 1

    print(dict_)
    return solution


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