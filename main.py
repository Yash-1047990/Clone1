print("hello world")

import math
user_name = "John Doe"
entered_name = input("User name, please: ")
size_user_name = len(user_name)
size_entered_name = len(entered_name)
user_name_is_bigger = size_user_name > size_entered_name
entered_name_is_bigger = size_entered_name > size_user_name
print(f"The user name {user_name} has more characters than the entered name {entered_name} is: {user_name_is_bigger}")
print(f"The entered name {entered_name} has more characters then the user name {user_name} is: {entered_name_is_bigger}")
lights_on = False
lock_closed = True
alarm_activated = not lights_on and lock_closed
print(f"The alarm is activated, is: {alarm_activated}")
print(9//3)
print(81//9)
x=9.1
y=(math.sqrt(3*x-1)+(1+x)**2)
print(y)
