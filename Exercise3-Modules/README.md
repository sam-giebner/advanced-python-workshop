# Exercise 3: Modules
## Applying what you've learned so far about modules and modularization:
#### 1. Open and examine summarize_roads.py
- You will find that it contains many different process which run sequentially. 
- There are CSV read and write process defined which could be handy to resuse in the future. 
- As it the script currently sits, it lacks modularization and would be hard to test or troubleshoot the different processes.
#### 2. Create a module with functions that will allow us to resuse the CSV read and write processes currently defined in summarize_road_surface.py
- Remember, you are writing the functions with the intention of resusing them in the future. Make sure that you generalize your object names (functions, variables, etc.).
- If you put your module in a subfolder, remeber to include a \_\_init\_\_.py file.
#### 2. Modify summarize_road_surface.py so that it leverages the functions you defined in your module.
- Remeber to utilize dot notation when importing your module.
#### 3. Modularize the data summary processes by creating functions in summarize_road_surface.py
- Spliting process into smaller subprocesses using function helps modularize the code and makes it easier to test the individual processes.
#### 4. (Optional) Modify your module so that the CSV writing functionality can be tested by running the file as a script.
- Hint: Use \_\_name\_\_ == '\_\_main\_\_': to determine the file execution context (imported as module, run as script, etc.).
- Hint: Define a variable which contains dummy data that can be used by to test the CSV output function.