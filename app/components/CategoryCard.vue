<script setup lang="ts">
defineProps<{
  title: string
  description: string
  href?: string
}>()
</script>

<template>
  <article class="category-card">
    <div class="category-card__preview" aria-hidden="true">
      <slot />
    </div>
    <div class="category-card__body">
      <h3>
        <NuxtLink v-if="href" :to="href">{{ title }}</NuxtLink>
        <template v-else>{{ title }}</template>
      </h3>
      <p>{{ description }}</p>
    </div>
  </article>
</template>

<style scoped>
.category-card {
  display: grid;
  grid-template-columns: 1fr;
  min-width: 0;
  overflow: hidden;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-card);
  background: var(--color-bg);
}

.category-card__preview {
  display: grid;
  min-height: 112px;
  place-items: center;
  overflow: hidden;
  background: var(--color-card);
}

.category-card__body {
  padding: 18px 18px 20px;
}

h3 {
  font-size: 18px;
  line-height: 1.3;
}

h3 a:hover {
  color: var(--color-accent);
}

p {
  margin-top: 8px;
  color: var(--color-text-secondary);
  font-size: 15px;
  line-height: 1.55;
}

@media (min-width: 640px) {
  .category-card {
    grid-template-columns: 168px 1fr;
    min-height: 148px;
  }

  .category-card__body {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 20px 22px 20px 4px;
  }
}
</style>
