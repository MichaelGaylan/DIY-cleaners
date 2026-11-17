import math
def gear():
  out=[];n=8
  for k in range(n):
    c=k*2*math.pi/n
    for da,r in((-.42,7.2),(-.22,9.6),(.22,9.6),(.42,7.2)):
      a=c+da;out.append(f"{12+r*math.cos(a):.2f} {12+r*math.sin(a):.2f}")
  return "M"+" L".join(out)+"Z"
G2={
"bathroom":("Bathroom","🛁",'<path d="M3 12h18v1.5a5.5 5.5 0 0 1-5.5 5.5h-7A5.5 5.5 0 0 1 3 13.5z"/><path d="M6 12V5.8A2.8 2.8 0 0 1 8.8 3c1.3 0 2.2.8 2.5 2"/><path d="M7.5 19l-1 2.2M16.5 19l1 2.2"/>'),
"surfaces":("Floors and surfaces","🧽",'<path d="M4 11h13a3 3 0 0 1 3 3v3a3 3 0 0 1-3 3H7a3 3 0 0 1-3-3z"/><path d="M4 15h16"/><circle cx="8" cy="5.5" r="2"/><circle cx="13.5" cy="4" r="1.3"/><circle cx="17.5" cy="7" r="1.5"/>'),
"glass":("Glass and mirrors","🪟",'<rect x="4" y="3" width="16" height="18" rx="3"/><path d="M8 10l4-4M8 15l8-8"/>'),
"laundry":("Laundry","🧺",'<rect x="4" y="2.5" width="16" height="19" rx="3"/><path d="M4 7h16"/><circle cx="12" cy="14.2" r="4.3"/><path d="M9.2 14.6c.9-.9 1.9.9 2.8 0s1.9.9 2.8 0" stroke-width="1.6"/><g fill="currentColor" stroke="none"><circle cx="7.4" cy="4.8" r="1"/><circle cx="10.2" cy="4.8" r="1"/></g>'),
"upholstery":("Upholstery and carpets","🛋️",'<path d="M5 11V8a3 3 0 0 1 3-3h8a3 3 0 0 1 3 3v3"/><path d="M3 13a2 2 0 0 1 4 0v2h10v-2a2 2 0 0 1 4 0v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M6 19v2M18 19v2"/>'),
"outdoor":("Outdoor and garage","🏡",'<path d="M3 11 12 4l9 7"/><path d="M5 9.5V20h14V9.5"/><path d="M8.5 20v-6h7v6M8.5 17h7"/>'),
"specialty":("Specialty household","💍",'<circle cx="12" cy="16" r="5.3"/><path d="M8.2 2.5h7.6l2.7 3.2L12 10.7 5.5 5.7z"/><path d="M5.5 5.7h13M10.2 2.5 9 5.7l3 5M13.8 2.5 15 5.7l-3 5" stroke-width="1.3"/>'),
"odor":("Odor and drains","🌿",'<path d="M5 19.5C5 10.5 11 5 20 4c0 9-5.5 15.5-15 15.5z"/><path d="M5 19.5l9-9"/>'),
"recipes":("Recipes tab","🧽",'<path d="M12 6.2C10 4.7 7 4.2 3.5 4.6v14.2c3.5-.4 6.5.1 8.5 1.6 2-1.5 5-2 8.5-1.6V4.6C17 4.2 14 4.7 12 6.2z"/><path d="M12 6.2v14.2"/>'),
"pantry":("What can I make? tab","🧺",'<path d="M6.5 3.5h11V7h-11z"/><path d="M7 7h10v11a3 3 0 0 1-3 3h-4a3 3 0 0 1-3-3z"/><path d="M7 11h10v5H7"/>'),
"safety":("Safety tab","⚠️",'<path d="M12 2.5 4 5.5v6c0 5 3.4 8.8 8 10 4.6-1.2 8-5 8-10v-6z"/><path d="M12 8v5"/><circle cx="12" cy="16.4" r="1.1" fill="currentColor" stroke="none"/>'),
"saved":("Saved tab","♥",'<path d="M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0 1 12 7.4 4.3 4.3 0 0 1 19.5 10c0 5.4-7.5 10-7.5 10z"/>'),
"logo":("App icon and logo","🧴",'<path d="M7.5 10.5a2 2 0 0 1 2-2h3.5a2 2 0 0 1 2 2V20a1.5 1.5 0 0 1-1.5 1.5H9A1.5 1.5 0 0 1 7.5 20z"/><path d="M9.8 8.5V6.2h3v2.3"/><path d="M7.5 3h7l1.5 3.2H9.6"/><path d="M7.5 3v3"/><path d="M9.8 17.6c0-2.3 1.4-3.6 3.6-3.6 0 2.3-1.4 3.6-3.6 3.6z" fill="currentColor" stroke="none"/><g fill="currentColor" stroke="none"><circle cx="18.6" cy="2.8" r=".9"/><circle cx="20.4" cy="5" r=".9"/><circle cx="18.6" cy="7.2" r=".9"/></g>'),
"settings":("Settings (gear)","new",f'<path d="{gear()}"/><circle cx="12" cy="12" r="3"/>'),
"help":("Help","❓",'<circle cx="12" cy="12" r="9.5"/><path d="M9.4 9.3a2.7 2.7 0 0 1 5.2.9c0 1.9-2.6 2.2-2.6 4"/><circle cx="12" cy="17.2" r="1.1" fill="currentColor" stroke="none"/>'),
"about":("About","ℹ️",'<circle cx="12" cy="12" r="9.5"/><path d="M12 11v6"/><circle cx="12" cy="7.6" r="1.2" fill="currentColor" stroke="none"/>'),
"nevermix":("Never mix","🚫",'<path d="M9 3h6M10 3v5l-4.5 9.5A2.4 2.4 0 0 0 7.7 21h8.6a2.4 2.4 0 0 0 2.2-3.5L14 8V3"/><path d="M9.3 13.3l5.4 5.4M14.7 13.3l-5.4 5.4"/>'),
"print":("Print label","🖨",'<path d="M7 9V3h10v6"/><path d="M7 17H5a2 2 0 0 1-2-2v-4a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2h-2"/><path d="M7 13h10v8H7z"/>'),
"search":("Search / finding","🔎",'<circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21"/>'),
"install":("Install and offline","📲",'<rect x="6" y="2.5" width="12" height="19" rx="3"/><path d="M12 7v7M9 11l3 3 3-3M10 18.5h4"/>'),
"data":("Your data","💾",'<ellipse cx="12" cy="5.5" rx="7.5" ry="3"/><path d="M4.5 5.5v13c0 1.7 3.4 3 7.5 3s7.5-1.3 7.5-3v-13"/><path d="M4.5 12c0 1.7 3.4 3 7.5 3s7.5-1.3 7.5-3"/>'),
}
