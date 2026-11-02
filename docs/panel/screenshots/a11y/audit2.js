const { chromium } = require('playwright');
const pages = ['/', '/book/', '/papers/', '/references/', '/consulting/', '/author/', '/contact/'];
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1280, height: 900 } });
  const pg = await ctx.newPage();
  for (const p of pages) {
    await pg.goto('http://127.0.0.1:8765' + p);
    const r = await pg.evaluate(() => {
      const hs = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].map(h => h.tagName[1] + ':' + h.textContent.trim().slice(0, 40));
      let skips = []; let prev = 0;
      [...document.querySelectorAll('main h1,main h2,main h3,main h4')].forEach(h => { const l = +h.tagName[1]; if (prev && l > prev + 1) skips.push(h.textContent.trim()); prev = l; });
      const ids = {}; document.querySelectorAll('[id]').forEach(e => ids[e.id] = (ids[e.id] || 0) + 1);
      const dup = Object.entries(ids).filter(([k, v]) => v > 1);
      const brokenFrag = [...document.querySelectorAll('a[href^="#"]')].filter(a => a.getAttribute('href').length>1 && !document.getElementById(a.getAttribute('href').slice(1))).map(a=>a.href);
      const landmarks = [...document.querySelectorAll('header,nav,main,footer,aside,[role]')].map(e => e.tagName.toLowerCase() + (e.getAttribute('aria-label') ? '[' + e.getAttribute('aria-label') + ']' : '') + (e.getAttribute('role')?'(role='+e.getAttribute('role')+')':''));
      // links in running text without underline
      const inText = [];
      document.querySelectorAll('main a, footer a').forEach(a => {
        const cs = getComputedStyle(a);
        if (cs.textDecorationLine.includes('underline')) return;
        if (a.classList.contains('btn')) return;
        const par = a.parentElement; const pt = par.textContent.replace(/\s+/g,' ').trim(); const at = a.textContent.trim();
        if (pt.length > at.length + 3 && !['LI','NAV'].includes(par.tagName) && !par.classList.contains('links') && !par.classList.contains('actions')) inText.push(par.tagName + '.' + par.className + ': "' + at + '"');
      });
      const anames = {}; document.querySelectorAll('a').forEach(a => { const n = (a.getAttribute('aria-label') || a.textContent).trim(); (anames[n] = anames[n] || new Set()).add(a.getAttribute('href')); });
      const ambiguous = Object.entries(anames).filter(([n, s]) => s.size > 1).map(([n, s]) => n + ' -> ' + [...s].join(','));
      return { hs, skips, dup, brokenFrag, landmarks, inText, ambiguous };
    });
    console.log('=== ' + p); console.log(' headings:', r.hs.join(' | ')); console.log(' skips:', r.skips, 'dupIDs:', r.dup, 'brokenFrag:', r.brokenFrag);
    console.log(' landmarks:', r.landmarks.join(', ')); console.log(' non-underlined in-text links:', r.inText); console.log(' same name diff target:', r.ambiguous);
  }
  // keyboard walk on home
  await pg.goto('http://127.0.0.1:8765/');
  for (let i = 0; i < 25; i++) {
    await pg.keyboard.press('Tab');
    const f = await pg.evaluate(() => { const e = document.activeElement; const cs = getComputedStyle(e); const rc = e.getBoundingClientRect(); return `${e.tagName} "${(e.textContent||'').trim().slice(0,30)}" outline=${cs.outlineStyle} ${cs.outlineWidth} ${cs.outlineColor} rect=${Math.round(rc.x)},${Math.round(rc.y)},${Math.round(rc.width)}x${Math.round(rc.height)}`; });
    console.log('tab', i + 1, f);
    if (i === 0) { await pg.screenshot({ path: 'skip-focus.png', clip: { x: 0, y: 0, width: 600, height: 120 } }); }
  }
  // skip link activation
  await pg.goto('http://127.0.0.1:8765/'); await pg.keyboard.press('Tab'); await pg.keyboard.press('Enter'); await pg.keyboard.press('Tab');
  console.log('after skip, next focus:', await pg.evaluate(() => document.activeElement.textContent.trim().slice(0, 40)));
  // form submit without JS behaviour
  await pg.goto('http://127.0.0.1:8765/contact/'); await pg.fill('#email-contact', 'a@b.co');
  const [resp] = await Promise.all([pg.waitForNavigation().catch(e=>null), pg.click('form.signup button')]);
  console.log('form submit ->', pg.url(), resp ? resp.status() : 'no nav');
  // chart size at phone
  for (const w of [390, 320]) { await pg.setViewportSize({ width: w, height: 800 }); await pg.goto('http://127.0.0.1:8765/'); console.log(w, 'chart', await pg.evaluate(() => { const s = document.querySelector('.fit-chart').getBoundingClientRect(); return Math.round(s.width) + 'px wide, scale ' + (s.width / 560).toFixed(2) + ', 12px label renders ' + (12 * s.width / 560).toFixed(1) + 'px'; })); }
  // A-Z spacing
  await pg.setViewportSize({ width: 390, height: 800 }); await pg.goto('http://127.0.0.1:8765/references/');
  console.log('az', await pg.evaluate(() => { const r = [...document.querySelectorAll('.az a')].map(a => a.getBoundingClientRect()); let min = 999, pair=''; for (let i = 1; i < r.length; i++) { if (Math.abs(r[i].y - r[i-1].y) < 2) { const d = (r[i].x + r[i].width / 2) - (r[i-1].x + r[i-1].width / 2); if (d < min) { min = d; pair = i; } } } return 'min centre distance ' + min.toFixed(1) + ' at index ' + pair; }));
  await b.close();
})();
