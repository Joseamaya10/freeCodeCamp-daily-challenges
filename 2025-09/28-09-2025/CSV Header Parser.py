def get_headings(csv):
    csv = csv.split(",")
    csv_list = list()
    for i in csv:
        i_stripped = i.strip()
        csv_list.append(i_stripped)
    return csv_list
print(get_headings("first name,last name,phone"))
print(get_headings("username , email , signup date "))
print(get_headings("name,age,city"))
print(get_headings("first name,last name,phone"))
print(get_headings("username , email , signup date "))