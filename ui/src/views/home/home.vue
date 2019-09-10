<template>
    <div id="home">
        <div class="title">蓝鲸VUE开发框架</div>
    </div>
</template>
<script>
    export default {
        name: 'home',
        data() {
            return {
                name: 'qwre'
            }
        },
        mounted() {
            console.log(window.location.href)
            // alert('aaa')
            var id2 = this.$route.params.id
            console.log(id2);
        }
    }
</script>
<style lang='scss'>
    .title {
        height: 100%;
        width: 100%;
        margin: auto;
        color: #1facdd;
        text-align: center;
        font-size: 30px;
    }
</style>
