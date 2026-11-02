const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 320, height: 800 } });
  for (const p of ['/', '/book/', '/papers/', '/references/', '/consulting/', '/author/', '/contact/']) {
    await pg.goto('http://127.0.0.1:8765' + p);
    await pg.addStyleTag({ content: '*{line-height:1.5!important;letter-spacing:0.12em!important;word-spacing:0.16em!important} p{margin-bottom:2em!important}' });
    const r = await pg.evaluate(() => { const de = document.documentElement; const clip=[]; document.querySelectorAll('body *').forEach(e=>{ if (e.scrollWidth > e.clientWidth+1 && getComputedStyle(e).overflowX!=='visible') clip.push(e.tagName+'.'+e.className); const rc=e.getBoundingClientRect(); if(rc.right>de.clientWidth+1) clip.push('OVER '+e.tagName+'.'+e.className+' '+Math.round(rc.right)+' "'+(e.textContent||'').trim().slice(0,30)+'"'); }); return { sw: de.scrollWidth, clip: [...new Set(clip)].slice(0,8) }; });
    console.log('textspacing 320', p, r.sw, r.clip.join(' | '));
  }
  // 200% text-only: double root and body font-size (simulates Firefox zoom text only)
  for (const p of ['/', '/papers/', '/references/', '/book/']) {
    await pg.setViewportSize({ width: 1280, height: 900 });
    await pg.goto('http://127.0.0.1:8765' + p);
    await pg.addStyleTag({ content: 'html{zoom:1} body{font-size:34px!important} .nav,.btn,.text-link,.eyebrow,dl.facts dt,.site-footer h2,.az,.badge,.papers .copy{font-size:200%!important}' });
    const sw = await pg.evaluate(() => document.documentElement.scrollWidth);
    console.log('text200 1280', p, sw);
    await pg.screenshot({ path: 'text200' + p.replace(/\//g,'_') + '.png' });
  }
  await b.close();
})();
