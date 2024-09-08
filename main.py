import download_img
import property_metadata

file_name = '/home/minh/Documents/Code/python/aihomegroup/input_for_Nazib.txt'
with open(file_name, 'r', encoding='utf-8') as file:
    file_content = file.read()

get_metadata = property_metadata.Property(file_content) 
property_data = get_metadata.extract_property_infor(file_content)

## Get agents infor
agent_infor   = get_metadata.extract_agent_infor(file_content)
print(agent_infor)
## Get House infor
house_infor = property_metadata.Get_infor(property_data)
house_if    = house_infor.home_infor(property_data)
images      = house_infor.images_infor(property_data)
print(house_if)

# Download image

imgs_folder = download_img.download_images(images)
print(f"Images are downloaded in the folder: {imgs_folder}")

