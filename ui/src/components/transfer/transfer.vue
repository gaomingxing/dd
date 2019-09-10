<template>
    <Transfer
        :data="data3"
        :target-keys="targetKeys3"
        :list-style="listStyle"
        :render-format="render3"
        :operations="['移除','添加']"
        filterable
        @on-change="handleChange3">
    </Transfer>
</template>

<script>
    export default {
        name: 'transfer',
        props: {
            data: {
                default: function () {
                    return []
                },
                type: Array
            },
            exist: {
                default: function () {
                    return []
                },
                type: Array
            },
            addVisible: {
                default: false
            },
            dialogShow: {
                default: false
            },
            transMessage: {
                type: Function,
                default: () => {
                }
            }
        },
        data() {
            return {
                data3: this.data,
                targetKeys3: this.exist,
                listStyle: {
                    width: '250px',
                    height: '300px'
                }
            }
        },
        created() {
        },
        methods: {
            initPage() {
                this.data3 = this.data;
                this.targetKeys3 = this.exist;
            },
            handleChange3(newTargetKeys) {
                this.targetKeys3 = newTargetKeys;
                // this.transMessage('11111');
            },
            render3(item) {
                return item.label;
            }
        },
        watch: {
            data: function () {
                this.initPage();
            },
            addVisible: function () {
                if (this.dialogShow) {
                    this.$emit('message', this.targetKeys3);
                } else {
                    this.targetKeys3 = this.exist;
                }
            }
        },
    }
</script>

<style scoped>

</style>
