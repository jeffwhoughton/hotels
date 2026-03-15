import json
import urllib.request
import re
import time

def extract_coords_from_booking(html):
    # Try different patterns
    match = re.search(r'data-atlas-latlng="([^"]+)"', html)
    if match:
        lat, lng = match.group(1).split(',')
        return float(lat), float(lng)
    
    match = re.search(r'"latitude":([0-9.]+),"longitude":([0-9.]+)', html)
    if match:
        return float(match.group(1)), float(match.group(2))
        
    match = re.search(r'b_map_center_lat\s*=\s*([0-9.]+)', html)
    match2 = re.search(r'b_map_center_lon\s*=\s*([0-9.]+)', html)
    if match and match2:
        return float(match.group(1)), float(match2.group(1))
        
    return None, None

def extract_coords_from_expedia(html):
    match = re.search(r'"lat":\s*"*([0-9.]+)"*,\s*"long":\s*"*([0-9.]+)"*', html)
    if match:
        return float(match.group(1)), float(match.group(2))
    
    match = re.search(r'coordinates":\{"latitude":([0-9.]+),"longitude":([0-9.]+)', html)
    if match:
        return float(match.group(1)), float(match.group(2))
        
    return None, None

with open('hotels_data.json', 'r', encoding='utf-8') as f:
    hotels = json.load(f)

for hotel in hotels:
    if 'lat' in hotel and 'lng' in hotel:
        continue
        
    print(f"Trying to find coords for {hotel['name']}...")
    url = hotel['url']
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
            lat, lng = None, None
            if 'booking.com' in url:
                lat, lng = extract_coords_from_booking(html)
            elif 'expedia.ca' in url or 'expedia.com' in url:
                lat, lng = extract_coords_from_expedia(html)
                
            if lat and lng:
                hotel['lat'] = lat
                hotel['lng'] = lng
                print(f"Found coords: {lat}, {lng}")
            else:
                print("Could not parse coords from HTML.")
    except Exception as e:
        print(f"Error fetching URL: {e}")
        
    time.sleep(1)

with open('hotels_data.json', 'w', encoding='utf-8') as f:
    json.dump(hotels, f, indent=4, ensure_ascii=False)

print("Finished second pass.")