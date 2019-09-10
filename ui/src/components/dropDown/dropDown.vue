<template>
    <div id="dropDown">
        <Dropdown transfer trigger="custom" :visible="showMenu" @on-click="showMe">
            <Button :type="type" @click="showMenu=!showMenu">
                下拉菜单
                <Icon type="ios-arrow-down"></Icon>
            </Button>
            <DropdownMenu slot="list" :class="{'primary-drop-down':type==='primary'}" disabled>
                <DropdownItem disabled class="drop-down-input" v-if="search" name="cw-search">
                    <Input v-model="dropSearch" search @on-search='searchItem()'
                           style="width: 80px"></Input>
                </DropdownItem>
                <DropdownItem class="margin-top5"
                              v-for="item in dropList"
                              :key="item.name"
                              :name="item.disable?'cw-search':item.name"
                              :disabled="item.disable">
                    {{item.name}}
                </DropdownItem>
            </DropdownMenu>
        </Dropdown>
    </div>
</template>

<script>
    export default {
        /**
         * 参考: https://www.iviewui.com/components/dropdown
         * @param {boolean} search 是否显示搜索框
         * @param {string} type 按钮样式
         * @param {list} dropBack 下拉展示数据
         */
        name: 'CWDropDown',
        props: {
            type: {
                default: function () {
                    return 'default'
                }
            },
            search: {
                default: function () {
                    return false
                }
            },
            dropBack: {
                default: function () {
                    return [
                        {
                            name: '驴打滚',
                            disable: false,
                        },
                        {
                            name: '炸酱面',
                            disable: false,
                        },
                        {
                            name: '冰糖葫芦',
                            disable: true,
                        },
                        {
                            name: '北京烤鸭',
                            disable: false,
                        },
                    ]
                }
            },
        },
        data() {
            return {
                dropSearch: '',
                dropList: [],
                showMenu: false
            }
        },
        mounted() {
            this.dropList = this.$Copy(this.dropBack);
        },
        watch: {
            dropBack: function () {
                this.dropList = this.$Copy(this.dropBack);
            }
        },
        methods: {
            showMe(data) {
                if (data !== 'cw-search') {
                    this.showMenu = false;
                    this.$emit('menuDrop', data);
                }
            },
            searchItem() {
                let seList = [];
                if (this.dropSearch === '') {
                    this.dropList = this.$Copy(this.dropBack);
                } else {
                    for (let i = 0; i < this.dropBack.length; i++) {
                        if (this.dropBack[i].name.indexOf(this.dropSearch) !== -1) {
                            seList.push(this.dropBack[i]);
                        }
                    }
                    if (seList.length === 0) seList.push({name: '无数据', disable: true});
                    this.dropList = seList;
                }
            }
        }
    }
</script>

<style scoped>
    #dropDown {
    }
</style>
