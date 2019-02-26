import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'vue-awesome/icons'

import Icon from 'vue-awesome/components/Icon'
import router from './router/router'

Vue.use(BootstrapVue);
Vue.config.productionTip = false;
Vue.component('v-icon', Icon);

new Vue({
    router,
    render: h => h(App)
}).$mount('#app');
