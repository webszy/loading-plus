export type AnimationCategory = 'spinners' | 'dots' | 'text' | 'progress' | 'shimmer'

export type AnimationId =
  | 'circular'
  | 'bouncing-dots'
  | 'text-loading'
  | 'indeterminate-bar'
  | 'shimmer'
  | 'pulse'
  | 'orbit'
  | 'wave-bars'
  | 'three-dots'

export interface AnimationItem {
  id: AnimationId
  name: string
  category: AnimationCategory
}

export const animationFilters = [
  { id: 'all', label: 'All' },
  { id: 'spinners', label: 'Spinners' },
  { id: 'dots', label: 'Dots' },
  { id: 'text', label: 'Text' },
  { id: 'progress', label: 'Progress' },
  { id: 'shimmer', label: 'Shimmer' },
] as const

export type AnimationFilter = (typeof animationFilters)[number]['id']

export const animations: AnimationItem[] = [
  { id: 'circular', name: 'Circular Spinner', category: 'spinners' },
  { id: 'bouncing-dots', name: 'Bouncing Dots', category: 'dots' },
  { id: 'text-loading', name: 'Text Loading', category: 'text' },
  { id: 'indeterminate-bar', name: 'Indeterminate Progress Bar', category: 'progress' },
  { id: 'shimmer', name: 'Shimmer Skeleton', category: 'shimmer' },
  { id: 'pulse', name: 'Pulse Loader', category: 'spinners' },
  { id: 'orbit', name: 'Orbit Spinner', category: 'spinners' },
  { id: 'wave-bars', name: 'Wave Bars', category: 'progress' },
  { id: 'three-dots', name: 'Three Dots', category: 'dots' },
]
