<template>
  <span class="circular" />
</template>

<style scoped>
.circular {
  width: 34px;
  height: 34px;
  border: 3px solid color-mix(in srgb, var(--color-accent) 18%, transparent);
  border-top-color: var(--color-accent);
  border-radius: 50%;
}

@media (prefers-reduced-motion: no-preference) {
  .circular {
    animation: spin 0.8s linear infinite;
  }
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}
</style>
