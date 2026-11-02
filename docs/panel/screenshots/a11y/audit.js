const { chromium } = require('playwright');
const pages = ['/', '/book/', '/papers/', '/references/', '/consulting/', '/author/', '/contact/', '/404.html'];
(async () => {
  const b = await chromium.launch();
  for (const w of [1280, 640, 390, 320]) {
    const ctx = await b.newContext({ viewport: { width: w, height: 900 }, javaScriptEnabled: false });
    const pg = await ctx.newPage();
    let bytes = {};
    pg.on('response', async r => { try { const buf = await r.body(); bytes[r.url()] = buf.length; } catch(e){} });
    for (const p of pages) {
      bytes = {};
      await pg.goto('http://127.0.0.1:8765' + p, { waitUntil: 'networkidle' });
      const r = await pg.evaluate(() => {
        const de = document.documentElement;
        const over = [];
        document.querySelectorAll('body *').forEach(el => {
          const rc = el.getBoundingClientRect();
          if (rc.width && rc.right > de.clientWidth + 1) over.push(el.tagName + '.' + el.className + ' right=' + Math.round(rc.right));
        });
        // small targets (WCAG 2.5.8: 24x24)
        const small = [];
        document.querySelectorAll('a,button,input').forEach(el => { const rc = el.getBoundingClientRect(); if (rc.width && (rc.height < 24 || rc.width < 24)) small.push(el.textContent.trim().slice(0,30) + ' ' + Math.round(rc.width) + 'x' + Math.round(rc.height)); });
        return { sw: de.scrollWidth, cw: de.clientWidth, over: over.slice(0, 6), small: small.slice(0, 40), nsmall: small.length };
      });
      const total = Object.values(bytes).reduce((a, c) => a + c, 0);
      console.log(`${w} ${p} scrollW=${r.sw} clientW=${r.cw} bytes=${total} reqs=${Object.keys(bytes).length}`);
      if (r.over.length) console.log('  overflow:', r.over.join(' | '));
      if (w === 390 || w===1280) console.log('  small targets', r.nsmall, r.small.slice(0,12).join(' ; '));
      if (w === 390 || w === 1280 || w===320) await pg.screenshot({ path: `shot-${w}-${p.replace(/\//g, '_') || 'home'}.png`, fullPage: true });
    }
    await ctx.close();
  }
  await b.close();
})();
