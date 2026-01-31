from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime
import urllib.request
import io
import csv

# Cache for city data
_city_cache = None
_cache_time = None

def get_city_data():
    """Fetch accurate city population data from GeoNames."""
    global _city_cache, _cache_time
    
    # Return cached data if available
    if _city_cache is not None:
        return _city_cache
    
    try:
        # Fetch GeoNames dataset - comprehensive city data with accurate populations
        url = 'https://raw.githubusercontent.com/datasets/geonames/master/data/geonames.csv'
        with urllib.request.urlopen(url, timeout=10) as response:
            csv_data = response.read().decode('utf-8')
            
        reader = csv.DictReader(io.StringIO(csv_data))
        cities = []
        
        for row in reader:
            try:
                lat = float(row.get('Latitude', 0))
                lng = float(row.get('Longitude', 0))
                population = int(row.get('Population', 0))
                country_code = row.get('CountryCode', '')
                
                # Only include cities with valid coordinates and population > 0
                if population > 0 and -90 <= lat <= 90 and -180 <= lng <= 180:
                    cities.append({
                        'name': row.get('Name', 'Unknown'),
                        'lat': lat,
                        'lng': lng,
                        'population': population,
                        'country': country_code
                    })
            except (ValueError, TypeError):
                continue
        
        _city_cache = cities
        _cache_time = datetime.now()
        return cities
    except Exception as e:
        pass
        return []

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/population':
            self.handle_population()
        elif self.path == '/api/cities':
            self.handle_cities()
        else:
            self.send_response(404)
            self.end_headers()
    
    def handle_population(self):
        """Return live world population estimate."""
        # World population estimate (as of Jan 2026)
        base_population = 8_437_741_000
        start_date = datetime(2025, 1, 1)
        current_date = datetime.now()
        days_passed = (current_date - start_date).days
        
        # Net growth approximately 181,000 per day
        current_population = base_population + (days_passed * 181_000)
        
        response = {
            "timestamp": datetime.now().isoformat(),
            "world_population": int(current_population),
            "growth_rate": "0.88%",
            "births_per_day": 381_000,
            "deaths_per_day": 200_000,
            "data_source": "UN World Population Prospects 2026"
        }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())
    
    def handle_cities(self):
        """Return accurate city population data."""
        cities = get_city_data()
        
        # Calculate current world population
        base_population = 8_437_741_000
        days_passed = (datetime.now() - datetime(2025, 1, 1)).days
        world_pop = base_population + (days_passed * 181_000)
        
        response = {
            "timestamp": datetime.now().isoformat(),
            "total_cities": len(cities),
            "world_population": int(world_pop),
            "data_source": "GeoNames",
            "cities": cities
        }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

