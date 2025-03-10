import { createApp } from 'vue'
import App from './App.vue'
import 'ant-design-vue/dist/reset.css';
import { Carousel } from "ant-design-vue";
import gsap from 'gsap';
import { ScrollTrigger } from "gsap/ScrollTrigger";

const app = createApp(App);
app.use(Carousel);

app.mount('#app')
gsap.registerPlugin(ScrollTrigger);
