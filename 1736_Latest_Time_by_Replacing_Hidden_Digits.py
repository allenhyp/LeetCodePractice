class Solution:
    def maximumTime(self, time: str) -> str:
        hour = time[:2]
        minute = time[3:5]
        print(hour, minute)
        if hour[0] == '?':
            if hour[1] == '?':
                hour = '23'
            elif int(hour[1]) < 4:
                hour = '2' + hour[1]
            else:
                hour = '1' + hour[1]
        elif hour[1] == '?':
            if int(hour[0]) < 2:
                hour = hour[0] + '9'
            else:
                hour = hour[0] + '3'
                
        if minute[0] == '?': minute = '5' + minute[1]
        if minute[1] == '?': minute = minute[0] + '9'
            
        return "{0}:{1}".format(hour, minute)
