<script setup lang="ts">
import gifs from '~/data/gifs.json'
defineProps<{ group: keyof typeof gifs; title: string }>()
</script>
<template><section class="container collection"><h2 class="section-title">{{ title }}</h2><p class="section-lead">Original looping GIFs. Free for personal and commercial use; no attribution required. Pause any preview or download a still cover.</p>
<div class="gif-grid" :class="`gif-grid--${group}`"><GifPreviewCard v-for="(asset, index) in gifs[group]" :key="asset.src" :asset="asset" :eager="index === 0" /></div></section></template>
