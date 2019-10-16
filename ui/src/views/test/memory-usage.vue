<template>
    <div id="memory-usage-id">
        <div id="memory-usage-select">
            <span>选择业务：</span>
            <el-select v-model="bk_biz_id" placeholder="请选择">
                <el-option
                    v-for="item in business_options"
                    :key="item.bk_biz_id"
                    :label="item.bk_biz_name"
                    :value="item.bk_biz_id">
                </el-option>
            </el-select>
            <span>选择集群：</span>
            <el-select v-model="bk_set_id" placeholder="请选择">
                <el-option
                    v-for="item in cluster_options"
                    :key="item.bk_set_id"
                    :label="item.bk_set_name"
                    :value="item.bk_set_id">
                </el-option>
            </el-select>
        </div>
        <div id="memory-usage-info">
            <el-table
                :data="tableData"
                style="width: 100%">
                <el-table-column
                    prop="bk_host_innerip"
                    label="内网ip"
                    width="180">
                </el-table-column>
                <el-table-column
                    prop="bk_os_name"
                    label="系统名"
                    width="180">
                </el-table-column>
                <el-table-column
                    prop="bk_cpu"
                    label="CPU(核数)">
                </el-table-column>
                <el-table-column
                    prop="bk_host_name"
                    label="主机名">
                </el-table-column>
                <el-table-column
                    prop="bk_inst_name"
                    label="云区域">
                </el-table-column>
                <el-table-column
                    label="操作">
                    <template slot-scope="scope" style="">
                        <!--<el-button @click='search_detail(scope.row)' type="warning" size="medium">查询详情</el-button>-->
                        <el-button @click='search_memory(scope.row)' type="warning" size="medium">查询详情</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </div>

        <div class='detail_dialog'>
            <el-dialog title="主机详情" :visible.sync="dialogTableVisible" :before-close="handleClose">
                <!--<el-table
                    :data="innerListData"
                    style="width: 100%">
                    <el-table-column
                        prop="total"
                        label="总和"
                    >
                    </el-table-column>
                    <el-table-column
                        prop="used"
                        label="已用"
                    >
                    </el-table-column>
                    <el-table-column
                        prop="free"
                        label="可用"
                    >
                    </el-table-column>
                    <el-table-column
                        prop="shared"
                        label="共享"
                    >
                    </el-table-column>
                    <el-table-column
                        prop="cache"
                        label="缓存"
                    >
                    </el-table-column>
                    <el-table-column
                        prop="available"
                        label="空余"
                    >
                    </el-table-column>
                </el-table>-->
                <div id="memory_main" v-loading="loading" element-loading-text="拼命加载中" style="width: 600px;height:400px;"
                     :visible.sync="dialogTableVisible"></div>
            </el-dialog>
        </div>

    </div>
</template>

<script>
    export default {
        // name: "memory-usage",
        data() {
            return {
                business_options: [],
                bk_biz_name: '',
                bk_biz_id: '',
                bk_set_id: '',
                bk_set_name: '',
                cluster_options: [],
                tableData: [],
                innerListData: [],
                dialogTableVisible: false,
                loading: true,
                memory_used: 0,
                memory_free: 0,
            }
        },
        methods: {
            select_business: function () {
                this.$http.get('select_business').then(data => {
                    if (data.result) {
                        this.business_options = data.data
                    } else {
                        this.$message.error(data.message);
                    }
                })
            },
            search_detail: function (row) {
                this.dialogTableVisible = true;
                this.$http.post('search_info', {
                    'bk_host_innerip': row.bk_host_innerip,
                    'bk_biz_id': this.bk_biz_id
                }).then(res => {
                    this.loading = false;
                    if (res.result) {
                        this.innerListData = res.data;
                    } else {
                    }
                })
            },
            search_memory: function (row) {
                this.dialogTableVisible = true;
                this.loading = true
                this.$http.post('search_info', {
                    'bk_host_innerip': row.bk_host_innerip,
                    'bk_biz_id': this.bk_biz_id
                }).then(res => {
                    this.loading = false;
                    if (res.result) {
                        this.memory_used = res.data[0]['used'];
                        this.memory_free = res.data[0]['free'];
                        let myChart = this.$echarts.init(document.getElementById('memory_main'));
                        var memory_option = {
                            title: {
                                text: '主机内存',
                                x: 'center'
                            },
                            tooltip: {
                                trigger: 'item',
                            },
                            legend: {
                                orient: 'vertical',
                                left: 'left',
                                data: ['已用内存容量（M）', '剩余内存容量（M）']
                            },
                            series: [
                                {
                                    name: '主机内存',
                                    type: 'pie',
                                    radius: '55%',
                                    center: ['50%', '60%'],
                                    data: [
                                        {value: this.memory_used, name: '已用内存容量（M）'},
                                        {value: this.memory_free, name: '剩余内存容量（M）'},
                                    ],
                                    itemStyle: {
                                        emphasis: {
                                            shadowBlur: 10,
                                            shadowOffsetX: 0,
                                            shadowColor: 'rgba(10, 10, 0, 0.5)'
                                        }
                                    }
                                }
                            ]
                        };
                        // 使用刚指定的配置项和数据显示图表。
                        myChart.setOption(memory_option);
                    } else {
                    }
                });
            },
            handleClose() {
                this.memory_used = 0;
                this.memory_free = 0;
                this.dialogTableVisible = false
            }
        },
        mounted() {
            this.select_business();
        },
        watch: {
            bk_biz_id: function () {
                this.$http.post('search_set', {'bk_biz_id': this.bk_biz_id}).then(data => {
                    if (data.result) {
                        this.cluster_options = data.data
                    } else {
                        this.$message.error(data.message);
                    }
                })
            },
            bk_set_id: function () {
                this.$http.post('search_hosts', {'bk_set_id': this.bk_set_id}).then(data => {
                    if (data.result) {
                        this.tableData = data.data;
                    } else {
                        this.$message.error(data.message);
                    }
                })
            }
        }
    }


</script>

<style scoped>

</style>
