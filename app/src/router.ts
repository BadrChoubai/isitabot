import { createRouter, createWebHistory } from 'vue-router';
// 1. Define route components.
// These can be imported from other files
import Home from "./views/Home.vue";
import About from "./views/About.vue";
import TextAnalysis from "./views/TextAnalysis.vue";

// 2. Define some routes
// Each route should map to a component.
// We'll talk about nested routes later.
const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About },
  { path: '/text-analysis', component: TextAnalysis },
]

// 3. Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
export default createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: createWebHistory(),
  routes, // short for `routes: routes`
})
