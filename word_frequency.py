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

    # removes punctuation
    contents = remove_punc(contents)

    # converts text string into list of words
    contents_list = contents.split()

    # creates new list without repeating words
    contents_list_no_repeats = no_repeat(contents_list)

    # removes stop words
    for word in STOP_WORDS:
        if contents_list_no_repeats.count(word) == 1:
            contents_list_no_repeats.remove(word)

    # creates new list with counts for each word
    counts = []
    for word in contents_list_no_repeats:
        counts.append(contents_list.count(word))

    # creates new list with * representations of counts
    astr = []
    for count in counts:
        astr.append('*' * count)

    # combines the non-repeating words, counts
    # and * representations into a list of sublists
    # with each sublist containing corresponding values
    # then sorts the list by counts
    contents_with_counts = combine(contents_list_no_repeats, counts, astr)

    # finds character length of longest word
    length = len(max(contents_list_no_repeats, key=len))

    # prints out results
    for wordpair in contents_with_counts:
        print(f'{wordpair[0].rjust(length)} | {wordpair[1]} {wordpair[2]}')


# function removes punctuation
def remove_punc(cont_string):
    punc = string.punctuation
    punc = punc.replace('-', '')
    return cont_string.translate(
        str.maketrans(punc, ' '*len(punc)))


# function creates new list without repeating words
def no_repeat(list):
    list_no_repeats = []
    for word in list:
        if list_no_repeats.count(word) == 0:
            list_no_repeats.append(word)
    return list_no_repeats


def combine(list1, list2, list3):
    # combines the three lists
    combo = []
    for i in range(len(list2)):
        combo.append(
            [list1[i], list2[i], list3[i]])

    # sorts lists by the second entry
    combo.sort(key=lambda x: x[1], reverse=True)
    return combo


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
