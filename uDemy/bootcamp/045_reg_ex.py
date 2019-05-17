import re

def intro():
    #define phone nr regex
    pattern = re.compile(r'\d{3} 555-\d{4}')

    #search a string with our regex
    res = pattern.search('Call me at 401 555-9021 or 310 555-8955')
    print(res.group()) # only yields the first find

    res = pattern.findall('Call me at 401 555-9021 or 310 555-8955')
    print(res) #

def extract_phone(input_str):
    phone_regex = re.compile(r'0\d{3}\d{2}')
    return phone_regex.search(input_str)

def is_valid_phone():
    tel = '0468/13.92.15'
    tel2 = '03/825.20.19'
    tel_re_obj = extract_phone(tel)
    tel2_re_obj = extract_phone(tel2)
    print(f"Tel: {tel_re_obj}")
    print(f"Tel2: {tel2_re_obj}")


is_valid_phone()