const { chromium } = require('playwright');
(async () => { const b = await chromium.launch();
 for (const [w,n] of [[1280,'d'],[390,'m']]) { const p = await b.newPage({viewport:{width:w,height:900}});
  await p.goto('file:///home/user/tcl-website/research.html');
  console.log(n, await p.evaluate(()=>document.documentElement.scrollWidth));
  await p.screenshot({path:'/tmp/claude-0/-home-user/ebcd420f-94ce-55f8-a8c9-103d7b678fc3/scratchpad/papers_'+n+'.png', fullPage:true}); }
 await b.close(); })();
