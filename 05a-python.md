# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and Tuples are similar because they both contain collections of items. The main difference is that lists are mutable (you can change their contents) but tuples are not. This is the main reason for why tuples can be used as dictionary keys but not lists. If you set a list as a key to a dictionary, what happens if you change the contents of that list? It would effect the dictionary in a weird ways.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets both contain a collection of objects. However lists deal with the ordering of objects in a different way than sets. Sets do not contain duplicate objects and are generally ordered least --> greatest, though the order does not really matter in sets. Sets are used to check for membership or to reduce collections to their components. Lists however can contain duplicate objects because the order or placement of an object within a list matters and differentiates them.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> lambda is amazing. It's used to define anonymous functions, basically if you need something done quickly/on the fly and on a very specific group of objects, you use a lambda funciton. Lambda functions are disposable, you use it and then throw it away. This is particularly useful for indicating how to sort a collection. For example:

say you had a collection of names and ages:
```
  kids = [('john', 14), ('abbey', 17), ('mark', 13), ('chelsea', 21)]
```
you could sort these by name alphabetically by referencing the first item in each tuple -
```sorted(kids, key = lambda k : k[0])```
or you could sort by age by referencing the second item

```sorted(kids, key = lambda k: k[1])```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List/set/dict comprehensions are short-hand ways of iterating/ generating lists/sets/dicts. The most basic way to look at list comps is as a short-hand for loop:

```
one_over = []
for n in range(10):
  one_over.append(1./n)
```
is the same as:
``` [1./n for n in range(10)] ```

This is not only useful for saving keystrokes, but list comprehensions are also faster than for loops (because they run on a deeper level in the computer ??)


map and filter are functions to modify/filter collections. They are particularly useful along with lambda functions to apply the transformation to each item in a collection:
```
collection = range(10)
# transform colleciton so it matches our "one_over" list from before.
map(lambda n: 1./n, collection)

# filter collection so that it only contains even numbers
filter(lambda n: n%2 == 0, collection)
# note this would be the same as:
[n for n in range(10) if n%2 == 0]
```



---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> I know you can do this using datetime or dateutil in python but i prefer pandas datetime handling
``` 
import pandas as pd
date_start = pd.to_datetime(date_start)
date_stop = pd.to_datetime(date_stop)
td = date_stop - date_start # 937 days
```
b.  
```
date_start = '12312013'  
date_stop = '05282015'  
date_start = pd.to_datetime(date_start, format = '%m%d%Y')
date_stop = pd.to_datetime(date_stop, format = '%m%d%Y')
td = date_stop - date_start # 513 days

```

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
date_start = pd.to_datetime(date_start, format = '%d-%b-%Y')
date_stop = pd.to_datetime(date_stop, format = '%d-%b-%Y')
td = date_stop - date_start # 7850 days

```

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





