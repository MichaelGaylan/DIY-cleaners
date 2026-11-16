# DIY Cleaners

A small web app for making safe, low-waste household cleaners at home.

- **44 recipes** in 9 categories: all-purpose, degreasers, glass & bathroom, rust & mineral removal, laundry, hand & dish soaps, sanitizers, bugs & pests, aromatic & deodorizers
- Every recipe has ingredients with amounts, steps, uses, storage and shelf life, and safety notes
- **Cleans only / Sanitizes / Disinfects** label on each recipe, so no DIY mix is oversold as a disinfectant
- **Safety** tab: never-mix chart, what really disinfects (CDC and EPA sourced), ground rules, Poison Control
- **What can I make?** Tick what's in your cupboard and see what you can mix now, or with one more item
- Saved recipes, print a bottle label, works offline and installs to the Home Screen

## Run it
Static site. Open `index.html` through any static server, or publish with GitHub Pages (Settings → Pages → main, / root).

## Files
- `index.html`: the whole app
- `data/recipes.json`: all recipes as structured data (IDs R01 to R44 are stable)
- `manifest.webmanifest`, `sw.js`, `icon*`: Home Screen install and offline use

Homemade cleaners aren't lab-tested. Spot-test, label everything, and keep it out of reach of children and pets.
