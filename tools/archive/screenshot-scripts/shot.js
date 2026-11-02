const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
for (const [w,n] of [[1280,'d'],[390,'m']]){const p=await b.newPage({viewport:{width:w,height:900}});
await p.goto('http://127.0.0.1:8765/');await p.screenshot({path:`union-home-${n}.png`});await p.close();}
await b.close();})();
