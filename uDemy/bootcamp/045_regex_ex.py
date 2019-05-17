import re

def is_valid_time(time_str):
    time = re.compile(r'\d{1,2}:\d{2}')
    match = time.fullmatch(time_str)
    if match:
        return True
    return False

print(is_valid_time("17:45"))