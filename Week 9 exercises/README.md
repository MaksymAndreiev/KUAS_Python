# Information Processing 1 — Week 9 exercises

## 1. Analysing words, reading input from a text file

### 1.1 Testing whether a word excludes certain letters

Write a function called avoids(word, letters) that returns `True` if word does not contain any of the letters. For
example, avoids("cat", "ct") returns False but avoids("dog", "ct") returns True.

```
print(avoids("cat",	"ct")) # False 
print(avoids("dog",	"ct")) # True 
print(avoids("chimpanzee", "ct")) # False 
print(avoids("elephant",	"ct")) # False 
print(avoids("mongoose",	"ct")) # True
```

Hint: One way to look as this is that the `avoids()` should return `False` as soon as it detects that any one of the
letters occurs in word, and only if there are none then it finally returns True.

### 1.2 Reading input from the user and from a file

Use your `avoids(word, letters)` function to write a program that prompts the user to enter a string of ‘forbidden
letters’ and then prints the number of words in the file words.txt that do *not* contain any of those letters.

Can you find which combination of 5 letters excludes the *smallest* number of words from being counted?

## 2 Selecting words from a file based on various criteria

Practice on a few more example problems that analyse words read from a file.

## 2.1 Testing whether a word includes certain letters

Write a function `uses_only(word, letters)` that returns `True` if word contains *only* the given
letters.

```
print(uses_only("appeal",	"aple")) # True 
print(uses_only("apple",	"aple")) # True 
print(uses_only("apples",	"aple")) # False 
print(uses_only("lapel",	"aple")) # True 
print(uses_only("palpable", "aple")) # False 
print(uses_only("palpable", "abple")) # True
```

Hint: One way to look at this is to return `False` if word contains any letter that is not in letters.

### 2.2 Selecting words that include only certain letters

Use your function uses\_only(word, letters) to write a program that prints all the words in the file `words.txt` that
use *only* these letters: `"acefhlo"`

### 2.3 Selecting words that include all given letters

Write a function called `uses_all(word, letters)`, that returns `True` if word uses *every* letter in

letters at least once.

(It is possible to write `uses_all()` with only one line of code in the body of the function.)

### 2.4 Selecting words that contain all given letters

Use your function `uses_all(word, letters)` to write a program that counts how many words in

`words.txt` use all of these letters: `"aeiou"`.

## 3 Performing more difficult analyses of words

Try to solve two slightly more difficult problems.

### 3.1 Counting monotonic words

Write a function `is_monotonic(word)` that returns `True` if the letters in word are in alphabetical order from left to
right (double letters are OK). For example, `is_monotonic("beefily")` returns `True` but `is_monotonic("beefiness")` returns
`False` (because ‘e’ comes before ‘n’ in the alphabet).

### 3.2 Double letters

A double letter is one which occurs twice, such as ‘oo’ in ‘hoof’. Consecutive double letters are two pairs of double
letters that occur with no other letter in between them. For example, consecutive double letters ‘tt’ and ‘ee’ occur in
the word ‘committee’, but ‘mm’ and ‘tt’ are not consecutive because the letter ‘i’ comes between them.

Write a program to detect and print all the words in the file words.txt which have *three consecutive* double letters.

Hints: You might benefit from a function `is_double(word, position)` that checks for the same letter in word at indexes
`position` and `position+1`. For each word you could then easily check for three consecutive letters from index 0 up to (and
including) the element at index len(word)-6.

## 4 Presenting information visually

A program that prints only text output can display information visually, for example by printing a histogram of results
made from lines of asterisks of different lengths.

### 4.1 Average length of words

Write a program that calculates the average length of the words in the file `words.txt`. Print the result with one decimal
place of precision (one digit after the decimal point).

Hint: The function `round(f, n)` rounds the floating point number f to i decimal places. What is the average length of the
words?

### 4.2 Printing histograms

The following program prints a *histogram* of how many times each letter of the alphabet appears in the
`words.txt` file.

```
for letter in "abcdefghijklmnopqrstuvwxyz": 
    words = open("words.txt")
    count = 0
    for line in words:
        word = line.strip()
        count = count + word.count(letter) 
    if count > 0:
        \# ensure at least one '\*' is printed 
        count = count + 1000
    print(letter, "\*" \* (count // 1000))
```

letter frequencies
```
a \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
b \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
c \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
d \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
e \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
f \*\*\*\*\*\*\*\*\*\*\*\*\*
g \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* h \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
i \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
j \*\*
k \*\*\*\*\*\*\*\*\*\*
l \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
m \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
n \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
o \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
p \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* q \*\*
r \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
s \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
t \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
u \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* v \*\*\*\*\*\*\*\*\*\*
w \*\*\*\*\*\*\*\*\* x \*\*\*
y \*\*\*\*\*\*\*\*\*\*\*\*\*\* 
z \*\*\*\*
```
Modify the program so that it prints a histogram of the *lengths* of the words in `words.txt`. For example, print one line
of asterisks for each of the possible word lengths between 1 and 25 letters, inclusive.

What is the most common word length?

## 5 Challenges

Complete all the challenges before the end of the exercises class to earn a bonus point.

### 5.1 Counting words in a text file

The `readline()` function can be used for more than reading words. It can also read an entire line of text from a file.

Write a program that reads the text file text.txt containing English sentences and counts the number of words in the
entire file. Note that each individual line might contain zero, one, or many words.

Hint: One way to approach this is to inspect each character in the line from left to right, looking for *transitions*
from non-letters to letters. At the start of the line you are in ‘non-letter’ mode. When you see a letter you change
mode from ‘non-letter’ to ‘letter’ and increment the word counter. Continue scanning and if you see a non-letter then
you switch back to ‘non-letter’ mode.

### 5.2 Counting lines, words, and characters

Extend your program from the previous question to count the number of lines, words, and characters in `text.txt` at the
same time. At the end of the program, print all three counts. (If you have macOS or a Linux distribution then you can
compare the output of your program with that of the wc program.)
