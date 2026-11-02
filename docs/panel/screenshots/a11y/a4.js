const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 320, height: 800 } });
for (const ts of [false,true]) {
await pg.goto('http://127.0.0.1:8765/references/');
if (ts) await pg.addStyleTag({ content: '*{line-height:1.5!important;letter-spacing:0.12em!important;word-spacing:0.16em!important}' });
console.log(ts, await pg.evaluate(() => { const out=[]; const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT); let n; while(n=w.nextNode()){ const r=document.createRange(); r.selectNodeContents(n); for(const rc of r.getClientRects()){ if(rc.right>321){ out.push(Math.round(rc.right)+' '+n.parentElement.tagName+'.'+n.parentElement.className+' "'+n.textContent.trim().slice(0,60)+'"'); break;} } } return [document.documentElement.scrollWidth, out.slice(0,6)]; }));
}
await b.close(); })();
