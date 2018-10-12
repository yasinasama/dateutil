from datetime import datetime,timedelta

now = datetime.now()

weekdays = {
    '0':('monday','mon'),
    '1':('tuesday','tue'),
    '2':('wednesday','wed'),
    '3':('thusday','thu'),
    '4':('friday','fri'),
    '5':('saturday','sat'),
    '6':('sunday','sun')
}

def weekday_to_day(year,month,weekday,count):
    fd = datetime(year=year,month=month,day=1)
    wd = fd.weekday()

    weeks = int(count)-1
    days = 7 * weeks + (weekday-wd+7)%7

    return fd+timedelta(days)

if __name__=='__main__':
    print(weekday_to_day(2018,10,1,3))