const CACHE = "aplus-uyghur-v6.5-rtl-content-polish-translation-v5.30";
const CORE = [
  "/",
  "/index.html",
  "/manifest.webmanifest",
  "/favicon.svg",
  "/icons/icon-192.png",
  "/icons/icon-512.png"
];

const FONT_HOSTS = new Set([
  "fonts.googleapis.com",
  "fonts.gstatic.com"
]);

self.addEventListener("install", event => {
  event.waitUntil(caches.open(CACHE).then(cache => cache.addAll(CORE)));
  self.skipWaiting();
});

self.addEventListener("activate", event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

async function cacheFirst(request) {
  const cache = await caches.open(CACHE);
  const cached = await cache.match(request);
  if (cached) {
    fetch(request).then(response => {
      if (response && (response.ok || response.type === "opaque")) {
        cache.put(request, response.clone());
      }
    }).catch(() => {});
    return cached;
  }

  const response = await fetch(request);
  if (response && (response.ok || response.type === "opaque")) {
    cache.put(request, response.clone());
  }
  return response;
}

self.addEventListener("fetch", event => {
  const request = event.request;
  if (request.method !== "GET") return;

  const url = new URL(request.url);

  // Cache Google Fonts after the first successful online visit.
  // This preserves the preferred Uyghur typography during later offline use.
  if (url.origin !== self.location.origin) {
    if (FONT_HOSTS.has(url.hostname)) {
      event.respondWith(
        cacheFirst(request).catch(() => caches.match(request))
      );
    }
    return;
  }

  // Network-first for page navigation so newly deployed versions appear quickly.
  if (request.mode === "navigate") {
    event.respondWith(
      fetch(request)
        .then(response => {
          if (response && response.ok) {
            const copy = response.clone();
            caches.open(CACHE).then(cache => cache.put("/index.html", copy));
          }
          return response;
        })
        .catch(() => caches.match("/index.html"))
    );
    return;
  }

  // Cache-first for local static assets, while refreshing them in the background.
  event.respondWith(
    cacheFirst(request).catch(() => caches.match(request))
  );
});
