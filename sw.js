/* Eighters-stats service worker – cache name is bumped by make-version.py */
const CACHE='eighters-stats-3.12';
const SHELL=['./','index.html','manifest.webmanifest','jersey.png','figure.webp','poses/point.webp','poses/arms.webp','poses/cap.webp','poses/back.webp','poses/bighat.webp','poses/c_point.webp','poses/c_arms.webp','poses/c_cap.webp','poses/c_back.webp','poses/c_bat.webp','poses/c_ball.webp','poses/c_heart.webp','poses/c_hand.webp','poses/c_dab.webp','poses/c_glove.webp','poses/b_thumbs.webp','poses/b_bat.webp','poses/b_up.webp','poses/b_head.webp','poses/b_flex.webp','poses/b_glove.webp','poses/b_heart.webp','poses/b_point.webp','poses/b_batdown.webp','poses/b_hip.webp','lions.png','ravens.png','icons/favicon-64.png','icons/icon-192.png','icons/icon-512.png','icons/icon-maskable-512.png','icons/apple-touch-icon.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(SHELL.map(u=>new Request(u,{cache:'reload'})))).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{
  const r=e.request,u=new URL(r.url);
  if(r.method!=='GET'||u.origin!==location.origin)return;           // APIs go straight to the network
  if(u.pathname.endsWith('version.json')){e.respondWith(fetch(r,{cache:'no-store'}));return}  // never cached: update signal
  e.respondWith(caches.match(r,{ignoreSearch:true}).then(c=>c||fetch(r).then(n=>{const cp=n.clone();caches.open(CACHE).then(k=>k.put(r,cp));return n})));
});
