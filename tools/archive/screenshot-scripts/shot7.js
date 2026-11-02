const { chromium } = require('playwright');
(async () => { const b = await chromium.launch();
 const m = await b.newPage({viewport:{width:390,height:900}}); await m.goto('http://127.0.0.1:8766/');
 const fig = await m.$('figure'); await fig.screenshot({path:'/tmp/claude-0/-home-user/ebcd420f-94ce-55f8-a8c9-103d7b678fc3/scratchpad/v_chart_m.png'});
 for (const p of ['/','/book/','/consulting/','/author/','/references/','/papers/']) { await m.goto('http://127.0.0.1:8766'+p); const w = await m.evaluate(()=>document.documentElement.scrollWidth); console.log(p, w); }
 const d = await b.newPage({viewport:{width:1280,height:900}}); await d.goto('http://127.0.0.1:8766/book/');
 await d.screenshot({path:'/tmp/claude-0/-home-user/ebcd420f-94ce-55f8-a8c9-103d7b678fc3/scratchpad/v_book_d.png', fullPage:true});
 const az = await d.goto('http://127.0.0.1:8766/references/'); const sz = await d.$$eval('.az a', a=>a.map(e=>{const r=e.getBoundingClientRect();return [e.textContent, Math.round(r.width), Math.round(r.height)]}).filter(x=>x[1]<24||x[2]<24)); console.log('small az targets', JSON.stringify(sz));
 await b.close(); })();
