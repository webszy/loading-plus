<script setup lang="ts">
import { categories } from '~/data/categories'
</script>

<template>
  <section id="categories" class="categories" aria-labelledby="categories-title">
    <div class="container">
      <h2 id="categories-title" class="section-title">Explore by category</h2>
      <p class="section-lead">
        Four kinds of loading states, from spinners to skeleton screens.
      </p>
      <div class="category-grid">
        <CategoryCard
          v-for="category in categories"
          :key="category.id"
          :title="category.title"
          :description="category.description"
          :href="category.href"
        >
          <AnimationPreview :id="category.preview" />
        </CategoryCard>
      </div>
      <p style="margin-top: 20px"><NuxtLink class="text-link" to="/loading-text-gif">Prefer ready-made images? Browse loading text GIFs →</NuxtLink></p>
    </div>
  </section>
</template>

<style scoped>
.categories {
  padding: 8px 0 72px;
}

.category-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
  margin-top: 24px;
}

@media (min-width: 900px) {
  .category-grid {
    grid-template-columns: 1fr 1fr;
  }
}
</style>
