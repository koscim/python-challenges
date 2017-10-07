from time import localtime

activities = {  8: 'Sleeping',
                9: 'Commuting',
                17: 'Working',
                18: 'Commuting',
                20: 'Eating',
                22: 'Resting' }

time_now = localtime()
hour = time_now.tm_hour
minutes = time_now.tm_min

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print "It is now {hour}:{minutes}, your next activity is {activity}".format(hour=hour, activity=activities[activity_time], minutes=minutes)
        break
else:
    print 'Unkown, AFK or sleeping!'
