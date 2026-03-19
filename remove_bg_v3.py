from PIL import Image, ImageDraw
import sys

def remove_background_flood(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size
    
    # We create a mask for the background
    # Assume the four corners are background
    bg_seeds = [(0, 0), (width-1, 0), (0, height-1), (width-1, height-1)]
    
    # We use ImageDraw.floodfill or a custom flood fill to find the background
    # Let's use a simpler approach: any pixel connected to the edge with a color similar to corner
    
    # For a more robust result, we can use a small threshold
    # But for a white background, even simple flood fill starting from (0,0) is good.
    
    # Using a library like PIL's floodfill? No, let's just do a manual BFS/DFS for the mask.
    mask = Image.new('L', (width, height), 0) # 0 is foreground, 255 is background
    visited = set()
    
    target_color = img.getpixel((0, 0)) # Start pixel color
    stack = bg_seeds
    
    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        curr_color = img.getpixel((x, y))
        # Similarity check
        diff = sum(abs(curr_color[i] - target_color[i]) for i in range(3))
        if diff < 100: # Decent threshold for white-ish backgrounds
            mask.putpixel((x, y), 255)
            # Add neighbors
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in visited:
                    stack.append((nx, ny))
    
    # Apply mask
    datas = img.getdata()
    mask_datas = mask.getdata()
    new_data = []
    for i in range(len(datas)):
        if mask_datas[i] == 255:
            new_data.append((0, 0, 0, 0)) # Transparent
        else:
            new_data.append(datas[i])
            
    img.putdata(new_data)
    img.save(output_path, "PNG")

if __name__ == "__main__":
    remove_background_flood(sys.argv[1], sys.argv[2])
