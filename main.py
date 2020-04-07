# 1. Introduction to Coding and to Python
# - Computational Thinking
# - Information binary representation
# - Introduction to the Python programming language
# - Jupyter notebooks

# region 2. Python Data Types
# - Variables, values and types
# - Integer, Float, String, Boolean data types and their operators
x = 9
x = 9.6  # NO double SI float
x = 'ciao'
x = True
print(type(x))

x = 9 == 7
x = 'ciaoo' == 'ciao'

# NUMBERS
# 9 operatore 9
# my_func(9, 9)
somma = 9 + 9
differenza = 4 - 9
# power **
# resto divisione %
# /

# ERROR --> False - 'ciao'

# STRING
print('ciao' + ' Lorenzo')
print('ciao', 'Lorenzo')
'ciao'.replace('c', 'd')

# BOOLEAN
# or ||
# and &&
x = True or False
x = True and False


# endregion

# region 3. Simple programs
# - From pseudo-code to code

# if ci sono 4 mele:
#     allora stampo una mela
#
# ciclo tutti gli elementi:
#     per ogni

# endregion

# region 4. Functions and Conditional Statements
# - Function definition
def get_result(x, y):
    return x + y


get_result(8, 9)
# - Variable's scope
BASE_URL = 'www.google.com'


def get_result(x, y):
    print(BASE_URL)
    URL = ''
    return x + y


# URL
get_result(8, 9)

# - Conditional Statements
if 6 > 8:
    print('la matematica non esiste')

# endregion

# region 5. Iterative Computation
# - Formalization of iterative solutions
# - The while loop
condition = True
while condition:
    # body
    pass

# - The for loop
items = [1, 'ciao', [1, 2, 4], {}]
for item in items:
    # body
    pass

# endregion

# region 6. Iterative Computation II
# - Nested loops
x, y, z = 1, 2, 3
rows = cols = []
for row in rows:
    for col in cols:
        pass
# endregion

# region 7. Python Lists
# - Creating and manipulating lists
x = [1, 2, 3]
elements = (1, 2, 3)
# - Iterating through lists
for element in elements:
    print(element)

# endregion

# region 8. Introduction to matplotlib
# - Plotting functions with matplotlib
# import matplotlib
# matplotlib.plot()

# - Customizing appearance

# - Using matplotlib to validate data analysis tasks

# endregion

# region 9. Python Lists II
# - Time-series analysis through list processing
# endregion

# region 10. Python Lists III
# - List comprehensions
x = [x + h
     for x in [1, 2]
     for h in [2, 3]
     if x == 9]

# - List sorting
sorted([2, 4, 1])


# - Mutable and Immutable types
# list vs tuple

# - Anonymous functions
def my_func(y):
    return y > 1


x = filter(lambda y: y > 1, [1, 2, 3])
x = filter(my_func, [1, 2, 3])

# endregion

# region 11. Python Strings
# - String slicing, concatenation and traversal
# - String manipulation methods
# 12. Python Strings II
# - Text processing, string manipulation and sub-string search
x = [1, 2, 3][1]
x = 'ciao lo'[1:5]
x = 'ciao lo'[-1]
x = 'ciao lo'[5:]
x = 'ciao lo'[:5]

# endregion

# region 13. Python Dictionaries
# - Dictionaries and mapping, keys and values
# - Dictionary creation and access
x = {
    'name': 'Lorenzo',
    'ral': 15000,
    'label3': False,
    'label4': [],
    'label5': {

    },
}
x = x['label1']  # se label1 non esiste spara eccezione
x = x.get('label1', default='Non ho trovato niente')  # se label1 non esiste torna None
x['label1'] = 'ciao'

# endregion

# region 14. Python Dictionaries II
# - Iterating through dictionaries
# for x in [1, 2, 3]:
# for label, value in [['l', 'v'], ['l', 'v']]:
for label, value in {}.items():
    print(label, value)

# - Efficiency of presence checking
if 'affitto' in {}:
    print()

# endregion

# 15. Problem Solving
# - Binary search



