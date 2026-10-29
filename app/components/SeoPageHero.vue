<script setup lang="ts">
defineProps<{ heading: string; description: string }>()
</script>
<template>
  <div class="container landing-hero">
    <nav aria-label="Breadcrumb" class="breadcrumb"><NuxtLink to="/">Home</NuxtLink><span aria-hidden="true">/</span><span aria-current="page">{{ heading }}</span></nav>
    <p class="landing-eyebrow">The motion collection</p>
    <h1>{{ heading }}</h1><p class="section-lead">{{ description }}</p>
    <NuxtLink class="text-link" to="/#categories">Browse all animation categories →</NuxtLink>
  </div>
</template>
