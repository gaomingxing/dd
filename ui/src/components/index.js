import container from './base/container'
import header from './base/header'
import headerMenu from './base/headerMenu'
import leftMenu from './base/leftMenu'
import iView from './element/iView'
import iViewTwo from './element/iViewTwo'
import Buttons from './element/Buttons'
import Modals from './element/Modals'
import CWTable from './table/cw-table'
import Transfer from './transfer/transfer.vue'
import CWDropDown from './dropDown/dropDown.vue'

const components = [
    container,
    header,
    headerMenu,
    leftMenu,
    iView,
    CWTable,
    Transfer,
    CWDropDown,
    iViewTwo,
    Buttons,
    Modals,
];

const install = function (Vue) {
    components.forEach(component => {
        Vue.component(component.name, component)
    })
};

export default install;
