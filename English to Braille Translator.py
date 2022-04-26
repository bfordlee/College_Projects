braille_dict = {
    'eng_to_braille_1': {' ': ' ', 'a': '. ', 'b': '. ', 'c': '..', 'd': '..', 'e': '. ', 'f': '..', 'g': '..',
                         'h': '. ', 'i': ' .', 'j': ' .', 'k': '. ', 'l': '. ', 'm': '..', 'n': '..', 'o': '. ',
                         'p': '..', 'q': '..', 'r': '. ', 's': ' .', 't': ' .', 'u': '. ', 'v': '. ', 'w': ' .',
                         'x': '..', 'y': '..', 'z': '. '},
    'eng_to_braille_2': {' ': ' ', 'a': '  ', 'b': '. ', 'c': '  ', 'd': ' .', 'e': ' .', 'f': '. ', 'g': '..',
                         'h': '..', 'i': '. ', 'j': '..', 'k': '  ', 'l': '. ', 'm': '  ', 'n': ' .', 'o': ' .',
                         'p': '. ', 'q': '..', 'r': '..', 's': '. ', 't': '..', 'u': '  ', 'v': '. ', 'w': '..',
                         'x': '  ', 'y': ' .', 'z': ' .'},
    'eng_to_braille_3': {' ': ' ', 'a': '  ', 'b': '  ', 'c': '  ', 'd': '  ', 'e': '  ', 'f': '  ', 'g': '  ',
                         'h': '  ', 'i': '  ', 'j': '  ', 'k': '. ', 'l': '. ', 'm': '. ', 'n': '. ', 'o': '. ',
                         'p': '. ', 'q': '. ', 'r': '. ', 's': '. ', 't': '. ', 'u': '..', 'v': '..', 'w': ' .',
                         'x': '..', 'y': '..', 'z': '..'}
}

word = raw_input("Type a word to be translated: ").lower()


def translate(word):
    translation_0 = ""
    translation_1 = ""
    translation_2 = ""
    translation_3 = ""
    for letter in word:
        translation_0 += letter + "   "
        translation_1 += braille_dict['eng_to_braille_1'][letter] + "  "
        translation_2 += braille_dict['eng_to_braille_2'][letter] + "  "
        translation_3 += braille_dict['eng_to_braille_3'][letter] + "  "
    return "\n" + translation_0 + "\n" + translation_1 + "\n" + translation_2 + "\n" + translation_3


print translate(word)