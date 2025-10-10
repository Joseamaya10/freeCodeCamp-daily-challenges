from datetime import date
def moon_phase(date_string):
    date_reference = date(2000, 1, 6)
    year, month, day = map(int, date_string.split("-"))
    input_date = date(year, month, day)
    difference = int(abs(date_reference - input_date).days)
    rango = difference % 28
    if rango in range(0, 7):
        return "New"
    elif rango in range(7, 14):
        return "Waxing"
    elif rango in range(14, 21):
        return "Full"
    else:
        return "Waning"
print(moon_phase("2014-10-15"))
print(moon_phase("2000-01-12"))