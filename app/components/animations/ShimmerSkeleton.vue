<template>
  <span class="shimmer">
    <i /><i /><i />
  </span>
</template>

<style scoped>
.shimmer {
  display: grid;
  gap: 8px;
  width: min(132px, 72%);
}

.shimmer i {
  position: relative;
  display: block;
  height: 10px;
  overflow: hidden;
  border-radius: 6px;
  background: #e6e8f0;
}

.shimmer i:nth-child(1) {
  width: 100%;
}

.shimmer i:nth-child(2) {
  width: 84%;
}

.shimmer i:nth-child(3) {
  width: 58%;
}

.shimmer i::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, transparent, rgb(255 255 255 / 88%), transparent);
  transform: translateX(-100%);
}

@media (prefers-reduced-motion: no-preference) {
  .shimmer i::after {
    animation: sheen 1.6s ease-in-out infinite;
  }
}

@keyframes sheen {
  to {
    transform: translateX(100%);
  }
}
</style>
