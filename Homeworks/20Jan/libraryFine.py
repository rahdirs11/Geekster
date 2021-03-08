# from datetime import date
#
# def calculateFine(returned, due) -> int:
#
#     if returned.year > due.year:
#         return 10000
#     elif returned.month > due.month and returned.year == due.year:
#         return 500 * (returned.month - due.month)
#     elif returned.month == due.month and returned.day > due.day and returned.year == due.year:
#         return 15  * (returned.day - due.day)
#     else:
#         return 0
#
#


def calculateFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return 10000
    else:
        if m1 > m2:
            return 500 * (m1 - m2)
        else:
            if d1 > d2:
                return 15 * (d1 - d2)
            else:
                return 0

d1, m1, y1 = map(int, input().split())
# returned = date(y, m, d)

d2, m2, y2 = map(int, input().split())
# due = date(y, m, d)

print(calculateFine(d1, m1, y1, d2, m2, y2))
