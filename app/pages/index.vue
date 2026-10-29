<script setup lang="ts">
import { faqItems } from '~/data/faq'
import { site } from '~/data/site'

const websiteSchema = {
  '@context': 'https://schema.org',
  '@type': 'WebSite',
  name: site.name,
  url: site.url,
  description: site.description,
  inLanguage: 'en',
}

const faqSchema = {
  '@context': 'https://schema.org',
  '@type': 'FAQPage',
  mainEntity: faqItems.map(item => ({
    '@type': 'Question',
    name: item.question,
    acceptedAnswer: {
      '@type': 'Answer',
      text: item.answer,
    },
  })),
}

useSeoMeta({
  title: site.title,
  description: site.description,
  ogTitle: site.title,
  ogDescription: site.description,
  ogUrl: site.url,
  ogType: 'website',
  ogSiteName: site.name,
  ogLocale: 'en_US',
  twitterCard: 'summary',
  twitterTitle: site.title,
  twitterDescription: site.description,
})

useHead({
  link: [{ rel: 'canonical', href: site.url }],
  script: [
    {
      key: 'ld-website',
      type: 'application/ld+json',
      innerHTML: JSON.stringify(websiteSchema),
    },
    {
      key: 'ld-faq',
      type: 'application/ld+json',
      innerHTML: JSON.stringify(faqSchema),
    },
  ],
})
</script>

<template>
  <SiteHeader />
  <main id="main">
    <HeroSection />
    <AnimationGallery />
    <CategorySection />
    <SeoContent />
    <FaqSection />
  </main>
  <SiteFooter />
</template>
