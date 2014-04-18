py_time
=======

Add breaks in functions to track which parts take longer.

While [timeit](https://docs.python.org/2/library/timeit.html) is good to check how long a short piece of code takes to execute, PyTime allows you to put markers inside much larger blocks of code that can help give you information about which lines are taking the longest to execute. This can immensely help optimization by showing which parts of the code are taking up the most computational time.

Import using `from py_time.main import *`. After importing, initialize with `t = PyTime()`. This will create the start marker, after which you can call `t.get_split()` to get the time since the last `get_split` call as well as the time since initialization.

```python
from py_time.main import *

def codeYouWantToTest():
	t = PyTime()

	# stuff happens

	t.get_split()

	# more things happen

	t.get_split()

```

to-do:

- finish __init__ to allow custom titles

- default to wait until end of script to print, option to print as you go

- ability to add custom computations - what could they even be?

- ability to combine with timeit to print out average splits after multiple calls