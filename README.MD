# Sequentor

Simple module to allow 'lazy-like' sequential operations.

Also contains lists in functional-like manner.



## Examples
* Sequentor example

``` python
from Sequentor.sequentor import sequentor as seq

my_seq = new seq(state = 10)
my_seq.add_action(" / 5")
my_seq.add_action(" + 43").add_action(" - 11 ")
my_seq.show_graph()
print(my_seq.evaluate())

10
|
+---+>   / 5
    |
    +---+>   + 43
        |
        +---+>   - 11

34.0
```

* Lazy List example

``` python
from Sequentor.flist import FList

my_lst = FList([7,8])

l = my_lst\
.map(lambda x: x + 2)\
.flatMap(lambda x: list(range(0, x)))\
.filter(lambda x: x < 8)

print(l)

FList([0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7])
```

* Combination example (word-count :tada:)

```python
from Sequentor.sequentor import sequentor as sq
from Sequentor.FList import FList

txt = '\
This is just a simple Simple text about simple \
text with some very simple text \
well \
maybe it is not that much simple \
but still relatively simple'

counter = sq(FList([txt]))

counter.add_action(".flatMap(lambda x:x.split())")\
.add_action(".map(lambda x: x.lower())")\
.add_action(".map(lambda x: (x, 1))")\
.add_action(".reduceByKey()")
# reduceByKey supports only "+" now

counter.evaluate().foreach(print)

('this', 1)
('is', 2)
('just', 1)
('a', 1)
('simple', 6)
('text', 3)
('about', 1)
('with', 1)
('some', 1)
('very', 1)
('well', 1)
('maybe', 1)
('it', 1)
('not', 1)
('that', 1)
('much', 1)
('but', 1)
('still', 1)
('relatively', 1)
```
