<script setup>
</script>

<template>
  <div class="flex flex-col justify-center h-100 ">
    <div class="flex flex-col justify-center items-center w-150">
      <h1 class="text-3xl my-2">AI-powered Chest X-ray Classification</h1>
      <p class="my-2">Upload an X-ray image and get instant predictions.</p>
      <button
        class="block px-2 py-1 mx-auto w-20 bg-[#2563EB] hover:bg-[#366bde] text-white cursor-pointer border rounded-2"
      >
       <RouterLink :to="{name: 'Classify'}">Predict</RouterLink>
      </button>
    </div>
  </div>
</template>

<style scoped>
</style>
