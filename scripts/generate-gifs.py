"""Offline asset build: Python 3 + Pillow. No production runtime dependency.
Run: python3 scripts/generate-gifs.py --font /path/to/font.ttf
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import argparse, math, json
p=argparse.ArgumentParser(); p.add_argument('--font', required=True); args=p.parse_args()
root=Path(__file__).resolve().parents[1]
font=ImageFont.truetype(args.font,28)
bg=(248,249,252); accent=(105,97,232); pale=(226,228,238)
groups={
'loading-text': [('classic-loading-text','Classic Loading Text','A gently pulsing loading message.'),('loading-dots','Loading Dots GIF','Three dots take turns after a steady label.'),('please-wait','Please Wait GIF','A calm waiting message with a moving underline.'),('processing','Processing GIF','A processing message with a cycling activity marker.')],
'progress-bar':[('linear-indeterminate-bar','Linear Indeterminate Bar','A short segment crosses an open track.'),('sliding-progress-bar','Sliding Progress Bar','A segment glides back and forth without measuring completion.'),('continuous-looping-bar','Continuous Looping Bar','A moving band wraps around the track.'),('dual-segment-progress-bar','Dual Segment Progress Bar','Two offset segments travel across the track.')],
'shimmer':[('text-skeleton-shimmer','Text Skeleton Shimmer','An article heading and three lines of body copy.'),('card-skeleton-loading','Card Skeleton Loading','A feed card with media, a title, and a text excerpt.'),('image-placeholder-shimmer','Image Placeholder Shimmer','A media placeholder reserves space while an image arrives.'),('profile-skeleton-loading','Profile Skeleton Loading','An avatar and account details form a compact profile row.')]}
manifest={}
for group,items in groups.items():
 manifest[group]=[]
 for index,(slug,name,description) in enumerate(items):
  w,h=(640,120) if group=='progress-bar' else (480,260) if group=='shimmer' else (400,160)
  frames=[]
  for f in range(24):
   t=f/24; im=Image.new('RGB',(w,h),bg); d=ImageDraw.Draw(im)
   if group=='loading-text':
    label=['Loading','Loading','Please wait','Processing'][index]
    color=tuple(round(bg[k]+(accent[k]-bg[k])*(.45+.55*(1+math.cos(t*2*math.pi))/2)) for k in range(3)) if index==0 else accent
    box=d.textbbox((0,0),label,font=font); x=(w-(box[2]-box[0]))/2-12; y=57
    d.text((x,y),label,font=font,fill=color)
    if index==1:
     for j in range(3):
      dx=x+box[2]+9+j*9; d.ellipse((dx,82,dx+4,86),fill=accent if f//8==j else pale)
    elif index==2:
     dx=120+120*(1-math.cos(t*2*math.pi))/2; d.rounded_rectangle((dx,105,dx+36,108),radius=2,fill=accent)
    elif index==3:
     a=t*2*math.pi; cx=315+9*math.cos(a); cy=80+9*math.sin(a); d.ellipse((cx-3,cy-3,cx+3,cy+3),fill=accent)
   elif group=='progress-bar':
    d.rounded_rectangle((32,54,608,66),radius=6,fill=pale)
    mask=Image.new('L',(w,h)); md=ImageDraw.Draw(mask); md.rounded_rectangle((32,54,608,66),radius=6,fill=255)
    layer=im.copy(); ld=ImageDraw.Draw(layer)
    positions=[32-140+716*t] if index==0 else [32+436*(1-math.cos(t*2*math.pi))/2] if index==1 else [32+576*t,32+576*t-576] if index==2 else [32-100+808*t,32-100+808*((t+.5)%1)]
    length=140 if index!=3 else 100
    for x in positions: ld.rounded_rectangle((x,54,x+length,66),radius=6,fill=accent)
    im.paste(layer,(0,0),mask)
   else:
    mask=Image.new('L',(w,h)); md=ImageDraw.Draw(mask)
    def rect(box,r=6): md.rounded_rectangle(box,radius=r,fill=255)
    if index==0:
     for box in [(36,48,320,68),(36,100,444,112),(36,132,420,144),(36,164,360,176)]: rect(box)
    elif index==1:
     rect((30,22,450,156)); rect((30,178,290,194)); rect((30,214,400,224))
    elif index==2: rect((24,20,456,240),12)
    else:
     md.ellipse((32,46,112,126),fill=255)
     for box in [(136,52,340,70),(136,92,420,106),(32,164,430,176),(32,198,330,210)]: rect(box)
    fill=Image.new('RGB',(w,h),pale); fd=ImageDraw.Draw(fill); center=-160+(w+320)*t
    for x in range(w):
     light=max(0,1-abs(x-center)/90)*19; c=tuple(min(255,int(v+light)) for v in pale); fd.line((x,0,x,h),fill=c)
    im.paste(fill,(0,0),mask)
   frames.append(im.quantize(colors=48))
  folder=root/'public/gifs'/group; folder.mkdir(parents=True,exist_ok=True)
  path=folder/(slug+'.gif'); frames[0].save(path,save_all=True,append_images=frames[1:],duration=80,loop=0,optimize=True,disposal=2)
  frames[0].convert('RGB').save(folder/(slug+'.png'),optimize=True)
  manifest[group].append(dict(name=name,description=description,src=f'/gifs/{group}/{slug}.gif',poster=f'/gifs/{group}/{slug}.png',width=w,height=h,bytes=path.stat().st_size,alt=name+' — '+description))
(root/'app/data/gifs.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Generated',sum(map(len,manifest.values())),'GIFs;',sum(a['bytes'] for g in manifest.values() for a in g),'bytes')
