const { chromium } = require('playwright');
(async () => { const b = await chromium.launch();
 for (const [p,w,n] of [['/',1280,'home'],['/papers/',1280,'papers'],['/consulting/',390,'consult_m'],['/author/',1280,'author']]) {
  const pg = await b.newPage({viewport:{width:w,height:1000}}); await pg.goto('http://localhost:8765'+p);
  const sw = await pg.evaluate(()=>document.documentElement.scrollWidth); const f = await pg.evaluate(()=>document.fonts.check('600 16px Montserrat'));
  console.log(n, sw, 'font', f); await pg.screenshot({path:'/tmp/claude-0/-home-user/ebcd420f-94ce-55f8-a8c9-103d7b678fc3/scratchpad/j_'+n+'.png', fullPage: n!=='papers'}); }
 await b.close(); })();
