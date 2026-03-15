import json
import urllib.request
import urllib.parse
import time
import re

def get_coordinates(address):
    url = f"https://nominatim.openstreetmap.org/search?q={urllib.parse.quote(address)}&format=json&limit=1"
    headers = {'User-Agent': 'HotelUpdaterScript/2.0'}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            if data:
                return float(data[0]['lat']), float(data[0]['lon'])
    except Exception as e:
        pass
    return None, None

def generate_search_queries(name):
    queries = []
    
    # Clean up standard Rome/Roma
    name_clean = name.replace(" - Roma", "").replace(" - Rome", "")
    
    # 1. Base query with just "Rome"
    queries.append(f"{name_clean}, Rome")
    
    # 2. Strip specific known long bits
    short_name = name_clean
    if "DOWNTOWN SRL - " in short_name:
        short_name = short_name.replace("DOWNTOWN SRL - ", "")
        queries.append(f"{short_name}, Rome")
        if " and " in short_name:
            queries.append(f"{short_name.split(' and ')[0]}, Rome")
            
    if "by Premium Suites Collection" in short_name:
        short_name = short_name.replace(" by Premium Suites Collection", "")
        queries.append(f"{short_name}, Rome")

    if "Experience Collection by " in short_name:
        short_name = short_name.replace("Experience Collection by ", "")
        queries.append(f"{short_name}, Rome")
        
    remove_words = [" Boutique Palace", " Boutique", " Luxury Suites", " Luxury", " Suites", " Suite", " Inn", " Apartments"]
    for word in remove_words:
        if word in short_name:
            stripped = short_name.replace(word, "")
            queries.append(f"{stripped}, Rome")
            
    # Try just the first two words if there are many
    words = short_name.split()
    if len(words) > 2:
        queries.append(f"{words[0]} {words[1]}, Rome")
        if len(words) > 3:
            queries.append(f"{words[0]} {words[1]} {words[2]}, Rome")

    # Remove strict duplicates while preserving order
    seen = set()
    unique_queries = []
    for q in queries:
        if q not in seen:
            seen.add(q)
            unique_queries.append(q)
            
    return unique_queries

with open('hotels_data.json', 'r', encoding='utf-8') as f:
    hotels = json.load(f)

for hotel in hotels:
    if 'lat' in hotel and 'lng' in hotel:
        continue # Already have this one!
        
    print(f"\nMissing coords for: {hotel['name']}")
    queries_to_try = generate_search_queries(hotel['name'])
    
    found = False
    for q in queries_to_try:
        print(f"  Trying query: {q}")
        lat, lng = get_coordinates(q)
        if lat and lng:
            hotel['lat'] = lat
            hotel['lng'] = lng
            print(f"  -> Found! {lat}, {lng}")
            found = True
            break
        time.sleep(1.2) # Sleep to respect rate limits
        
    if not found:
        print("  -> Exhausted all variations.")

# Save back to JSON
with open('hotels_data.json', 'w', encoding='utf-8') as f:
    json.dump(hotels, f, indent=4, ensure_ascii=False)

print("\nDone trying loose terms for coordinates!")
