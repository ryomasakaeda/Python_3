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

## 6. Lists

  * Write elements inside square brackets `[]`

```python
cheeses = ['cheddar', 'stilton', 'brie']
primes = [2, 3, 5, 7, 11]
```

  * Length of list

```python
print(len(cheeses))  # 3
print(len(primes))   # 5
```

  * Elements and slices

```python
print(primes[2])     # 5
print(primes[-1])    # 11
print(cheeses[0:2])  # ['cheddar', 'stilton']
```

  * Loop

```python
for prime in primes:
    print(prime)
```

  * Adding

```python
primes = [2, 3, 5, 7, 11]
primes.append(13)   
print(primes)  # [2, 3, 5, 7, 11, 13]
```

  * Removing

```python
# Remove the first element 5
primes = [2, 3, 5, 7, 11]
primes.remove(5)    
print(primes)  # [2, 3, 7, 11]

primes = [2, 3, 5, 5, 7, 11]
primes.remove(5)    
print(primes)  # [2, 3, 5, 7, 11]

# Remove the element of specified index
primes = [2, 3, 5, 7, 11]
a = primes.pop(1)  # pop the 1st element
print(a)       # 3
print(primes)  # [2, 5, 7, 11]
```

  * Sorting

```python
# Method 1:
primes = [3, 2, 5, 11, 7]
primes.sort()  # sort
print(primes)  # [2, 3, 5, 7, 11]

# Method 2:
primes = [3, 2, 5, 11, 7]
p = sorted(primes)       
print(p)       # [2, 3, 5, 7, 11]
print(primes)  # [3, 2, 5, 11, 7]
```

  * Concatenating

```python
prime1 = [2, 3, 5]
prime2 = [7, 11]
p = prime1 + prime2
print(p)  # [2, 3, 5, 7, 11]
```

  * Search

```python
# Test the exisitence
print('Chico' in ['Groucho', 'Chico', 'Harpo', 'Zeppo'])    # True
print('Gummo' in ['Groucho', 'Chico', 'Harpo', 'Zeppo'])    # False

# Get the index
primes = [2, 3, 5, 7, 11]
a = primes.index(5)
print(a)            # 2

* Replacement

primes = [2, 3, 5, 7, 11]
primes[2] = 6
print(primes)       # [2, 3, 6, 7, 11]
```

  * Range to list

```python
list(range(5))      # [0, 1, 2, 3, 4]
```

  * Example: command-line arguments

    - Command-line arguments stored in sys.argv
    - Start with `import sys`

```python
import sys

# python program.py lancelot arthur bedivere

for arg in sys.argv:
    print(arg)
```


  * WARNING: `a = b` does not copy a list, it makes a reference to it.
    Lists can be deep copied with `a = b[:]`

```python
a = [1, 2, 3]
b = a
b[2] = 4
print(b)
print(a)  # <-- :o
```

### Exercise

  * e1. Copy a list using a loop
  * e2. Make a list which contains even numbers between 1 to 30.
      Next, replace the numbers that are multiples of 3 with 0.
  * e3. Write a program to give the nth day of the week, for a command-line argument n.
    - e.g. `python program.py 3  # ==> Wednesday`
    - e.g. `python program.py 5  # ==> Friday`

## 7. Strings

  * Attach `'` or `"` at the first and the end

```python
string = 'baseball'     # "baseball" is same
print(string)
```

  * Length of string

```python
print(len('baseball'))  # 8
```

  * Elements and slices

```python
string = 'baseball'
print(string[0])      # 'b'
print(string[-1])     # 'l'
print(string[0:4])    # 'base' (equal to string[:4])
print(string[4:4])    # ''
print(string[4:5])    # 'b'
print(string[4:8])    # 'ball' (equal to string[4:])
print(string[0:8:2])  # 'bsbl' (equal to string[::2])
print(string[::-1])   # 'llabesab'
```

  * Concatenate

```python
print('more' + ' ' + 'spam')  # 'more spam'
print('spam'*3)               # 'spamspamspam'
```

  * String to List,  List to String

```python
string = 'swallow rabbit tiger'
print(string.split())    # ['swallow', 'rabbit', 'tiger']

string = 'swallow,rabbit,tiger'
print(string.split(','))    # ['swallow', 'rabbit', 'tiger']

print('/'.join(['swallow', 'rabbit', 'tiger'])) # 'swallow/rabbit/tiger'
```

### Exercises

  * e4. 'Yakult'と'Swallows'のそれぞれの冒頭の文字列を抜き出し結合せよ.
  * e5. 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．(100本ノック 問題00)
  * e6. 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．(100本ノック 問題01)
  * e7. 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．(100本ノック 問題02,  ヒント: zip関数, python_tips.txt参照)
  * e8. "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
      という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
      それ以外の単語は先頭に2文字を取り出し，取り出した文字列を結合せよ．(100本ノック 問題04改)

## 8. Dictionaries

  * Basically a hash table (key-value pairs).
    Write elements inside curly brackets `{}`.

```python
freq = {'hovercraft': 1, 'eel': 100}
freq['hole'] = 7
print(freq['eel'])
print(freq['hole'])
```

  * Be careful of non-defined keys

```python
# Don't do this
print(freq['milkman'])

# Do this
if 'milkman' in freq:
    print(freq['milkman'])

# Or you can use defaultdict
from collections import defaultdict
freq = defaultdict(int)
print(freq['milkman'])  # <-- 0
```

  * Loops

```python
foo = {0:'zero', 1:'one', 2:'two'}
# Method 1
for key in foo:
    print(key, foo[key])
# Method 2
for key, value in foo.items():
    print(key, value)

# Sorted by key
for key in sorted(foo):
    print(key, foo[key])
```

### Exercises

  * e9. 'yakultswallows'に含まれる文字種とその数を列挙せよ.  (e.g. 'y'-->1, 's'-->2, ..)
  * e10. Count the frequency of all words in a given list (e.g. ['eggs', 'spam', 'spam', 'bacon'])
      and store in a dictionary. Now output all parirs of word and its frequency. (see python_tips.txt)
  * e11. Implement a simple substitution cipher that encrypts then decrypts a string.
        e.g. a->c, b->z, c->q, ...

## 9. Functions

  * Function definition

```python
def print_hello():
    print("hello")

def add(a, b):
    return a + b
```

  * Function call

```python
print_hello()
x = add(1, 2)
```

  * Optional arguments

```python
def add_opt(a, b=1, c=2):
    return a + b + c

print(add_opt(3)) # => 6
print(add_opt(3, 0)) # => 5
print(add_opt(3, 4, 5)) # => 12
print(add_opt(3, c=4)) # => 8
print(add_opt(b=3, a=2, c=1)) # => 6

# This causes an error
# print(add_opt(b=3, 2))
```

  * Functions can be called recursively

A program to calculate a factorial.

```
def fact(n, a=1):
    if n == 0: return a
    return fact(n-1, n*a)
```

```
fact(4, 1)
  fact(3, 4)
    fact(2, 12)
      fact(1, 24)
        fact(0, 24)
        => a の値 24 を返す
      => 24
    => 24
  => 24
=> 24
```

  * Functions can return multiple values (separate with commas)

```python
def four_arithmetic_operations(a,b):
  return a+b, a-b, a*b, a/b

a, b, c, d = four_arithmetic_operations(2,3)
```

---

## Homework

  1. 3つの数字を受け取り、その中の最大の値を返す関数を実装せよ.
  2. 数字の入った配列を受け取り、その中の最大の値とその添字 (インデックス)を返す関数を実装せよ.
  3. 配列の先頭はそのままに、先頭以外の要素をすべて0に置き換えよ.
     - ex. [3, 5, 2, 4, 2] --> [3, 0, 0, 0, 0]
  4. フィボナッチ数列とは、次のような数列である. 1 1 2 3 5 8 13 21 34 55 89 144 ...
     - 4-1. フィボナッチ数列の第n項を求めるプログラムを再帰呼出しを用いて実装せよ. ただしnはコマンドライン引数で得るものとする.
     - 4-2. フィボナッチ数列の第n項を求めるプログラムを再帰呼出しを用いずに実装せよ. ただしnはコマンドライン引数で得るものとする.
     - 4-3. 再帰呼出しを用いた場合と用いない場合、どちらがどのような点で優れているかを考察せよ.
  5. ユークリッドの互除法を用いて、2つの自然数を受け取りその最大公約数を返す関数を作成せよ．
  6. エラトステネスの篩を用いて、10000までの素数を全て求めよ．
     また、前回の課題で求めた方法と実行速度を比較せよ．
     - ヒント1: 実行速度の比較の仕方
```
import time
t0 = time.clock()   # 処理前の時刻(t0)を取得
time.sleep(3)       # 計測したい処理
t1 = time.clock()   # 処理後の時刻(t1)を取得
print("dt="+str(t1-t0)+"[s]")   # 処理後の時刻(t1)-処理前の時刻(t0)で処理時間を計算
```
     - ヒント2: 平方根の求め方
```
import math
sqrt_num = math.sqrt(num)
```
  7. バブルソート、クイックソート、マージソートを実装せよ.
  8. チェス盤(8×8)に、8つのクイーンを互いに取り合わないように置ける場合が何通りあるか計算せよ．ただしチェスにおけるクイーンは、タテ・ヨコ・ナナメのラインに動くことができる．
