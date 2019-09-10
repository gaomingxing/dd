<template>
    <div>
        <!--<div>{{obj.id}}</div>-->
        <!--<div><Test @changeobj="change"></Test></div>-->
        <button @click="change">点击</button>
        <button @click="btn">点击2</button>
        <div>--------------------练习-------------------</div>
        <div>
        </div>
        <div>
            <Two @changeobj="change_two"></Two>
            <span>{{obj2.id}}----------{{obj2.item}}</span>
        </div>
        {{num}}
    </div>
</template>

<script>
    import Two from '@/views/test/two'

    export default {
        name: 'exercise',
        data() {
            return {
                num: 1,
                condition: {
                    id: 123,
                    name: 'xiaoming'
                },
                obj1: {
                    id: '1111',
                    item: '2222'
                },
                obj2: {
                    id: '1111',
                    item: '2222'
                }
            }
        },
        components: {
            Two
        },
        methods: {
            change: function () {
                console.log(1111111)
                this.$http.post('test', {condition: this.condition}).then(res => {
                    if (res.result) {
                        console.log('接口正常')
                    } else {
                        console.log('接口不正常')
                    }
                })
            },
            btn: function () {
                this.$router.push({name: 'home', params: {id: 'qaz'}})
                this.$http.post('exercise_test', {gao: 'mingxing'}).then(res => {
                    console.log(res);
                    if (res.result) {
                        console.log('接口正常');
                    } else {
                        console.log('接口不正常');
                    }
                })
            },
            change_two: function (i) {
                this.obj2 = i
            }
        }
    }
</script>

<style scoped>

</style>
