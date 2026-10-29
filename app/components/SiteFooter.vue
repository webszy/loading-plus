<template>
  <footer class="site-footer">
    <div class="container">
      <div class="site-footer__top">
        <div>
          <p class="site-footer__name">Loading.plus</p>
          <p class="site-footer__tag">Simple animations for better interfaces.</p>
        </div>
        <nav class="site-footer__nav" aria-label="Footer">
          <a href="#animations">Animations</a>
          <a href="#categories">Categories</a>
          <a href="#faq">FAQ</a>
        </nav>
      </div>
      <p class="site-footer__copy">© 2026 Loading.plus</p>
    </div>
  </footer>
</template>

<style scoped>
.site-footer {
  padding: 36px 0 28px;
  border-top: 1px solid var(--color-border);
}

.site-footer__top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 24px;
}

.site-footer__name {
  font-size: 16px;
  font-weight: 600;
  letter-spacing: -0.03em;
}

.site-footer__tag {
  margin-top: 6px;
  color: var(--color-text-secondary);
  font-size: 14px;
}

.site-footer__nav {
  display: flex;
  flex-wrap: wrap;
  gap: 8px 20px;
}

.site-footer__nav a {
  color: var(--color-text-secondary);
  font-size: 14px;
  font-weight: 500;
}

.site-footer__nav a:hover {
  color: var(--color-text);
}

.site-footer__copy {
  margin-top: 28px;
  color: var(--color-text-secondary);
  font-size: 14px;
}

@media (max-width: 640px) {
  .site-footer__top {
    flex-direction: column;
  }
}
</style>
