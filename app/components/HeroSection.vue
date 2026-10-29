<template>
  <section class="hero">
    <div class="container hero__inner">
      <p class="eyebrow">
        <span class="eyebrow__dot" aria-hidden="true" />
        Free loading animations
      </p>
      <h1>
        Make waiting<br>
        <span>look better.</span>
      </h1>
      <p class="hero__lead">
        Beautiful loading animations, GIFs, and UI components.
        Find CSS loaders, loading spinners, and the perfect loading state for your next project.
      </p>
      <a class="hero__link" href="#animations">
        Explore animations
        <svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true">
          <path
            d="M3.5 6.5 8 11l4.5-4.5"
            fill="none"
            stroke="currentColor"
            stroke-width="1.5"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </svg>
      </a>
    </div>
  </section>
</template>

<style scoped>
.hero {
  padding: 40px 0 4px;
}

.hero__inner {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 5px 11px 5px 9px;
  border-radius: 999px;
  background: var(--color-accent-soft);
  color: var(--color-accent-strong);
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.eyebrow__dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--color-accent);
}

h1 {
  margin-top: 18px;
  font-size: 40px;
  line-height: 1.05;
  letter-spacing: -0.04em;
}

h1 span {
  color: var(--color-accent);
}

.hero__lead {
  margin-top: 14px;
  max-width: 38rem;
  color: var(--color-text-secondary);
  font-size: 16px;
  line-height: 1.55;
}

.hero__link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-top: 16px;
  color: var(--color-accent);
  font-size: 15px;
  font-weight: 600;
}

.hero__link:hover {
  text-decoration: underline;
  text-underline-offset: 3px;
}

@media (min-width: 768px) {
  .hero {
    padding-top: 48px;
  }

  h1 {
    font-size: 52px;
  }

  .hero__lead {
    font-size: 17px;
  }
}

@media (min-width: 1100px) {
  h1 {
    font-size: 60px;
  }
}
</style>
