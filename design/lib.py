import json,sys
OUT=sys.argv[1]
def L(h):
  h=h.lstrip('#');c=[int(h[i:i+2],16)/255 for i in (0,2,4)]
  c=[x/12.92 if x<=.03928 else ((x+.055)/1.055)**2.4 for x in c];return .2126*c[0]+.7152*c[1]+.0722*c[2]
cr=lambda a,b:(max(L(a),L(b))+.05)/(min(L(a),L(b))+.05)
NAVY="#071338"
THEMES=[("VYBEON",["#071338","#0d1d4f","#16265e"]),
("Blush",["#D8DEDA","#F7E4DA","#F5CAD3","#E7AEB5","#957F86"]),
("Midnight",["#111520","#212C45","#465B75","#788AA8","#EBE7D8"]),
("Mocha",["#E8DED6","#E1CCB4","#D7B795","#A7886C","#7A573D","#93674A"]),
("Coastal",["#F0A9A0","#F8F0DF","#C5EEE4","#B6D7DE","#5D636F"]),
("Rosewood",["#F3DBC0","#F0A9AE","#C96A7C","#963F5F","#3F1020"]),
("Forest",["#D9D6D0","#A5B08C","#62805C","#405842","#384C42"]),
("Linen",["#ECEDE9","#D5CCC3","#F2E9E0","#DFD4CA","#D1BCAE"])]
# glyphs: 24x24, drawn with currentColor strokes; 'F' marks filled shapes
G={
"K1":('Pot with steam','<path d="M4 11h16v4.5a4.5 4.5 0 0 1-4.5 4.5h-7A4.5 4.5 0 0 1 4 15.5z"/><path d="M1.5 12.5H4M20 12.5h2.5"/><path d="M8.5 3.5c-1 1.3 1 2.2 0 4M12 3c-1 1.3 1 2.2 0 4M15.5 3.5c-1 1.3 1 2.2 0 4"/>'),
"K2":('Fork and knife','<path d="M5 3v4.5a2.5 2.5 0 0 0 5 0V3M7.5 3v18"/><path d="M17 21V3c2.5 1.5 3.5 5 3.5 9H17"/>'),
"K3":('Chef hat','<path d="M7 14.5a4 4 0 1 1 1.6-7.7 4 4 0 0 1 6.8 0A4 4 0 1 1 17 14.5z"/><path d="M7 14.5V20h10v-5.5M7 17.5h10"/>'),
"P1":('Paw print','<g fill="currentColor" stroke="none"><circle cx="5.5" cy="10" r="2.1"/><circle cx="9.3" cy="5.6" r="2.1"/><circle cx="14.7" cy="5.6" r="2.1"/><circle cx="18.5" cy="10" r="2.1"/><path d="M12 11c-3.2 0-6 3.8-6 6.4 0 1.7 1.3 2.8 2.9 2.8 1.2 0 2-.6 3.1-.6s1.9.6 3.1.6c1.6 0 2.9-1.1 2.9-2.8 0-2.6-2.8-6.4-6-6.4z"/></g>'),
"P2":('Dog face','<path d="M7 6.5C5 5 2.5 5.5 2.5 9c0 2.5 1.2 4 2.5 4.2M17 6.5C19 5 21.5 5.5 21.5 9c0 2.5-1.2 4-2.5 4.2"/><path d="M6.5 7.5C8 6 9.8 5 12 5s4 1 5.5 2.5V14a5.5 5.5 0 0 1-11 0z"/><g fill="currentColor" stroke="none"><circle cx="9.5" cy="11" r="1.1"/><circle cx="14.5" cy="11" r="1.1"/><path d="M10.4 14.2h3.2L12 16z"/></g>'),
"P3":('Bowl and bone','<path d="M2.5 13.5h19l-2.2 6.5H4.7z"/><path d="M8.5 8.5h7"/><g fill="currentColor" stroke="none"><circle cx="7.3" cy="7.3" r="1.5"/><circle cx="7.3" cy="9.7" r="1.5"/><circle cx="16.7" cy="7.3" r="1.5"/><circle cx="16.7" cy="9.7" r="1.5"/></g>'),
"B1":('Ant','<g fill="currentColor" stroke="none"><circle cx="18.6" cy="10.4" r="2.3"/><ellipse cx="13.2" cy="12" rx="2.3" ry="1.7"/><ellipse cx="6.3" cy="12.4" rx="3.9" ry="2.9"/></g><path d="M9 12.2h8M12.2 13.3l-2.6 5.7M13.2 13.6v5.9M14.2 13.3l2.8 5.7M19.6 8.4c.6-1.8 1.6-3 2.9-3.4M18 8.2c-.1-1.9.5-3.4 1.6-4.4"/>'),
"B2":('Beetle','<path d="M12 7.5c3.6 0 6 3 6 6.8 0 3.6-2.6 6.2-6 6.2s-6-2.6-6-6.2c0-3.8 2.4-6.8 6-6.8z"/><path d="M9.2 8.2a2.8 2.8 0 0 1 5.6 0M12 8v12.3M10 5.4 8.5 3M14 5.4 15.5 3M6 12H2.8M6.2 16.5 3.2 18.5M18 12h3.2M17.8 16.5l3 2"/><g fill="currentColor" stroke="none"><circle cx="9.3" cy="12.6" r="1"/><circle cx="14.7" cy="12.6" r="1"/><circle cx="9.5" cy="16.6" r="1"/><circle cx="14.5" cy="16.6" r="1"/></g>'),
"B3":('Bug with stop badge','<g fill="currentColor" stroke="none"><ellipse cx="10" cy="11.5" rx="4.3" ry="5.2"/><circle cx="10" cy="4.9" r="2.3"/></g><path d="M5.7 8.6 2.8 7M5.6 11.8H2.4M6 15l-2.6 2M14.3 8.6 17.2 7M14.4 11.8h2.4M8.6 3 7.4 1.4M11.4 3l1.2-1.6"/><circle cx="17.6" cy="17.6" r="5.6" fill="HALO" stroke="HALO" stroke-width="2.4"/><circle cx="17.6" cy="17.6" r="4.4"/><path d="M14.5 14.5l6.2 6.2"/>'),
}
CATS=[("Kitchen & food prep","🍳",["K1","K2","K3"]),("Pet areas & pet laundry","🐾",["P1","P2","P3"]),("Bugs & pests","🐜",["B1","B2","B3"])]
# Style A: white glyph on deep VYBEON gradient tile, double ring (white inner, navy outer)
# Style B: navy glyph on white chip, gradient inner ring, navy outer ring
def icon(key,style,size):
  g=G[key][1]; uid=f"{key}{style}{size}{icon.n}"; icon.n+=1
  if style=="A":
    tile=f'<defs><linearGradient id="g{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3a55e8"/><stop offset="1" stop-color="#8338d6"/></linearGradient></defs><rect x="1" y="1" width="30" height="30" rx="9" fill="url(#g{uid})" stroke="{NAVY}" stroke-width="2"/><rect x="2.6" y="2.6" width="26.8" height="26.8" rx="7.6" fill="none" stroke="#fff" stroke-opacity=".9" stroke-width="1.2"/>'
    col="#ffffff"
  else:
    tile=f'<defs><linearGradient id="g{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#22c4ff"/><stop offset=".55" stop-color="#4b6bff"/><stop offset="1" stop-color="#b04dff"/></linearGradient></defs><rect x="1" y="1" width="30" height="30" rx="9" fill="#fff" stroke="{NAVY}" stroke-width="2"/><rect x="2.8" y="2.8" width="26.4" height="26.4" rx="7.4" fill="none" stroke="url(#g{uid})" stroke-width="1.6"/>'
    col=NAVY
  g=g.replace("HALO",f"url(#g{uid})" if style=="A" else "#fff")
  return f'<svg width="{size}" height="{size}" viewBox="0 0 32 32">{tile}<g transform="translate(6.4 6.4) scale(.8)" fill="none" stroke="{col}" color="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{g}</g></svg>'
icon.n=0
def emoji(e,size):return f'<span style="font-size:{int(size*.62)}px;line-height:{size}px;width:{size}px;display:inline-block;text-align:center">{e}</span>'
allbg=[c for _,cs in THEMES for c in cs]
def edge_min(style):
  # outer ring navy, inner ring white (A) / tile white (B): best of the two layers touching/near the background
  return min(max(cr(NAVY,b),cr("#ffffff",b)) for b in allbg)
glyphA=min(cr("#ffffff","#3a55e8"),cr("#ffffff","#8338d6")); glyphB=cr(NAVY,"#ffffff")
