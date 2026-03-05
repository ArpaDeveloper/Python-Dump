# My code dump with Python-language
Different codes that I have done using Python-language. 
## Files
### Error Test
Tests for various different errors that python can throw.

Filename: __ErrorTest.py__
### "Rock-Paper-Scissors-Lizard-Spock"-game
My implementation of "Rock-Paper-Scissors-Lizard-Spock"-game. First iteration was "Rock-Paper-Scissors-Lizard-Spock.py", which was my base implementation. I then improved it by shortening the code in "Rock-Paper-Scissors-Lizard-SpockMINI.py". Final implementation was "Rock-Paper-Scissors-Lizard-Spock_COMPRESSED.py", where I tried to make it with a smallest amount of characters possible, with same printing than the 2 other ones.

Game explained: <br />
Scissors > Paper, Lizard <br />
Paper > Rock, Spock <br />
Rock > Lizard, Scissors <br />
Lizard > Spock, Paper <br />
Spock > Scissors, Rock <br />


Filenames:<br />__Rock-Paper-Scissors-Lizard-Spock.py__, <br />__Rock-Paper-Scissors-Lizard-SpockMINI.py__, <br />__Rock-Paper-Scissors-Lizard-Spock_COMPRESSED.py__

### Simple Calculator
Simple implementation of basic calculator in python.

Filename: __SimpleCalculator.py__

### Student Grade Management System.py
Small system to handle student course grades, where you can: <br />
Add student record <br />
Display all records <br />
Delete a record (by student ID and course ID) <br />
Display records sorted by course ID and score (descending) <br />
Query records by student ID <br />

Filename: __StudentGradeManagementSystem.py__

### Expression Tree
This "program" evaluates mathematical forms written in infix form. First it builds a expression tree using stacks&binary tree. Then it turns it to postfix using a non-recursive postorder traversal. 
Then it evaluates the postfix expression using a stack to compute the final result.

Filename: __expressiontree.py__

### Finnish cities weather analysis 
This "program" analyzes weather data for 100 random Finnish cities using the OpenWeatherMap API. <br />Steps: <br />
Loads a JSON database of cities and selects those located in Finland.<br />
Randomly chooses 100 Finnish cities.<br />
Requests current weather data (temperature and coordinates) for each city from the API.<br />
Stores the data in a pandas DataFrame.<br />
Calculates the correlation between temperature and latitude using linear regression.<br />
Visualizes the results with a scatter plot and a trend line showing the relationship between latitude and temperature.<br />

Filename: __finnishcities_weatheranalysis.py__

### Number guess game
Small game, where you have to guess a random number picked by computer.

Filename: __guess_number.py__

### Random password generator
Generates a random password.

Filename: __random_psswd.py__

### Scatter test
Does a random scatter using matplotlib.

Filename: __scatter.py__

### Sorting Algorithms test
This "program" compares the performance of four sorting algorithms: Insertion Sort, Bubble Sort, Merge Sort, and Quick Sort by generating a random lists of different sizes, and then sorting them using each algorithm. 
The program measures time taken to sort the lists.

Filename: __sorting_methods.py__

### Weather application test
Gets the weather of user inputted city using OpenWeatherMap API.

Filename: __weatherapp.py__

