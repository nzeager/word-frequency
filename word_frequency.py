import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    # pulls text from file
    with open(file, 'r') as input_file:
        contents = input_file.read()

    # remove punctuation
    contents = contents.translate(
        str.maketrans(string.punctuation, ' '*len(string.punctuation)))

    # make characters lowercase
    contents = contents.lower()

    # remove stop words (not working yet)
    # for word in STOP_WORDS:
    #     contents = contents.replace(word, '')

    # converts text string into list of words
    contents_list = contents.split()

    # create new list without repeating words
    contents_list_no_repeats = []
    for word in contents_list:
        if contents_list_no_repeats.count(word) == 0:
            contents_list_no_repeats.append(word)

    # create new list with counts for each word
    counts = []
    for word in contents_list_no_repeats:
        counts.append(contents_list.count(word))

    # combine the non-repeating words with the counts into a list of sublists with each word and corresponding count
    contents_with_counts = []
    for i in range(len(counts)):
        contents_with_counts.append([contents_list_no_repeats[i], counts[i]])

    # sort contents_with_counts in descending order by the second element in each sublist
    contents_with_counts.sort(key=lambda x: x[1], reverse=True)
    print(contents_with_counts)


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
