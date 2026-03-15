import json

with open('hotels_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

short_names = {
    'The Couper Piazza di Spagna': 'Couper',
    'Experience Collection by ROMAC': 'ROMAC',
    'DOWNTOWN SRL - The Great Court and The Great Chill': 'Downtown',
    'Via Del Corso Home Roma': 'Corso',
    'Gambero Apartments': 'Gambero',
    'Castellino Roma': 'Castellino'[:10],
    'Pantheon Inn': 'Pantheon',
    'Tree Charme Augusto Boutique': 'Charme',
    'Residenza Pierret': 'Pierret',
    'Piccola Navona Roof Garden': 'Piccola',
    'Babuino 79': 'Babuino',
    'Albergo Ottocento': 'Ottocento',
    'Piazza Venezia Grand Suite': 'Venezia',
    'Passpartout Boutique Palace': 'Passpartou'[:10],
    'Navona Stay': 'Navona S',
    'Navona Palace Luxury Inn': 'Navona P',
    'Esposizione Luxury Rome': 'Esposizion'[:10],
    'Spagna Dream Suites': 'Spagna DS',
    'Trevi Imperial Suite': 'Trevi',
    'Spagna Ave': 'Spagna Ave',
    'La Foresteria Luxury Suites': 'Foresteria'[:10],
    'Rome River Inn': 'River Inn',
    'Passepartout': 'Passeparto'[:10],
    'NAMAN HOTELLERIE - Roma': 'NAMAN',
    'Adelaide Suite Dreams': 'Adelaide',
    'Hiberia': 'Hiberia',
    'Restart Accommodations Rome': 'Restart',
    'The Code': 'The Code',
    'Barberini Retreat Boutique': 'Barberini',
    'Erdarelli': 'Erdarelli',
    'Gonfalone 6': 'Gonfalone',
    'Magenta Deluxe Cancello': 'Magenta',
    'Muzio 48 Private Suites by Premium Suites Collection': 'Muzio'
}

for h in data:
    h['short_name'] = short_names.get(h['name'], h['name'][:10].strip())

with open('hotels_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)
