<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
import AppHeader from './components/Display/AppHeader.vue';
</script>

<template>
  <AppHeader></AppHeader>

  <router-view class="container pl-1 pr-1 my-2"></router-view>
</template>

<style>
#app {
  font-family: "Inter", "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
