const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:390,height:844}});
for (const u of ['','book/','consulting/','author/','contact/']){await p.goto('http://127.0.0.1:8765/'+u);
const n=(u||'home').replace('/','');await p.screenshot({path:`panel/ned-${n}-fold.png`});
await p.screenshot({path:`panel/ned-${n}-full.png`,fullPage:true});
const h=await p.evaluate(()=>document.body.scrollHeight);console.log(n,h);}
await b.close();})();
