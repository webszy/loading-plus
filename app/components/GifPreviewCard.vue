<script setup lang="ts">
defineProps<{ asset: { name: string; description: string; src: string; poster: string; width: number; height: number; bytes: number; alt: string }; eager?: boolean }>()
const paused = ref(false)
</script>
<template>
  <figure class="gif-card">
    <div class="gif-stage"><picture>
      <source media="(prefers-reduced-motion: reduce)" :srcset="asset.poster">
      <img :src="paused ? asset.poster : asset.src" :alt="asset.alt" :width="asset.width" :height="asset.height" :loading="eager ? 'eager' : 'lazy'" decoding="async">
    </picture></div>
    <figcaption><h3>{{ asset.name }}</h3><p>{{ asset.description }}</p>
      <p class="asset-spec">{{ asset.width }} × {{ asset.height }} px · {{ (asset.bytes / 1024).toFixed(1) }} KB · GIF</p>
      <div class="asset-actions"><a class="download-link" :href="asset.src" download>Download GIF <span class="visually-hidden">— {{ asset.name }}</span><span aria-hidden="true">↓</span></a>
      <button class="motion-toggle" type="button" :aria-pressed="paused" :aria-label="`Static preview: ${asset.name}`" @click="paused = !paused">{{ paused ? 'Play preview' : 'Pause preview' }}</button>
      <span class="reduced-label">Static preview · reduced motion</span>
      <a class="text-link" :href="asset.poster" download>PNG cover<span class="visually-hidden"> — {{ asset.name }}</span></a></div>
    </figcaption>
  </figure>
</template>
