def sponge_case(sentence):
    new_sentence = sentence.split(" ")
    sponge_sentence = []

    for word in new_sentence:
        sponge_sentence.append(sponge_single_word(word))

    return " ".join(sponge_sentence)

def sponge_single_word(word):
    new_word = []
    index = 0

    for letter in word:
        if index == 0:
            new_word.append(letter.lower())
        elif index == 1:
            new_word.append(letter.upper())
        elif index >= 2 and index % 2 == 0:
            new_word.append(letter.lower())
        else:
            new_word.append(letter.upper())
        index += 1

    return "".join(new_word)

# Test cases
assert sponge_case("spongebob") == "sPoNgEbOb"
assert sponge_case("Who are YOU calling A Pinhead") == "wHo aRe yOu cAlLiNg a pInHeAd"
assert sponge_case("WHAT is UP my dude") == "wHaT iS uP mY dUdE"
assert sponge_case("E") == "e"
assert sponge_case("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")