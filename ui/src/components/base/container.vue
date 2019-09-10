<template>
    <div id="main-container">
        <LeftMenu v-if="showLeftMenu" @menuChange="menuChange"></LeftMenu>
        <div v-bind:class="{'full-width':!showLeftMenu}" style="width: calc(100% - 17%);">
            <div class="top-menu" v-if="showLeftMenu">
                <Icon type="md-home" size="18" style="vertical-align: text-bottom"/>
                <span>{{coMenu}}</span>
            </div>
            <router-view style="height: calc(100% - 24px);padding-left: 16px"/>
        </div>
    </div>
</template>

<script>
    import LeftMenu from '@/components/base/leftMenu'

    export default {
        name: 'main-container',
        components: {
            LeftMenu
        },
        data() {
            return {
                showLeftMenu: true,
                coMenu: {},
                appType: ''
            }
        },
        created() {
            this.showLeftMenu = window.location.href.indexOf('userIndex.html') === -1;
        },
        methods: {
            menuChange(data) {
                this.coMenu = data;
            }
        },
        watch: {}
    }
</script>

<style lang="scss" scoped>
    $headerHeight: 60px;
    #main-container {
        width: 100%;
        background: #fff;
        top: $headerHeight;
        position: absolute;
        display: flex;
        overflow: hidden;

        .full-width {
            width: 100% !important;
        }

        .top-menu {
            height: 24px;
            font-size: 14px;
            line-height: 24px;
            padding-left: 16px;
            vertical-align: bottom;
            border-bottom: 1px solid #e3e5e8;
        }
    }
</style>
