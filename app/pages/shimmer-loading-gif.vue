<script setup lang="ts">
const code = "<div role=\"status\">\n  <picture>\n    <source media=\"(prefers-reduced-motion: reduce)\"\n            srcset=\"/gifs/shimmer/card-skeleton-loading.png\">\n    <img id=\"loading-preview\" src=\"/gifs/shimmer/card-skeleton-loading.gif\"\n         width=\"480\" height=\"260\" alt=\"\"\n         style=\"max-width: 100%; height: auto;\">\n  </picture>\n  <span>Loading content\u2026</span>\n</div>\n<button type=\"button\" onclick=\"document.getElementById('loading-preview').src='/gifs/shimmer/card-skeleton-loading.png'\">\n  Stop animation\n</button>"
</script>
<template><SeoLandingPage page-key="shimmer-loading-gif" :code="code"><GifCollection group="shimmer" title="Placeholders in context" /></SeoLandingPage></template>
