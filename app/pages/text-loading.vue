<script setup lang="ts">
const code = "<p role=\"status\">Loading<span class=\"dots\" aria-hidden=\"true\">...</span></p>\n<style>\n  .dots { display: inline-block; }\n  @media (prefers-reduced-motion: no-preference) {\n    .dots { animation: pulse 1.2s ease-in-out infinite; }\n  }\n  @keyframes pulse { 50% { opacity: .25; } }\n</style>"
</script>
<template><SeoLandingPage page-key="text-loading" :code="code"><TextAnimationCollection /></SeoLandingPage></template>
