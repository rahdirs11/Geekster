def dayOfProgrammer(year: int) -> str:
    isLeap = False
    if year < 1918:
        if not year % 4:
            isLeap = True
    elif year >= 1919:
        if (not year % 4 and year % 100) or (not year % 400):
            isLeap = True
    else:
        return f"26.09.{year}"
    return f'12.09.{year}' if isLeap else f'13.09.{year}'

print(dayOfProgrammer(int(input())))
