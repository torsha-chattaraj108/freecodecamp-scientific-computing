def add_time(start,duration,day_of_week=None):
    days_of_week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    t_time,am_pm=start.split(' ')
    t_hour,t_min=t_time.split(':')
    dur_hour,dur_min=duration.split(':')
    start_hour=int(t_hour)
    if am_pm=='PM':
        start_hour+=12
    elif am_pm=='AM' and start_hour==12:
        start_hour=0
    total_min=int(t_min)+int(dur_min)
    total_hour=start_hour+int(dur_hour)
    if total_min>=60:
        hours=total_min//60
        total_min=total_min%60
        total_hour+=hours
    final_hour=total_hour%24
    if final_hour>=12:
        am_pm='PM'
    else:
        am_pm='AM'
    if final_hour==0:
        final_hour_12=12
    elif final_hour>12:
        final_hour_12=final_hour-12
    else:
        final_hour_12=final_hour
    days=total_hour//24
    day_string=''
    if days==1:
        day_string=' (next day)'
    elif days>1:
        day_string=f' ({days} days later)'
    final_min=f'{total_min:02d}'
    if day_of_week!=None:
        start_index=days_of_week.index(day_of_week.capitalize())
        new_index=(start_index+days)%7
        final_time=f'{final_hour_12}:{final_min} {am_pm}, {days_of_week[new_index]}{day_string}'
    else:
        final_time=f'{final_hour_12}:{final_min} {am_pm}{day_string}'
    return final_time
