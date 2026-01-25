# Question 5:Write a function that takes the radii of two circles and performs the following:
# • Validates that both radii are positive integers.
# • Computes the area of each circle.
# • Returns the percentage of the larger circle’s area that can be covered by the smaller circle.
# If invalid input is provided, return a meaningful message instead of performing the calculation

import math

#this function calculates how much of the larger circle's area can be covered by the smaller circle, expressed as a percentage
def area_covered_by_the_circle(radius_of_the_first_circle, radius_of_the_second_circle):

    #validate that both inputs are integers
    if not isinstance(radius_of_the_first_circle, int) or not isinstance(radius_of_the_second_circle,int):
        return "Error: both radii must be positive integers."

    #calculate the area of the first circle
    area_of_the_first_circle = math.pi * (radius_of_the_first_circle ** 2)

    # calculate the area of the second circle
    area_of_the_second_circle = math.pi * (radius_of_the_second_circle ** 2)

    # determine which circle has the larger area
    larger_circle_area = max(area_of_the_first_circle, area_of_the_second_circle)
    smaller_circle_area = min(area_of_the_first_circle, area_of_the_second_circle)

    # calculate the percentage of the larger circle covered by the smaller circle
    percentage_of_larger_circle_covered = (
    smaller_circle_area / larger_circle_area) * 100

    # return the calculated percentage
    return percentage_of_larger_circle_covered

#example tests
print(area_covered_by_the_circle(3, 5))
