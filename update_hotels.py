import json
import urllib.request
import urllib.parse
import time
import re

image_files_str = "Adelaide Suite Dreams01.jpg,Adelaide Suite Dreams02.jpg,Adelaide Suite Dreams03.jpg,Adelaide Suite Dreams04.jpg,Adelaide Suite Dreams05.jpg,Adelaide Suite Dreams06.jpg,Adelaide Suite Dreams07.jpg,Adelaide Suite Dreams08.jpg,Adelaide Suite Dreams09.jpg,Adelaide Suite Dreams10.jpg,Adelaide Suite Dreams11.jpg,Adelaide Suite Dreams12.jpg,Adelaide Suite Dreams13.jpg,Adelaide Suite Dreams14.jpg,Albergo Ottocento01.jpg,Albergo Ottocento02.jpg,Albergo Ottocento03.jpg,Albergo Ottocento04.jpg,Albergo Ottocento05.jpg,Albergo Ottocento06.jpg,Albergo Ottocento07.jpg,Albergo Ottocento08.jpg,Albergo Ottocento09.jpg,Albergo Ottocento10.jpg,Albergo Ottocento11.jpg,Albergo Ottocento12.jpg,Albergo Ottocento13.jpg,Albergo Ottocento14.jpg,Albergo Ottocento15.jpg,Albergo Ottocento16.jpg,Babuino 7901.jpg,Babuino 7902.jpg,Babuino 7903.jpg,Babuino 7904.jpg,Babuino 7905.jpg,Babuino 7906.jpg,Babuino 7907.jpg,Babuino 7908.jpg,Babuino 7909.jpg,Babuino 7910.jpg,Babuino 7911.jpg,Babuino 7912.jpg,Babuino 7913.jpg,Babuino 7914.jpg,Babuino 7915.jpg,Babuino 7916.jpg,Barberini Retreat Boutique Hotel01.jpg,Barberini Retreat Boutique Hotel02.jpg,Barberini Retreat Boutique Hotel03.jpg,Barberini Retreat Boutique Hotel04.jpg,Barberini Retreat Boutique Hotel05.jpg,Barberini Retreat Boutique Hotel06.jpg,Barberini Retreat Boutique Hotel07.jpg,Barberini Retreat Boutique Hotel08.jpg,Barberini Retreat Boutique Hotel09.jpg,Barberini Retreat Boutique Hotel10.jpg,Barberini Retreat Boutique Hotel11.jpg,Barberini Retreat Boutique Hotel12.jpg,Barberini Retreat Boutique Hotel13.jpg,Barberini Retreat Boutique Hotel14.jpg,Barberini Retreat Boutique Hotel15.jpg,Barberini Retreat Boutique Hotel16.jpg,Barberini Retreat Boutique Hotel17.jpg,Barberini Retreat Boutique Hotel18.jpg,Barberini Retreat Boutique Hotel19.jpg,Barberini Retreat Boutique Hotel20.jpg,Barberini Retreat Boutique Hotel21.jpg,Esposizione Luxury Rome01.jpg,Esposizione Luxury Rome02.jpg,Esposizione Luxury Rome03.jpg,Esposizione Luxury Rome04.jpg,Esposizione Luxury Rome05.jpg,Esposizione Luxury Rome06.jpg,Esposizione Luxury Rome07.jpg,Esposizione Luxury Rome08.jpg,Esposizione Luxury Rome09.jpg,Esposizione Luxury Rome10.jpg,Esposizione Luxury Rome11.jpg,Esposizione Luxury Rome12.jpg,Esposizione Luxury Rome13.jpg,Experience Collection by ROMAC1.avif,Experience Collection by ROMAC2.avif,Experience Collection by ROMAC3.avif,Experience Collection by ROMAC4.avif,Experience Collection by ROMAC5.avif,Experience Collection by ROMAC6.avif,Experience Collection by ROMAC7.avif,Experience Collection by ROMAC8.avif,Experience Collection by ROMAC9.avif,Gambero Apartments01.jpg,Gambero Apartments02.jpg,Gambero Apartments03.jpg,Gambero Apartments04.jpg,Gambero Apartments05.jpg,Gambero Apartments06.jpg,Gambero Apartments07.jpg,Gambero Apartments08.jpg,Gambero Apartments09.jpg,Gambero Apartments10.jpg,Gambero Apartments11.jpg,Gambero Apartments12.jpg,Gambero Apartments13.jpg,Gambero Apartments14.jpg,Gambero Apartments15.jpg,Gambero Apartments16.jpg,Gonfalone 601.jpg,Gonfalone 602.jpg,Gonfalone 603.jpg,Gonfalone 604.jpg,Gonfalone 605.jpg,Gonfalone 606.jpg,Gonfalone 607.jpg,Gonfalone 608.jpg,Gonfalone 609.jpg,Gonfalone 610.jpg,Gonfalone 611.jpg,Gonfalone 612.jpg,Gonfalone 613.jpg,Gonfalone 614.jpg,Hotel Castellino Roma01.jpg,Hotel Castellino Roma02.jpg,Hotel Castellino Roma03.jpg,Hotel Castellino Roma04.jpg,Hotel Castellino Roma05.jpg,Hotel Castellino Roma06.jpg,Hotel Castellino Roma07.jpg,Hotel Castellino Roma08.jpg,Hotel Castellino Roma09.jpg,Hotel Castellino Roma10.jpg,Hotel Castellino Roma11.jpg,Hotel Castellino Roma12.jpg,Hotel Castellino Roma13.jpg,Hotel Castellino Roma14.jpg,Hotel Castellino Roma15.jpg,Hotel Castellino Roma16.jpg,Hotel Erdarelli01.jpg,Hotel Erdarelli02.jpg,Hotel Erdarelli03.jpg,Hotel Erdarelli04.jpg,Hotel Erdarelli05.jpg,Hotel Erdarelli06.jpg,Hotel Erdarelli07.jpg,Hotel Erdarelli08.jpg,Hotel Erdarelli09.jpg,Hotel Erdarelli10.jpg,Hotel Erdarelli11.jpg,Hotel Hiberia01.jpg,Hotel Hiberia02.jpg,Hotel Hiberia03.jpg,Hotel Hiberia04.jpg,Hotel Hiberia05.jpg,Hotel Hiberia06.jpg,Hotel Hiberia07.jpg,Hotel Hiberia08.jpg,Hotel Hiberia09.jpg,Hotel Hiberia10.jpg,Hotel Hiberia11.jpg,Hotel Hiberia12.jpg,Hotel Hiberia13.jpg,Hotel Hiberia14.jpg,Hotel Hiberia15.jpg,Hotel Hiberia16.jpg,La Foresteria Luxury Suites01.jpg,La Foresteria Luxury Suites02.jpg,La Foresteria Luxury Suites03.jpg,La Foresteria Luxury Suites04.jpg,La Foresteria Luxury Suites05.jpg,La Foresteria Luxury Suites06.jpg,La Foresteria Luxury Suites07.jpg,La Foresteria Luxury Suites08.jpg,La Foresteria Luxury Suites09.jpg,La Foresteria Luxury Suites10.jpg,La Foresteria Luxury Suites11.jpg,La Foresteria Luxury Suites12.jpg,La Foresteria Luxury Suites13.jpg,La Foresteria Luxury Suites14.jpg,La Foresteria Luxury Suites15.jpg,La Foresteria Luxury Suites16.jpg,Magenta Deluxe Cancello01.jpg,Magenta Deluxe Cancello02.jpg,Magenta Deluxe Cancello03.jpg,Magenta Deluxe Cancello04.jpg,Magenta Deluxe Cancello05.jpg,Magenta Deluxe Cancello06.jpg,Magenta Deluxe Cancello07.jpg,Magenta Deluxe Cancello08.jpg,Magenta Deluxe Cancello09.jpg,Magenta Deluxe Cancello10.jpg,Magenta Deluxe Cancello11.jpg,Magenta Deluxe Cancello12.jpg,Magenta Deluxe Cancello13.jpg,Magenta Deluxe Cancello14.jpg,Magenta Deluxe Cancello15.jpg,Magenta Deluxe Cancello16.jpg,Muzio 48 Private Suites by Premium Suites Collection01.jpg,Muzio 48 Private Suites by Premium Suites Collection02.jpg,Muzio 48 Private Suites by Premium Suites Collection03.jpg,Muzio 48 Private Suites by Premium Suites Collection04.jpg,Muzio 48 Private Suites by Premium Suites Collection05.jpg,Muzio 48 Private Suites by Premium Suites Collection06.jpg,Muzio 48 Private Suites by Premium Suites Collection07.jpg,Muzio 48 Private Suites by Premium Suites Collection08.jpg,Muzio 48 Private Suites by Premium Suites Collection09.jpg,Muzio 48 Private Suites by Premium Suites Collection10.jpg,Muzio 48 Private Suites by Premium Suites Collection11.jpg,Muzio 48 Private Suites by Premium Suites Collection12.jpg,Muzio 48 Private Suites by Premium Suites Collection13.jpg,Muzio 48 Private Suites by Premium Suites Collection14.jpg,Muzio 48 Private Suites by Premium Suites Collection15.jpg,Muzio 48 Private Suites by Premium Suites Collection16.jpg,NAMAN HOTELLERIE - Roma1.jpg,NAMAN HOTELLERIE - Roma2.jpg,NAMAN HOTELLERIE - Roma3.jpg,NAMAN HOTELLERIE - Roma4.jpg,NAMAN HOTELLERIE - Roma5.jpg,NAMAN HOTELLERIE - Roma6.jpg,NAMAN HOTELLERIE - Roma7.jpg,Navona Palace Luxury Inn1.jpg,Navona Palace Luxury Inn2.jpg,Navona Palace Luxury Inn3.jpg,Navona Palace Luxury Inn4.jpg,Navona Palace Luxury Inn5.jpg,Navona Palace Luxury Inn6.jpg,Navona Palace Luxury Inn7.jpg,Navona Palace Luxury Inn8.jpg,Navona Stay01.jpg,Navona Stay02.jpg,Navona Stay03.jpg,Navona Stay04.jpg,Navona Stay05.jpg,Navona Stay06.jpg,Navona Stay07.jpg,Navona Stay08.jpg,Navona Stay09.jpg,Navona Stay10.jpg,Navona Stay11.jpg,Pantheon Inn01.jpg,Pantheon Inn02.jpg,Pantheon Inn03.jpg,Pantheon Inn04.jpg,Pantheon Inn05.jpg,Pantheon Inn06.jpg,Pantheon Inn07.jpg,Pantheon Inn08.jpg,Pantheon Inn09.jpg,Pantheon Inn10.jpg,Pantheon Inn11.jpg,Pantheon Inn12.jpg,Passepartout01.jpg,Passepartout02.jpg,Passepartout03.jpg,Passepartout04.jpg,Passepartout05.jpg,Passepartout06.jpg,Passepartout07.jpg,Passepartout08.jpg,Passepartout09.jpg,Passepartout10.jpg,Passepartout11.jpg,Passepartout12.jpg,Passepartout13.jpg,Passpartout Boutique Palace01.jpg,Passpartout Boutique Palace02.jpg,Passpartout Boutique Palace03.jpg,Passpartout Boutique Palace04.jpg,Passpartout Boutique Palace05.jpg,Passpartout Boutique Palace06.jpg,Passpartout Boutique Palace07.jpg,Passpartout Boutique Palace08.jpg,Passpartout Boutique Palace09.jpg,Passpartout Boutique Palace10.jpg,Piazza Venezia Grand Suite01.jpg,Piazza Venezia Grand Suite02.jpg,Piazza Venezia Grand Suite03.jpg,Piazza Venezia Grand Suite04.jpg,Piazza Venezia Grand Suite05.jpg,Piazza Venezia Grand Suite06.jpg,Piazza Venezia Grand Suite07.jpg,Piazza Venezia Grand Suite08.jpg,Piazza Venezia Grand Suite09.jpg,Piazza Venezia Grand Suite10.jpg,Piazza Venezia Grand Suite11.jpg,Piazza Venezia Grand Suite12.jpg,Piazza Venezia Grand Suite13.jpg,Piazza Venezia Grand Suite14.jpg,Piazza Venezia Grand Suite15.jpg,Piccola Navona Roof Garden01.jpg,Piccola Navona Roof Garden02.jpg,Piccola Navona Roof Garden03.jpg,Piccola Navona Roof Garden04.jpg,Piccola Navona Roof Garden05.jpg,Piccola Navona Roof Garden06.jpg,Piccola Navona Roof Garden07.jpg,Piccola Navona Roof Garden08.jpg,Piccola Navona Roof Garden09.jpg,Piccola Navona Roof Garden10.jpg,Piccola Navona Roof Garden11.jpg,Piccola Navona Roof Garden12.jpg,Piccola Navona Roof Garden13.jpg,Piccola Navona Roof Garden14.jpg,Piccola Navona Roof Garden15.jpg,Piccola Navona Roof Garden16.jpg,Residenza Pierret1.jpg,Residenza Pierret2.jpg,Residenza Pierret3.jpg,Residenza Pierret4.jpg,Residenza Pierret5.jpg,Residenza Pierret6.jpg,Residenza Pierret7.jpg,Residenza Pierret8.jpg,Residenza Pierret9.jpg,Restart Accommodations Rome01.jpg,Restart Accommodations Rome02.jpg,Restart Accommodations Rome03.jpg,Restart Accommodations Rome04.jpg,Restart Accommodations Rome05.jpg,Restart Accommodations Rome06.jpg,Restart Accommodations Rome07.jpg,Restart Accommodations Rome08.jpg,Restart Accommodations Rome09.jpg,Restart Accommodations Rome10.jpg,Restart Accommodations Rome11.jpg,Rome River Inn01.jpg,Rome River Inn02.jpg,Rome River Inn03.jpg,Rome River Inn04.jpg,Rome River Inn05.jpg,Rome River Inn06.jpg,Rome River Inn07.jpg,Rome River Inn08.jpg,Rome River Inn09.jpg,Rome River Inn10.jpg,Spagna Ave01.jpg,Spagna Ave02.jpg,Spagna Ave03.jpg,Spagna Ave04.jpg,Spagna Ave05.jpg,Spagna Ave06.jpg,Spagna Ave07.jpg,Spagna Ave08.jpg,Spagna Ave09.jpg,Spagna Ave10.jpg,Spagna Ave11.jpg,Spagna Dream Suites01.jpg,Spagna Dream Suites02.jpg,Spagna Dream Suites03.jpg,Spagna Dream Suites04.jpg,Spagna Dream Suites05.jpg,Spagna Dream Suites06.jpg,Spagna Dream Suites07.jpg,Spagna Dream Suites08.jpg,Spagna Dream Suites09.jpg,Spagna Dream Suites10.jpg,Spagna Dream Suites11.jpg,Spagna Dream Suites12.jpg,Spagna Dream Suites13.jpg,Spagna Dream Suites14.jpg,The Code Hotel01.jpg,The Code Hotel02.jpg,The Code Hotel03.jpg,The Code Hotel04.jpg,The Code Hotel05.jpg,The Code Hotel06.jpg,The Code Hotel07.jpg,The Code Hotel08.jpg,The Code Hotel09.jpg,The Code Hotel10.jpg,The Code Hotel11.jpg,The Code Hotel12.jpg,The Code Hotel13.jpg,The Code Hotel14.jpg,The Code Hotel15.jpg,The Code Hotel16.jpg,The Couper Piazza di Spagna1.webp,The Couper Piazza di Spagna2.avif,The Couper Piazza di Spagna3.avif,The Couper Piazza di Spagna4.avif,The Couper Piazza di Spagna5.avif,The Couper Piazza di Spagna5.webp,The Couper Piazza di Spagna6.avif,The Couper Piazza di Spagna7.avif,The Couper Piazza di Spagna8.avif,The Couper Piazza di Spagna9.webp,Tree Charme Augusto Boutique Hotel01.jpg,Tree Charme Augusto Boutique Hotel02.jpg,Tree Charme Augusto Boutique Hotel03.jpg,Tree Charme Augusto Boutique Hotel04.jpg,Tree Charme Augusto Boutique Hotel05.jpg,Tree Charme Augusto Boutique Hotel06.jpg,Tree Charme Augusto Boutique Hotel07.jpg,Tree Charme Augusto Boutique Hotel08.jpg,Tree Charme Augusto Boutique Hotel09.jpg,Tree Charme Augusto Boutique Hotel10.jpg,Tree Charme Augusto Boutique Hotel11.jpg,Tree Charme Augusto Boutique Hotel12.jpg,Tree Charme Augusto Boutique Hotel13.jpg,Trevi Imperial Suite 21.jpg,Trevi Imperial Suite 22.jpg,Trevi Imperial Suite 23.jpg,Trevi Imperial Suite 24.jpg,Trevi Imperial Suite 25.jpg,Trevi Imperial Suite 26.jpg,Trevi Imperial Suite 27.jpg,Trevi Imperial Suite 28.jpg,Via Del Corso Home Roma1.jpg,Via Del Corso Home Roma2.jpg,Via Del Corso Home Roma3.jpg,Via Del Corso Home Roma4.jpg,Via Del Corso Home Roma5.jpg,Via Del Corso Home Roma6.jpg,Via Del Corso Home Roma7.jpg"

image_files = image_files_str.split(',')

def get_hotel_name_from_image(image_name):
    # Remove numbers and extensions from the end
    # e.g., "Adelaide Suite Dreams01.jpg" -> "Adelaide Suite Dreams"
    name = re.sub(r'\d+\.(jpg|avif|webp)$', '', image_name)
    return name.strip()

image_map = {}
for img in image_files:
    hotel_name_key = get_hotel_name_from_image(img).lower()
    if hotel_name_key not in image_map:
        image_map[hotel_name_key] = []
    image_map[hotel_name_key].append(img)

def get_coordinates(address):
    url = f"https://nominatim.openstreetmap.org/search?q={urllib.parse.quote(address)}&format=json&limit=1"
    headers = {'User-Agent': 'HotelUpdaterScript/1.0'}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            if data:
                return float(data[0]['lat']), float(data[0]['lon'])
    except Exception as e:
        print(f"Error fetching coordinates for {address}: {e}")
    return None, None

with open('hotels_data.json', 'r', encoding='utf-8') as f:
    hotels = json.load(f)

for hotel in hotels:
    hotel_name_lower = hotel['name'].lower()
    
    # Try to find matching images
    best_match_key = None
    for key in image_map.keys():
        if key in hotel_name_lower or hotel_name_lower in key or \
           hotel_name_lower.replace(' ', '') in key.replace(' ', ''):
            best_match_key = key
            break
            
    # Some hardcoded fallbacks
    if not best_match_key:
        if "downtown srl" in hotel_name_lower:
            pass # No images provided?
        elif "castellino" in hotel_name_lower:
            best_match_key = "hotel castellino roma"
        elif "tree charme augusto" in hotel_name_lower:
            best_match_key = "tree charme augusto boutique hotel"
        elif "gambero" in hotel_name_lower:
            best_match_key = "gambero apartments"
        elif "erdarelli" in hotel_name_lower:
            best_match_key = "hotel erdarelli"
        elif "hiberia" in hotel_name_lower:
            best_match_key = "hotel hiberia"

    if best_match_key and best_match_key in image_map:
        hotel['images'] = image_map[best_match_key]
    else:
        print(f"No images found for: {hotel['name']}")
        
    print(f"Assigning images for {hotel['name']} (Count: {len(hotel.get('images', []))})")

    # Geocoding
    search_query = hotel['name'] + ", Rome, Italy"
    print(f"Fetching coordinates for: {search_query}")
    lat, lng = get_coordinates(search_query)
    
    if lat and lng:
        hotel['lat'] = lat
        hotel['lng'] = lng
        print(f"Found: {lat}, {lng}")
    else:
        print("Failed to find coordinates.")
    
    time.sleep(1.5) # respect Nominatim rate limits

with open('hotels_data.json', 'w', encoding='utf-8') as f:
    json.dump(hotels, f, indent=4, ensure_ascii=False)

print("Done updating hotels_data.json!")
