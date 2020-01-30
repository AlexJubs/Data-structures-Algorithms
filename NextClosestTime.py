class Solution:
    def nextClosestTime(self, time: str) -> str:
        if (time == "00:00"): return time

        digits = [time[0],time[1],time[3],time[4]]
        hours = int(time[0:2])
        minutes = int(time[3:5])
        c=0
        while c<10:
            if (minutes < 59): minutes = minutes+1
            elif (minutes == 59):
                minutes = 0
                if (hours < 23): hours = hours+1
                elif (hours == 23): hours = 0
            if (hours < 10): 
                temp1 = "0"
                temp2 = str(hours)
            if (minutes < 10):
                temp3 = "0"
                temp4 = str(minutes)
            if (hours > 9): 
                temp1 = str(int(hours/10))
                temp2 = str(hours%10)
            if (minutes > 9):
                temp3 = str(int(minutes/10))
                temp4 = str(minutes%10)
            if ((temp1 in digits) and (temp2 in digits) and (temp3 in digits) and (temp4 in digits)):
                return temp1+temp2+":"+temp3+temp4