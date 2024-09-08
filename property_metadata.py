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
    def extract_agent_infor(self,file):
        agent_data_match = re.search(r'"agents":\[.*?\]',file)

        if not agent_data_match: return None

        agent_data_json = "{" + agent_data_match.group(0) + "}"

        agent_data = json.loads(agent_data_json)['agents']

        return agent_data

class Get_infor(object):
    def __init__(self,property_data):
        self.property_data = property_data
    
    def home_infor(self,property_data):
        home_if = {}
        if 'address' in property_data: home_if['Address'] = property_data['address']
        else: home_if['Address'] = None
        if 'bathrooms' in property_data: home_if['Bathrooms'] = property_data['bathrooms']
        else: home_if['Bathrooms'] = None
        if 'bedrooms' in property_data: home_if['Bedrooms'] = property_data['bedrooms']
        else: home_if['Bedrooms'] = None
        if 'parking' in property_data: home_if['Parking'] = property_data['parking']
        else: home_if['Parking'] = None
        return home_if
    def images_infor(self,property_data):
        imgs = property_data['images']
        return imgs

