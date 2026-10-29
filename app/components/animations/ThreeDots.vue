<template>
  <span class="three">
    <i /><i /><i />
  </span>
</template>

<style scoped>
.three {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 10px 14px;
  border-radius: 999px;
  background: color-mix(in srgb, var(--color-accent) 10%, white);
}

.three i {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--color-accent);
  opacity: 0.9;
}

@media (prefers-reduced-motion: no-preference) {
  .three i {
    animation: blink 1.2s ease-in-out infinite;
  }

  .three i:nth-child(2) {
    animation-delay: 0.15s;
  }

  .three i:nth-child(3) {
    animation-delay: 0.3s;
  }
}

@keyframes blink {
  0%,
  80%,
  100% {
    opacity: 0.28;
    transform: scale(0.8);
  }

  40% {
    opacity: 1;
    transform: scale(1);
  }
}
</style>
