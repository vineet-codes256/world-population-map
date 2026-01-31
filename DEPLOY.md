# Deploy to Vercel

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Deploy:**
   ```bash
   vercel
   ```
   
   Then follow the prompts to connect your GitHub account and deploy.

3. **Your live endpoints:**
   - Map: `https://your-project.vercel.app/`
   - Population API: `https://your-project.vercel.app/api/population`

## Local Testing

To test the API locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run with Vercel CLI
vercel dev
```

Then visit `http://localhost:3000/api/population` to test the endpoint.

## How it works

- The map loads city data and builds a spatial index
- Draw circles on the map to calculate population within that area
- The HUD shows real-time statistics updated live as you edit circles
- The `/api/population` endpoint provides current world population estimates
