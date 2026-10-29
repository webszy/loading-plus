<script setup lang="ts">
import { animationFilters, animations, type AnimationFilter } from '~/data/animations'

const active = ref<AnimationFilter>('all')

const visible = computed(() => {
  if (active.value === 'all') {
    return animations
  }

  return animations.filter(item => item.category === active.value)
})

const activeLabel = computed(() => {
  return animationFilters.find(filter => filter.id === active.value)?.label ?? 'All'
})
</script>

<template>
  <section id="animations" class="gallery" aria-labelledby="animations-title">
    <div class="container">
      <h2 id="animations-title" class="section-title">Explore loading animations</h2>
      <p class="section-lead">
        A collection of simple, beautiful loading animations for modern interfaces.
      </p>

      <div class="filters" role="group" aria-label="Filter animations">
        <button
          v-for="filter in animationFilters"
          :key="filter.id"
          type="button"
          class="filter-btn"
          :aria-pressed="active === filter.id"
          @click="active = filter.id"
        >
          {{ filter.label }}
        </button>
      </div>
      <p class="visually-hidden" aria-live="polite">
        Showing {{ activeLabel }}: {{ visible.length }} animations
      </p>

      <ul class="gallery-grid">
        <li v-for="item in visible" :key="item.id">
          <AnimationCard :item="item" />
        </li>
      </ul>
    </div>
  </section>
</template>

<style scoped>
.gallery {
  padding: 28px 0 72px;
}

.filters {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 18px;
}

.filter-btn {
  border: 1px solid transparent;
  border-radius: 999px;
  padding: 6px 12px;
  color: var(--color-text-secondary);
  font-size: 14px;
  font-weight: 500;
}

.filter-btn:hover {
  color: var(--color-text);
}

.filter-btn[aria-pressed="true"] {
  background: var(--color-accent-soft);
  color: var(--color-accent-strong);
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
  margin-top: 18px;
  padding: 0;
  list-style: none;
}

.gallery-grid > li {
  min-width: 0;
}

@media (min-width: 768px) {
  .gallery {
    padding-top: 32px;
  }

  .gallery-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 16px;
  }
}

@media (min-width: 1100px) {
  .gallery-grid {
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }
}
</style>
