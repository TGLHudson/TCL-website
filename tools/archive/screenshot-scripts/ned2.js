const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:390,height:844}});
await p.goto('http://127.0.0.1:8765/');const f=await p.$('figure');await f.screenshot({path:'panel/ned-chart.png'});
await p.goto('http://127.0.0.1:8765/consulting/');await p.screenshot({path:'panel/ned-consult-fold.png'});
const r=await p.evaluate(()=>[...document.querySelectorAll('h2,h3')].map(h=>h.textContent.trim()+' @'+Math.round(h.getBoundingClientRect().top)));console.log(r.join('\n'));
await p.goto('http://127.0.0.1:8765/contact/');await p.screenshot({path:'panel/ned-contact-full.png',fullPage:true});
await b.close();})();
