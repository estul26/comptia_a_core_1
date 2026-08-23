const CACHE="aplus-uyghur-v5";
const CORE=[
  "/",
  "/index.html",
  "/manifest.webmanifest",
  "/favicon.svg",
  "/icons/icon-192.png",
  "/icons/icon-512.png"
];

self.addEventListener("install",event=>{
  event.waitUntil(caches.open(CACHE).then(cache=>cache.addAll(CORE)));
  self.skipWaiting();
});

self.addEventListener("activate",event=>{
  event.waitUntil(
    caches.keys()
      .then(keys=>Promise.all(keys.filter(k=>k!==CACHE).map(k=>caches.delete(k))))
      .then(()=>self.clients.claim())
  );
});

self.addEventListener("fetch",event=>{
  const req=event.request;
  if(req.method!=="GET")return;

  const url=new URL(req.url);
  if(url.origin!==location.origin){
    // External fonts/resources: use network; do not block the app offline.
    return;
  }

  if(req.mode==="navigate"){
    event.respondWith(
      fetch(req)
        .then(res=>{
          const copy=res.clone();
          caches.open(CACHE).then(c=>c.put("/index.html",copy));
          return res;
        })
        .catch(()=>caches.match("/index.html"))
    );
    return;
  }

  event.respondWith(
    caches.match(req).then(cached=>{
      const fresh=fetch(req).then(res=>{
        if(res && res.ok){
          const copy=res.clone();
          caches.open(CACHE).then(c=>c.put(req,copy));
        }
        return res;
      }).catch(()=>cached);
      return cached || fresh;
    })
  );
});
