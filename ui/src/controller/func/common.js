import Vue from 'vue';
//loading显示
Vue.prototype.$showLoading = function () {
    this.$Spin.show({
        render: (h) => {
            return h('div', [
                h('Icon', {
                    'class': 'demo-spin-icon-load',
                    props: {
                        type: 'ios-loading',
                        size: 18
                    }
                }),
                h('div', 'Loading')
            ])
        }
    });
};
//loading关闭
Vue.prototype.$CloseLoading = function () {
    this.$Spin.hide();
};
//去重
Vue.prototype.$DupRem = function (list) {
    let newArr = [];
    for (var i = 0; i < list.length; i++) {
        if (newArr.indexOf(list[i]) < 0) {
            newArr.push(list[i])
        }
    }
    return newArr;
};
//深拷贝
Vue.prototype.$Copy = function (data) {
    return JSON.parse(JSON.stringify(data))
};
