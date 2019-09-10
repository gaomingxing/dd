<template>
    <div id="Modals">
        <h3 class="margin-bottom10">弹窗</h3>
        <div class="padding-10">
            <Button type="primary" @click="openModal('info')">info</Button>
            <Button @click="openModal('success')">Success</Button>
            <Button @click="openModal('warning')">Warning</Button>
            <Button @click="openModal('error')">Error</Button>
        </div>
        <div class="padding-10">
            <Button @click="openModal('success',2)">Success2</Button>
            <Button @click="openModal('error',2)">Error2</Button>
        </div>
        <div class="padding-10">
            <Button @click="openModal('success',3)">Success3</Button>
            <Button @click="openModal('error',3)">Error3</Button>
        </div>
        <h3 class="margin-bottom10">confirm</h3>
        <div class="padding-10">
            <Button @click="openConfirm('edit')">编辑</Button>
            <Button @click="openConfirm('del')">删除</Button>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Modals',
        methods: {
            openModal(type, style) {
                this.$CWMessage({
                    title: '欢迎',
                    content: '欢迎使用普通对话弹窗',
                    type: type,
                    okText: '确定',
                    style: style
                });
            },
            openConfirm(type) {
                this.$CWConfirm({
                    type: type,
                    title: '删除',
                    content: '是否删除这条数据',
                    okText: '确定',
                    cancelText: '取消',
                }).then(() => {
                    console.log('确定')
                }).catch(() => {
                    console.log('取消')
                });
            }
        }
    }
</script>

<style scoped>

</style>
