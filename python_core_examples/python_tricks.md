# Python Tricks, Gotchas & "Just How Python Works"

This page is a quick-revision reference for Python behaviors that may
look like tricks at first, but are really just useful details about how
Python works.

The goal is not to memorize obscure trivia. These examples are here
because they help explain real Python behavior and can also make useful
interview discussion questions.

------------------------------------------------------------------------

## 1. `bool()` and Truthy / Falsy Values

Python treats some values as `False` and most others as `True`.

``` python
print(bool(""))
print(bool(0))

print(bool("hello"))
print(bool(1))
print(bool(-1))
```

Output:

``` text
False
False
True
True
True
```

### The interesting one

``` python
print(bool("0"))
print(bool(0))
```

Output:

``` text
True
False
```

Why?

``` text
"0"  -> non-empty string -> True
0    -> numeric zero     -> False
```

So Python is not looking at what `"0"` means to a human. It sees a
non-empty string.

------------------------------------------------------------------------

## 2. `repr()` vs Normal `print()`

Consider:

``` python
text = "hello\nworld"

print(text)
print(repr(text))
```

Output:

``` text
hello
world
'hello\nworld'
```

`print(text)` displays the string normally, so the newline takes effect.

`repr(text)` gives a debug-friendly representation that makes the `\n`
visible.

A useful way to remember it:

``` text
repr = representation
```

------------------------------------------------------------------------

## 3. `repr()` vs `!r` in an f-string

These two produce essentially the same representation:

``` python
text = "hello\nworld"

print(repr(text))
print(f"{text!r}")
```

Output:

``` text
'hello\nworld'
'hello\nworld'
```

`!r` tells the f-string to use the object's `repr()` representation.

**Interview/revision question:** Why do these two lines produce the same
output?

------------------------------------------------------------------------

## 4. `.find()` vs `.index()`

Both locate where a substring begins.

``` python
text = "ERROR connection timeout"

print(text.find("connection"))
print(text.index("connection"))
```

Output:

``` text
6
6
```

But they behave differently when the text does not exist.

``` python
print(text.find("warning"))
```

Output:

``` text
-1
```

Whereas:

``` python
print(text.index("warning"))
```

raises:

``` text
ValueError: substring not found
```

Quick reminder:

``` text
find()  -> returns -1 if missing
index() -> raises ValueError if missing
```

------------------------------------------------------------------------

## 5. Method Chaining

Python lets you call one method after another when the result of one
method supports the next method.

``` python
log_line = "ERROR timeout ERROR connection ERROR error"

error_count = log_line.casefold().count("error")

print(error_count)
```

Output:

``` text
4
```

Conceptually:

``` text
original string
    |
    v
casefold()
    |
    v
lowercase string
    |
    v
count("error")
    |
    v
4
```

Another common example:

``` python
hostname = "  PROD-APP-01  "

print(hostname.strip().lower())
```

Output:

``` text
prod-app-01
```

------------------------------------------------------------------------

## 6. Method vs Function

A useful rule of thumb:

``` text
object.method()
function(object)
```

Examples of methods:

``` python
text.strip()
text.lower()
text.find("abc")
text.count("error")
```

Examples of functions:

``` python
len(text)
type(text)
bool(text)
repr(text)
```

The `.` is usually the clue that you are calling a method on an object.

------------------------------------------------------------------------

## 7. `split()` vs `rsplit()`

Consider a container image:

``` python
image = "localhost:5000/team/app:v1.2.3"
```

Using:

``` python
repository, tag = image.split(":", 1)

print(repository)
print(tag)
```

Output:

``` text
localhost
5000/team/app:v1.2.3
```

That is probably not what we wanted.

Using `rsplit()`:

``` python
repository, tag = image.rsplit(":", 1)

print(repository)
print(tag)
```

Output:

``` text
localhost:5000/team/app
v1.2.3
```

Quick reminder:

``` text
split()  -> starts splitting from the left
rsplit() -> starts splitting from the right
```

------------------------------------------------------------------------

## 8. Sequence Unpacking

This:

``` python
image = "myapp:v1.2.3"

repository, tag = image.rsplit(":", 1)
```

works because `rsplit()` returns two strings in a list:

``` python
["myapp", "v1.2.3"]
```

Python assigns them automatically:

``` text
repository -> "myapp"
tag        -> "v1.2.3"
```

Instead of writing:

``` python
parts = image.rsplit(":", 1)

repository = parts[0]
tag = parts[1]
```

Python lets us write:

``` python
repository, tag = image.rsplit(":", 1)
```

------------------------------------------------------------------------

## 9. Reverse a String with Slicing

Strings do not have a `.reverse()` method.

This will not work:

``` python
text.reverse()
```

Instead, Python commonly uses slicing:

``` python
text = "hello"

print(text[::-1])
```

Output:

``` text
olleh
```

Remember the slicing form:

``` text
[start : stop : step]

[::-1]

step = -1 -> move backwards
```

------------------------------------------------------------------------

## 10. Simple Palindrome Check

Because strings can be reversed with slicing, palindrome checking
becomes compact:

``` python
word = "madam"

print(word == word[::-1])
```

Output:

``` text
True
```

Case-insensitive version:

``` python
word = "Madam"

normalized = word.casefold()

print(normalized == normalized[::-1])
```

Output:

``` text
True
```

------------------------------------------------------------------------

## 11. `print()` Adds Spaces Between Arguments

This:

``` python
name = "Vikas"

print("Hello", name, "!")
```

Output:

``` text
Hello Vikas !
```

Why is there a space before `!`?

Because `print()` uses a space as its default separator:

``` python
sep=" "
```

A cleaner solution is usually an f-string:

``` python
print(f"Hello {name}!")
```

Output:

``` text
Hello Vikas!
```

You can also change the separator:

``` python
print("Hello ", name, "!", sep="")
```

Output:

``` text
Hello Vikas!
```

------------------------------------------------------------------------

## 12. `"8080"` Is Not the Same as `8080`

``` python
data1 = "8080"
data2 = 8080

print(type(data1))
print(type(data2))
```

Output:

``` text
<class 'str'>
<class 'int'>
```

They may look similar when printed:

``` python
print(data1)
print(data2)
```

Output:

``` text
8080
8080
```

But Python treats them as different types.

------------------------------------------------------------------------

## 13. String Methods Only Work on Strings

This works:

``` python
data = "8080"

print(data.isdigit())
```

Output:

``` text
True
```

But after:

``` python
data = float(data)
```

`data` is now:

``` text
8080.0
```

and this will fail:

``` python
data.isdigit()
```

because `.isdigit()` is a string method.

Typical error:

``` text
AttributeError: 'float' object has no attribute 'isdigit'
```

Important distinction:

``` text
isdigit()     -> asks about characters inside a string

type()
isinstance()  -> ask what kind of Python value/object something is
```

------------------------------------------------------------------------

## 14. `type()` Output vs Type Comparison

``` python
data = 8080.0

print(type(data))
```

Output:

``` text
<class 'float'>
```

But checking the type can look like:

``` python
if type(data) == float:
    print("data is a float")
```

Output:

``` text
data is a float
```

For now, the simple mental model is:

``` text
<class 'float'> -> Python is telling us the value is a float
```

In normal Python code, `isinstance()` is generally preferred:

``` python
if isinstance(data, float):
    print("data is a float")
```

------------------------------------------------------------------------

## 15. Empty String vs String Containing Spaces

These are not the same:

``` python
text1 = ""
text2 = "   "

print(bool(text1))
print(bool(text2))
```

Output:

``` text
False
True
```

Why?

``` text
""      -> empty string     -> False
"   "   -> non-empty string -> True
```

But:

``` python
print(bool(text2.strip()))
```

Output:

``` text
False
```

Because `.strip()` removes the spaces and produces an empty string.

This combines:

``` text
bool()   -> function
strip()  -> string method
```

------------------------------------------------------------------------

# Quick Interview Revision

``` text
bool("0")              -> True
bool(0)                -> False

repr(text)             -> debug-friendly representation
f"{text!r}"            -> uses repr-style conversion

find("x") missing      -> -1
index("x") missing     -> ValueError

text[::-1]             -> reverse string

split(":", 1)          -> split from left
rsplit(":", 1)         -> split from right

object.method()        -> method
function(object)       -> function

""                     -> False
"   "                  -> True
"   ".strip()          -> ""
bool("   ".strip())    -> False
```

------------------------------------------------------------------------

## Notes

This file should grow naturally as new Python behaviors are encountered.

The goal is:

> **Understand why Python behaves this way, rather than memorize trick
> questions.**
