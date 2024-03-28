for _ in range(int(input())):
    time = input()
    hour = int(time[:2])

    if hour < 12:
        s = 'AM'
    else:
        s = 'PM'
    if hour > 12:
        hour -= 12
    if hour == 0:
        hour = 12
    
    hour = "{:02d}".format(hour)

    print(f"{hour}{time[2:]} {s}")
