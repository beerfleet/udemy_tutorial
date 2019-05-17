import re

def is_valid_time(time_str):
    time = re.compile(r'\d{1,2}:\d{2}')
    match = time.fullmatch(time_str)
    if match:
        return True
    return False

def parse_bytes(date_str):
    bin_regex = re.compile(r'\b[10]{8}\b')    
    #return bin_regex.findall(date_str)
    print(bin_regex.findall(date_str))

def parse_date(date_str):
    date_regex = re.compile(r'(?P<d>\d{2})[/.,](?P<m>\d{2})[/.,](?P<y>\d{4})')
    match = date_regex.fullmatch(date_str)
    indexes = ('d', 'm', 'y')
    groups = match.groups()
    print(groups)
    zip_obj = list(zip(groups, indexes))
    print(zip_obj)
    return {tup[0]:tup[1] for tup in zip_obj}
    # return zip_obj

print(parse_date('11/11/1111'))
