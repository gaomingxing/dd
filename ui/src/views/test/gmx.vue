<!--<template>-->
<!--<div>-&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;》高明星《&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;</div>-->
<!--</template>-->

<!--<script>-->
<!--export default {-->
<!--name: 'gmx'-->
<!--}-->
<!--</script>-->

<!--<style scoped>-->

<!--</style>-->

<template>
    <div id="actual" style="">
        <div class="select" style="margin-top: 15px;border-bottom: 1px solid lightgrey;padding-bottom: 15px">
            <span style="font-size: 15px">姓名：</span>
            <el-input v-model="obj.name" style="width: 150px;" placeholder="请输入姓名"></el-input>
            <span style="font-size: 15px;margin-left: 20px">性别：</span>
            <el-input v-model="obj.gender" style="width: 150px;" placeholder="请输入性别"></el-input>
            <el-button @click="search_user" type="primary" style="margin-left: 5px">查询</el-button>
            <el-button @click="add_user" style="margin-left: 45%" type="primary">添加</el-button>
        </div>
        <div class="table" style="height: 80%;overflow: auto">
            <el-table
                :data="listData"
                style="width: 100%">
                <el-table-column
                    prop="name"
                    label="姓名"
                >
                </el-table-column>
                <el-table-column
                    prop="age"
                    label="年龄"
                >
                </el-table-column>
                <el-table-column
                    prop="gender"
                    label="性别"
                >
                </el-table-column>
                <el-table-column
                    prop="addr"
                    label="籍贯"
                >
                </el-table-column>
                <el-table-column
                    prop="height"
                    label="身高"
                >
                </el-table-column>
                <el-table-column
                    label="操作"
                >
                    <template slot-scope="scope" style="">
                        <el-button @click='edit(scope.row)' type="warning" size="medium">编辑</el-button>
                        <el-button @click="del(scope.row)" type="danger" size="medium">删除</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </div>
        <div class="bottom" style="text-align: center;margin-top: 8px">
            <el-pagination
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                :current-page="currentPage"
                :page-sizes="[5, 10, 15, 20]"
                :page-size="pageSize"
                layout="total, sizes, prev, pager, next, jumper"
                :total="totalNum">
            </el-pagination>
        </div>
        <div class="tanchuang">
            <el-dialog
                :title="title"
                :visible.sync="dialogVisible"
                width="32%"
            >
                <div>
                    <div style="margin-left: 50px">
                        <span>姓名：</span>
                        <el-input v-model="condition.name" style="width: 200px;" placeholder="请输入姓名"></el-input>
                    </div>
                    <div style="margin-left: 50px;margin-top: 15px">
                        <span>年龄：</span>
                        <el-input v-model="condition.age" style="width: 200px;" placeholder="请输入年龄"></el-input>
                    </div>
                    <div style="margin-left: 50px;margin-top: 15px">
                        <span>性别：</span>
                        <el-input v-model="condition.gender" style="width: 200px;" placeholder="请输入性别"></el-input>
                    </div>
                    <div style="margin-left: 50px;margin-top: 15px">
                        <span>籍贯：</span>
                        <el-input v-model="condition.addr" style="width: 200px;" placeholder="请输入籍贯"></el-input>
                    </div>
                    <div style="margin-left: 50px;margin-top: 15px">
                        <span>身高：</span>
                        <el-input v-model="condition.height" style="width: 200px;" placeholder="请输入身高"></el-input>
                    </div>
                </div>
                <span slot="footer" class="dialog-footer">
                    <el-button @click="cancel">取 消</el-button>
                    <el-button type="primary" @click="confirm">确 定</el-button>
                </span>
            </el-dialog>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'actual',
        data() {
            return {
                tableData: [],
                currentPage: 1,
                pageSize: 5,
                totalNum: 0,
                listData: [],
                loading: true,
                title: '',
                dialogVisible: false,
                obj: {
                    name: '',
                    gender: ''
                },
                condition: {
                    name: '',
                    age: '',
                    gender: '',
                    height: '',
                    addr: '',
                    id: ''
                },
            }
        },
        methods: {
            error: function () {
                var error = []
                if (this.condition.name === '') {
                    error.push('姓名不能为空！')
                }
                return error
            },
            init: function () {
                this.$http.post('search_user', {condition: this.obj}).then(res => {
                    this.loading = false;
                    if (res.result) {
                        this.tableData = res.data;
                        this.totalNum = this.tableData.length
                        console.log(this.totalNum)
                        console.log(this.tableData)
                        this.handleCurrentChange(this.currentPage)
                    } else {
                        this.$message.error(res.message);
                    }
                })
            },
            //修改每页显示条数
            handleSizeChange(val) {
                console.log(`每页 ${val} 条`);
                this.pageSize = val
                this.listData = this.tableData.slice(0, val)
                console.log(this.listData)
            },
            //修改页数
            handleCurrentChange(val) {
                console.log(`当前页: ${val}`);
                this.currentPage = val
                // 当前页数显示 = 总数的第n页*页数显示个数，slice(start,end)从第几个到第几个的子集
                this.listData = this.tableData.slice(
                    (val - 1) * this.pageSize,
                    val * this.pageSize
                )
                console.log(this.listData)
            },
            search_user: function () {
                this.init()
            },
            edit: function (row) {
                this.title = '编辑用户'
                this.dialogVisible = true
                this.$http.get('get_user?id=' + row.id).then(res => {
                    if (res.result) {
                        this.condition.id = row.id
                        this.condition = res.data
                    } else {
                        this.$message.error('获取用户信息失败！');
                    }
                })
            },
            del: function (row) {
                console.log(row)
                //弹窗组件
                this.$confirm('此操作将永久删除该任务, 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    this.$http.get('delete_user?id=' + row.id).then(res => {
                        if (res.result) {
                            this.$message({
                                type: 'success',
                                message: '删除成功!'
                            });
                            this.init()
                        } else {
                            this.$message({
                                showClose: true,
                                type: 'error',
                                message: '删除失败,请联系开发人员！'
                            });
                        }
                    })
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消删除'
                    });
                });
            },
            confirm: function () {
                var error = this.error()
                console.log(error)
                if (error.length > 0) {
                    this.$message.error(error[0]);
                    return
                }
                this.$http.post('update_user', {condition: this.condition}).then(res => {
                    if (res.result) {
                        if (this.condition.id) {
                            this.dialogVisible = false
                            this.$message.success('更新用户成功！');
                        } else {
                            this.$message.success('添加用户成功！');
                        }
                        this.init()
                    } else {
                        this.$message.error(res.msg);
                    }
                })
            },
            cancel: function () {
                this.dialogVisible = false
            },
            add_user: function () {
                this.condition = {
                    name: '',
                    age: '',
                    gender: '',
                    height: '',
                    addr: '',
                    id: ''
                }
                this.title = '添加用户'
                this.dialogVisible = true
            }
        },
        mounted() {
            this.init()
        }
    }
</script>
<style type="text/css" lang="scss">
    #actual {
        .el-input__inner {
            height: 30px;
            line-height: 30px;
        }

        .el-table .cell {
            text-align: center;
        }

        .el-table th > .cell {
            text-align: center;
        }

        .el-button {
            padding: 5px 5px;
            /* margin-left: 5px; */
        }
    }


</style>


