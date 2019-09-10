// axios基础配置
import axios from 'axios'
import {responseSuccessFunc, responseFailFunc, requestFunc} from './interceptor'

axios.defaults.timeout = 200000;
axios.defaults.crossDomain = true;
axios.defaults.withCredentials = true;
let VueEnv = process.env.NODE_ENV;
let ApiUrl = 'http://127.0.0.1:8000';
if (VueEnv === 'production') {
    ApiUrl = '.'
} else {
    ApiUrl = 'http://127.0.0.1:8000'
}
// 配置接口默认地址
axios.defaults.baseURL = ApiUrl;
// 添加请求拦截器
axios.interceptors.request.use(requestFunc);
// 添加响应拦截器
axios.interceptors.response.use(responseSuccessFunc, responseFailFunc);

// 发送请求 (接口路径，参数，请求配置)
export function post(url, params, config) {
    return new Promise((resolve, reject) => {
        axios.post(url, params, config).then(
            res => {
                resolve(res)
            },
            err => {
                reject(err)
            }
        )
            .catch(err => {
                reject(err)
            })
    })
}

export function get(url, params, config) {
    return new Promise((resolve, reject) => {
        axios.get(url, {
            params: params,
            config: config
        })
            .then(res => {
                resolve(res)
            })
            .catch(err => {
                reject(err)
            })
    })
}

// 前后端分离开发时重定向配置
// reUrl = '';  不需要重定向
//  reUrl = VueEnv === 'production' ? '' : '/api'; 重定向
export const reUrl = '';
