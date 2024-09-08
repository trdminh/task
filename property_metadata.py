import json
import re

class Property(object):
    def __init__(self,file):
        self.file = file
    
    def extract_property_infor(self,file):
        property_data_match = re.search(r'"property":\{.*?\}', file)
        if not property_data_match: return None

        property_data_json = "{" + property_data_match.group(0) + "}"

        property_data = json.loads(property_data_json)['property']

        return property_data



# Load the content of the file
file_path = '/home/minh/Documents/Code/python/aihomegroup/input_for_Nazib.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()
test = Property(file_content)
# Extract property information
property_info = test.extract_property_infor(file_content)
print(property_info)


def extract_phone_number(text):
    # Regular expression to match phone numbers
    phone_match = re.search(r"\(?\+?\d{1,3}\)?[\s\-]?\(?\d{1,4}\)?[\s\-]?\d{1,4}[\s\-]?\d{1,4}", text)
    phone_number = phone_match.group(0) if phone_match else "N/A"
    return phone_number


# Extract phone number
agent_phone_number = extract_phone_number(file_content)
print(f"Agent's Phone Number: {agent_phone_number}")
