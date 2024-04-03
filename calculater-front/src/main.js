import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
//引入axios，进行网络调用
import axios from 'axios'
Vue.prototype.$http = axios
// axios.defaults.baseURL = 'https://api.thecatapi.com/v1/images';
axios.defaults.baseURL = 'http://127.0.0.1:8000';
//axios.defaults.baseURL = 'http://116.62.135.116:8000'

//引入echart
import echarts from 'echarts'
Vue.prototype.$echarts = echarts;
// Vue.use(echarts);

//引入字体
import './assets/fonts/TheFont.css'


Vue.config.productionTip = false
Vue.use(ElementUI);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
