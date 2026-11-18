# DIY Cleaners — Build list

## 🔴 Needs you

## 🔵 Build list
(empty)

## 🟡 Hold

## 🟣 Done
### 1.4.1 · build 2026.11.18-4
- [x] MAKE-028 · Dedicated DIY Cleaners Web3Forms key swapped in (was reusing VYBEON Make's) · Build · S · added 2026-11-18

### 1.4.0 · build 2026.11.18-3
- [x] MAKE-027 · Report a problem sends in-app via Web3Forms straight to the VYBEON inbox (success:true before "Sent", Copy report text + clipboard fallback, subject prefix "Cleaners —", problem type kept after it); inbox address removed from the app and repo · Feature · M · added 2026-11-18

### 1.3.2 · build 2026.11.18-2
- [x] MAKE-026 · Report email subject line is exactly "Cleaners" · UI · S · added 2026-11-18

### 1.3.1 · build 2026.11.18-1
- [x] MAKE-025 · "Report a problem" sends a pre-filled email to the VYBEON team (mailto) instead of a GitHub issue · UI · S · added 2026-11-18

### 1.3.0 · build 2026.11.17-4
- [x] MAKE-018 · "Put DIY Cleaners on your Home Screen" banner (DIY Cleaners name and app icon, not VYBEON Make): no app store needed; iPhone: Share, then Add to Home Screen; Android: ⋮, then Install app; dismissible with ✕, hidden once installed (reference: design/home-screen-banner-reference.png) · UI · S · added 2026-11-17
- [x] MAKE-019 · Hero header under the title bar: "Make it yourself" with "Everyday products, with ingredients you can say out loud." (reference: design/hero-header-reference.png) · UI · S · added 2026-11-17
- [x] MAKE-020 · Print button at the bottom of each recipe, or wherever it fits best (today's Print label button sits mid-page, under the recipe card) · UI · S · added 2026-11-17
- [x] MAKE-021 · Costs and savings: give every pantry ingredient a typical US cost, show each recipe's cost per batch next to the store-bought product it replaces, plus a "Saved by making it yourself" running total card (tap "I made this" to count a batch) (reference: design/savings-card-reference.png) · Feature · L · added 2026-11-17
- [x] MAKE-022 · Scramble (minify/obfuscate) the published app code so the live site is unreadable, while the source in GitHub stays readable · Build · M · added 2026-11-17
- [x] MAKE-023 · Keep a private decoder map (readable source + mapping) only in the GitHub repo, excluded from the live site · Build · S · added 2026-11-17
- [x] MAKE-024 · Copyright notice in the app (About and footer) and in the source code · Content · S · added 2026-11-17

### 1.2.0 · build 2026.11.17-3
- [x] MAKE-008 · Create a proper app icon (Home Screen and favicon) in VYBEON style · UI · S · added 2026-11-17
- [x] MAKE-009 · Color theme switcher using the 7 VYBEON ONE swatches (source: design/vybeon-theme-swatches.pdf): Blush #D8DEDA #F7E4DA #F5CAD3 #E7AEB5 #957F86; Midnight #111520 #212C45 #465B75 #788AA8 #EBE7D8; Mocha #E8DED6 #E1CCB4 #D7B795 #A7886C #7A573D #93674A; Coastal #F0A9A0 #F8F0DF #C5EEE4 #B6D7DE #5D636F; Rosewood #F3DBC0 #F0A9AE #C96A7C #963F5F #3F1020; Forest #D9D6D0 #A5B08C #62805C #405842 #384C42; Linen #ECEDE9 #D5CCC3 #F2E9E0 #DFD4CA #D1BCAE · UI · M · added 2026-11-17
- [x] MAKE-010 · Link for reporting problems (from a recipe and the ☰ menu) · UI · S · added 2026-11-17
- [x] MAKE-011 · Liquid glass buttons: a bubble stretches across and springs into place where it applies (nav tabs, category picks) · UI · M · added 2026-11-17
- [x] MAKE-012 · Replace Kitchen, Pets and Bugs category icons with picks K2 fork and knife, P1 paw print, B2 beetle; glow tile on dark swatches, light chip on light swatches (glyphs and tile rules: design/category-icons.py, preview: design/category-icon-options.html) · UI · S · added 2026-11-17
- [x] MAKE-013 · Safety gate on first open: one-time popup ("mixing chemicals can be life threatening") with OK that opens Safety; Safety ends with Accept / Decline; the app stays locked until Accept, and Decline loops back to the warning · Safety · M · added 2026-11-17
- [x] MAKE-014 · What can I make? groups the makeable recipes by category, with a recipe count on each category tile like the Recipes page · UI · S · added 2026-11-17
- [x] MAKE-015 · New title bar with round icon buttons, including a gear that opens a new Settings page (reference: title-bar-reference.png) · UI · M · added 2026-11-17
- [x] MAKE-016 · Redo all remaining app icons in the agreed MAKE-012 style (glow tile on dark swatches, light chip on light) · UI · M · added 2026-11-17
- [x] MAKE-017 · Add Ammonia to the What can I make? ingredient list; ticking it shows a warning popup (never mix with bleach: chloramine gas; ventilate; store apart) that must be acknowledged before it is added · Safety · S · added 2026-11-17

### 1.1.1 · build 2026.11.17-2
- [x] MAKE-005 · (fix) "MAIN" meant the all-recipes list: removed it, so Recipes opens on a category grid (Kitchen, Bathroom, Glass and mirrors…); the never-mix banner is back on top · UI · S · added 2026-11-16

### 1.1.0 · build 2026.11.17-1
- [x] MAKE-007 · Merge the 250 recipes from the VYBEON Clean PDF with the 44-recipe library: 269 total, 24 duplicates combined, 1 left out (DIY hand sanitizer, FDA advises against), #139 relabeled Disinfect → Sanitize, never-mix check on every recipe · Content · L · added 2026-11-17
- [x] MAKE-004 · VYBEON color swatches: navy #071338, glow #22c4ff → #4b6bff → #b04dff, action blue #2fa8ff → #2463ff, glass cards, system font, rounded corners · UI · M · added 2026-11-16
- [x] MAKE-005 · First attempt: removed the never-mix banner (misread; corrected in 1.1.1) · UI · S · added 2026-11-16
- [x] MAKE-006 · ☰ menu with Help and About (version, build, recipe counts and sources, what's new) · UI · M · added 2026-11-16

### 1.0.0 · build 2026.11.16-1
- [x] MAKE-003 · Standalone DIY cleaning app: 44 recipes, 9 categories, Cleans/Sanitizes/Disinfects labels, Safety tab, What can I make?, saved recipes, print labels, offline · UI · L
- [x] MAKE-001 · DIY cleaning recipe library (Claude Doc, content for the app) · Content · L

## ⚪ Dropped
- MAKE-002 · Recipe library built into VYBEON-make v1.4.0 · UI — wrong repo, overwrote an existing app; reverted (commit df9fb8b)

---
Next free ID: MAKE-029
