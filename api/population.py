from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime

# For production, you'd use: from worldometer.world import WorldCounters
# For now, we'll return a realistic estimate that updates based on time

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # World population estimate (as of Jan 2026)
        # Based on ~8.3B at start of 2024, growing at ~0.88% annually
        base_population = 8_300_000_000
        start_date = datetime(2024, 1, 1)
        current_date = datetime.now()
        days_passed = (current_date - start_date).days
        
        # Add ~81,000 births per day (roughly 2.5B births/year)
        current_population = base_population + (days_passed * 181_000)  # net growth ~181k/day
        
        response = {
            "timestamp": datetime.now().isoformat(),
            "world_population": int(current_population),
            "growth_rate": "0.88%",
            "births_per_day": 381_000,
            "deaths_per_day": 200_000
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
