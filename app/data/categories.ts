import type { AnimationId } from './animations'

export interface CategoryItem {
  id: string
  title: string
  description: string
  preview: AnimationId
  /** Reserved for a future category page. Omit until that route exists. */
  href?: string
}

export const categories: CategoryItem[] = [
  {
    id: 'css-loading-animations',
    title: 'CSS Loading Animations',
    description: 'Lightweight CSS spinners, dots, and animated loaders for websites.',
    preview: 'circular',
  },
  {
    id: 'text-loading-animations',
    title: 'Text Loading Animations',
    description: 'Animated loading text, typing effects, and waiting indicators.',
    preview: 'text-loading',
  },
  {
    id: 'progress-bar-animations',
    title: 'Progress Bar Animations',
    description: 'Indeterminate progress bars and smooth loading indicators.',
    preview: 'indeterminate-bar',
  },
  {
    id: 'shimmer-skeleton-loaders',
    title: 'Shimmer & Skeleton Loaders',
    description: 'Skeleton screens and shimmer placeholders for loading content.',
    preview: 'shimmer',
  },
]
