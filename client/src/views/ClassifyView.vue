<script setup>
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-[#F8FAFC]">

    <!-- Card -->
    <div class="w-125 h-87.5 bg-white rounded-3xl shadow-xl flex flex-col items-center justify-center text-center p-8">

      <!-- Upload Button -->
      <button
        class="px-10 py-3 bg-linear-to-r from-blue-600 to-indigo-500
               hover:from-blue-700 hover:to-indigo-600
               text-white text-lg font-medium
               rounded-full shadow-md transition duration-200"
      >
        Upload Image
      </button>

      <!-- Text -->
      <p class="mt-6 text-gray-600 text-base">
        or drop a file,
      </p>

      <p class="text-sm text-gray-400 mt-1">
        paste image or
        <span class="underline cursor-pointer hover:text-gray-600">URL</span>
      </p>

    </div>

  </div>
</template>

<style scoped>
</style>
