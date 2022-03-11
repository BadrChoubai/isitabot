<script setup lang="ts">
import { Ref, ref } from 'vue';
import Card from '../components/Card.vue';
const sampleTexts = [
	{
		title: "Anna Karenina",
		body: "Happy families are all alike; every unhappy family is unhappy in its own way Everything was in confusion in the Oblonskys’ house The wife had discovered that the husband was carrying on an intrigue with a French girl, who had been a governess in their family, and she had announced to her husband that she could not go on living in the same house with him."
	},
	{
		title: "GPT-2 Generated Creative Writing Piece",
		body: "The wisdom of our ancestors was the sword; meant for use in war. The sword was of great power, able to annihilate any enemy. It was divine knowledge. Imperial literature contains stories of emperor Anu using the sword."
	},
	{
		title: "Bot-Generated News Article",
		body: "Here to help you develop your Chatbot to become a winner in your industry. Let’s get started and build a bot that saves editors 50% on their shipping costs.  Our fast and gentle algorithms detect the common mistakes people make when typing about themselves and match the feedback from existing users to give users a much better experience."
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
	