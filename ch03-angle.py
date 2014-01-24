print "Handwritten by Arunram A"
print "Handwrite - Do not copy paste, is the most important rule of this book"
print "Learn Python the hard way by Zed A. Shaw"
print "Chapter 3 - Exercise - Angele between hour and minute hand"

input_time = raw_input("Enter the time in hh:mm format")
in_hr = int(input_time[0:2])
in_min = int(input_time[3:5])

in_hr = in_hr % 12

angle_deg = (30 * in_hr - 5.5 * in_min) % 360

# The two statements below one commented and the other active, both are equivalent 
# if(angle_deg > 180): angle_deg = 360 - angle_deg
angle_deg = int(angle_deg / 180) * (360 - angle_deg) + int(not(angle_deg / 180)) * angle_deg

print "The interior angle between hour and minute hand at ", input_time, " is ", angle_deg, " degrees"

dummy_variable = raw_input("Keyboard stroke; use raw_input in python2.x and input in python3.x")
