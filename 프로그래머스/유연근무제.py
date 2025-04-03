def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(timelogs)):
        schedules[i] = (schedules[i] // 100) * 60 + (schedules[i] % 100)
        for j in range(len(timelogs[i])):
            timelogs[i][j] = (timelogs[i][j] // 100) * 60 + (timelogs[i][j] % 100)

    for i in range(len(timelogs)):
        result = 0
        for j in range(len(timelogs[i])):
            if timelogs[i][j] <= schedules[i]+10:
                weekday = (startday - 1 + j) % 7
                if weekday == 5 or weekday == 6:
                    continue
                result += 1
        if result == 5:
            answer += 1
    return answer
