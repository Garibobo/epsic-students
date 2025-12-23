// Service Worker pour EPSIC Students PWA
const CACHE_NAME = 'epsic-students-v1.25.1';
const urlsToCache = [
  './',
  './index.html',
  './style.css',
  './avatar-colorful.png',
  './qrcode_site.png',
  './manifest.json'
];

// Installation du Service Worker
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('Cache ouvert');
        return cache.addAll(urlsToCache);
      })
  );
});

// Activation du Service Worker
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log('Suppression ancien cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

// Stratégie Network First avec Cache Fallback
self.addEventListener('fetch', (event) => {
  // Ignorer les requêtes non-GET et les requêtes vers des domaines externes
  if (event.request.method !== 'GET' || 
      !event.request.url.startsWith(self.location.origin)) {
    return;
  }

  // Stratégie spéciale pour l'API GitHub
  if (event.request.url.includes('api.github.com')) {
    event.respondWith(
      fetch(event.request)
        .then((response) => {
          // Si la requête réussit, retourner la réponse
          if (response.ok) {
            return response;
          }
          throw new Error('Réponse réseau non OK');
        })
        .catch(() => {
          // En cas d'échec, retourner une réponse par défaut
          return new Response(JSON.stringify([]), {
            headers: { 'Content-Type': 'application/json' }
          });
        })
    );
    return;
  }

  // Stratégie Network First pour les autres ressources
  event.respondWith(
    fetch(event.request)
      .then((response) => {
        // Si la requête réussit, mettre en cache et retourner
        if (response.ok) {
          const responseToCache = response.clone();
          caches.open(CACHE_NAME)
            .then((cache) => {
              cache.put(event.request, responseToCache);
            });
        }
        return response;
      })
      .catch(() => {
        // En cas d'échec réseau, chercher dans le cache
        return caches.match(event.request)
          .then((response) => {
            if (response) {
              return response;
            }
            // Si pas trouvé dans le cache, retourner page offline pour les pages HTML
            if (event.request.headers.get('accept').includes('text/html')) {
              return caches.match('./index.html');
            }
          });
      })
  );
});

// Gestion des messages du client
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});
