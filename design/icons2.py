import json,sys
exec(open('lib.py').read())
exec(open('g2.py').read())
G.update({k:(v[0],v[2]) for k,v in G2.items()})
meta={k:[v[0],v[1]] for k,v in G2.items()}
def auto(bg):return "A" if L(bg)<0.18 else "B"
def strip(render):
  out=""
  for name,cs in THEMES:
    cells="".join(f'<div class="cell" style="background:{c}">{render(28,c)}</div>' for c in cs)
    out+=f'<div class="th"><div class="tn">{name}</div><div class="cells">{cells}</div></div>'
  return out
def emoji(e,size):return f'<span style="font-size:{int(size*.55)}px">{e}</span>'
def row(k,label,old):
  o=f'<div class="old">{emoji(old,40) if old!="new" else "<i>new</i>"}<span>now</span></div>'
  return f'<div class="row"><div class="lab"><b>{label}</b></div>{o}<div class="hero" style="background:#071338">{icon(k,"A",56)}</div><div class="hero" style="background:#ECEDE9">{icon(k,"B",56)}</div>{strip(lambda s,c,k=k:icon(k,auto(c),s))}</div>'
def roundbtn(k,style,size=44):
  svg=icon(k,style,size)
  return svg.replace('rx="9"','rx="15"').replace('rx="7.6"','rx="13.4"').replace('rx="7.4"','rx="13.2"')
def titlebar(bg,ink,muted,barbg,style):
  logo=icon("logo",style,46)
  return f'''<div class="tbwrap" style="background:{bg}"><div class="tb" style="background:{barbg}">{logo}<div class="tt"><b style="{("background:linear-gradient(135deg,#22c4ff,#4b6bff 55%,#b04dff);-webkit-background-clip:text;color:transparent" if style=="A" else "color:"+ink)}">DIY Cleaners</b><span style="color:{muted}">SAFE CLEANERS YOU MIX AT HOME</span></div><div class="tbb">{roundbtn("help",style)}{roundbtn("settings",style)}</div></div></div>'''
sections=[("Title bar",None),("Categories (the 8 not yet redrawn)",["bathroom","surfaces","glass","laundry","upholstery","outdoor","specialty","odor"]),
("Already approved",["K2","P1","B2"]),("Bottom tabs",["recipes","pantry","safety","saved"]),
("Title bar, menu and buttons",["logo","settings","help","about","nevermix","print"]),("Help topics",["search","install","data"])]
body=""
appr={"K2":("Kitchen (K2)","🍳"),"P1":("Pets (P1)","🐾"),"B2":("Bugs (B2)","🐜")}
for title,keys in sections:
  body+=f"<h2>{title}</h2>"
  if keys is None:
    body+='<p class="note">Glass bar with the app icon as a glow tile, the name in the VYBEON glow, a small-caps tagline, and round Help and Settings buttons on the right (Settings replaces the ☰ menu). Shown on the VYBEON navy, Midnight, Rosewood and Linen.</p><div class="tbs">'
    body+=titlebar("#071338","#eef2ff","#a3adcf","rgba(255,255,255,.07)","A")
    body+=titlebar("#212C45","#EBE7D8","#b9c2d4","rgba(255,255,255,.07)","A")
    body+=titlebar("#3F1020","#F3DBC0","#d9b3a8","rgba(255,255,255,.07)","A")
    body+=titlebar("#ECEDE9","#071338","#5b6380","rgba(255,255,255,.75)","B")
    body+="</div>";continue
  for k in keys:
    if k in appr: body+=row(k,*appr[k])
    else: body+=row(k,meta[k][0],meta[k][1])
html=f'''<!DOCTYPE html><html><head><meta charset="utf-8"><title>DIY Cleaners · all icons for approval</title><style>
body{{margin:0;padding:24px;background:#071338;color:#eef2ff;font:14px/1.4 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;width:1820px}}
h1{{margin:0 0 4px;font-size:22px;background:linear-gradient(135deg,#22c4ff,#4b6bff 55%,#b04dff);-webkit-background-clip:text;color:transparent}}
h2{{margin:22px 0 8px;font-size:17px}} .note{{color:#a3adcf;margin:0 0 8px}}
.row{{display:flex;align-items:center;gap:10px;padding:8px;border-radius:16px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);margin-bottom:6px}}
.lab{{width:120px}} .lab b{{font-size:13px}}
.old{{width:44px;display:flex;flex-direction:column;align-items:center;color:#a3adcf;font-size:10px}} .old i{{font-size:12px;height:30px;line-height:30px}}
.hero{{width:72px;height:72px;border-radius:14px;display:grid;place-items:center;flex:none}}
.th{{display:flex;flex-direction:column;align-items:center;gap:2px}} .tn{{font-size:10px;color:#a3adcf}}
.cells{{display:flex;border-radius:10px;overflow:hidden}} .cell{{width:34px;height:38px;display:grid;place-items:center}}
svg{{display:block}}
.tbs{{display:grid;grid-template-columns:1fr 1fr;gap:12px}} .tbwrap{{padding:16px;border-radius:18px;border:1px solid rgba(255,255,255,.12)}}
.tb{{display:flex;align-items:center;gap:12px;padding:10px 12px;border-radius:22px;border:1px solid rgba(127,140,190,.35);backdrop-filter:blur(10px);box-shadow:0 8px 28px rgba(0,0,0,.18)}}
.tt{{flex:1;display:flex;flex-direction:column}} .tt b{{font-size:21px;letter-spacing:.2px}} .tt span{{font:600 10.5px ui-monospace,Menlo,monospace;letter-spacing:1.4px}}
.tbb{{display:flex;gap:8px}}
</style></head><body><h1>DIY Cleaners · all icons for approval (MAKE-016)</h1>
<p class="note">Same look as the approved K2, P1 and B2. Each row shows: today's icon, the glow tile, the light chip, then what you'd see on the VYBEON navy and every color of the 7 swatch themes (glow tile on dark colors, light chip on light ones). Icon on tile: 5.8:1 glow, 18.1:1 light. Tile edges stay at least 4.4:1 on all 38 colors.</p>
{body}</body></html>'''
open(sys.argv[1],'w').write(html)
