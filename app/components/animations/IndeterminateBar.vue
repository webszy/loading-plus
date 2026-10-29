<template>
  <span class="track">
    <span class="bar" />
  </span>
</template>

<style scoped>
.track {
  position: relative;
  display: block;
  width: min(132px, 70%);
  height: 6px;
  overflow: hidden;
  border-radius: 999px;
  background: color-mix(in srgb, var(--color-accent) 16%, white);
}

.bar {
  position: absolute;
  top: 0;
  left: 0;
  width: 42%;
  height: 100%;
  border-radius: inherit;
  background: var(--color-accent);
  transform: translateX(70%);
}

@media (prefers-reduced-motion: no-preference) {
  .bar {
    animation: slide 1.3s ease-in-out infinite;
  }
}

@keyframes slide {
  0% {
    transform: translateX(-110%);
  }

  100% {
    transform: translateX(250%);
  }
}
</style>
