<template>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="container site-header__inner">
      <NuxtLink class="brand" to="/" aria-label="Loading.plus, home">
        <span class="brand__mark" aria-hidden="true" />
        <span class="brand__name">loading.plus</span>
      </NuxtLink>
      <nav class="site-nav" aria-label="Primary">
        <NuxtLink to="/#animations">Animations</NuxtLink>
        <NuxtLink to="/text-loading">Text Loading</NuxtLink>
        <NuxtLink to="/loading-text-gif">GIFs</NuxtLink>
      </nav>
    </div>
  </header>
</template>

<style scoped>
.site-header {
  position: sticky;
  top: 0;
  z-index: 20;
  height: var(--header-height);
  background: var(--color-bg);
  border-bottom: 1px solid var(--color-border);
}

.site-header__inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  height: 100%;
}

.brand {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  min-width: 0;
  font-weight: 600;
  letter-spacing: -0.03em;
}

.brand__mark {
  position: relative;
  flex: none;
  width: 32px;
  height: 32px;
  border-radius: 9px;
  background: var(--color-accent);
}

.brand__mark::before,
.brand__mark::after {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  border-radius: 1px;
  background: #fff;
  transform: translate(-50%, -50%);
}

.brand__mark::before {
  width: 14px;
  height: 2px;
}

.brand__mark::after {
  width: 2px;
  height: 14px;
}

.brand__name {
  font-size: 16px;
}

.site-nav {
  display: flex;
  align-items: center;
  gap: 22px;
}

.site-nav a {
  display: inline-flex;
  align-items: center;
  height: 44px;
  white-space: nowrap;
  color: var(--color-text-secondary);
  font-size: 15px;
  font-weight: 500;
}

.site-nav a:hover {
  color: var(--color-text);
}

@media (max-width: 720px) {
  .brand {
    gap: 8px;
  }

  .brand__mark {
    width: 28px;
    height: 28px;
    border-radius: 8px;
  }

  .brand__mark::before {
    width: 12px;
  }

  .brand__mark::after {
    height: 12px;
  }

  .brand__name {
    font-size: 14px;
  }

  .site-nav {
    gap: 12px;
  }

  .site-nav a {
    font-size: 13px;
  }
}
</style>
