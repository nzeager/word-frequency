# Word Frequency

## Momentum Boot Camp Project 7

Skills:

- first python project
- counting the number of times a word is used in a file
- removing any differences based on punctuation or letter case
- removing some common words from the count (ex: a)

## Below are Project Directions

In this project, you will use `open` to read in a text file and calculate the frequency of words in that file.

To calculate the frequency of words, you must:

- remove punctuation
- normalize all words to lowercase
- remove "stop words" -- words used so frequently they are ignored
- go through the file word by word and keep a count of how often each word is used

When your program is complete, you should be able to run 
```
python3 word_frequency.py praise_song_for_the_day.txt
``` 
and get a printed report showing the number of times each word appears in that file, formatted like this:

```
     we | 7 *******
   each | 5 *****
     or | 5 *****
   need | 5 *****
   love | 5 *****
  about | 4 ****
 praise | 4 ****
   song | 4 ****
    day | 3 ***
    our | 3 ***
```

## Starter Files

A starting program is located in `word_frequency.py`. There are also text files that you can use as your input files.

## Resources

- [The `dict` type in Python 3](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
- [f-strings in Python 3](https://realpython.com/python-f-strings/)

### Bibliography

- [Elizabeth Alexander, _Praise Song for the Day_](https://www.poetryfoundation.org/poems/52141/praise-song-for-the-day)
- [Richard Blanco, _One Today_](https://poets.org/poem/one-today)
- [Amanda Gorman, _The Hill We Climb_](https://en.wikipedia.org/wiki/The_Hill_We_Climb)
