<template>
    <div>
        <button @click="add">增加一个</button>
    </div>
</template>

<script>
    export default {
        name: 'two',
        data() {
            return {
                obj2: {
                    id: '22222222',
                    item: '3333333333'
                }
            }
        },
        methods: {
            add: function () {
                this.$emit('changeobj', this.obj2)
            }
        }
    }
</script>

<style scoped>

</style>
