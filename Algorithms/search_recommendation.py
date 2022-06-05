"""Search recommendation program

Made in Python v3.10
"""


class SearchRecommendation():
    """Recommends words based on searched word"""

    searchable_dict = {}  # To hold sets of words searchable by alphabet letter


    def __init__(self, searchable_list) -> None:
        self.searchable_list = searchable_list
        self.create_searchable_object()


    def create_searchable_object(self) -> dict:
        """Adds list data to dictionary of sets for key alphabet letter search"""

        for word in self.searchable_list:
            word = word.lower()

            if word[0] in self.searchable_dict:
                self.searchable_dict[word[0]].add(word)
            else:
                self.searchable_dict[word[0]] = {word}

        return self.searchable_dict


    def insert_word(self, word: str) -> None:
        """Adds new word to set for specific key value in dictionary"""

        if word[0] in self.searchable_dict:
            word = word.lower()

            self.searchable_dict[word[0]].add(word)
        else:
            self.searchable_dict[word[0]] = {word}


    def search_word(self, word: str) -> list:
        """Search for word and returns list of matches starting with word"""

        matched_words = []
        word = word.lower()

        if word[0] in self.searchable_dict:
            matched_words = [
                val for val in self.searchable_dict[word[0]] if val.startswith(word)
            ]

            if not matched_words:
                self.insert_word(word)
                return None
        else:
            self.insert_word(word)
            return None

        return matched_words


if __name__ == "__main__":

    #Tests

    searchable_list = [
        "hello",
        "car",
        "stereo",
        "help",
        "cool",
        "hard",
        "ten"
    ]

    search_one = SearchRecommendation(searchable_list)

    # Test if data from list has been added to searchable dictionary properly
    # print(search_one.searchable_dict)
    print("Passed!" if search_one.searchable_dict["h"] == {"hello", "hard", "help"} else "Failed.")
    print("Passed!" if search_one.searchable_dict["c"] == {'car', 'cool'} else "Failed.")
    print("Passed!" if search_one.searchable_dict["s"] == {'stereo'} else "Failed.")
    print("Passed!" if search_one.searchable_dict["t"] == {'ten'} else "Failed.")
    print("-----------------")


    # Test if searched word returns proper values
    print("Passed!" if search_one.search_word("h").sort() == ["hello", "help", "hard"].sort() else "Failed.")
    print("Passed!" if search_one.search_word("he").sort() == ["hello", "help"].sort() else "Failed.")
    print("Passed!" if search_one.search_word("hell") == ["hello"] else "Failed.")
    print("Passed!" if search_one.search_word("help") == ["help"] else "Failed.")

    # The word "hide" should also be added to set since it does not exist
    print("Passed!" if search_one.search_word("hide") == None else "Failed.")
    print("Passed!" if search_one.search_word("hideout") == None else "Failed.")
    # print(search_one.searchable_dict["h"])
    # Search for the words that were not found before again
    print("Passed!" if search_one.search_word("hide").sort() == ["hide", "hideout"].sort() else "Failed.")

