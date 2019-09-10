<template>
    <div id="header-menu">
        <el-menu
            :default-active="activeIndex"
            class="el-menu-demo"
            mode="horizontal"
            menu-trigger="hover"
            @open="handleopen"
            @close="handleclose"
            show-timeout="10"
            hide-timeout="400"
            router>
            <el-menu-item
                v-for="item in routeList"
                :key="item.to"
                :index="item.name"
                :to="item.to" v-if="!item.hasChild">{{item.cnName}}
            </el-menu-item>
            <el-submenu v-if="item.hasChild"
                        v-for="item in routeList"
                        :key="item.to"
                        :index="item.name">
                <template slot="title">{{item.cnName}}</template>
                <div v-for="child in item.children"
                     :key="child.to">
                    <el-menu-item
                        v-if="!child.hasChild"
                        :index="child.name" :to="child.to">{{child.name}}
                    </el-menu-item>
                    <el-submenu v-if="child.hasChild"
                                :index="child.name" :to="child.to">
                        <template slot="title">{{child.cnName}}</template>
                        <el-menu-item
                            v-for="third in child.children"
                            :key="third.to"
                            :index="third.name"
                            :to="third.to">{{third.name}}
                        </el-menu-item>
                    </el-submenu>
                </div>
            </el-submenu>
        </el-menu>
    </div>
</template>
<script>
    export default {
        name: 'headerMenu',
        props: {
            menuOption: {}
        },
        data() {
            return {
                theme1: 'light',
                activeIndex: '/home',
                routeList: [
                    {
                        name: 'home',
                        cnName: '首页',
                        to: 'home',
                        icon: 'ios-desktop',
                        hasChild: false,
                        children: []
                    },
                    {
                        name: 'exercise',
                        cnName: '练习',
                        to: 'exercise',
                        icon: 'ios-desktop',
                        hasChild: false,
                        children: []
                    },
                    {
                        name: 'gmx',
                        cnName: '高明星',
                        to: 'gmx',
                        icon: 'ios-desktop',
                        hasChild: false,
                        children: []
                    }, {
                        name: 'test',
                        cnName: '测试',
                        to: '',
                        icon: 'ios-filing',
                        hasChild: true,
                        children: [
                            {
                                name: 'test',
                                cnName: 'test',
                                // to: 'test',
                                hasChild: false
                            },
                            // {
                            //     name: 'test2',
                            //     cnName: 'test2',
                            //     to: 'test2',
                            //     hasChild: true,
                            //     children: [
                            //         {
                            //             name: 'test3',
                            //             cnName: 'test3',
                            //             to: 'test3',
                            //             hasChild: false
                            //         }
                            //     ]
                            // }
                        ]
                    },
                ],
            };
        },
        mounted() {
            this.activeIndex = this.$route.name;
            if (this.$route.path === '/') {
                this.activeIndex = '/home'
            }
        },
        methods: {
            handleopen(key, keyPath) {
            },
            handleclose(key, keyPath) {
            },
        }
    }
</script>
<style lang="scss">
</style>

