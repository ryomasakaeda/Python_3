# Introduction to Python

  - Kurohashi-Kawahara Lab
  - Author: John Richardson (john@), Yuta Hayashibe (yuta-h@)
  - Based on [Perl version](http://nlp.ist.i.kyoto-u.ac.jp/local/misc/perl-lec-2012-1.txt)

## 0. Contents

   1. The Very Basics
   2. Variables
   3. Operators
   4. Operators (part 2)
   5. Control Statements
   6. Lists
   7. Strings
   8. Dictionaries
   9. Functions
  10. Format
  11. File I/O
  12. Regular Expressions (regex)
  13. Type Hints

---

## 10. Format

### Basic

```python
print("My name is {0}.".format("Hikaru"))   # 'My name is Hikaru.'
print("My name is {0}. Hello {1}.".format("Hikaru", "Ayumi"))   # 'My name is Hikaru. Hello Ayumi.'

print("My name is {person1}. Hello {person2}.".format(person1="Hikaru", person2="Ayumi"))   # 'My name is Hikaru. Hello Ayumi.'
```

### Form

```python
print("{0:.3f}".format(12.34))      # '12.340'
print("{0:0>6}".format(123))        # '000123'
```

### Exercise

- 半径3.5cmの円の面積を求め、小数点以下2桁まで出力せよ (ヒント: 冒頭でimport math をした後、math.piを円周率として利用)

## 11. File I/O

### Basic

Read file

```python
with open(filename) as my_file:
    for line in my_file:
        # .strip() removes newlines and trailing whitespace
        print(line.strip())
        # .split() splits string (on some character) into list
        print(line.strip().split(','))
```

Write to file

```python
with open(filename, 'w') as my_file:
    # '\n' is a newline character
    my_file.write("He's pushing up the daisies.\n")
```

Write to stderr

```python
import sys
print("Error: He's pining for the fjords.", file=sys.stderr)

for i in range(9999999999):
    if i % 10000 == 0:
        print("{0:15d}".format(i), file=sys.stderr)
```

### Unicode/UTF-8

- What is the difference? Look it up if you don't know!
- *Internal processing should always be Unicode*
    - Immediate after getting ``byte``, convert ``string``
    - Immediate before output to files, convert ``string``

```python
# codes are written in Unicode (string type)
foo = '大学'
assert isinstance(foo, str)
assert len(foo) == 2
print(foo)

bar = '大学'.encode('utf8')
assert isinstance(bar, bytes)
assert bar ==  '大学'
assert len(bar) == 6
print(bar)

baz = bar.decode('utf8')
assert isinstance(baz, str)
```

### Exercise

- Implement 'cp'
- UTF-8/Unicode practice:
    - Read a Japanese sentence from a UTF-8 file and convert to Unicode
    - Split the Unicode sentence into characters, separated by whitespace
    - Output the split sentence to a file (UTF-8) and check it is UTF-8 (use the 'file' command)
- Output the POS for each line of JUMAN input


## 12. Regular Expressions

Simple pattern matching in Python:

```python
"ni" in "knights"        # <-- True
"ni" not in "knights"    # <-- False
"test".startswith("te")  # <-- True
"test".endswith("ts")    # <-- False
```

Use regex to match more complicated patterns. ([reference](http://docs.python.jp/2/library/re.html))

```python
# Use regex library
import re

# Does string match (entirely) pattern?
re.match(pattern, string)

# Does string contain pattern?
re.search(pattern, string)

# Replace pattern with replace in string
re.sub(pattern, replace, string)
```

Regex syntax

```
^    Start of sentence
$    End of sentence
.    Wildcard (any character)
       e.g. ....shima ==> Takashima, Hiroshima, ...
*    Repeat 0+ times
       e.g. a* ==> b, a, aa
+    Repeat 1+ times
       e.g. a+ ==> a, aa
\d   Digit (0-9)
\D   Non-digit
\w   A-Za-z0-9_
\W   Not the above
\s   Space, tab, newline
\S   Not the above
```

Simple examples

```python
# Note: prefix regex with 'r', e.g. r'[0-9]'

# Result: "The KNIghts who say 'NI'."
print(re.sub(r"ni", r"NI", "The knights who say 'ni'.")):

# Result: (no output)
if re.match(r"F.*", "One! Two! Five!"):
    print("Three, sir!")

# Result: "Three, sir!"
if re.search(r"F.*", "One! Two! Five!"):
    print("Three, sir!")
```

Escaping symbols

- Use ``\`` to escape special symbols, e.g. brackets (``[`` -> ``\[``).
- Use ``\\`` to escape ``\``.

Matched groups

- Entire match can be displayed with ``.group(0)``.

```python
print(re.match(pattern, string).group(0))
```

Partial matches can be defined by using ``()``. They can then be referenced with ``\1, \2, ...``  in a replace regex, or ``.group(1), .group(2), ...,`` in a match.

```python
print(re.sub(r"the (\d*) knights", r"\1", "the 12 knights"))
# --> 12

print(re.sub(r"the (\d*) and (\d*) knights", r"\1 + \2", "the 6 and 20 knights"))
# --> 6 + 20
```

Greedy matching

- Regex is normally greedy (returns longest match)
- Use ``?`` to return shortest match

```python
print(re.match(r"<.*>", "<tag>val</tag>").group(0))
# --> <tag>val</tag>
print(re.match(r"<.*?>", "<tag>val</tag>").group(0))
# --> <tag>
```

Tokenization

```python
print(re.split(r",","banana,orange,mikan,apple"))
# --> ['banana', 'orange', 'mikan', 'apple']

for w in re.split(r"，", "バナナ，オレンジ、みかん,リンゴ"):
    print(w)
# --> バナナ
# --> オレンジ、みかん,リンゴ

for w in re.split(r"[，,、]", "バナナ，オレンジ、みかん,リンゴ"):
    print(w)
# --> バナナ
# --> オレンジ
# --> みかん
# --> リンゴ
```

### Exercise

- check if a string is empty with and without a regex
- Double all vowels in some input string with and without a regex
    - e.g. Sir Robin -> Siir Roobiin


## 13. Type Hints

We can specify a type of variable or function for readability.

Annotate to variable:
```python
s: str = '十一月同窓会'  # specify "s" is a string variable
l: int = len(s)
even: bool = (l % 2 == 0)
```

Annotate to function:
```python
def repeat(s: str, n: int) -> str:
    return s * n

rep: str = repeat(s, 3)         # 十一月同窓会十一月同窓会十一月同窓会
rrep: str = repeat(s[::-1], 3)  # 会窓同月一十会窓同月一十会窓同月一十
```

Various types:
```python
from typing import List, Dict, Tuple, Optional

lst: List[int] = [3, 4, 5]                             # list of integer
dct: Dict[int, str] = {3: 'san', 4: 'yon', 5: 'go'}    # integer to string dictionary
tpl: Tuple[int, float, str] = (3, 4.0, 'five')         # tuple of integer, float and string
opt: Optional[int] = lst[0] if len(lst) > 0 else None  # integer or NoneType
nst: List[List[int]] = [[0], [1, 2], [3, 4, 5]]        # nest

class Foo:
    def __init__(self, n: int) -> None:
        self.n: int = n

usr: List[Foo] = [Foo(3), Foo(4), Foo(5)]  # user-defined type
```

Reference

- https://docs.python.org/3/library/typing.html (English)
- https://docs.python.org/ja/3/library/typing.html (日本語)


---


## Homework

- Build a bigram language model using the following file: ``/share/text/WWW.en/txt.en/tsubame00/doc0000000000.txt.gz``
- Then write a function to estimate the probability of the sentence: ``The man is in the house.``
    - Hints
        - Ignore all lines starting with ``<PAGE URL=...>`` or ``</PAGE>``
        - Fill a dictionary with the frequencies of all unigrams and bigrams
        - ``P(a b) ~= P(a) * P(b | a) = [freq(a) / freq(*)] * [freq(a b) / freq(a)]``

Submit by email to TA by 5pm the *day before* the next lesson.
