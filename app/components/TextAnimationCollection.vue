<script setup lang="ts">
import TextLoading from './animations/TextLoading.vue'
const paused = ref(false)
const examples = [
  { id: 'blink', name: 'Blinking Loading Text', text: 'Loading...', description: 'A crisp, stepped change in emphasis.', tag: 'CSS · opacity' },
  { id: 'typing', name: 'Typing Loading Text', text: 'Please wait', description: 'Characters appear in discrete typing steps.', tag: 'CSS · steps' },
  { id: 'wave', name: 'Wave Text Loading', text: 'Loading', description: 'A gentle wave passes through each letter.', tag: 'CSS · transform' },
  { id: 'fade', name: 'Fading Loading Text', text: 'Processing', description: 'A smooth pulse keeps the message calm.', tag: 'CSS · opacity' },
  { id: 'dots', name: 'Animated Loading Dots', text: 'Loading', description: 'A steady word with three moving dots.', tag: 'CSS · stagger' },
  { id: 'letters', name: 'Letter-by-Letter Loading', text: 'Loading', description: 'Sequential emphasis travels across the word.', tag: 'CSS · delay' },
]
</script>
<template>
  <section class="container collection text-collection" :class="{ 'is-paused': paused }">
    <div class="collection-heading"><div><h2 class="section-title">Six ways to say “one moment”</h2><p class="section-lead">Live HTML and CSS. No images, animation libraries, or JavaScript timers.</p></div><button class="download-link" type="button" :aria-pressed="paused" @click="paused = !paused">{{ paused ? 'Play animations' : 'Pause animations' }}</button></div>
    <div class="text-grid"><article v-for="item in examples" :key="item.id" class="text-demo">
      <div class="text-stage" aria-hidden="true"><TextLoading v-if="item.id === 'dots'" /><span v-else class="live-text" :class="`effect-${item.id}`"><template v-if="item.id === 'wave' || item.id === 'letters'"><span v-for="(letter, i) in item.text" :key="i" :style="{ '--i': i }">{{ letter }}</span></template><template v-else>{{ item.text }}</template></span></div>
      <div class="text-demo-body"><h3>{{ item.name }}</h3><p>{{ item.description }}</p><span class="effect-tag">{{ item.tag }}</span></div>
    </article></div>
  </section>
</template>
<style scoped>
.text-grid { display: grid; grid-template-columns: repeat(3,minmax(0,1fr)); gap: 20px; margin-top: 24px; }
.text-demo { border: 1px solid var(--color-border); border-radius: var(--radius-card); overflow: hidden; }
.text-stage { display: grid; place-items: center; height: 176px; background: var(--color-card); }
.text-demo-body { padding: 20px; }
h3 { font-size: 18px; }
p { color: var(--color-text-secondary); font-size: 14px; margin-top: 8px; }
.effect-tag { display: inline-block; margin-top: 16px; font-size: 12px; color: var(--color-accent-strong); background: var(--color-accent-soft); padding: 4px 8px; border-radius: 30px; }
.live-text { color: var(--color-accent); font-size: 24px; font-weight: 600; display: inline-block; }
.live-text span { display: inline-block; }
.effect-typing { font-family: monospace; white-space: nowrap; }
@media (prefers-reduced-motion: no-preference) {
  .effect-blink { animation: blink 1.6s steps(2,end) infinite; }
  .effect-typing { animation: typing 2.8s steps(11,end) infinite; }
  .effect-wave span { animation: wave 1.6s ease-in-out infinite; animation-delay: calc(var(--i) * 100ms); }
  .effect-fade { animation: fade 2s ease-in-out infinite; }
  .effect-letters span { animation: fade 1.6s ease-in-out infinite; animation-delay: calc(var(--i) * 140ms); }
}
.is-paused :deep(*) { animation-play-state: paused !important; }
@keyframes blink { 50% { opacity: .3; } }
@keyframes typing { 0%,10% { clip-path: inset(0 100% 0 0); } 65%,100% { clip-path: inset(0 0 0 0); } }
@keyframes wave { 0%,60%,100% { transform: translateY(0); } 30% { transform: translateY(-9px); } }
@keyframes fade { 50% { opacity: .25; } }
@media (max-width: 900px) { .text-grid { grid-template-columns: repeat(2,minmax(0,1fr)); } }
@media (max-width: 540px) { .text-grid { grid-template-columns: 1fr; } }
</style>
