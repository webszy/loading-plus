<template>
  <span class="text-loader">
    <span class="text-loader__word">Loading</span>
    <span class="text-loader__dots"><i /><i /><i /></span>
  </span>
</template>

<style scoped>
.text-loader {
  display: inline-flex;
  align-items: flex-end;
  gap: 2px;
  color: var(--color-accent);
  font-size: 17px;
  font-weight: 600;
  letter-spacing: -0.03em;
  line-height: 1;
}

.text-loader__dots {
  display: inline-flex;
  gap: 2px;
  padding-bottom: 3px;
}

.text-loader__dots i {
  width: 3px;
  height: 3px;
  border-radius: 50%;
  background: currentColor;
  opacity: 0.35;
}

@media (prefers-reduced-motion: no-preference) {
  .text-loader__dots i {
    animation: dot 1.2s ease-in-out infinite;
  }

  .text-loader__dots i:nth-child(2) {
    animation-delay: 0.15s;
  }

  .text-loader__dots i:nth-child(3) {
    animation-delay: 0.3s;
  }
}

@keyframes dot {
  0%,
  70%,
  100% {
    opacity: 0.25;
    transform: translateY(0);
  }

  35% {
    opacity: 1;
    transform: translateY(-2px);
  }
}
</style>
