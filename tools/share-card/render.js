// Renders card.html to assets/share-card.png (1200 x 630) with the pre-installed Playwright.
// Run from the repository root:  node tools/share-card/render.js
const path = require('path');
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
  await p.goto('file://' + path.resolve(__dirname, 'card.html'));
  await p.waitForTimeout(300);
  await p.screenshot({ path: path.resolve(__dirname, '../../assets/share-card.png') });
  await b.close();
})();
