// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import iViewUI from 'iview';
import store from './vuex'
import 'iview/dist/styles/iview.css';
// 几何图
import Echarts from 'echarts'
import G2 from '@antv/g2';
// 引用API文件
import api from './api/index'
//时间格式化插件
import moment from 'moment'
//filter统一引入
import './fiter/index.js';
//公共方法
import './controller/func/common.js';
// 统一样式引入
import './assets/index'
// 引入自定义方法
import Dire from './directive/index.js'
// 引入自定义组件
import Component from './components/index.js'
import axios from 'axios'

Vue.use(ElementUI);
Vue.use(iViewUI);
Vue.use(Echarts);
Vue.use(G2);
Vue.use(Dire);
Vue.use(Component);
Vue.prototype.$echarts = Echarts;
Vue.prototype.$G2 = G2;
Vue.prototype.$moment = moment;
// 将API方法绑定到全局
Vue.prototype.$api = api;
const headTheme = 'light'; //选择 light 或 blue
Vue.prototype.headTheme = headTheme;
axios.defaults.baseURL = window.siteUrl;
axios.defaults.withCredentials = true;
Vue.prototype.$http = axios


axios.interceptors.request.use(config => {
    config.headers['X-Requested-With'] = 'XMLHttpRequest';
    let regex = /.*cwcsrftoken=([^;.]*).*$/;
    // console.log(document.cookie)
    config.headers['X-CSRFToken'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1];
    // config.headers['X-CSRFToken'] = 'WdPzWMHJBxgp5Uj7Tw38dFDHgBVEnmfF';
    return config
});

// axios.interceptors.response.use(response => {
//     // 登录重定向begin
//     // let resUrl = response.request.responseURL;
//     // if (resUrl.indexOf('/login/') !== -1) {
//     //     let login_url = resUrl.split('?')[0] + '?c_url=' + window.location.href;
//     //     window.location.href = login_url
//     // }
//     // 登录重定向end
//     console.log(response)
//     if (response.status !== 200) {
//         return {
//             code: response.status,
//             message: '请求异常，请刷新重试',
//             result: false
//         }
//     }
//     return response.data
// }, error => {
//     return {
//         code: 500,
//         message: '未知错误，请刷新重试',
//         error: error,
//         result: false
//     }
// });

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    store,
    data() {
        return {
            website: '我是全局变量',
        }
    },
    components: {App},
    template: '<App/>',
});
