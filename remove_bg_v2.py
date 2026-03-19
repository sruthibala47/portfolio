from PIL import Image, ImageChops
import sys

def remove_background(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    
    # Simple threshold is often not enough. Let's try to detect the background color.
    # We assume the top-left pixel is background.
    bg_color = img.getpixel((0, 0))
    
    datas = img.getdata()
    new_data = []
    
    for item in datas:
        # If the pixel is very similar to the background color, make it transparent
        diff = sum(abs(item[i] - bg_color[i]) for i in range(3))
        if diff < 60: # Threshold for similarity
            new_data.append((0, 0, 0, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(output_path, "PNG")

if __name__ == "__main__":
    remove_background(sys.argv[1], sys.argv[2])
