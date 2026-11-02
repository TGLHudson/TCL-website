const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1280,height:1400}});
 await p.goto('file:///home/user/tcl-website/references.html#ref-c'); await p.screenshot({path:'/tmp/claude-0/-home-user/ebcd420f-94ce-55f8-a8c9-103d7b678fc3/scratchpad/refs2_c.png'});
 const m = await b.newPage({viewport:{width:390,height:900}}); await m.goto('file:///home/user/tcl-website/references.html');
 console.log(await m.evaluate(()=>document.documentElement.scrollWidth));
 await b.close(); })();
