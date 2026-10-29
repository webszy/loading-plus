<template>
  <span class="wave">
    <i /><i /><i /><i /><i />
  </span>
</template>

<style scoped>
.wave {
  display: flex;
  align-items: flex-end;
  gap: 5px;
  height: 28px;
}

.wave i {
  display: block;
  width: 4px;
  border-radius: 999px;
  background: var(--color-accent);
  transform-origin: center bottom;
}

.wave i:nth-child(1) {
  height: 10px;
}

.wave i:nth-child(2) {
  height: 18px;
}

.wave i:nth-child(3) {
  height: 28px;
}

.wave i:nth-child(4) {
  height: 16px;
}

.wave i:nth-child(5) {
  height: 12px;
}

@media (prefers-reduced-motion: no-preference) {
  .wave i {
    animation: wave 1s ease-in-out infinite;
  }

  .wave i:nth-child(2) {
    animation-delay: 0.1s;
  }

  .wave i:nth-child(3) {
    animation-delay: 0.2s;
  }

  .wave i:nth-child(4) {
    animation-delay: 0.3s;
  }

  .wave i:nth-child(5) {
    animation-delay: 0.4s;
  }
}

@keyframes wave {
  0%,
  100% {
    transform: scaleY(0.45);
  }

  50% {
    transform: scaleY(1);
  }
}
</style>
