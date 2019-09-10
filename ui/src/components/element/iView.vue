<template>
    <div id="iView">
        <h3 class="margin-bottom10">下拉菜单</h3>
        <div class="padding-10">
            <div class="dis-inline">
                <CWDropDown :dropBack="lists" @menuDrop="selectMenu" type="primary"></CWDropDown>
            </div>
            <div class="dis-inline">
                <CWDropDown :dropBack="lists" :search="true" class="margin-top10"></CWDropDown>
            </div>
        </div>
        <h3 class="margin-bottom10 margin-top10">按钮组</h3>
        <div class="padding-10">
            <ButtonGroup class="CW-group-buttons">
                <Button type="info">按钮1</Button>
                <Button type="info">按钮2</Button>
                <Button type="info">按钮3</Button>
            </ButtonGroup>
            <ButtonGroup class="margin-top10 CW-group-ghost">
                <Button type="info" ghost>按钮1</Button>
                <Button type="info" ghost>按钮2</Button>
                <Button type="info" ghost>按钮3</Button>
            </ButtonGroup>
        </div>
        <h3 class="margin-bottom10 margin-top10">选项卡</h3>
        <div class="padding-10">
            <Tabs value="name1" :animated="false">
                <TabPane label="标签一" name="name1">标签一的内容</TabPane>
                <TabPane label="标签二" name="name2">标签二的内容</TabPane>
                <TabPane label="标签三" name="name3">标签三的内容</TabPane>
            </Tabs>
        </div>
        <div class="padding-10">
            <Tabs type="card" :animated="false">
                <TabPane label="标签一" name="name1">标签一的内容</TabPane>
                <TabPane label="标签二" name="name2">标签二的内容</TabPane>
                <TabPane label="标签三" name="name3">标签三的内容</TabPane>
            </Tabs>
        </div>
    </div>
</template>

<script>


    export default {
        name: 'iView',
        data() {
            return {
                lists: [
                    {
                        name: '驴打1',
                        disable: false,
                    },
                    {
                        name: '炸酱2',
                        disable: false,
                    },
                    {
                        name: '冰糖3',
                        disable: true,
                    },
                    {
                        name: '北京烤4',
                        disable: false,
                    },
                ],
                modal1: false
            }
        },
        mounted() {
        },
        methods: {
            selectMenu(data) {
                console.log(data);
            }
        }
    }
</script>

<style scoped lang="scss">
    #iView {
        padding-top: 10px;

        .ghost-back {
            background: $split-color;
        }
    }
</style>
