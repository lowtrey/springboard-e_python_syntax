def print_upper_words(words, must_start_with):
    """For a list of words, print out each word on a separate line.
    - Words should be in all uppercase. 
    """

    for word in words:
        for letter in must_start_with:
            if word.lower().startswith(letter):
                print(word.upper())


print(print_upper_words(["hello", "hey", "goodbye", "yo", "yes", "eating", "zoo"],
                        must_start_with={"h", "y", "z"}))
