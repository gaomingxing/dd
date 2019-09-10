// server模块（各模块）api
import {get, post, reUrl} from '../axiosconfig/axiosconfig'

// 返回在vue模板中的调用接口
export default {
    //----GET-------------------------------------------------------------
    //获取服务使用审批历史
    homeInfo: function (params) {
        return get(reUrl + '/login_info', params)
    },
    //----POST------------------------------------------------------------
    //服务审批
    serverApproval: function (params) {
        return post(reUrl + '/service_register_approval', params, {showLoad: true})
    }
}
