<script setup lang="ts">
const props = defineProps<{
  title: string,
  body: string,
}>()

const addSnippetToClipboard = async (textSnippet: string) => {
	const clipboard = await navigator.clipboard;
	clipboard.writeText(textSnippet);
	alert("Snippet copied to clipboard");
}
</script>
<template>
	<div class="card col-sm-3">
		<div class="card-body">
			<h3 class="card-title">{{ title }}</h3>
			<p
				class="card-text"
			>{{ body }}</p>
		</div>
		<button class="mb-2 btn  btn-secondary" @click.prevent="addSnippetToClipboard(body)">Paste to Clipboard</button>
	</div>
</template>