
class SearchRecommendation():
    """Recommends words based on searched word"""

    searchable_dict = {}  # To hold sets of words searchable by alphabet letter


    def __init__(self, searchable_list) -> None:
        self.searchable_list = searchable_list
        self.create_searchable_object()


    def create_searchable_object(self) -> dict:
        """Adds list data to dictionary of sets for key alphabet letter search"""

        for word in self.data_list:
            if word[0] in self.searchable_dict:
                self.searchable_dict[word[0]].add(word)
            else:
                self.searchable_dict[word[0]] = {word}

        return self.searchable_dict


    def insert_word(self, word: str) -> None:
        """Adds new word to set for specific key value in dictionary"""

        if word[0] in self.searchable_dict:
            self.searchable_dict[word[0]].add(word)
        else:
            self.searchable_dict[word[0]] = {word}
    








if __name__ == "__main__":

    searchable_list = [
        "hello",
        "car",
        "stereo",
        "help",
        "cool",
        "hard",
        "ten"
    ]