# Builds index.html (installable PWA) from app.html (the artifact source).
src = open('app.html', encoding='utf-8').read()
cut = src.index('</style>') + len('</style>')
head, body = src[:cut], src[cut:]
out = f'''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#0F1D28">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icon-192.png">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}</style>
{head}
</head>
<body>
{body}
<script>if ('serviceWorker' in navigator) navigator.serviceWorker.register('sw.js').catch(() => {{}});</script>
</body>
</html>
'''
open('index.html', 'w', encoding='utf-8').write(out)
print('index.html built', len(out))
