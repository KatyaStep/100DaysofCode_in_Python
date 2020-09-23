s = '07:40:22AM'

def timeConversion(s):
    hours_conversion = 0
    if 'PM' in s:
        if s[ 0:2 ] == '12':
            converted_time = s[ :-2 ]
        else:
            hours_conversion = int(s[0:2]) + 12
            converted_time = str(hours_conversion) + s[2:-2]
        print(converted_time)

    elif 'AM' in s:
        if s[0:2] == '12':
            hours_conversion = '00'
            converted_time = str(hours_conversion) + s[2:-2]
            print(converted_time)
        else:
            converted_time = s[:-2]
            print(converted_time)


timeConversion(s)