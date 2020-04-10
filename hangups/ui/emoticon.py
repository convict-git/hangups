"""Hangouts emoticon to emoji converter."""


def replace_emoticons(string):
    """Replace emoticon words in string with corresponding emoji."""
    return _replace_words(HANGOUTS_EMOTICONS_TO_EMOJI, string)


def _replace_words(replacements, string):
    """Replace words with corresponding values in replacements dict.

    Words must be separated by spaces or newlines.
    """
    output_lines = []
    for line in string.split('\n'):
        output_words = []
        for word in line.split(' '):
            new_word = replacements.get(word, word)
            output_words.append(new_word)
        output_lines.append(output_words)
    return '\n'.join(' '.join(output_words) for output_words in output_lines)


# Emoticon conversions extracted from hangouts.google.com
HANGOUTS_EMOTICONS_TO_EMOJI = {
        ":)": "\xF0\x9F\x98\x81",
        ":-)": "\xF0\x9F\x98\x81",
        "<3": "\xF0\x9F\x92\x93",
        "-<@%": "\U0001f41d",
        ":(|)": "\U0001f435",
        ":(:)": "\U0001f437",
        "(y)": "\U0001f44d",
        "(Y)": "\U0001f44d",
        "(n)": "\U0001f44e",
        "(N)": "\U0001f44e",
        "(]:{": "\U0001f473",
        "<\\3": "\U0001f494",
        "</3": "\U0001f494",
        "~@~": "\U0001f4a9",
        ":D": "\U0001f600",
        ":-D": "\U0001f600",
        "^_^": "\xF0\x9F\x98\x81",
        ":''D": "\xF0\x9F\x98\x82",
        "=D": "\xF0\x9F\x98\x84",
        "^_^;;": "\xF0\x9F\x98\x85",
        "O:)": "\U0001f607",
        "O=)": "\U0001f607",
        "O:-)": "\U0001f607",
        "}:-)": "\U0001f608",
        "}=)": "\U0001f608",
        "}:)": "\U0001f608",
        ";-)": "\xF0\x9F\x98\x89",
        ";)": "\xF0\x9F\x98\x89",
        "=)": "\xF0\x9F\x98\x8A",
        "B-)": "\U0001f60e",
        ":,": "\xF0\x9F\x98\x8F",
        ":-,": "\xF0\x9F\x98\x8F",
        "=|": "\U0001f610",
        ":-|": "\U0001f610",
        ":|": "\U0001f610",
        "-_-": "\U0001f611",
        "o_o;": "\xF0\x9F\x98\x93",
        "u_u": "\xF0\x9F\x98\x94",
        "=\\": "\U0001f615",
        ":-\\": "\U0001f615",
        ":-/": "\U0001f615",
        ":\\": "\U0001f615",
        ":/": "\U0001f615",
        "=/": "\U0001f615",
        ":-s": "\xF0\x9F\x98\x96",
        ":-S": "\xF0\x9F\x98\x96",
        ":S": "\xF0\x9F\x98\x96",
        ":s": "\xF0\x9F\x98\x96",
        ":*": "\U0001f617",
        ":-*": "\U0001f617",
        ";-*": "\xF0\x9F\x98\x98",
        ";*": "\xF0\x9F\x98\x98",
        "=*": "\xF0\x9F\x98\x9A",
        ":-P": "\U0001f61b",
        ":p": "\U0001f61b",
        ":-p": "\U0001f61b",
        ":P": "\U0001f61b",
        "=P": "\U0001f61b",
        "=p": "\U0001f61b",
        ";p": "\xF0\x9F\x98\x9C",
        ";P": "\xF0\x9F\x98\x9C",
        ";-p": "\xF0\x9F\x98\x9C",
        ";-P": "\xF0\x9F\x98\x9C",
        "=(": "\xF0\x9F\x98\x9E",
        ":-(": "\xF0\x9F\x98\x9E",
        ">.<": "\xF0\x9F\x98\xA1",
        ">=(": "\xF0\x9F\x98\xA1",
        ">:(": "\xF0\x9F\x98\xA1",
        ">:-(": "\xF0\x9F\x98\xA1",
        ";_;": "\xF0\x9F\x98\xA2",
        "='(": "\xF0\x9F\x98\xA2",
        "T_T": "\xF0\x9F\x98\xA2",
        ":'(": "\xF0\x9F\x98\xA2",
        ">_<": "\xF0\x9F\x98\xA3",
        "D:": "\U0001f626",
        ":""(": "\xF0\x9F\x98\xAD",
        ":o": "\U0001f62e",
        ":-o": "\U0001f62e",
        ":-O": "\U0001f62e",
        "=O": "\U0001f62e",
        ":O": "\U0001f62e",
        "o.o": "\U0001f62e",
        "=o": "\U0001f62e",
        "O.O": "\xF0\x9F\x98\xB2",
        "X-O": "\xF0\x9F\x98\xB5",
        "x_x": "\xF0\x9F\x98\xB5",
        "X(": "\xF0\x9F\x98\xB5",
        "X-o": "\xF0\x9F\x98\xB5",
        "X-(": "\xF0\x9F\x98\xB5",
        ":X)": "\xF0\x9F\x98\xB8",
        "(=^..^=)": "\xF0\x9F\x98\xB8",
        ":3": "\xF0\x9F\x98\xB8",
        "=^_^=": "\xF0\x9F\x98\xB8",
        "(=^.^=)": "\xF0\x9F\x98\xB8",
        "!:)": "\U0001f643",
        "!:-)": "\U0001f643",
        ">:(X": "\xF0\x9F\x99\x85",
        "o/": "\xF0\x9F\x99\x8B",
        "\\o": "\xF0\x9F\x99\x8B",
        ":)X": "\U0001f917",
        ">:D<": "\U0001f917",
        ":-)X": "\U0001f917",
        "\\m/": "\U0001f918",
        "V.v.V": "\U0001f980",
}
