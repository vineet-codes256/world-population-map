# World Population Map

An interactive world population visualization using Leaflet, D3.js, and a custom spatial grid index.

## Features

- **Interactive Map**: Built with Leaflet.js and CartoDB Dark tiles
- **Draw Tools**: Use Leaflet.Draw to create circles on the map
- **Population Analysis**: Automatically calculates total population within drawn circles
- **Spatial Grid Index**: Custom JavaScript implementation for efficient querying of 20,000+ cities
- **Real-time Statistics HUD**: Displays:
  - Total population in selected areas
  - Number of cities
  - Percentage of world population (8.3B baseline)
- **Heatmap Overlay**: Visual population density representation
- **Public Dataset**: Loads world cities data via D3.js from public CSV

## Usage

Simply open `index.html` in a web browser. The map will:
1. Load automatically with CartoDB Dark tiles
2. Fetch world cities data (20,000+ cities with population data)
3. Build a spatial grid index for efficient calculations
4. Display a heatmap overlay showing population density

### Drawing Circles

1. Click the circle icon in the draw toolbar (top-left)
2. Click on the map to set the center
3. Drag to set the radius
4. Release to complete the circle
5. The HUD (top-right) updates automatically with statistics

### Editing/Deleting

- Use the edit tool (polygon icon) to modify circles
- Use the delete tool (trash icon) to remove circles
- Statistics update in real-time

## Technical Implementation

### Spatial Grid Index

The custom `SpatialGridIndex` class divides the world into grid cells for O(1) lookup performance:
- Grid cells are 1° x 1° by default
- Uses Haversine formula for accurate distance calculations
- Efficiently queries only relevant cells when calculating populations

### Performance

- Handles 20,000+ cities smoothly
- Sub-second query times for circle intersections
- Optimized for multiple overlapping circles

## Technologies

- **Leaflet.js**: Map rendering and interaction
- **Leaflet.Draw**: Drawing tools
- **Leaflet.heat**: Heatmap visualization
- **D3.js**: CSV data loading and parsing
- **CartoDB**: Dark theme base tiles