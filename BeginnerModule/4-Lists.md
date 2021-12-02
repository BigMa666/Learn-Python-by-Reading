# Time for Lists
### So as we saw few Data Types in the last part. In this part we will discuss the remaining data types.

## Let's Get Started

## Sequence Types or Python Collections (Arrays)

### List - Lists are used in Python to store multiple values in a single variable.
### Properties of Lists :
1. Ordered
    - Means that the values have a defined order
2. Changeable
    - Means that we can change the values (add,remove)
3. Duplication 
    - Allows us to add same value multiple times
### Inside lists we can store any numeric, boolean or text types.

```python
marks = [95, 45, 80, 100, 95]
students  = ["James", "Leon", "Ram"]
answers = [True, False, False, True]
print(marks, marks[2])
```
### Tuples - Tuples are also used to store multiple values in one variable.
### Properties of Tuples : 
1. **Unchangeable**
    - Means that we **can not change** the values. (not add/remove)
2. Ordered
    - Means that the values have a defined order
3. Duplication 
    - Allows us to add same value multiple times

### Inside tuples we can store any numeric, boolean or text types.

```python
marks = (950/1000, 450/1000, 1000/1000)
students ('James', 'Leon', 'Ram')
answers = (True, False, False, True, False)
print(type(marks))
print(marks[0] + " " + "are the marks of " + students[0])
```