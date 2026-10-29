<template>
  <span class="bouncing">
    <i /><i /><i />
  </span>
</template>

<style scoped>
.bouncing {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  gap: 7px;
  height: 32px;
}

.bouncing i {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--color-accent);
}

@media (prefers-reduced-motion: no-preference) {
  .bouncing i {
    animation: bounce 0.9s ease-in-out infinite;
  }

  .bouncing i:nth-child(2) {
    animation-delay: 0.12s;
  }

  .bouncing i:nth-child(3) {
    animation-delay: 0.24s;
  }
}

@keyframes bounce {
  0%,
  100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-12px);
  }
}
</style>
