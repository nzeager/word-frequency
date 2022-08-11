import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by',
    'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    # pulls text from file and makes it lowercase
    with open(file, 'r') as input_file:
        contents = input_file.read().lower()

    # remove punctuation
    punc = string.punctuation
    punc = punc.replace('-', '')
    contents = contents.translate(
        # str.maketrans(string.punctuation, ' '*len(string.punctuation)))
        str.maketrans(punc, ' '*len(punc)))

    # converts text string into list of words
    contents_list = contents.split()

    # create new list without repeating words
    contents_list_no_repeats = []
    for word in contents_list:
        if contents_list_no_repeats.count(word) == 0:
            contents_list_no_repeats.append(word)

    # remove stop words
    for word in STOP_WORDS:
        if contents_list_no_repeats.count(word) == 1:
            contents_list_no_repeats.remove(word)

    # create new list with counts for each word
    counts = []
    for word in contents_list_no_repeats:
        counts.append(contents_list.count(word))

    # create new list with * representations of counts
    astr = []
    for count in counts:
        astr_disp = ''
        round = 0
        while round < count:
            astr_disp += '*'
            round += 1
        astr.append(astr_disp)

    # combine the non-repeating words with counts
    # and * representations into a list of sublists
    # with each sublist containing corresponding values
    contents_with_counts = []
    for i in range(len(counts)):
        contents_with_counts.append(
            [contents_list_no_repeats[i], counts[i], astr[i]])

    # sort contents_with_counts in descending order
    # by the second element in each sublist
    contents_with_counts.sort(key=lambda x: x[1], reverse=True)

    # find character length of longest word
    length = 0
    for word in contents_list_no_repeats:
        if len(word) > length:
            length = len(word)

    # print out results
    for wordpair in contents_with_counts:
        print(f'{wordpair[0] : >10} | {wordpair[1]} {wordpair[2]}')


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
