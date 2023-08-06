import pytz
from datetime import datetime, timedelta

def adjust_dst(zonename, date):
    tz = pytz.timezone(zonename)
    date_with_tzinfo = tz.localize(date)
    now = pytz.utc.localize(date)
    current_zone_offset_date = date_with_tzinfo.astimezone(pytz.utc)
    if now.astimezone(tz).dst() != timedelta(0):
        current_zone_offset_date = current_zone_offset_date + timedelta(hours=1)
    current_zone_offset_date = str(current_zone_offset_date)[:-6]
    return str(datetime.strptime(str(current_zone_offset_date), '%Y-%m-%d %H:%M:%S'))


def is_dst(zonename, date):
    tz = pytz.timezone(zonename)
    now = pytz.utc.localize(date)
    return now.astimezone(tz).dst() != timedelta(0)

def timezone_appender(timzone, date):
    tz_ny = pytz.timezone(timzone)
    timezone_name = currentDateTime.astimezone(tz_ny)
    return timezone_name.strftime('%Y-%m-%d %H:%M:%S %Z')
	
def timezone_appender_with_time_format(timzone, date):
    tz_ny = pytz.timezone(timzone)
    timezone_name = currentDateTime.astimezone(tz_ny)
    return timezone_name.strftime('%A, %b %d %Y at %I:%M %p %Z')
    
def adjust_zoneoffset(zonename, date):
    tz = pytz.timezone(zonename)
    now = pytz.utc.localize(date)
    current_zone_offset = now.astimezone(tz).strftime('%z')
    offset_minutes  = int(current_zone_offset[1:3]) * 60 + int(current_zone_offset[3:])
    if current_zone_offset[0] == '-':
        offset_minutes  = -offset_minutes 
    hours = int(offset_minutes) // 60
    minutes = int(offset_minutes) % 60
    # format the result as a string in the format of H:MM
    if offset_minutes > 0:
        current_zone_offset = f"+{hours}:{minutes:02d}"
    else:
        current_zone_offset = f"{hours}:{minutes:02d}"
    return str(current_zone_offset)

def adjust_zoneoffset_dst(zonename, date):
    tz = pytz.timezone(zonename)
    now = pytz.utc.localize(date)
    current_zone_offset = now.astimezone(tz).strftime('%z')
    offset_minutes  = int(current_zone_offset[1:3]) * 60 + int(current_zone_offset[3:])
    if current_zone_offset[0] == '-':
        offset_minutes  = -offset_minutes 
    if now.astimezone(tz).dst() != timedelta(0):
        offset_minutes = int(offset_minutes) - 60
    hours = int(offset_minutes) // 60
    minutes = int(offset_minutes) % 60
    # format the result as a string in the format of H:MM
    if offset_minutes > 0:
        current_zone_offset = f"+{hours}:{minutes:02d}"
    else:
        current_zone_offset = f"{hours}:{minutes:02d}"
    return str(current_zone_offset)