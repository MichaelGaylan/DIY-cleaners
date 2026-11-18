#!/usr/bin/env python3
# Repack the readable src/index.html into the packed, published root index.html.
import base64,re,hashlib,json,sys,os
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s=open(os.path.join(root,'src','index.html')).read()
m=re.search(r'<script>\n(/\* Release info.*?)</script>\s*</body>', s, re.S)
assert m,"app script not found"
js=m.group(1)
cm=re.search(r'<style>\n(.*?)\n</style>', s, re.S)
css=cm.group(1)
cmin=re.sub(r'/\*.*?\*/','',css,flags=re.S)
cmin=re.sub(r'\s*\n\s*','',cmin); cmin=re.sub(r';\}','}',cmin); cmin=re.sub(r'\s{2,}',' ',cmin)
b64=base64.b64encode(js.encode('utf-8')).decode()
ver=re.search(r'const VERSION="([^"]+)",BUILD="([^"]+)"',js)
boot=('/* DIY Cleaners © 2026 Michael Gaylan (VYBEON). All rights reserved. '
 'Published build is packed; readable source and the decoder map are kept privately in the GitHub repo and are not served here. */\n'
 'var __A="'+b64+'";(0,eval)(new TextDecoder().decode(Uint8Array.from(atob(__A),function(c){return c.charCodeAt(0)})));')
out=s.replace(cm.group(0),'<style>'+cmin+'</style>').replace(m.group(0),'<script>\n'+boot+'</script>\n</body>')
open(os.path.join(root,'index.html'),'w').write(out)
json.dump({"what":"Decoder map for the packed live build of DIY Cleaners. Kept in GitHub only; excluded from the published site via _config.yml.",
 "live_file":"index.html","readable_source":"src/index.html",
 "packing":"The app <script> body is the readable source's <script> body, UTF-8 then base64, stored as window.__A and run with indirect eval. CSS is whitespace-minified; HTML is unchanged.",
 "decode":"atob(__A) -> UTF-8 bytes -> text  (Python: base64.b64decode(__A).decode('utf-8'))",
 "source_sha256":hashlib.sha256(js.encode('utf-8')).hexdigest(),
 "version":ver.group(1),"build":ver.group(2)}, open(os.path.join(root,'src','decoder-map.json'),'w'), indent=2)
print("packed",ver.group(1),ver.group(2),"js",len(js))
