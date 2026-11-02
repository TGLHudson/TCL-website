const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1280,height:1100}});
 await p.goto('file:///home/user/tcl-website/research.html'); await p.screenshot({path:'/tmp/claude-0/-home-user/ebcd420f-94ce-55f8-a8c9-103d7b678fc3/scratchpad/copy_top.png'});
 await p.goto('file:///home/user/tcl-website/contact.html#copies'); await p.screenshot({path:'/tmp/claude-0/-home-user/ebcd420f-94ce-55f8-a8c9-103d7b678fc3/scratchpad/copy_contact.png'});
 await b.close(); })();
