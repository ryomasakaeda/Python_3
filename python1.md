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

## 1. The Very Basics

  * Check you are using the correct version of Python with `$ which python3`.
  * Check the version.
    - `$ python3 --version`
  * Interactive shell: `$ python3`
    - Type `print('Hello, World!')`, and enter.
    - To quit, type Ctrl-D.
  * Run code:
    - `$ echo "print('Hello, World!')" > program.py`
    - `$ python3 program.py`
  * Comments:
    - Text after '#' is ignored.
      - `# This is a comment`
      - `print("hi") # comment`

  * Print function
    - `print("aaa") # -> aaa\n`
    - `print("aaa", end="") # -> aaa`
    - `print("aaa", "bbb") # -> aaa bbb\n`
    - `print("aaa", "bbb", sep=",") # -> aaa,bbb\n`
    - `print("aaa", "bbb", sep=",", end="") # -> aaa,bbb`

### Exercise

  * e1. Write and run a program to output your name.
  * e2. Add a comment to explain the purpose of the program.

## 2. Variables

  * Plain types: integer, float, string
    - `a = 1       # integer`
    - `b = 2.7     # float`
    - `c = "spam"  # string`
    - `d = 'spam'  # string`

```python
message = "eggs!"
print(message)

value = 1.3 - 2.9
print(value)
```

## 3. Operators

  * Operators

    - `7 + 2   # add (=9)`
    - `7 - 2   # subtract (=5)`
    - `7 * 2   # multiply (=14)`
    - `7 / 2   # divide (quotient) (=3.5)`
    - `7 % 2   # divide (remainder) (=1)`
    - `7 ** 2  # exponential (=49)`

  * String Concatination

    - `"more" + " spam"  # (="more spam")`

  * Comparison

    - `3 == 2  # equal (=False)   <-- not '='`
    - `3 != 2  # non-equal (=True)`
    - `3 > 2   # greater than (=True)`
    - `3 < 2   # less than (=False)`
    - `3 >= 2  # greater than or equal (=True)`
    - `3 <= 2  # less than or equal (=False)`

### Exercise

  * e3. Output your name by joining your first and last names.
  * e4. Calculate 5 to the power of 4.
  * e5. Calculate 1 divided by 4
  * e6. What happens when you try to divide by zero?

## 4. Operators (Part 2)

  * Abbreviations
    - `var += 10   # var = var + 10`
    - `var -= 10   # var = var - 10`
    - `var *= 10   # var = var * 10`
    - etc.

  * Logic operators and boolean constants
    - `x and y   # and`
    - `x or y    # or`
    - `not x     # not`
    - `True      # = 1`
    - `False     # = 0`

  * [Advanced] Bitwise operators
    - `x & y   # and`
    - `x | y   # or`
    - `x ^ y   # xor`

### Exercise

  * e7. What should the result be of this code? Check it.

    - a) `not (1 == 1)`
    - b) `2 == 1 + 1`
    - c) `0.9 - 0.6 == 0.3`
    - d) `True or True and False`

## 5. Control Statements

Conditionals: if, else, elif ('else if')

  * Conditional ends in ':'
  * Must indent correctly (4 spaces, do not use tabs)
  * Brackets not needed in Python (c.f. Perl, C)

```python
if a == 1:
    print("a is 1")
```

```python
if condition1:
    # do something
elif condition2:
    # do something
else:
    # do something
```

While loop

```python
# While var is less than 10, output var
var = 0
while var < 10:
  print(var)
  var += 1
```

```python
# Infinite loop
print("Have you in fact got any cheese here at all?")
while True:
    print("No.")
```

For loop

```python
# 0 1 2 3 4
for i in range(5):
    print(i)
```

```python
# 2 3 4 5 6 7
for i in range(2, 8):
    print(i)
```

```python
# 2 4 6
for i in range(2, 8, 2):
    print(i)
```

Break and continue

- continue: skip remainder of iteration
- break: end loop

```python
# What does this do?
var = 0
while True:
    var += 1
    if var == 10:
        break
    if var % 2 == 1:
        continue
    print(var)
```

---

## Homework

  1. 1から30までの整数を出力せよ.
  2. 1から30までに現れる偶数を出力せよ.
  3. 1から30までに現れる偶数の和を計算せよ.
  4. 10! (10の階乗) を計算せよ.
  5. 九九の表を作成せよ.
  6. 1から30までの数で、その数が3で割り切れるなら”Fizz”、5で割り切れるなら”Buzz”、
     両方で割り切れるなら”FizzBuzz”、それ以外ならばその数を表示せよ。
     (1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, ...)
  7. 1000までの素数を全て出力せよ.
