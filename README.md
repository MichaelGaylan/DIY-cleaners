# DIY Cleaners

A small web app for making safe, low-waste household cleaners at home.

- **269 recipes** in 11 categories: the 250 from *VYBEON Clean: 250 DIY Household Cleaning Recipes* plus 19 from the DIY Cleaners library (24 duplicates combined, 1 left out for safety)
- Every recipe has ingredients with amounts, prepare, apply, limits (surfaces to avoid) and storage
- **CLEANS ONLY / SANITIZE / DISINFECT** label on each recipe, so no DIY mix is oversold as a disinfectant
- **Safety gate**: on first open you read the Safety page and tap Accept before using the app (Decline keeps it locked)
- **Safety** tab: never-mix chart, what really disinfects (CDC and EPA sourced), ground rules, Poison Control
- **What can I make?** Tick what's in your cupboard and see what you can mix now, or with one more item, sorted by category with counts. Ammonia can be ticked only after a bleach warning
- Saved recipes, print a bottle label, works offline and installs to the Home Screen
- Title bar with Help and a Settings gear: 8 color themes (VYBEON plus the 7 VYBEON ONE swatches), Report a problem, Help, About
- VYBEON style: glass cards, icon tiles (glow tile on dark themes, light chip on light themes), liquid glass tab bar

## Run it
Static site. Open `index.html` through any static server, or publish with GitHub Pages (Settings → Pages → main, / root).

## Files
- `index.html`: the whole app
- `data/recipes.json`: all recipes as structured data (recipe numbers 1 to 269 are stable; `merge` records duplicates and what was left out)
- `design/`: theme swatches, icon drawings and approval previews
- `manifest.webmanifest`, `sw.js`, `icon*`: Home Screen install and offline use

Homemade cleaners aren't lab-tested. Spot-test, label everything, and keep it out of reach of children and pets.
