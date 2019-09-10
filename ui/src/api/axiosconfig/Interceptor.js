// 拦截配置
import Vue from 'vue'

// 请求拦截，csrf_token校验
export function requestFunc(request) {
    if (request.config !== undefined && request.config.showLoad) Vue.prototype.$showLoading();
    request.headers['X-Requested-With'] = 'XMLHttpRequest';
    let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
    request.headers['X-CSRFToken'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1];
    return request
}

// axios 响应成功回调函数
export function responseSuccessFunc(response) {
    Vue.prototype.$CloseLoading();
    return response.data
}

// axios 响应失败回调函数
export function responseFailFunc(error) {
    Vue.prototype.$CloseLoading();
    if (error.response) {
        switch (error.response.status) {
            case 404:
                break
            case 500:
                Vue.prototype.$Message.error('服务器错误，请联系管理员')
        }
    } else if (error.request) {
        if (error.code === 'ECONNABORTED') {
            Vue.prototype.$Message.error('远程主机拒绝网络连接')
        }
    } else {

    }
    return Promise.reject(error)
}
