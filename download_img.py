import requests
import os

def download_images(image_urls, save_dir="images"):
    # Create the directory if it doesn't exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # Loop through the list of image URLs
    for index, url in enumerate(image_urls):
        try:
            # Get the image content
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP errors
            
            # Determine the file name and save path
            file_name = f"image_{index+1}.jpg"  # You can change the extension based on the image type
            file_path = os.path.join(save_dir, file_name)
            
            # Write the image content to a file
            with open(file_path, 'wb') as f:
                f.write(response.content)
                
            print(f"Downloaded {file_name} successfully.")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {url}: {e}")
    
    return save_dir

