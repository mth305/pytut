# Quiz

... or what we hopefully learned last time


## Basics

* Maths

    1 + 1
    >>> 2

    4 / 2
    >>> 2

    1 / 2
    >>> 0

    1.0 / 2
    >>> 0.5

* Types

    type(1)
    >>> <type 'int'>

    type(1.0)
    >>> <type 'float'>

    type("1")
    >>> <type 'str'>

    type(True)
    >>> <type 'bool'>

* Comparisons

    type(1) == int
    >>> True

* Conditionals

    if type(1) == int:
        print("integer found!")
    else:
        print("no integer...")

* Variables

    name = "Niklas"
    print(name)
    >>> Niklas

* String manipulation

    first = "Niklas"
    last  = "Heim"
    print(first + last)
    >>> NiklasHeim

    def prettyname(first, last):
        return last + ", " + first

    prettyname(first, last)
    >>> Heim, Niklas

* Lists. we looped over them.

    lst = ["some", "strings", "in", "this", "list", 1, 2, 4, 0.2, 12.1]
    # do this with function
    strings = [el for el in lst if type(el) == str]
    ints = [el for el in lst if type(el) == int]
    floats = [el for el in lst if type(el) == float]
