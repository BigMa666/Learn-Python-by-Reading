# Time for Lists
### So as we saw few Data Types in the last part. In this part we will discuss the remaining sequence data types.

## Let's Get Started

## Sequence Types or Python Collections (Arrays)

### List - Lists are used in Python to store multiple values in a single variable.
### Properties of Lists :
1. Ordered
    - Means that the values have a defined order
2. Changeable
    - Means that we can change the values (add,remove,edit)
3. Duplication 
    - Allows us to add same value multiple times
### Inside lists we can store any numeric, boolean or text types.

```python
marks = [95, 45, 80, 100, 95]
students  = ["James", "Leon", "Ram"]
answers = [True, False, False, True]
print(marks, marks[2])
```
## Accessing List Items
### For example you have a list of tasks and you want access it you can access them by referring to the index number of the item. An example is given below.
> In the indexing the numbers are Whole Numbers
```python
tasks = ['Get Up', 'Brush the teeth', 'Bath', 'Breakfast']
print(tasks[0]) # Accessing 'Get Up' by using its index number which is 0 in this case
```
## Negative Indexing
### In negative indexing it is from end to start.
### Example :
```python
tasks = ['Get Up', 'Brush the teeth', 'Bath', 'Breakfast']
print(tasks[-3])
```
| Item | Item Index |
| :---: | :---: |
| Get Up | -4 |
| Brush the teeth | -3 |
| Bath | -2 |
| Breakfast | -1 |

## Range of Indexing
### In Range of Indexing we specify the range of indexes to get the particular items.
```python
tasks = ['Get Up', 'Brush the teeth', 'Bath', 'Breakfast']
print(tasks[0:3])
print(tasks[2:])
```

## Change List Items
### We can change the value of a certain item in the list.
```python
tasks = ['Get Up', 'Brush the teeth', 'Bath', 'Breakfast']
tasks[0] = 'Wake Up' # Changing the value of the item using its index
print(tasks) # To Check
```

## Change a Range of Item values 
### We can aslo change the value of multiple items at the same time using range of the items.
```python
tasks = ['Get Up', 'Brush the teeth', 'Bath', 'Breakfast', 'Put Petrol']
tasks[2:4] = ['Go to Office', 'Eat Lunch']
print(tasks)
```
## Appending and Inserting Items
### Using Append function you can add a item at the end of the list (i.e You can not specify the index of it.), whereas while inserting we can specify the index.
### Append
```python
tasks = ['Get Up', 'Brush the teeth', 'Bath', 'Breakfast']
tasks.append("Go to Office") # Using the append function
print(tasks)
```
### Insert
```python
tasks = ['Get Up', 'Brush the teeth', 'Bath', 'Breakfast']
tasks.insert(3,"Go to Office") # Using the insert function
print(tasks)
```
## Extend List
### Using this function we can appends items from another list to a list
```python
fruits = ['apple', 'banana', 'orange']
seasonal = ['mango', 'jackfruit', 'strawberry']
fruits.extend(seasonal)
print(fruits)
```

## Remove & Clear List Items 
### Now you wil learn to remove items from lists and also remove items based on index.
## Remove Function
### It is used to remove items on the basis of their value.
```python
tasks = ['Get Up', 'Brush the teeth', 'Bath', 'Breakfast']
tasks.remove("Bath")
print(tasks)
```
## Pop Function 
### Pop Function is used to remove items based on index.
```python
tasks = ['Get Up', 'Brush the teeth', 'Bath', 'Breakfast']
tasks.pop(2)
print(tasks)
tasks.pop() # Deletes the whole list
```
## Del Keyword
### Del can be also used to remove a item based on index.
```python
tasks = ['Get Up', 'Brush the teeth', 'Bath', 'Breakfast']
del tasks[2] # Deleting the 2 indexed item.
print(tasks)
del tasks # Deletes the whole list.
```

## Clear Function
### To make the list empty
```python
tasks = ['Get Up', 'Brush the teeth', 'Bath', 'Breakfast']
tasks.clear()
```
## Code File - [Lists Code file](https://github.com/kaarn101/Learn-Python-by-Reading/blob/main/Python-Scripts/lists.py)
## Your Next Lesson - [Tuples](5-Tuples.md)
