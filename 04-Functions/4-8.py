
def time_string(hours, minutes, time_format):
    if len(str(minutes)) < 2:
        minutes = (f'0{minutes}')
    if time_format == '24':
        if len(str(hours)) < 2:
            hours = (f'0{hours}')
        time = str(f'{hours}:{minutes}')
    elif time_format == '12':
        if hours > 12:
            time = str(f'{hours-12}:{minutes}pm')
        else:
            if hours == 0:
                time = str(f'12:{minutes}am')
            else:
                time = str(f'{hours}:{minutes}am')
            
    return time

print(time_string(15, 38, '24'))
print(time_string(8, 3, '24'))
print(time_string(0, 5, '24'))
print(time_string(11, 15, '12'))
print(time_string(0, 7, '12'))
print(time_string(7, 30, '12'))
print(time_string(12, 46, '12'))
print(time_string(13, 10, '12'))
print(time_string(19, 2, '12'))

