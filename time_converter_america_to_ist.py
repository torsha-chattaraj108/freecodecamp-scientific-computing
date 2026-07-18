def time_converter(start,us_tz,day_of_week=None,is_dst=False):
    tz_list={'ET':10.5,
             'CT':11.5,
             'MT':12.5,
             'PT':13.5,
             'AST':9.5,
             'AKST':8.5,
             'HST':5.5,
             'ChST':-4.5
             }
    dst_timezones = ['ET', 'CT', 'MT', 'PT', 'AST', 'AKST']
    week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    s_time,am_pm=start.split(' ')
    s_hour,s_min=s_time.split(':')
    offset_value=tz_list[us_tz]
    if is_dst and us_tz in dst_timezones:
        offset_value-=1.0
    u_hour=int(offset_value)
    u_min=round((offset_value%1)*60)
    start_time=int(s_hour)
    if am_pm=='PM' and start_time!=12:
        start_time+=12
    elif am_pm=='AM' and start_time==12:
        start_time=0
    t_hour=start_time+u_hour
    t_min=int(s_min)+u_min
    if t_min>=60:
        hours=t_min//60
        t_min=t_min%60
        t_hour+=hours
    f_hour=t_hour%24
    if f_hour>=12:
        am_pm='PM'
    else:
        am_pm='AM'
    days=t_hour//24
    if f_hour==0:
        f_hour_12=12
    elif f_hour>12:
        f_hour_12=f_hour-12
    elif f_hour==12:
        f_hour_12=12
    else:
        f_hour_12=f_hour
    f_min=f'{t_min:02d}'
    day_string=''
    if days==1:
        day_string=f' (next day)'
    elif days>1:
        day_string=f' ({days} days later)'
    if day_of_week!=None:
        start_index=week.index(day_of_week)
        new_index=(start_index+days)%7
        f_time=f'{f_hour_12}:{f_min} {am_pm} {week[new_index]}'
    else:
        f_time=f'{f_hour_12}:{f_min} {am_pm}{day_string}'
    return f_time

print(time_converter("3:55 PM", "ET", "Sunday", is_dst=True))
