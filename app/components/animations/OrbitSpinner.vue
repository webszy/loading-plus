<template>
  <span class="orbit">
    <span class="orbit__core" />
    <span class="orbit__path">
      <span class="orbit__dot" />
    </span>
  </span>
</template>

<style scoped>
.orbit {
  position: relative;
  width: 42px;
  height: 42px;
}

.orbit__core {
  position: absolute;
  inset: 0;
  width: 10px;
  height: 10px;
  margin: auto;
  border-radius: 50%;
  background: var(--color-accent);
}

.orbit__path {
  position: absolute;
  inset: 0;
}

.orbit__dot {
  position: absolute;
  top: 0;
  left: 50%;
  width: 7px;
  height: 7px;
  margin-left: -3.5px;
  border-radius: 50%;
  background: color-mix(in srgb, var(--color-accent) 72%, white);
}

@media (prefers-reduced-motion: no-preference) {
  .orbit__path {
    animation: spin 1.6s linear infinite;
  }
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}
</style>
