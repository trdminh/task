import re


def extract_address(filename):
    match = re.search(r'<meta property="og:title" content="(.+?)\s\|', filename)
    return match.group(1)


def extract_number_of_bedroom(filename):
    match = re.search(r'"bedrooms":(\d+)', filename)
    return int(match.group(1))

def extract_number_of_bathroom(filename):
    match = re.search(r'"bathrooms":(\d+)', filename)
    return int(match.group(1))

def extract_number_of_garage(filename):
    match = re.search(r'"parking":(\d+)', filename)
    return int(match.group(1))

def extract_property_type(filename):
    match = re.search(r'"primaryPropertyType":"(\w+)"', filename)
    return match.group(1) 

def extract_date_auction(filename):
    match = re.search(r'"price":"(.+?)"', filename)
    return match.group(1)

def extract_metadata_property(text):
    return {
        "dia_chi": extract_address(text),
        "phong_ngu": extract_number_of_bedroom(text),
        "phong_tam": extract_number_of_bathroom(text),
        "cho_do_xe": extract_number_of_garage(text),
        "loai_bat_dong_san": extract_property_type(text),
        "ngay_dau_gia": extract_date_auction(text)
    }

with open('/home/minh/Documents/Code/python/aihomegroup/input_for_Nazib.txt', 'r') as file:
    text = file.read()
metadata = extract_metadata_property(text)
print(metadata)

