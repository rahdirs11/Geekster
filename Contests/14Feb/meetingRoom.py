n = int(input())
timings = []
for _ in range(n):
    timings.append(list(map(int, input().split())))

timings = sorted(timings, key=lambda x: x[1])
# from os import system
# system('cls')
# for start, end in timings:
#     print(f'{start} to {end}')

totalMeetings, i = int(), int()

while i < n:
    currMeeting = timings[i]
    # print(currMeeting)
    totalMeetings += 1
    j = i + 1
    while j < n and timings[j][0] <= currMeeting[1]:
        j += 1
    
    i = j

print(totalMeetings)