import json

coords = {
    "The Couper Piazza di Spagna": (41.904001, 12.484853),
    "Experience Collection by ROMAC": (41.894251, 12.479932),
    "Residenza Pierret": (41.906250762384396, 12.482559158076091),
    "Navona Stay": (41.89953969278679, 12.473728208370773),
    "Spagna Dream Suites": (41.90397212558183, 12.481641848658658),
    "Trevi Imperial Suite": (41.903189346325334, 12.485695124786874),
    "Spagna Ave": (41.90345900865259, 12.484491925096721),
    "La Foresteria Luxury Suites": (41.90217410336626, 12.483196606752674),
    "Passepartout": (41.89839251006145, 12.470185462205325),
    "NAMAN HOTELLERIE - Roma": (41.907515041285244, 12.480788273426015),
    "Adelaide Suite Dreams": (41.910711826248644, 12.474152486736248),
    "Restart Accommodations Rome": (41.889549992261216, 12.495473744936612),
    "Magenta Deluxe Cancello": (41.90229750180307, 12.473752749849545)
}

with open('hotels_data.json', 'r', encoding='utf-8') as f:
    hotels = json.load(f)

for hotel in hotels:
    for k, v in coords.items():
        if k in hotel['name']:
            hotel['lat'] = v[0]
            hotel['lng'] = v[1]
            print(f"Updated {hotel['name']}")

with open('hotels_data.json', 'w', encoding='utf-8') as f:
    json.dump(hotels, f, indent=4, ensure_ascii=False)
