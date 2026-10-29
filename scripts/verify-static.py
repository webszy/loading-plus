"""Verify generated SEO pages, discoverable links, and real animation assets.
Requires Pillow for decoding every GIF frame. Run after pnpm generate.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json, xml.etree.ElementTree as ET
from PIL import Image
root=Path(__file__).resolve().parents[1]; output=root/'.output/public'
pages=json.loads((root/'app/data/seo-pages.json').read_text())
class Page(HTMLParser):
 def __init__(self,path):
  super().__init__(); self.tags=[]; self.feed(path.read_text())
 def handle_starttag(self,tag,attrs): self.tags.append((tag,dict(attrs)))
 def matching(self,tag): return [a for t,a in self.tags if t==tag]
routes=['/']+['/'+p for p in pages]
parsed={r:Page(output/r.strip('/')/'index.html') for r in routes}
for route,page in parsed.items():
 assert len(page.matching('h1'))==1,route
 assert len(page.matching('main'))==1,route
 assert [a['href'] for a in page.matching('link') if a.get('rel')=='canonical']==['https://loading.plus'+route]
 if route!='/':
  text=(output/route.strip('/')/'index.html').read_text(); data=pages[route[1:]]
  assert data['title'] in text and data['heading'] in text
  for section in data['sections']: assert section['title'] in text
  for key in ['og:title','og:description','og:type','og:url']:
   assert any(a.get('property')==key for a in page.matching('meta')),(route,key)
  assert any(a.get('name')=='twitter:card' for a in page.matching('meta'))
 for a in page.matching('a'):
  url=urlsplit(a.get('href','')); target=url.path or route
  if url.scheme or url.netloc: continue
  if target in parsed:
   if url.fragment: assert any(attrs.get('id')==unquote(url.fragment) for _,attrs in parsed[target].tags),(route,a)
  else: assert (output/target.lstrip('/')).is_file(),(route,a)
 for img in page.matching('img'):
  assert img.get('alt') and img.get('width') and img.get('height'),route
  assert (output/img['src'].lstrip('/')).is_file()
sitemap=ET.parse(output/'sitemap.xml')
urls=[el.text for el in sitemap.findall('.//{*}loc')]
assert set(urls)=={'https://loading.plus'+r for r in routes} and len(urls)==5
assets=json.loads((root/'app/data/gifs.json').read_text()); count=0
for group in assets.values():
 for a in group:
  path=output/a['src'].lstrip('/'); im=Image.open(path)
  assert im.format=='GIF' and im.is_animated and im.n_frames>1 and im.info.get('loop')==0
  assert im.size==(a['width'],a['height']) and path.stat().st_size==a['bytes']
  for f in range(im.n_frames): im.seek(f); im.load()
  cover=Image.open(output/a['poster'].lstrip('/')); assert cover.size==im.size
  count+=1
print(f'PASS: {len(routes)} prerendered pages; unique H1/canonical, SEO tags, body content, links/anchors, sitemap, {count} decoded animated GIFs and PNG covers.')
