<template>
  <span class="pulse">
    <span class="pulse__ring" />
    <span class="pulse__core" />
  </span>
</template>

<style scoped>
.pulse {
  position: relative;
  display: grid;
  width: 44px;
  height: 44px;
  place-items: center;
}

.pulse__ring,
.pulse__core {
  grid-area: 1 / 1;
  border-radius: 50%;
}

.pulse__core {
  width: 12px;
  height: 12px;
  background: var(--color-accent);
}

.pulse__ring {
  width: 40px;
  height: 40px;
  border: 2px solid var(--color-accent);
  opacity: 0.4;
}

@media (prefers-reduced-motion: no-preference) {
  .pulse__ring {
    animation: pulse 1.7s ease-out infinite;
  }
}

@keyframes pulse {
  0% {
    opacity: 0.55;
    transform: scale(0.55);
  }

  100% {
    opacity: 0;
    transform: scale(1);
  }
}
</style>
