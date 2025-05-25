
def seconds_since_midnight(hour, seconds, minutes):
        hour_in_seconds = hour * 60 * 60
        minute_in_seconds = minutes * 60
        return hour_in_seconds + minute_in_seconds + seconds

#Driver code
hour = int(input("Enter hour in 24hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

print("Total seconds since midnight is: ", seconds_since_midnight(hour, seconds, minutes))