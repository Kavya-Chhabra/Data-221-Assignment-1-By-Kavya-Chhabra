# Question 7:Write a function that converts a given number of seconds since midnight into:
# • Hours
# • Minutes
# • Seconds
# • AM or PM
# The function should return a formatted string. If the input is invalid, return an appropriate
# message.

def conversion_of_number_of_seconds_since_midnight(total_seconds_since_midnight):
    #check if the input is a valid number (must be between 0 and 86399)
    if total_seconds_since_midnight < 0 or total_seconds_since_midnight >= 86400:
        return "Invalid input: seconds must be between 0 and 86399."

    #calculate total hours since midnight
    total_hours_since_midnight = total_seconds_since_midnight //3600

    #Calculate remaining seconds after hours are removed
    remaining_seconds_after_hours = total_seconds_since_midnight % 3600

    #calcualte minutes
    total_minutes = remaining_seconds_after_hours // 60

    #calculate remaining seconds
    remaining_seconds = remaining_seconds_after_hours % 60

    # Determine AM or PM
    if total_hours_since_midnight < 12:
        am_or_pm = "AM"
    else:
        am_or_pm = "PM"

    #Convert 24-hour time to 12-hour time
    hour_in_12_hour_format = total_hours_since_midnight % 12
    if hour_in_12_hour_format ==0:
        hour_in_12_hour_format = 12

    # Return formatted time string
    return (
        f"{hour_in_12_hour_format:02d}:"
        f"{total_minutes:02d}:"
        f"{remaining_seconds:02d}: {am_or_pm}"
    )

#example testing
print(conversion_of_number_of_seconds_since_midnight(3661))
print(conversion_of_number_of_seconds_since_midnight(90000))
