<script setup lang="ts">
import type { Component } from 'vue'
import type { AnimationId } from '~/data/animations'
import BouncingDots from './animations/BouncingDots.vue'
import CircularSpinner from './animations/CircularSpinner.vue'
import IndeterminateBar from './animations/IndeterminateBar.vue'
import OrbitSpinner from './animations/OrbitSpinner.vue'
import PulseLoader from './animations/PulseLoader.vue'
import ShimmerSkeleton from './animations/ShimmerSkeleton.vue'
import TextLoading from './animations/TextLoading.vue'
import ThreeDots from './animations/ThreeDots.vue'
import WaveBars from './animations/WaveBars.vue'

const previews: Record<AnimationId, Component> = {
  'circular': CircularSpinner,
  'bouncing-dots': BouncingDots,
  'text-loading': TextLoading,
  'indeterminate-bar': IndeterminateBar,
  'shimmer': ShimmerSkeleton,
  'pulse': PulseLoader,
  'orbit': OrbitSpinner,
  'wave-bars': WaveBars,
  'three-dots': ThreeDots,
}

defineProps<{
  id: AnimationId
}>()
</script>

<template>
  <component :is="previews[id]" />
</template>
