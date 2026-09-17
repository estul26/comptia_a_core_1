const CACHE_PREFIX = "aplus-uyghur-";
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

function isCacheable(response) {
  return Boolean(response && (response.ok || response.type === "opaque"));
}

self.addEventListener("install", event => {
  event.waitUntil(
    Promise.all([
      caches.open(CACHE).then(cache => cache.addAll(CORE)),
      self.skipWaiting()
    ])
  );
});

self.addEventListener("activate", event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        keys
          .filter(key => key.startsWith(CACHE_PREFIX) && key !== CACHE)
          .map(key => caches.delete(key))
      ))
      .then(() => self.clients.claim())
  );
});

async function cacheFirst(request, event) {
  const cache = await caches.open(CACHE);
  const cached = await cache.match(request);

  if (cached) {
    const refresh = fetch(request)
      .then(async response => {
        if (isCacheable(response)) {
          await cache.put(request, response.clone());
        }
      })
      .catch(() => {});

    event.waitUntil(refresh);
    return cached;
  }

  const response = await fetch(request);
  if (isCacheable(response)) {
    await cache.put(request, response.clone());
  }
  return response;
}

async function navigationNetworkFirst(request, event) {
  try {
    const response = await fetch(request);
    if (response && response.ok) {
      const copy = response.clone();
      const update = caches.open(CACHE)
        .then(cache => cache.put("/index.html", copy))
        .catch(() => {});
      event.waitUntil(update);
    }
    return response;
  } catch (error) {
    const cached = await caches.match("/index.html");
    if (cached) return cached;
    throw error;
  }
}

self.addEventListener("fetch", event => {
  const request = event.request;
  if (request.method !== "GET") return;

  const url = new URL(request.url);

  // Cache Google Fonts after the first successful online visit.
  // This preserves the preferred Uyghur typography during later offline use.
  if (url.origin !== self.location.origin) {
    if (FONT_HOSTS.has(url.hostname)) {
      event.respondWith(cacheFirst(request, event));
    }
    return;
  }

  // Network-first for page navigation so newly deployed versions appear quickly.
  if (request.mode === "navigate") {
    event.respondWith(navigationNetworkFirst(request, event));
    return;
  }

  // Cache-first for local static assets, while refreshing them in the background.
  event.respondWith(cacheFirst(request, event));
});
