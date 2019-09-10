// 给action注册事件处理函数。当这个函数被触发时候，将状态提交到mutations中处理
export function initialData({commit}, name) { // commit 提交；name即为点击后传递过来的参数，
    return commit('updateData', name) //第一个参数为 提交的mutations中的方法名
}
