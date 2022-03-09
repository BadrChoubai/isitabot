<script setup lang="ts">
import { Ref, ref } from 'vue';
import Card from '../components/Card.vue';
const sampleTexts = [
	{
		title: "Crime and Punishment",
		body: "lorem ipsum dolor site amet"
	},
	{
		title: "Political Twitter Bot",
		body: "lorem ipsum dolor site amet"
	},
	{
		title: "Bot-Generated News Article",
		body: "lorem ipsum dolor site amet"
	},
]

const textInput: Ref<string> = ref("");
const analysisResult: Ref<string> = ref("")
const loading: Ref<boolean> = ref(false);
const makeItLearn = (textInput: string) => {
	loading.value = true;
	setTimeout(() => {
		analysisResult.value = "This came from a bot";
		loading.value = false;
	}, 5000)
}

</script>
<template>
	<div>
		<section class="p-2 mb-4">
			<h1>Plain Text Analysis</h1>

			<form method="POST">
				<div class="mb-3 input-group">
					<span class="input-group-text">Paste Text</span>
					<textarea
						v-model="textInput"
						@input="(event) => textInput = (event.target as HTMLInputElement).value"
						name="encoded_text"
						class="form-control"
						aria-label="With textarea"
						placeholder="Enter your own text snippet or paste one from below you'd like to analyze."
					></textarea>
				</div>
				<button @click.prevent="makeItLearn(textInput)" type="submit" class="btn btn-primary">Submit</button>
			</form>
		</section>
		<section class="p-2 mb-4">
			<h2>Pre-selected Text Samples</h2>
			<div class="row gap-2">
				<Card v-for="text in sampleTexts" v-bind:key="text.title" :title="text.title" :body="text.body"></Card>
			</div>
		</section>
		<section class="p-2 mb-4 border">
			<h2>Analysis Results</h2>
			<div class="container">
				<p class="lead" v-if="analysisResult">{{ analysisResult }}</p>
				<p class="lead" v-else-if="loading">Analyzing Text... please hold.</p>
				<p class="lead" v-else>Analysis Result will show up here once it's been processed</p>
			</div>
		</section>
	</div>
</template>
	