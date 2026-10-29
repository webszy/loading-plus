<script setup lang="ts">
import pages from '~/data/seo-pages.json'
const props = defineProps<{ pageKey: keyof typeof pages; code: string }>()
const page = pages[props.pageKey]
useLandingSeo(page)
</script>
<template>
  <SiteHeader /><main id="main" class="landing-page">
    <SeoPageHero :heading="page.heading" :description="page.hero" />
    <slot />
    <div class="container editorial">
      <section v-for="section in page.sections" :key="section.title"><h2>{{ section.title }}</h2><p>{{ section.text }}</p></section>
      <section><h2>Implementation example</h2><p><template v-if="pageKey === 'text-loading'">Copy this HTML and CSS into your page. Show the status while work is pending and replace it when the task finishes.</template><template v-else>Copy this HTML into your page. Download both the GIF and its still cover and keep the file paths consistent.</template></p><pre><code>{{ code }}</code></pre></section>
    </div>
    <FaqSection :items="page.faq" />
    <RelatedAnimations :current="page.path" />
  </main><SiteFooter />
</template>
