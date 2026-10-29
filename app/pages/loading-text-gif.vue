<script setup lang="ts">
const code = "<div role=\"status\">\n  <picture>\n    <source media=\"(prefers-reduced-motion: reduce)\"\n            srcset=\"/gifs/loading-text/classic-loading-text.png\">\n    <img id=\"loading-preview\" src=\"/gifs/loading-text/classic-loading-text.gif\"\n         width=\"400\" height=\"160\" alt=\"\"\n         style=\"max-width: 100%; height: auto;\">\n  </picture>\n  <span>Loading content\u2026</span>\n</div>\n<button type=\"button\" onclick=\"document.getElementById('loading-preview').src='/gifs/loading-text/classic-loading-text.png'\">\n  Stop animation\n</button>"
</script>
<template><SeoLandingPage page-key="loading-text-gif" :code="code"><GifCollection group="loading-text" title="Ready-made waiting messages" /></SeoLandingPage></template>
