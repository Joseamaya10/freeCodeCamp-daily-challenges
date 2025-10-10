def format_number(n):
    number_tel = f"+{n[-11::-1][::-1]} ({n[-8:-11:-1][::-1]}) {n[-5:-8:-1][::-1]}-{n[-1:-5:-1][::-1]}"
    return number_tel
print(format_number("05552340182"))
print(format_number("575554354792"))