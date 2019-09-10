<template>
    <div id="left-menu">
        <Menu :active-name="defaultActive" accordion :open-names="seFather" @on-select="selectChild"
              @on-open-change="selectItem" ref="leftMenu">
            <div v-for="item in routeList" :key="item.name">
                <MenuItem class="font-16"
                          :name="item.name"
                          :to="item.to" v-if="!item.hasChild" :class="{'homeSe':item.name===defaultActive}">
                    <Icon :type="item.icon"/>
                    {{item.cnName}}
                </MenuItem>
                <Submenu :name="item.name"
                         v-if="item.hasChild" :class="{'seOpen':item.name===seFather[0]}">
                    <template slot="title">
                        <Icon :type="item.icon"/>
                        {{item.cnName}}
                    </template>
                    <div v-for="child in item.children" :key="child.name">
                        <MenuItem v-if="!child.hasChild"
                                  :name="child.name"
                                  :to="child.to">
                            {{child.cnName}}
                        </MenuItem>
                        <Submenu v-if="child.hasChild"
                                 :name="child.name"
                                 class="second-menu"
                                 :class="{'second-selected':child.name===seFather[1]}">
                            <template slot="title">
                                {{child.cnName}}
                            </template>
                            <MenuItem v-for="third in child.children"
                                      :key="third.name"
                                      :name="third.name"
                                      :to="third.to">
                                {{third.cnName}}
                            </MenuItem>
                        </Submenu>
                    </div>
                </Submenu>
            </div>
        </Menu>
    </div>
</template>

<script>
    export default {
        name: 'leftMenu',
        data() {
            return {
                defaultActive: '',
                openName: [],
                seFather: [],
                routeList: [
                    {
                        name: 'home',
                        cnName: '首页',
                        to: 'home',
                        icon: 'ios-desktop',
                        hasChild: false,
                        children: []
                    }, {
                        name: '注册审批',
                        cnName: '注册审批',
                        to: '',
                        icon: 'ios-filing',
                        hasChild: true,
                        children: [
                            {
                                name: 'appAgency',
                                cnName: '我的待办',
                                to: 'appAgency',
                                hasChild: false
                            }, {
                                name: '审批历史',
                                cnName: '审批历史',
                                hasChild: true,
                                children: [
                                    {
                                        name: 'app',
                                        cnName: '我的待办',
                                        to: 'app',
                                    }, {
                                        name: 'history',
                                        cnName: '审批历史',
                                        to: 'history',
                                    }
                                ]
                            }
                        ]
                    }, {
                        name: '服务管理',
                        cnName: '服务管理',
                        to: '',
                        icon: 'ios-text',
                        hasChild: true,
                        children: [
                            {
                                name: 'serverList',
                                cnName: '服务列表',
                                to: 'serverList',
                                hasChild: false,
                            },
                            {
                                name: 'serverAccess',
                                cnName: '服务接入',
                                hasChild: false,
                                to: 'serverAccess'
                            },
                            {
                                name: 'applyList',
                                cnName: '服务注册',
                                hasChild: false,
                                to: 'applyList'
                            },
                        ]
                    }, {
                        name: '系统管理',
                        cnName: '系统管理',
                        icon: 'ios-cog',
                        hasChild: true,
                        children: [
                            {
                                name: 'roleManage',
                                cnName: '角色管理',
                                hasChild: false,
                                to: 'roleManage'
                            }, {
                                name: 'globalParam',
                                cnName: '全局参数',
                                hasChild: false,
                                to: 'globalParam'
                            }, {
                                name: 'operation',
                                cnName: '操作日志',
                                hasChild: false,
                                to: 'operation'
                            }
                        ]
                    }
                ],
                isCollapse: true
            }
        },
        created() {
            this.defaultActive = this.$route.name;
            this.getParent();
            let data = this.$route.meta.title;
            this.$emit('menuChange', data)
        },
        watch: {
            $route: function () {
                let data = this.$route.meta.title;
                this.$emit('menuChange', data)
            }
        },
        methods: {
            getParent() {
                let data = this.routeList;
                for (let i = 0; i < data.length; i++) {
                    if (data[i].hasChild) {
                        for (let j = 0; j < data[i].children.length; j++) {
                            if (data[i].children[j].hasChild) {
                                for (let m = 0; m < data[i].children[j].children.length; m++) {
                                    if (data[i].children[j].children[m].name === this.defaultActive) {
                                        this.seFather.push(data[i].name);
                                        this.seFather.push(data[i].children[j].name);
                                        return;
                                    }
                                }
                            } else if (data[i].children[j].name === this.defaultActive) {
                                this.seFather.push(data[i].name);
                                return;
                            }
                        }
                    }
                }
            },
            open() {
            },
            close() {
            },
            selectChild(name) {
                let data = this.routeList;
                this.defaultActive = name;
                this.seFather = this.openName;
                for (let i = 0; i < data.length; i++) {
                    if (data[i].name === name && !data[i].hasChild) {
                        this.seFather = [];
                        this.$nextTick(() => {
                            this.$refs.leftMenu.updateOpened();
                        });
                    }
                }
            },
            selectItem(name) {
                this.openName = name;
            }
        }
    }
</script>
<style lang="scss" scoped>
    $headerHeight: 60px;
    #left-menu {
        width: 17%;
        height: 100%;
        background-color: #fff;
        border-right: 1px solid #e3e5e8;

        .ivu-menu {
            width: 100% !important;

        }

        .el-menu {
            border: none;
        }

        .ivu-icon {
            font-size: 20px;
            padding-right: 10px;
        }
        .ivu-menu-vertical.ivu-menu-light:after {
            content: '';
            width: 0 !important;
            display: none !important;
        }
    }

</style>
