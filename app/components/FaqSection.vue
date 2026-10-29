<script setup lang="ts">
import { faqItems } from '~/data/faq'
</script>

<template>
  <section id="faq" class="faq" aria-labelledby="faq-title">
    <div class="container faq__inner">
      <h2 id="faq-title" class="section-title">Frequently asked questions</h2>
      <div class="faq__list">
        <details v-for="item in faqItems" :key="item.question" class="faq-item">
          <summary>
            <h3>{{ item.question }}</h3>
          </summary>
          <p>{{ item.answer }}</p>
        </details>
      </div>
    </div>
  </section>
</template>

<style scoped>
.faq {
  padding: 8px 0 80px;
}

.faq__inner {
  max-width: 760px;
}

.faq__list {
  margin-top: 8px;
  border-top: 1px solid var(--color-border);
}

.faq-item {
  border-bottom: 1px solid var(--color-border);
}

.faq-item summary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 18px 0;
  cursor: pointer;
  list-style: none;
}

.faq-item summary::-webkit-details-marker {
  display: none;
}

.faq-item summary::after {
  content: "";
  flex: none;
  width: 12px;
  height: 12px;
  background:
    linear-gradient(currentColor, currentColor) center / 12px 1.5px no-repeat,
    linear-gradient(currentColor, currentColor) center / 1.5px 12px no-repeat;
  color: var(--color-text-secondary);
}

.faq-item[open] summary::after {
  background: linear-gradient(currentColor, currentColor) center / 12px 1.5px no-repeat;
}

.faq-item h3 {
  font-size: 16px;
  font-weight: 600;
  line-height: 1.4;
  letter-spacing: -0.02em;
}

.faq-item p {
  max-width: 65ch;
  padding-bottom: 18px;
  color: var(--color-text);
  font-size: 15px;
  line-height: 1.65;
}
</style>
