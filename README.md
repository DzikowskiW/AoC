# Advent of Code

## Disclaimer
This repo is a collection of my [Advent of Code](https://adventofcode.com) solutions. Some of them are polished, but some are just a dump of messy code that produced a correct solution. 

## Notes
Lately I find Python to be the best language to efficiently do the job. Besides Advent of Code I rarely if ever use Python over the year, so as I write this I am starting to document what I should remember before staring next year's Advent of Code

### Resources
1. Advent of Code [subreddit](https://www.reddit.com/r/adventofcode/) 
2. Jonathan Paulson [Youtube channel](https://www.youtube.com/@jonathanpaulson5053) - screecasts of solving tasks in Python by a profficient dev 
3. Eric Wastl [Twitter](https://twitter.com/ericwastl) - Twitter of Advent of Code creator

### VS Code shortcuts

1. Use Code Runner Extension.
    1. `alt + ctrl + N` - Run current file
    1. `alt + ctrl + M` - Stop current process
1. F5 - start a debugger

## Python tips & tricks

[defaultdic](https://docs.python.org/3/library/collections.html#collections.defaultdict) - Dictionary with default value
```python
parts = defaultdict(list)
parts['foo'].append('bar)

a = defaultdict(int)
d = defaultdict(set)
```

`enumerate()` - adds index to for loop, use `start` flag to start from other value than 0
```python
for count, value in enumerate(values):
    ...
```

`math.prod` - multiplies array values
```python
a = [1, 2, 3, 4]
print(mathprod(a)) # 24
```

`@functools.cache` - memoization of function results, [documetation link](https://docs.python.org/3/library/functools.html)
```python
import functools

@functools.cache
def factorial(n):
    return n * factorial(n-1) if n else 1
```

intertools - useful library for efficient looping [documentation link](https://docs.python.org/3/library/itertools.html)

### Parsing input

```python
  for i, line in enumerate(lines, start=1):
      (p1, p2) = line.split('|')
      i, *winning = list(map(int,re.findall(r'(\d+)', p1)))
      mine = list(map(int,re.findall(r'\d+', p2)))
```

`re.finditer()` - creates iterable list of matches
```python
matches = re.finditer(pattern, s)
for match in matches:
    print(match)
```