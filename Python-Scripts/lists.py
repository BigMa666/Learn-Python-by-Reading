#Lists
marks = [95, 45, 80, 100, 95]
students  = ["James", "Leon", "Ram"]
answers = [True, False, False, True]
print(marks, marks[2])

# Accessing Items
tasks = ['Get Up', 'Brush the teeth', 'Bath', 'Breakfast']
print(tasks[2]) # Normal
print(tasks[1:3]) # Range
print(tasks[-4]) # Negative Indexing

# Changing List Items
tasks = ['Get Up', 'Brush the teeth', 'Bath', 'Breakfast']
tasks[0] = 'Wake Up' # Changing the value of the item using its index
print(tasks) # To Check

# Change a Range of items
tasks = ['Get Up', 'Brush the teeth', 'Bath', 'Breakfast', 'Put Petrol']
tasks[2:4] = ['Go to Office', 'Eat Lunch']
print(tasks)

# Append
tasks = ['Get Up', 'Brush the teeth', 'Bath', 'Breakfast']
tasks.append("Go to Office") # Using the append function
print(tasks)

# Insert
tasks = ['Get Up', 'Brush the teeth', 'Bath', 'Breakfast']
tasks.insert(3,"Go to Office") # Using the insert function
print(tasks)

# Extend 
fruits = ['apple', 'banana', 'orange']
seasonal = ['mango', 'jackfruit', 'strawberry']
fruits.extend(seasonal)
print(fruits)

# Remove Function
tasks = ['Get Up', 'Brush the teeth', 'Bath', 'Breakfast']
tasks.remove("Bath")
print(tasks)

# Pop 
tasks = ['Get Up', 'Brush the teeth', 'Bath', 'Breakfast']
tasks.pop(2)
print(tasks)
tasks.pop() # Deletes the whole list

# Del 
tasks = ['Get Up', 'Brush the teeth', 'Bath', 'Breakfast']
del tasks[2] # Deleting the 2 indexed item.
print(tasks)
del tasks # Deletes the whole list.

# Clear
tasks = ['Get Up', 'Brush the teeth', 'Bath', 'Breakfast']
tasks.clear()