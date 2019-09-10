<template>
    <div>
        <div>
            <button @click="add">增加</button>
            <!--{{num}}-->
        </div>
        <!--<div>{{name}}</div>-->
    </div>
</template>

<script>
    export default {
        name: 'test',
        data() {
            return {
                name: 'qqqqq',
                obj: {
                    id: 666,
                    item: 'qaz'
                }
            }
        },
        methods: {
            add: function () {
                this.$emit('changeobj', this.obj)
            }
        }
    }
</script>

<style scoped>
</style>
