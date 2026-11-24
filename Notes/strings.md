# Strings

- Just a sequence of characters.
- surrounded by single or double quotes.
- multiline string uses """ or '''

```
my_str_3 = """Multiline
string"""
my_str_4 = '''Another
multiline
string'''
```

- if string also contains single or double quotes, then two options
  - use opposite kid of quotes.

  ```
  msg = "It's a sunny day"
  quote = 'She said, "Hello World!"'
  ```

  - or use escape character - backslash ( \\ )

  ```
  msg = 'It\'s a sunny day'
  quote = "She said, \"Hello!\""
  ```

  - Backslash can also be combined with other characters
    - `\n` for new line
    - `\t` for tab
    - `\\` a single backslash

- to check if string contains some characters.
  - use `in` operator.
  - returns boolean whether exists or not.
  ```
  string = 'Hello world'
  print('Hello' in string) # True
  print('f' in string) # False
  ```
- length of string using `len()` function
  ```
  string = 'Hello'
  print(len(string)) # 5
  ```
- every character in a string has a position called index.
  - index is zero based.
  - starts with 0
  - increases by 1 for each char
  - to access char use `[]` with index in it. - `[0]` for first letter - `[-1]` for last letter.

## Mutable vs immutable

- variables can be mutable or immutable.
- mutable - value can be changed after it is created.
- pointing to new variable is possible.
  ```
  greeting = 'hi'
  greeting = 'hello'
  print(greeting) # hello
  ```
- but direct modification is not allowed.
  ```
  greeting = 'hi'
  greeting[0] = "H" # TypError
  ```
- Integers, floats and boolean are also immutable.
