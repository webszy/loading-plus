<script setup lang="ts">
import pages from '~/data/seo-pages.json'
defineProps<{ current: string }>()
</script>
<template><section class="container related"><h2 class="section-title">Related animations</h2>
<div class="related-grid"><NuxtLink v-for="page in Object.values(pages).filter(p => p.path !== current)" :key="page.path" :to="page.path"><h3>{{ page.heading }} <span aria-hidden="true">↗</span></h3><p>{{ page.hero }}</p></NuxtLink></div>
</section></template>
