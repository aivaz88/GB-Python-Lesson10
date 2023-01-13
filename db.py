import csv

def numeric_forecast(number):
    result = []
    forecasts = []
    with open('baseforecasts.txt', 'r', encoding='utf-8') as file:
        count = 0
        num_data = []
        while True:
            x = file.readline().replace('\n', '')
            if x == '':
                count += 1
                if count == 2:
                    break
                forecasts.append(num_data)
                num_data = []
            else:
                count = 0
                num_data.append(x)
    num = number%10 + (number//10)%10
    result.append(forecasts[num-1][:2])
    if num == 1:
        if number == 10:
            result.append(forecasts[num-1][2:4])
        elif number == 19:
            result.append(forecasts[num-1][4:6])
        elif number == 28:
            result.append(forecasts[num-1][6:])
    elif num == 2:
        if number == 11:
            result.append(forecasts[num-1][2:4])
        elif number == 20:
            result.append(forecasts[num-1][4:6])
        elif number == 29:
            result.append(forecasts[num-1][6:])
    elif num == 3:
        if number == 12:
            result.append(forecasts[num-1][2:4])
        elif number == 21:
            result.append(forecasts[num-1][4:6])
        elif number == 30:
            result.append(forecasts[num-1][6:])
    elif num == 4:
        if number == 13:
            result.append(forecasts[num-1][2:4])
        elif number == 22:
            result.append(forecasts[num-1][4:6])
        elif number == 31:
            result.append(forecasts[num-1][6:])
    elif num == 5:
        if number == 14:
            result.append(forecasts[num-1][2:4])
        elif number == 23:
            result.append(forecasts[num-1][4:])
    elif num == 6:
        if number == 15:
            result.append(forecasts[num-1][2:4])
        elif number == 24:
            result.append(forecasts[num-1][4:])
    elif num == 7:
        if number == 16:
            result.append(forecasts[num-1][2:4])
        elif number == 25:
            result.append(forecasts[num-1][4:])
    elif num == 8:
        if number == 17:
            result.append(forecasts[num-1][2:4])
        elif number == 26:
            result.append(forecasts[num-1][4:])
    elif num == 9:
        if number == 18:
            result.append(forecasts[num-1][2:4])
        elif number == 27:
            result.append(forecasts[num-1][4:])
    return result
