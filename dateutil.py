import calendar

# 返回某年某月第n个weekday是几号
def month_weekday_to_day(year,month,weekday,n):
    c = calendar.Calendar()
    weeks = c.monthdayscalendar(year,month)
    firstweek = weeks[0]

    if firstweek[weekday] == 0:
        n += 1

    if n > len(weeks):
        return -1

    day = weeks[n-1][weekday] 

    return -1 if day == 0 else day

def year_weekday_to_day(year,weekday,n):
    c = calendar.Calendar()

    


if __name__=='__main__':
    # print(weekday_to_day(2018,5,4,4))
    

    # print(calendar.firstweekday())
    # print(calendar.weekheader(1))
    # print(calendar.leapdays)

    c = calendar.Calendar()
    print(c.yeardayscalendar(2016))
    # print(c.monthdatescalendar(2018,11))
    # print(c.monthdays2calendar(2018,10))

    # print(c.monthdayscalendar(2018,11))