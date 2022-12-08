# Code challenges for Control Flow (Beginners).
# 1. Write your large_power function here:
def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False


# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False

# 2. Write your over_budget function here:


def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    if budget < food_bill + electricity_bill + internet_bill + rent:
        return True
    else:
        return False


# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True

# 3. Write your twice_as_large function here:


def twice_as_large(num1, num2):
    if num1 > num2 * 2:
        return True
    else:
        return False


# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True

# 4. Write your divisible_by_ten() function here:


def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False


# Uncomment these print() function calls to test your divisible_by_ten() function:

print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False

# 5. Write your not_sum_to_ten function here:


def not_sum_to_ten(num1, num2):
    if num1 + num2 != 10:
        return True
    else:
        return False


# Uncomment these function calls to test your not_sum_to_ten function:
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5, 5))
# should print False

# Coding challenge Control Flow (Advanced).
# 1. Write your in_range function here:


def in_range(num, lower, upper):
    if lower <= num <= upper:
        return True
    else:
        return False

# In this solution, we test the two bounds connected with an and boolean operator. This means that the code nested in the if statement will only execute if both of the conditions are true. We also do not include the else statement here. Since our if statement will return True and exit the function if the condition is true, the last line will only be reached if the condition was false.


# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False

# 2. Write your same_name function here:


def same_name(your_name, my_name):
    if your_name == my_name:
        return True
    else:
        return False
# As you can see in this solution code, comparing two strings in python can be done using the == operator. If you want an added challenge, you can try shortening the function body to one line of code!


# Uncomment these function calls to test your same_name function:
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False

# 3. Write your always_false function here:


def always_false(num):
    if (num < 0 and num > 0):
        return True
    else:
        return False

# In our example, we use the contradiction of being greater than and less than 0 at the same time. No matter what value we pass into the function, our condition will always be false since it is not logically possible. You normally want to avoid creating conditions like this.


# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False

# 4. Write your movie_review function here:


def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif rating < 9:
        return "This one was fun."
    else:
        return "Outstanding!"

# def movie_review(rating):
#   if(rating <= 5):
#     return "Avoid at all costs!"
#   if(rating < 9):
#     return "This one was fun."
#   return "Outstanding!"
# To solve this, we used a series of if statements to select which string to return. Another way of solving this would be to use if, elif and else statements.


# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."

# 5. Write your max_num function here:


def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    if num1 and num2 > num3:
        return "It's a tie!"
    elif num1 and num3 > num2:
        return "It's a tie!"
    elif num2 and num3 > num1:
        return "It's a tie!"

# One other way to do it:
# def max_num(num1, num2, num3):
#   if num1 > num2 and num1 > num3:
#     return num1
#   elif num2 > num1 and num2 > num3:
#     return num2
#   elif num3 > num1 and num3 > num2:
#     return num3
#   else:
#     return "It's a tie!"

# In this code, we use a series of if, elif, and else statements. We test the first parameter against the other two parameters and return the value if it is greater than the other two. We have two more tests to check if the second parameter is greater than the other two, then if the third parameter is greater than the other two. In the case where none of the parameters were greater than both of the other parameters, then we know that there must have been a tie and the final return statement is reached.


# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"

# Code challenge: Lists(Basic)
# 1. Append size


def append_size(lst):
    lst.append(len(lst))
    return lst


# Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

# 2. Append sum


def append_sum(lst):
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    return lst

# In our solution, we add the numbers and append the result in one line. We add the last and second to last elements within the .append() function and we repeat this line two more times. Remember that when we use negative indices, it starts from the end of the list and goes towards the beginning of the list. You could also use a loop to solve this instead of repeating the lines.


# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

# 3. Larger list


def larger_list(lst1, lst2):
    if len(lst1) >= len(lst2):
        return lst1[-1]
    else:
        return lst2[-1]

# We start by comparing the lengths of each of the lists using the len() function. This determines whether to return the last element of the first list or the second list. Notice that we use >=. This way, we know what to do if the lists have an equal length.

# In order to get the last element, we get the element at the -1 index. The negative index starts at the end of the list and works towards the start of the list.


# Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# 4. More than N


def more_than_n(lst, item, n):
    if lst.count(item) > n:
        return True
    else:
        return False
# We use the count() function to count the number of times item appears in lst. You could also do this manually by looping through lst and incrementing a variable every time you see item. We then compare the result to n.


# Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

# 5. Combine sort


def combine_sort(lst1, lst2):
    lst = lst1 + lst2
    lst.sort()
    return lst

# def combine_sort(lst1, lst2):
#   unsorted = lst1 + lst2
#   sortedList = sorted(unsorted)
#   return sortedList

# We start by combining the two lists together using + in order to get a new list. Next, in order to sort them, we use the sorted() function which returns a new sorted version of the list.


# Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

# Code challenge: Lists (Advanced)
# 1. Every three numbers


def every_three_nums(start):
    return list(range(start, 101, 3))

# We can write the body of this function in one line by nesting the range() function inside of the list() function. The range function accepts the starting number, the ending number (exclusive), and the amount to increment by.


# Uncomment the line below when your function is done
print(every_three_nums(91))

# 2. Remove middle


def remove_middle(lst, start, end):
    return lst[:start] + lst[end + 1:]

# This can be solved using one line of code if you combine and slice the lists at the same time. Slicing allows us to get the segments of the list before and after the index range and the operation + allows us to combine them together.


# Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# 3. More frequent item


def more_frequent_item(lst, item1, item2):
    if lst.count(item1) >= lst.count(item2):
        return item1
    else:
        return item2

# We use the count() function to find the number of occurrences for each item. We then compare the counts against each other to find the item which appears the most in the list. The item with the most appearances is returned by the function.


# Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

# 4. Double index


def double_index(lst, index):
    # Checks to see if index is too big
    if index >= len(lst):
        return lst
    else:
        # Gets the original list up to index
        new_lst = lst[0:index]
     # Adds double the value at index to the new list
    new_lst.append(lst[index]*2)
    #  Adds the rest of the original list
    new_lst = new_lst + lst[index+1:]
    return new_lst

# Note that this solution is careful not to modify the original input list. If we were to simply use lst[index] = lst[index] * 2 then the list that was passed into the function would be modified outside of the function as well. Creating a new list and writing the values to it prevents this from happening. We use slicing to extract the values before and after the index and we append the modified value at the index to our new list.


# Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

# 5. Middle item


def middle_element(lst):
    if len(lst) % 2 != 0:
        return lst[int(len(lst)/2)]
    if len(lst) % 2 == 0:
        sum_average = (lst[int(len(lst)/2 - 1)] + lst[int(len(lst)/2)])/2
        return sum_average

# def middle_element(lst):
#   if len(lst) % 2 == 0:
#     sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
#     return sum / 2
#   else:
#     return lst[int(len(lst)/2)]

# We used modulus to determine if the list had an even or odd number of elements. After determining this, for an odd number of elements, we calculate the middle index and return the middle element from the list. For an even number of elements, we calculate the index of the element close to the middle and the other element close to the middle (by subtracting 1 from the middle calculation). We get the values at those indices and calculate the average.

# Note that the math to find the middle index is a bit tricky. In some cases, when we divide by 2, we would get a double. For example, if our list had 3 items in it, then 3/2 would give us 1.5. The middle index should be 1, so in order to go from 1.5 to 1, we cast 1.5 as an int. In total, this is int(len(lst)/2).


# Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))

# Code challenge: Loops
# 1. Divisible by ten


def divisible_by_ten(nums):
    counter = 0
    for number in nums:
        if (number % 10 == 0):
            counter += 1
    return(counter)

# In this solution, we defined the function and set up our counter. We use a for loop to iterate through each number and check if its divisible by ten. If a number is divisible by another number then the remainder should be zero, so we use modulus. After the loop has finished, we return our count.


# Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

# 2. Greetings


def add_greetings(names):
    new_list = []
    for name in names:
        new_list.append("Hello, " + str(name))
    return new_list

# First, we set up our function to accept the list of strings and we initialized a new list of strings to hold our greetings. We iterate through each name and we append and concatenate the strings at the same time within our loop. Finally, we return the list containing all of our eloquent greetings.


# Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

# 3. Delete starting even numbers


def delete_starting_evens(lst):
    while (len(lst) > 0 and lst[0] % 2 == 0):
        lst = lst[1:]
    return lst

# After defining our method, we use a while loop to keep iterating as long as some provided conditions are true. We provide two conditions for the while loop to continue. We will keep iterating as long as there is at least one number left in the list len(lst) > 0 and if the first element in the list is even lst[0] % 2 == 0. If both of these conditions are true, then we replace the list with every element except for the first one using lst[1:]. Once the list is empty or we hit an odd number, the while loop terminates and we return the modified list.


# Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# 4. Odd indices


def odd_indices(lst):
    new_list = []
    for index in range(1, len(lst), 2):
        new_list.append(lst[index])
    return new_list
# In our solution, we iterate through a range of values. The function range(1, len(lst), 2) returns a list of numbers starting at 1, ending at the length of len, and incrementing by 2. This causes the loop to iterate through every odd number until the last index of our list of numbers. Using this, we can simply append the element at whatever index we are at since we know that using our range we will be iterating through only odd indices.#Another way to do this would be to iterate through all indices and use an if statement to see if the index you’re currently looking at is odd.


# Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

# 5. Exponents


def exponents(bases, powers):
    new_lst = []
    for base in bases:
        for power in powers:
            new_lst.append(base ** power)
    return new_lst

# As you can see in this solution, we used two nested for loops so that, for every base, we iterate through every power. This allows us to raise each base to every single power in our list and append the answers to our new list. Finally, we return the list of answers.


# Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

# Code challenge: Loops (Advanced)
# 1. Larger sum


def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for number in lst1:
        sum1 += number
    for number in lst2:
        sum2 += number
    if sum1 >= sum2:
        return lst1
    else:
        return lst2

# In this solution, we manually iterate through each element in each list and calculate our sums. We then return the list with the greater sum and break the tie by returning lst1. You can also try solving this problem using the sum() function in python. The body of this function could also be condensed into one line of code if you want an additional challenge!


# Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

# 2. Over 9000


def over_nine_thousand(lst):
    sum = 0
    for number in lst:
        sum += number
        if sum > 9000:
            break
    return sum

# Our solution follows a similar pattern to some of the other code challenges, except that we have a condition where we end early. In the case where we reach a sum greater than 9000, we can use the break keyword to exit our loop. This will continue to execute the code outside of our loop, which in this case, returns the sum that we found.


# Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

# 3. Max num


def max_num(nums):
    max = nums[0]
    for number in nums:
        if (number > max):
            max = number
    return max

# There are a few different ways to accomplish this task, but the way we did it was to check every element in the list and see if there is one bigger than what we currently think is the biggest. If there is a bigger one, then replace it. We keep replacing the number until the largest number has been found.


# Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

# 4. Same values


def same_values(lst1, lst2):
    new_lst = []
    for index in range(len(lst1)):
        if lst1[index] == lst2[index]:
            new_lst.append(index)
    return new_lst

# In this solution, we used a loop that iterates using the range of the len of our list. This generates the indices we need to iterate through. Note that we assume the lists are of equal size. We then access the element at the current index from each list using lst1[index] and lst2[index]. If they are equal we add the index to the new list. Finally, we return the results.


# Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# 5. Reversed list


def reversed_list(lst1, lst2):
    for index in range(len(lst1)):
        if (lst1[index] != lst2[len(lst2) - 1 - index]):
            return False
    return True

# In this code, we iterate through each of the indices for the entire length of either of the lists (since we assume the lengths are equal) and we perform a comparison on each of the elements. We get the element at the current index from our first list with lst1[index] and we test it against the last index of the second list minus the current index len(lst2) - 1 – index.

# That math is a little complicated — it helps to look at a concrete example. If we are given a list of 5 elements, the valid indices are 0 to 4. Because of this, the last index in the second list is len(lst2) - 1, or 5 - 1 = 4. Now in order to get the inverse of the position we are at in the first list, we subtract the index we are at from the end of the second list. So on the first pass, we’ll compare the element at position 0 to the element at position 5 - 1 - 0 = 4. On the next pass, we’ll compare the element at position 1 to the element at position 5 - 1 - 1 = 3, and so on.

# If any of the two elements are not equal then we know that the second list is not the reverse of the first list and we return False. If we made it to the end without a mismatch then we can return True since the second list is the reverse of the first. You could also try simplifying this code by using the python function reversed() or other methods that you will learn later on such as ‘slicing’.


# Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

# Code challenge: Functions
# 1. Tenth power


def tenth_power(num):
    return num ** 10

# This is one way to solve this problem using two lines of code.

# The first line is the function header which uses def to define the function followed by the function name. Within the parentheses we include num which is our formal parameter. Because of this, num is the variable name for the value we pass into this function.

# On our next line, we use return to show that this function is going to return a value when it is called. Next to the return keyword, we define what value is going to be returned. Since we need the tenth power of our input value, we can use the power operator in python which is **. Using this knowledge, in order to get the tenth power of our input value, we use num ** 10.


# Uncomment these function calls to test your tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

# 2. Square root


def square_root(num):
    return num ** 0.5

# As you can see, this solution is very similar to the last problem. In this case, the only changes we need are the function name and changing the power value to 0.5. We define the function called square_root with one parameter. We then take the one half power of the input value which is mathematically the same as taking the square root and return it.


# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

# 3. Win percentage


def win_percentage(wins, losses):
    percent = (wins / (wins + losses)) * 100
    return percent

# First, we defined our function with two parameters, one for games won and one for games lost. Next, we calculated the total number of games using the number of wins + losses. After that, we use calculate the ratio of wins out of the total number of games by dividing wins by our total_games variable. Since this gives us a ratio and we want it in percentage form, we multiply the answer by 100 and return it.


# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100

# 4. Average


def average(num1, num2):
    avg = (num1 + num2) / 2
    return avg

# Or:


def average(num1, num2):
    return (num1 + num2) / 2

# In this solution, we defined the function with two parameters one line and returned the average on the next line. When returning the value, we used parentheses around the addition to cause the two numbers to be added together first before dividing by two.


# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

# 5. Remainder


def remainder(num1, num2):
    return ((2 * num1) % (num2 / 2))

# Our solution It shortened to use only two lines of code. The first line defines the function with two input parameters. The second line performs the two mathematical operations on either side of the modulus within parenthesis. This causes the two calculations to be performed before taking the remainder of the left side divided by the right side.


# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0

# Code challenge: Functions (Advanced)
# 1. First three multiples


def first_three_multiples(num):
    print(num * 1)
    print(num * 2)
    print(num * 3)
    return num * 3
# In this solution, we start by defining the function header with an input. We then use the next three lines to print the result of multiplying the input value by one, two, and three. Finally, we return the result of multiplying the input value by 3.


# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0

# 2. Tip


def tip(total, percentage):
    tip1 = (total * percentage) / 100
    return tip1

# In this solution, we defined the function with two parameters and then used them to calculate the tip amount. We multiplied the input values together and divided by 100 since the second input is in percentage form and we want a monetary amount. Lastly, we returned the calculated tip value.


# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

# 3. Bond, James Bond


def introduction(first_name, last_name):
    intro = (last_name + ", " + first_name + " " + last_name)
    return intro

# Or:


def introduction(first_name, last_name):
    return last_name + ", " + first_name + " " + last_name
# First, we defined the method to accept the first and last names. On the next line, we performed all of the concatenations at once by adding the comma, spaces, and names in the correct order. We also returned the result on the same line.


# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

# 4. Dog years


def dog_years(name, age):
    dog_age = age * 7
    return str(name) + ", you are " + str(dog_age) + " years old in dog years"

# Or:


def dog_years(name, age):
    return str(name) + ", you are " + str(age * 7) + " years old in dog years"

# In this solution we used two lines of code to accomplish this task. The first line defines the function with the two inputs and the second line concatenates the string while also performing the calculation. We used str(age * 7) to convert the number to a string, and since that function call returns a string, we can concatenate it in-line with the rest of the string.


# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

# 5. All operations


def lots_of_math(a, b, c, d):
    result1 = a + b
    result2 = c - d
    result3 = result1 * result2
    print(result1, result2, result3)
    return result3 % a

# Or:


def lots_of_math(a, b, c, d):
    first = a + b
    second = c - d
    third = first * second
    fourth = third % a
    print(first)
    print(second)
    print(third)
    return fourth

# After defining the function, we store each result into its own variable for first and second. We then use these two variables in the calculation for third and we use the value of third to get fourth. Afterwards, we print the first three variables and return the fourth one.


# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0
