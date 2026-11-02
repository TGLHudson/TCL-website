const { chromium } = require('playwright');
(async () => { const b = await chromium.launch();
 for (const [w,n] of [[390,'m'],[1280,'d']]) { const m = await b.newPage({viewport:{width:w,height:900}}); await m.goto('http://127.0.0.1:8767/');
 const fig = await m.$('figure'); await fig.screenshot({path:'/tmp/claude-0/-home-user/ebcd420f-94ce-55f8-a8c9-103d7b678fc3/scratchpad/v2_chart_'+n+'.png'}); }
 await b.close(); })();
