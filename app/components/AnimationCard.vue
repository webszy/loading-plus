<script setup lang="ts">
import type { AnimationItem } from '~/data/animations'

defineProps<{
  item: AnimationItem
}>()
</script>

<template>
  <article class="animation-card">
    <div class="animation-card__stage" aria-hidden="true">
      <AnimationPreview :id="item.id" />
    </div>
    <div class="animation-card__meta">
      <h3>{{ item.name }}</h3>
      <span class="css-tag">CSS</span>
    </div>
  </article>
</template>

<style scoped>
.animation-card {
  display: flex;
  flex-direction: column;
  height: 100%;
  overflow: hidden;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-card);
  background: var(--color-bg);
  transition: border-color 160ms ease;
}

.animation-card:hover {
  border-color: var(--color-border-hover);
}

.animation-card__stage {
  display: grid;
  height: 120px;
  place-items: center;
  overflow: hidden;
  background: var(--color-card);
}

.animation-card__meta {
  display: flex;
  flex: 1;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding: 12px 14px;
  border-top: 1px solid var(--color-border);
}

h3 {
  min-width: 0;
  font-size: 14px;
  font-weight: 500;
  line-height: 1.35;
  letter-spacing: -0.015em;
}

.css-tag {
  flex: none;
  padding: 3px 7px;
  border-radius: 999px;
  background: var(--color-accent-soft);
  color: var(--color-accent-strong);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.04em;
}

@media (min-width: 768px) {
  .animation-card__stage {
    height: 148px;
  }
}
</style>
