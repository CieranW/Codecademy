# Code challenge: Strings
# 1. Count Letters
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:


def unique_english_letters(word):
    count = 0
    for letter in letters:
        if letter in word:
            count += 1
    return count

# Since the provided alphabet string includes a single instance of all uppercase and lowercase letters in the English alphabet, we can iterate through that string and see if our input strings contains the current letter we are looking at. This can be accomplished using the keyword in. For every letter in the possible letters, we see if that letter is in our string!


# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

# 2. Count X


def count_char_x(word, x):
    count = 0
    for letter in word:
        if letter == x:
            count += 1
    return count

# This solution is similar to the last solution. In this case, we are looping through the input string and comparing it against the input character. If they are the same, then we increase the counter.


# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

# 3. Count Multi X


def count_multi_char_x(word, x):
    splits = word.split(x)
    return (len(splits)-1)

# In our function, we split the first input string using the second input string. What this does is cut the first string into an array of smaller substrings containing the parts not equal to our second parameter x. For example, when splitting "mississippi" with the string "iss", the resulting array will be [“m”, “”, “ippi”]. This includes the characters before "iss" was found, the empty space between the two instances of "iss" and the characters after the last"iss". Be careful! In order to get the correct result we need to return one less then the total number of split sections — in this example, "iss" was in the string twice, resulting in 3 sections. So we should return 3 - 1.


# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

# 4. Substring Between


def substring_between_letters(word, start, end):
    start_ind = word.find(start)
    end_ind = word.find(end)
    if start_ind > -1 and end_ind > -1:
        return(word[start_ind+1:end_ind])
    return word

# In this solution, we use the find function to get the starting and ending indices of our substring using our starting and ending characters. After getting those, we check to make sure neither of them are -1. In order to extract the portion of the string within those indices, we use slicing. We provide the starting index plus one in order to not include the starting character. We do not need to provide the end index plus one, since the value on the right of the colon is excluded. This causes our slicing to look like: word[start_ind+1:end_ind]).


# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

# 5. X Length


def x_length_words(sentence, x):
    for word in sentence.split():
        if len(word) < x:
            return False
        else:
            return True

# Or:


def x_length_words(sentence, x):
    words = sentence.split(" ")
    for word in words:
        if len(word) < x:
            return False
    return True

# We can use the split function with the space character provided in order to get an array of all of the words in the sentence. Next, we use the in keyword in order to loop through every element in our array of words. We check the length of each word and compare it against x to see if it is shorter. If any of the words in the array are shorter then we immediately return False and end the function. If we make through all of the words without returning False, we know we should return True since all of the word’s lengths were longer than x.


# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True

# Code challenge: Strings (Advanced)
# 1. Check Name


def check_for_name(sentence, name):
    if name.lower() in sentence.lower():
        return True
    else:
        return False

# Or:


def check_for_name(sentence, name):
    return name.lower() in sentence.lower()
# As you can see, this function can be created using one line. The in keyword will return True if the first provided string is within the second. So in this case, we’re checking if name is in sentence. In order to ignore differences in capitalization, we can use the .lower() function which converts all characters to lowercase characters.


# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

# 2. Every Other Letter


def every_other_letter(word):
    other = ""
    for i in range(0, len(word), 2):
        other += word[i]
    return other

# In order to alternate which character is added to the every_other string, we use a range of indices which starts at index 0 (the beginning of our word) and ends at the end of our word. The third parameter in the range function determines what value to increment by. In this case, we want to increment by 2 in order to get every other letter.

# Another way to loop through all indices of our original string, but only add the letters that correspond to an even index. As a challenge, try solving this problem that way!


# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print

# 3. Reverse


def reverse_string(word):
    reverse = ""
    for i in range(len(word)-1, -1, -1):
        reverse += word[i]
    return reverse

# This is similar to the last solution, but our range has been modified in order to start at the last index of the string (length of the string minus one) up to the first index. Since the parameter for the ending index is exclusive we need to provide the index of one more iteration than what we want to stop at. We want to stop at 0, and since we are incrementing by -1, we will set the ending index to -1. Finally, make sure to add the third parameter of -1. This makes us increment by -1 at each step.


# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

# 4. Make Spoonerism


def make_spoonerism(word1, word2):
    new = word2[0] + word1[1:]
    new2 = word1[0] + word2[1:]
    return new + " " + new2

# Or:


def make_spoonerism(word1, word2):
    return word2[0] + word1[1:] + " " + word1[0] + word2[1:]

# We can accomplish the task in one line by appending and slicing at the same time. We can get the first index of our words by using word1[0] and word2[0] which gets the letter at the first index. In order to get the remaining letters we can use word1[1:] and word2[1:]. This returns all characters in the strings starting with index 1 and on. We concatenate everything together to get the result.


# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

# 5. Add Exclamation


def add_exclamation(word):
    while len(word) < 20:
        word += "!"
    if len(word) >= 20:
        return word
# Or:


def add_exclamation(word):
    while(len(word) < 20):
        word += "!"
    return word
# This function shows how we can continuously append to our string based on some condition. In this case, we keep testing the length of the string to see if we should keep going. Once the length has reached 20, either by adding exclamation marks or by already being long, we return the result.


# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn

# Code challenge: Dictionaries
# 1. Sum Values


def sum_values(my_dictionary):
    count = 0
    for value in my_dictionary.values():
        count += value
    return count

# We start by creating a variable to keep track of the total. Next, we use the values() function in our for loop in order to iterate through each of the values in the dictionary. Using this, we can access each value and add it to our total variable. At the end of our loop, we return the total.


# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk": 5, "eggs": 2, "flour": 3}))
# should print 10
print(sum_values({10: 1, 100: 2, 1000: 3}))
# should print 6
# 2. Even Keys


def sum_even_keys(my_dictionary):
    total = 0
    for key in my_dictionary.keys():
        if key % 2 == 0:
            total += my_dictionary[key]
    return total

# Similar to the previous problem, we are iterating through our dictionary, except this time we are iterating through the keys instead of the values. In order to get the keys we use the keys() function and to get the value of a key we can use brackets. To test if the key is even we use the modulus operator and test if the remainder is 0 when dividing by 2.


# Uncomment these function calls to test your  function:
print(sum_even_keys({1: 5, 2: 2, 3: 3}))
# should print 2
print(sum_even_keys({10: 1, 100: 2, 1000: 3}))
# should print 6
# 3. Add Ten


def add_ten(my_dictionary):
    for key in my_dictionary.keys():
        my_dictionary[key] += 10
    return my_dictionary

# We use a for loop to iterate through each key and we access the value using the key. After accessing it, we overwrite the value with the value plus 10. Finally, we return the modified dictionary.


# Uncomment these function calls to test your  function:
print(add_ten({1: 5, 2: 2, 3: 3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10: 1, 100: 2, 1000: 3}))
# should print {10:11, 100:12, 1000:13}
# 4. Values that are Keys


def values_that_are_keys(my_dictionary):
    new = []
    for value in my_dictionary.values():
        if value in my_dictionary.keys():
            new.append(value)
    return new

# For this solution, we iterate through every value within the dictionary. In order to check if it is also a key, we can use the in keyword. This checks the value against all of the keys in the dictionary to see if it exists as a key as well. If it does, then we append it to our list of values which are also keys.


# Uncomment these function calls to test your  function:
print(values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))
# should print [1, 4]
print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))
# should print ["a"]
# 5. Largest Value


def max_key(my_dictionary):
    largest_key = float("-inf")
    largest_value = float("-inf")
    for key, value in my_dictionary.items():
        if value > largest_value:
            largest_value = value
            largest_key = key
    return largest_key

# In order to program the max algorithm using dictionaries, we need to keep track of the max value and the key which is used to access it. We start by using float("-inf") in order to initialize them to the lowest possible value. To retrieve the key and value at the same time, we use the items() function. Inside our loop, we overwrite the current largest value and the key used to access whenever we find a larger value. We return the largest value’s key once we have iterated through the entire dictionary.


# Uncomment these function calls to test your  function:
print(max_key({1: 100, 2: 1, 3: 4, 4: 10}))
# should print 1
print(max_key({"a": 100, "b": 10, "c": 1000}))
# should print "c"

# Code challenges: Dictionaries (Advanced)
# 1. Word Length Dict


def word_length_dictionary(words):
    word_lengths = {}
    for word in words:
        word_lengths[word] = len(word)
    return word_lengths

# To create a new dictionary we set a variable equal to {}. While iterating through each string in our string list, we can add the key and value to our dictionary using this syntax: word_lengths[word] = len(word).


# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

# 2. Frequency Count


def frequency_dictionary(words):
    frequency = {}
    for word in words:
        if word not in frequency:
            frequency[word] = 0
        frequency[word] += 1
    return frequency

# To create a new dictionary we set a variable equal to {}. We iterate through each of the strings in the list of strings and check if it is already in our dictionary using the in keyword. If it is not then we add it as a new key-value pair where the value is 0. Regardless of whether the string was already in the dictionary, increase the value by 1. This will make it so all new entries will have a value of 1 and all existing entries will increase their old value by 1.


# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0, 0, 0, 0, 0]))
# should print {0:5}

# 3. Unique Values


def unique_values(my_dictionary):
    seen_values = []
    for value in my_dictionary.values():
        if value not in seen_values:
            seen_values.append(value)
    return len(seen_values)

# This function has a similar structure to the last one except that the input has been changed to a dictionary. We iterate through each of the values and whenever we find one we have not added to our list already, we add it to the list. After the loop, we return the length of the list since that contains all unique values from the dictionary.


# Uncomment these function calls to test your  function:
print(unique_values({0: 3, 1: 1, 4: 1, 5: 3}))
# should print 2
print(unique_values({0: 3, 1: 3, 4: 3, 5: 3}))
# should print 1

# 4. Count First Letter


def count_first_letter(names):
    letters = {}
    for key in names:
        first_letter = key[0]
        if first_letter not in letters:
            letters[first_letter] = 0
        letters[first_letter] += len(names[key])
    return letters

# This function uses two dictionaries instead of one dictionary and one list. We iterate through each of the keys (which are the last names) and store the first letter of the last name in first_letter. We then use similar logic to what we have used before by testing if we have already seen that letter before. If we haven’t seen that letter before, then we add it to our dictionary with a value of 0. Next, we are going to increment the value. Since we know that some people share the last name (as seen by the list of first names in our names dictionary), we are going to increment the value in our letters dictionary by the length of first names that share the last name for our current iteration (key).


# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": [
      "Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": [
      "Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}

# Code challenge: Classes
# 1. Setting up our Robot


class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.sensor_range = 0
        self.direction = 0


robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.sensor_range = 10
robot_1.direction = 90
print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

# This shows the structure of a simple class which only contains instance variables. The three instance variables are set to 0 for now, which means that they can only be changed by manually by accessing them from an object of the DriveBot class.

# 2. Adding Robot Logic


class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0

    # Add the methods here!
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

# These two methods were added inside of the DriveBot class. They are used to replace the instance variables with new values from the input parameters. We use self.variable_name to access a certain instance variable within the class.


robot_1 = DriveBot()
# Use the methods here!
robot_1.motor_speed = 10
robot_1.sensor_range = 20
robot_1.direction = 180
print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

# 3. Enhanced Constructor


class DriveBot:
    # Update this constructor!
    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

# This upgraded constructor includes input parameters as well as default values for those parameters. This means that if no value is provided for those parameters, then the value they are set equal to will be used. Here are some examples of different ways to use the constructor:


robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

# Create robot_2 here!
robot_2 = DriveBot()
robot_2.motor_speed = 35
robot_2.direction = 75
robot_2.sensor_range = 25
print(robot_2.motor_speed)
print(robot_2.direction)
print(robot_2.sensor_range)

# sensor_range defaults to 10
test_bot_1 = DriveBot(10, 270)

# direction defaults to 180
test_bot_2 = DriveBot(sensor_range=20, motor_speed=45)

# direction defaults to 180 and sensor_range defaults to 10
test_bot_3 = DriveBot(50)

# all default values are used
test_bot_4 = DriveBot()

# no default values are used
test_bot_5 = DriveBot(18, 95, 30)

# 4. Controlling Them All


class DriveBot:
    # Create the class variables!
    all_disabled = False
    latitude = -999999
    longitude = -999999

    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range


robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

# Change the latitude, longitude, and all_disabled values for all three robots using only three lines of code!

# We placed the class variables at the top of the class outside of the constructor. These variables can be accessed within the scope of the entire class. This means that the class variables contained within every object from the DriveBot class will change if we modify the class variable directly. Here is an example of how to change each of these class variables:


DriveBot.latitude = -50.0
DriveBot.longitude = 50.0
DriveBot.all_disabled = True

print(robot_1.latitude)
print(robot_2.longitude)
print(robot_3.all_disabled)

# 5. Identifying Robots


class DriveBot:
  # Create a counter to keep track of how many robots were created
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count
        # Assign an `id` to the robot when it is constructed by incrementing the counter and assigning the value to `id`

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

# The final modifications to this class can be seen at the top of the class and in the constructor. We use a class variable to keep track of the total number of robots. This information is shared across all robot objects we create from the class. Every time a robot object is created, the constructor is called and the count is incremented. Each robot has an instance variable for id which is local to that robot object. This is assigned at the time of construction and stores what the count was at that time.


robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

print(robot_1.id)
print(robot_2.id)
print(robot_3.id)

# Code challenge: Classes (Advanced)
# 1. Robot Inheritance


class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed=0, direction=180, sensor_range=10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count += 1
        self.id = Robot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction + 180) % 360
            self.obstacle_found = False

# Create the DriveBot class here!


class DriveBot(Robot):
    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        super().__init__(motor_speed, direction, sensor_range)
# Create the WalkBot class here!


class WalkBot(Robot):
    def __init__(self, steps_per_minute=0, direction=180, sensor_range=10, step_length=5):
        super().__init__(steps_per_minute, direction, sensor_range)
        self.step_length = step_length


# Uncomment the robot instantiation!
robot_1 = DriveBot()
robot_2 = WalkBot()
robot_3 = WalkBot(20, 90, 15, 10)

# Use these print statements to test your code!

print(robot_2.id)
print(robot_3.step_length)
print(robot_1.speed)

# By placing Robot in the parentheses next to the two new classes, we cause them to inherit from the Robot class. We can use super().__init__(self, param_1, param_2, etc...) to call the superclass constructor. This will use the constructor in the Robot class to assign the values to the instance variables. Any new changes can then be added afterward.

# 2. Using the Superclass


class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed=0, direction=180, sensor_range=10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count += 1
        self.id = Robot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction + 180) % 360
            self.obstacle_found = False


class DriveBot(Robot):

    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        super().__init__(motor_speed, direction, sensor_range)


class WalkBot(Robot):

    def __init__(self, steps_per_minute=0, direction=180, sensor_range=10, step_length=5):
        super().__init__(steps_per_minute, direction, sensor_range)
        self.step_length = step_length

    # Override the adjust_sensor method here!
    def adjust_sensor(self, new_sensor_range):
        super().adjust_sensor(new_sensor_range)
        self.obstacle_found = False
        self.step_length = 5


robot_walk = WalkBot(60, 90, 10, 15)
robot_walk.obstacle_found = True
print(robot_walk.sensor_range)
print(robot_walk.obstacle_found)
print(robot_walk.step_length)
# Call the overridden adjust_sensor method here!
robot_walk.adjust_sensor(25)

print(robot_walk.sensor_range)
print(robot_walk.obstacle_found)
print(robot_walk.step_length)

# As you can see, in order to override the method, we can re-define it again with the same name. You can use super().method_name() in order to call the superclass version of the method.

# 3. Conditional Superclass Logic


class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed=0, direction=180, sensor_range=10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count += 1
        self.id = Robot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction + 180) % 360
            self.obstacle_found = False


class DriveBot(Robot):

    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        super().__init__(motor_speed, direction, sensor_range)


class WalkBot(Robot):

    def __init__(self, steps_per_minute=0, direction=180, sensor_range=10, step_length=5):
        super().__init__(steps_per_minute, direction, sensor_range)
        self.step_length = step_length

    def adjust_sensor(self, new_sensor_range):
        super().adjust_sensor(new_sensor_range)
        self.obstacle_found = False
        self.step_length = 5

    # Override the avoid_obstacles method here!
    def avoid_obstacles(self):
        if(self.obstacle_found):
            if(self.speed <= 60):
                super().avoid_obstacles()
            else:
                self.direction = (self.direction + 90) % 360
                self.obstacle_found = False
            self.speed /= 2
            self.step_length /= 2


robot_1 = WalkBot(150, 0, 10, 10)
robot_1.obstacle_found = True
robot_1.avoid_obstacles()

print(robot_1.direction)
print(robot_1.speed)
print(robot_1.step_length)

robot_2 = WalkBot(60, 0, 20, 40)
robot_2.obstacle_found = True
robot_2.avoid_obstacles()

print(robot_2.direction)
print(robot_2.speed)
print(robot_2.step_length)

# This method shows how the superclass method can be called conditionally. In this case it depends on the speed of the robot and if an obstacle was found. We use modulus when rotating the robot to loop back past 0 if we go over 360 degrees. This is because the robot would have made a full circle.


class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed=0, direction=180, sensor_range=10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count += 1
        self.id = Robot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction + 180) % 360
            self.obstacle_found = False

  # Override the + and - operations here!
    def __add__(self, value):
        self.speed += value

    def __sub__(self, value):
        self.speed -= value


class DriveBot(Robot):

    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        super().__init__(motor_speed, direction, sensor_range)

    # Override the + and - operations here while using those dunder methods from the superclass!
    def __add__(self, value):
        super().__add__(value)
        self.sensor_range += value

    def __sub__(self, value):
        super().__sub__(value)
        self.sensor_range -= value


class WalkBot(Robot):

    def __init__(self, steps_per_minute=0, direction=180, sensor_range=10, step_length=5):
        super().__init__(steps_per_minute, direction, sensor_range)
        self.step_length = step_length

    def adjust_sensor(self, new_sensor_range):
        super().adjust_sensor(new_sensor_range)
        self.obstacle_found = False
        self.step_length = 5

    def avoid_obstacles(self):
        if(self.obstacle_found):
            if(self.speed <= 60):
                super().avoid_obstacles()
            else:
                self.direction = (self.direction + 90) % 360
                self.obstacle_found = False
            self.speed /= 2
            self.step_length /= 2

    # Override the + and - operations here while using those dunder methods from the superclass!
    def __add__(self, value):
        super().__add__(value)
        self.step_length += value / 2

    def __sub__(self, value):
        super().__sub__(value)
        self.step_length -= value / 2


robot_1 = DriveBot()
robot_2 = WalkBot()

# Uncomment these lines when you are ready to test your code!
robot_1 + 20
robot_1 - 10
robot_2 + 10
robot_2 - 5

print(robot_1.speed)
print(robot_1.sensor_range)
print(robot_2.speed)
print(robot_2.step_length)

# Here are the overridden dunder methods in each class:

# class Robot:
#     def __add__(self, value):
#         self.speed += value

#     def __sub__(self, value):
#         self.speed -= value

# class DriveBot(Robot):
#     def __add__(self, value):
#         super().__add__(value)
#         self.sensor_range += value

#     def __sub__(self, value):
#         super().__sub__(value)
#         self.sensor_range -= value

# class WalkBot(Robot):
#     def __add__(self, value):
#        super().__add__(value)
#        self.step_length += value / 2

#     def __sub__(self, value):
#        super().__sub__(value)
#        self.step_length -= value / 2

# The above code only shows the dunder methods which were added to each class. The child classes both override those operations as well. This shows how superclass versions of dunder methods can also be called from a child class.

# 5. Preven a Robot Takeover


class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed=0, direction=180, sensor_range=10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count += 1
        self.id = Robot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction + 180) % 360
            self.obstacle_found = False

    def __add__(self, value):
        self.speed += value

    def __sub__(self, value):
        self.speed -= value


class DriveBot(Robot):

    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        super().__init__(motor_speed, direction, sensor_range)

    def __add__(self, value):
        super().__add__(value)
        self.sensor_range += value

    def __sub__(self, value):
        super().__sub__(value)
        self.sensor_range -= value


class WalkBot(Robot):
    walk_bot_count = 0

    def __init__(self, steps_per_minute=0, direction=180, sensor_range=10, step_length=5):
        super().__init__(steps_per_minute, direction, sensor_range)
        self.step_length = step_length
        WalkBot.walk_bot_count += 1
        if WalkBot.walk_bot_count >= 5 and Robot.robot_count >= 10:
            Robot.all_disabled = True

# This modification uses a similar method of counting from the Robot class, but it uses a separate counter to only track the number of WalkBots. Whenever a new WalkBot is created, the constructor is called and the two counts are checked. If the total number of robots is at least 10 and the number of WalkBots reaches 5 then all robots are disabled.

    def adjust_sensor(self, new_sensor_range):
        super().adjust_sensor(new_sensor_range)
        self.obstacle_found = False
        self.step_length = 5

    def avoid_obstacles(self):
        if(self.obstacle_found):
            if(self.speed <= 60):
                super().avoid_obstacles()
            else:
                self.direction = (self.direction + 90) % 360
                self.obstacle_found = False
            self.speed /= 2
            self.step_length /= 2

    def __add__(self, value):
        super().__add__(value)
        self.step_length += value / 2

    def __sub__(self, value):
        super().__sub__(value)
        self.step_length -= value / 2


robot_1 = DriveBot()
robot_2 = WalkBot()
robot_3 = DriveBot()
robot_4 = DriveBot()
robot_5 = WalkBot()
robot_6 = DriveBot()
robot_7 = DriveBot()
robot_8 = WalkBot()
robot_9 = WalkBot()
print(Robot.all_disabled)
robot_10 = WalkBot()
print(Robot.all_disabled)
