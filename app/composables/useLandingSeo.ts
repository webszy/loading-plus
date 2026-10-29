export function useLandingSeo(page: { path: string; heading: string; title: string; description: string }) {
  const url = `https://loading.plus${page.path}`
  useSeoMeta({ title: page.title, description: page.description, ogTitle: page.title,
    ogDescription: page.description, ogType: 'website', ogUrl: url, twitterCard: 'summary',
    twitterTitle: page.title, twitterDescription: page.description })
  useHead({ link: [{ rel: 'canonical', href: url }], script: [{ key: 'landing-schema', type: 'application/ld+json', innerHTML: JSON.stringify({
    '@context': 'https://schema.org', '@graph': [
      { '@type': 'WebPage', name: page.heading, description: page.description, url, inLanguage: 'en' },
      { '@type': 'BreadcrumbList', itemListElement: [
        { '@type': 'ListItem', position: 1, name: 'Home', item: 'https://loading.plus/' },
        { '@type': 'ListItem', position: 2, name: page.heading, item: url },
      ] },
    ],
  }) }] })
}
