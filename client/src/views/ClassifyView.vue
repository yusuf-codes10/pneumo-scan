<script setup>
// import { ref } from "vue";

// const message = ref('')


const sendImage = async () => {
  const API = 'http://127.0.0.1:5000/predict'

  try {
    const response = await fetch(API)
    const data = await response.json()
    console.log(data);
  } catch (err) {
    console.log(err.message);
  }
}

const handleFile = async (event) => {
  const file = event.target.files[0];
  if (!file) return;
  await sendXray(file);
}

const  sendXray = async (file) => {
  const formData = new FormData();
  formData.append('file', file); // 'file' must match request.files['file'] in Flask

  const response = await fetch('http://localhost:5000/predict', {
    method: 'POST',
    body: formData,
    // ⚠️ Do NOT set Content-Type manually — browser sets it with the boundary automatically
  });

  const result = await response.json();
  console.log(result.prediction, result.confidence);
}
</script>

<template>
  <div class="min-h-screen flex bg-[#F8FAFC]">
    <div class="bg-red-500">
        <input type="file" accept="image/*" @change="handleFile" />
    </div>

    <!-- Card -->
    <div class="w-125 h-87.5 bg-white rounded-3xl shadow-xl flex flex-col items-center justify-center text-center p-8">

      <!-- Upload Button -->
      <button
        @click="sendImage"
        class="px-10 py-3 bg-linear-to-r from-blue-600 to-indigo-500
               hover:from-blue-700 hover:to-indigo-600
               text-white text-lg font-medium cursor-pointer
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
