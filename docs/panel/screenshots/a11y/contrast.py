def h(c): c=c.lstrip('#'); return tuple(int(c[i:i+2],16) for i in (0,2,4))
def lum(rgb):
    def ch(v):
        v/=255; return v/12.92 if v<=0.03928 else ((v+0.055)/1.055)**2.4
    r,g,b=map(ch,rgb); return 0.2126*r+0.7152*g+0.0722*b
def cr(a,b):
    la,lb=lum(a),lum(b); return (max(la,lb)+0.05)/(min(la,lb)+0.05)
def mix(fg,a,bg): return tuple(round(f*a+b*(1-a)) for f,b in zip(fg,bg))
C=dict(ink='#000718',deep='#003E4A',teal='#349699',gold='#F4E59B',goldm='#E8DD93',cream='#F9EECA',text='#E8E6E6',text2='#b9c2c8',inktext='#0A0A1C')
c={k:h(v) for k,v in C.items()}
pairs=[('text','ink'),('text','deep'),('text2','ink'),('text2','deep'),('teal','ink'),('teal','deep'),('gold','ink'),('gold','deep'),('goldm','ink'),('goldm','deep'),('cream','deep'),('cream','ink'),('inktext','gold'),('goldm','text2')]
for f,b in pairs: print(f"{f:8} on {b:6}: {cr(c[f],c[b]):.2f}")
for bg in ('ink','deep'):
    stripe=mix(c['gold'],0.12,c[bg])
    print(bg,'todo stripe',stripe,'text',round(cr(c['text'],stripe),2),'gold',round(cr(c['gold'],stripe),2),'goldm link',round(cr(c['goldm'],stripe),2))
    band=mix(c['teal'],0.28,c[bg]); print(bg,'band',band,'vs bg',round(cr(band,c[bg]),2),'text on band',round(cr(c['text'],band),2),'text2 on band',round(cr(c['text2'],band),2))
    rule=mix(c['cream'],0.35,c[bg]); print(bg,'rule vs bg',round(cr(rule,c[bg]),2))
    ul=mix(c['goldm'],0.45,c[bg]); print(bg,'link underline vs bg',round(cr(ul,c[bg]),2))
    print(bg,'teal dot vs bg',round(cr(c['teal'],c[bg]),2),'gold floor',round(cr(c['gold'],c[bg]),2))
# link vs surrounding body text (for 1.4.1 when underline absent)
print('goldm vs text', round(cr(c['goldm'],c['text']),2), 'goldm vs text2', round(cr(c['goldm'],c['text2']),2))
# gold focus outline vs deep teal button hover bg
print('gold outline on deep', round(cr(c['gold'],c['deep']),2))
