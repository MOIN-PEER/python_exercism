"""
Instructions : Little Sister's Vocabulary

You are helping your younger sister with her English vocabulary homework,
which she is finding very tedious. Her class is learning to create new words by adding prefixes and suffixes.
Given a set of words, the teacher is looking for correctly transformed words with correct spelling by
 adding the prefix to the beginning or the suffix to the ending.

"""

"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return "un" + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    prefix = vocab_words[0]
    prefix_list = [prefix]
    for word in vocab_words[1:]:
        word = prefix + word
        prefix_list.append(word)
    return ' :: '.join(prefix_list)

    # return (" :: " + vocab_words[0]).join(vocab_words)

def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    words=str(word)
    if words.endswith("ness"):
        words=words[:-4]
        if words[-1] == "i":
            words=words.replace(words[-1],"y")
    return words

    # return word[:-4] if word[-5] != 'i' else word[:-5]+'y'


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    words = sentence.split()
    word = words[index].strip(".")
    return word + "en"

print(add_prefix_un("happy"))
# 'unhappy'

print(add_prefix_un("manageable"))
# 'unmanageable'

print(make_word_groups(['en', 'close', 'joy', 'lighten']))
# 'en :: enclose :: enjoy :: enlighten'

print(make_word_groups(['pre', 'serve', 'dispose', 'position']))
# 'pre :: preserve :: predispose :: preposition'

print(remove_suffix_ness("heaviness"))
# 'heavy'

print(remove_suffix_ness("sadness"))
# 'sad'

print(adjective_to_verb('I need to make that bright.', -1 ))
# 'brighten'

print(adjective_to_verb('It got dark as the sun set.', 2))
# 'darken'