def send_message(route):
    time = sum(route)/300000 + (len(route)-1)*0.5
    return round(time, 4)
print(send_message([802101, 725994, 112808, 3625770, 481239]))