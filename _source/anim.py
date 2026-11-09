import math
OR="#EC6A0E"; OR_L="#F6993A"; BLUE="#0A7CC4"
P=(44,32)
DEPTH=[94,66,40]; REACH=[66,60,50]
def branches(gap=3, ring=24):
    x,y=P; out=[]
    for i,(d,w) in enumerate(zip(DEPTH,REACH)):
        t=i/2
        sx,sy=x,y   # les connexions partent du centre du point orange
        c1=(x-22*(1-t)**1.2-4, y+0.78*d); c2=(x+0.26*w, y+d*1.02); e=(x+w, y+d)
        out.append(((sx,sy),c1,c2,e))
    return out
def css(scope):
    s=scope
    return f'''{s} .ps-pt,{s} .ps-dot,{s} .ps-halo,{s} .ps-dhalo{{transform-box:fill-box;transform-origin:center}}
{s} .ps-ul{{stroke-dasharray:100 100;stroke-dashoffset:0}}
{s} .ps-sig{{opacity:0;stroke-dasharray:14 200;stroke-dashoffset:14}}
{s} .ps-halo,{s} .ps-dhalo{{opacity:0}}
{s}:hover .ps-pt{{animation:psPt 1.8s ease-in-out infinite}}
{s}:hover .ps-halo{{animation:psHalo 1.8s ease-out infinite}}
{s}:hover .ps-sig{{animation:psSig 1.8s linear infinite}}
{s}:hover .ps-dot{{animation:psDot 1.8s ease-in-out infinite}}
{s}:hover .ps-dhalo{{animation:psDHalo 1.8s ease-out infinite}}
@keyframes psPt{{0%{{transform:scale(1)}}10%{{transform:scale(1.28)}}22%{{transform:scale(1)}}100%{{transform:scale(1)}}}}
@keyframes psHalo{{0%{{opacity:.7;transform:scale(1)}}30%{{opacity:0;transform:scale(2.1)}}100%{{opacity:0}}}}
@keyframes psSig{{0%,14%{{opacity:0;stroke-dashoffset:14}}16%{{opacity:1;stroke-dashoffset:10}}62%{{opacity:1;stroke-dashoffset:-86}}64%,100%{{opacity:0;stroke-dashoffset:-86}}}}
@keyframes psDot{{0%,60%{{transform:scale(1)}}70%{{transform:scale(1.7)}}84%,100%{{transform:scale(1)}}}}
@keyframes psDHalo{{0%,60%{{opacity:0;transform:scale(1)}}64%{{opacity:.6;transform:scale(1)}}88%{{opacity:0;transform:scale(3)}}100%{{opacity:0}}}}
{s}:hover .ps-ul{{animation:psUl 1.8s ease-in-out infinite}}
@keyframes psUl{{0%,62%{{stroke-dashoffset:0}}64%{{stroke-dashoffset:100}}86%,100%{{stroke-dashoffset:0}}}}
@media (prefers-reduced-motion:reduce){{{s}:hover *{{animation:none!important}}}}'''
def emblem(uid, sw=5.2, dr=5.4, dark=False):
    x,y=P; B=branches()
    c_or = "#F08A2A" if dark else OR
    g=f'<defs><linearGradient id="g{uid}" gradientUnits="userSpaceOnUse" x1="{x-30}" y1="{y}" x2="{x+64}" y2="{y+88}"><stop offset="0" stop-color="{c_or}"/><stop offset="1" stop-color="{OR_L}"/></linearGradient></defs>'
    d=[f'M{a[0]:.1f} {a[1]:.1f} C{b[0]:.1f} {b[1]:.1f} {c[0]:.1f} {c[1]:.1f} {e[0]:.1f} {e[1]:.1f}' for a,b,c,e in B]
    fib=''.join(f'<path d="{p}"/>' for p in d)
    sig=''.join(f'<path class="ps-sig" pathLength="100" d="{p}"/>' for p in d)
    dots=''.join(f'<circle class="ps-dhalo" cx="{e[0]+dr:.1f}" cy="{e[1]:.1f}" r="{dr}" fill="{OR}"/><circle class="ps-dot" cx="{e[0]+dr:.1f}" cy="{e[1]:.1f}" r="{dr}" fill="url(#g{uid})"/>' for a,b,c,e in B)
    return (g+f'<g fill="none" stroke="url(#g{uid})" stroke-width="{sw}" stroke-linecap="round">{fib}</g>'
            f'<g fill="none" stroke="#FFE3C7" stroke-width="{sw-1.2}" stroke-linecap="round">{sig}</g>{dots}'
            f'<circle class="ps-halo" cx="{x}" cy="{y}" r="17" fill="{OR}"/>'
            f'<circle cx="{x}" cy="{y}" r="24" fill="none" stroke="{c_or}" stroke-width="2"/><circle class="ps-pt" cx="{x}" cy="{y}" r="16.5" fill="{c_or}"/>')
EVB="4 2 116 140"
def logo(uid, dark=False, cls="ps-logo"):
    nf="#FFFFFF" if dark else BLUE; tf="#F08A2A" if dark else OR
    e=f'<g transform="translate(-4,2) scale(.98)">{emblem(uid,dark=dark)}</g>'
    w=(f'<text x="130" y="62" font-family="Inter Tight, Inter, sans-serif" font-size="56" font-weight="800" letter-spacing="-1" fill="{nf}">POINTSYS</text>'
       f'<text x="132" y="100" font-family="Inter Tight, Inter, sans-serif" font-size="33" font-weight="800" letter-spacing="4.6" fill="{nf}">TÉLÉCOM</text>'
       f'<text x="133" y="134" font-family="Inter, sans-serif" font-size="20" font-weight="600" font-style="italic" fill="{tf}">100 % disponible</text>'
       f'<path class="ps-ul" pathLength="100" d="M134 144 H300" stroke="{tf}" stroke-width="2.6" stroke-linecap="round" fill="none"/>')
    return f'<svg class="{cls}" viewBox="0 -2 430 152" role="img" aria-label="POINTSYS Télécom — 100 % disponible" style="display:block;width:100%;height:auto">{e}{w}</svg>'
def icon(uid,size,cls="ps-logo"):
    k=dict(sw=5.2,dr=5.4) if size>=48 else dict(sw=8,dr=8)
    return f'<svg class="{cls}" viewBox="{EVB}" width="{size}" height="{size}" aria-hidden="true" style="display:block;overflow:visible">{emblem(uid,**k)}</svg>'
