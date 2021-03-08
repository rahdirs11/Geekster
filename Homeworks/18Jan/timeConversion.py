def timeConversion(s: str) -> str:
    if s[-2:].lower() == 'am':
        if int(s[: 2]) == 12:
            return f"00{''.join(s[2: -2])}"
    else:
        if int(s[: 2]) != 12:
            return f"{12 + int(s[: 2])}{''.join(s[2: -2])}"
    return s[: -2]

print(timeConversion(input()))
