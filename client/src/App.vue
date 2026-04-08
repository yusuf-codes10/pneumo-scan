<script setup>
import NavBar from './components/NavBar.vue';

</script>

<template>
  <div class="hero">
    <NavBar />
    <RouterView />
  </div>
</template>

<style scoped>

.hero {
    height: 100vh;
    background-image: url(/images/main-bg2.png);
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
</style>
