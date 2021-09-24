# put your python code here
megan_time_hours = int(input())
megan_time_minutes = int(input())
megan_time_seconds = int(input())
rain_time_hours = int(input())
rain_time_minutes = int(input())
rain_time_seconds = int(input())
seconds_per_hour = 3600
seconds_per_minute = 60
print(abs(((megan_time_hours * seconds_per_hour)
           + (megan_time_minutes * seconds_per_minute)
           + megan_time_seconds)
          - ((rain_time_hours * seconds_per_hour)
             + (rain_time_minutes * seconds_per_minute)
             + rain_time_seconds)))
