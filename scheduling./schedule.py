from datetime import datetime, timedelta

# get user input for start time and duration
start_time_str = input("Enter start time (in format 'YYYY-MM-DD HH:MM:SS'): ")
duration_str = input("Enter duration (in minutes): ")

# convert user input to datetime objects
start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
duration = timedelta(minutes=int(duration_str))

# calculate end time
end_time = start_time + duration

# print out scheduled event
print(f"Your event is scheduled to start at {start_time.strftime('%Y-%m-%d %H:%M:%S')} and end at {end_time.strftime('%Y-%m-%d %H:%M:%S')}.")
