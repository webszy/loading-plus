export interface FaqItem {
  question: string
  answer: string
}

export const faqItems: FaqItem[] = [
  {
    question: 'What is a loading animation?',
    answer:
      'A loading animation is a short, repeating visual that tells someone the interface is busy. Spinners, animated dots, progress bars, and skeletons are all loading animations. Their job is to explain the pause, so a wait does not feel like a frozen page.',
  },
  {
    question: 'What is the difference between CSS and GIF loaders?',
    answer:
      'A CSS loader is built from markup and styles. It stays sharp at any size, can match an interface color, and can pause when someone prefers reduced motion. A GIF loader is an image sequence. It is simple to place, but its color, size, and timing are fixed in the file, and it does not respond to motion preferences.',
  },
  {
    question: 'When should I use a skeleton loader?',
    answer:
      'Use a skeleton when the finished content has a known layout, such as a card, a list, or an article. The placeholder previews that structure while data is still arriving. A spinner is a better fit when the result has no stable shape, or when the wait belongs to a single control such as a button.',
  },
  {
    question: 'What is an indeterminate progress bar?',
    answer:
      'An indeterminate progress bar moves without showing a percentage. Use it when a task has started and the interface cannot honestly estimate how much is left. If you know how much of the work is complete, show a determinate bar with that value instead.',
  },
]
