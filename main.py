import download_img
import property_metadata
import json
file_name = '/home/minh/Documents/Code/python/aihomegroup/input_for_Nazib.txt'
with open(file_name, 'r', encoding='utf-8') as file:
    file_content = file.read()

get_metadata = property_metadata.Property(file_content) 
property_data = get_metadata.extract_property_infor(file_content)

## Get agents infor
agent_infor   = get_metadata.extract_agent_infor(file_content)
schools_infor = get_metadata.extract_schools_infor(file_content)

## Get House infor
house_infor = property_metadata.Get_infor(property_data)
house_if    = house_infor.home_infor(property_data)
images      = house_infor.images_infor(property_data)


property_if = {}
property_if['agents']   = agent_infor
property_if['property'] = property_data
property_if['schools']  = schools_infor
print(property_if)
with open('output.txt','w') as f:
    json.dump(property_if, f, indent=0)
# Download image

imgs_folder = download_img.download_images(images)
print(f"Images are downloaded in the folder: {imgs_folder}")

