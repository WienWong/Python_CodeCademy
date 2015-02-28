
# Exam Statistics

# You'll see the grades listed (see what I did there). 
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
print "Grades:", grades

# Let's start to print out the list of grades, one element at a time.
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for gd in grades:
        print gd

print_grades(grades)

# The next step in the creation of our grade statistics program involves 
# computing the mean (average) of the grades.
print "Let's compute some stats!"

# The sum of scores
# Define a function grades_sum() that does the following:
# Takes in a list of scores, scores
# Computes the sum of the scores
# Returns the computed sum
# Call the newly created grades_sum() function with the list of grades and print the result.
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    tot=0
    for gd in scores:
        tot += gd
    return tot
    
print grades_sum(grades)

# Computing the Average
# Define a function grades_average(), below the grades_sum() function that does the following:
# Has one argument, grades, a list
# Calls grades_sum with grades
# Computes the average of the grades by dividing that sum by float(len(grades)).
# Returns the average.
# Call the newly created grades_average() function with the list of grades and print the result.
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    tot=0
    for gd in scores:
        tot += gd
        print tot
    return tot
    
print grades_sum(grades)

def grades_average(grades):
    return grades_sum(grades)/float(len(grades))

print grades_average(grades)

print "Time to conquer the variance!"

# The Variance
# A very large variance means that the students' grades were all over the place, while a small 
# variance (relatively close to the average) means that the majority of students did fairly well.
# On line 18, define a new function called grades_variance() that accepts one argument, scores, a list.
# First, create a variable average and store the result of calling grades_average(scores).
# Next, create another variable variance and set it to zero. We will use this as a rolling sum.
# for each score in scores: Compute its squared difference: (average - score) ** 2 and add that to variance.
# Divide the total variance by the number of scores.
# Then, return that result.
# Finally, after your function code, print grades_variance(grades).

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average=grades_average(scores)
    variance=0
    for score in scores:
        variance += (average - score) ** 2
    return variance/len(scores)
    
print grades_variance(grades)   

# Standard Deviation
# Define a function grades_std_deviation(variance).
# return the result of variance ** 0.5
# After the function, create a new variable called variance and store the result of calling grades_variance(grades).
# Finally print the result of calling grades_std_deviation(variance)
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average=grades_average(scores)
    variance=0
    for score in scores:
        variance += (average - score) ** 2
    return variance/len(scores)
    
print grades_variance(grades) 

def grades_std_deviation(variance):
    return variance ** 0.5
    
variance = grades_variance(grades) 

print grades_std_deviation(variance)

# Review
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average=grades_average(scores)
    variance=0
    for score in scores:
        variance += (average - score) ** 2
    return variance/len(scores)
    
print grades_variance(grades) 

def grades_std_deviation(variance):
    return variance ** 0.5
    
variance = grades_variance(grades) 

print "all of the grades:"
print print_grades(grades)

print "sum of grades:" 
print grades_sum(grades)

print "average grade:"
print grades_average(grades)

print "variance:" 
print grades_variance(grades)

print "standard deviation:" 
print grades_std_deviation(variance)









