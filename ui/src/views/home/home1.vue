<template>
    <div id='home'>
        <div v-if="showPage">
            <Row>
                <Col span="8">
                    <!--按钮组组件-->
                    <Buttons></Buttons>
                </Col>
                <Col span="8">
                    <!--下拉，组合按钮和选项卡组件-->
                    <i-view style="height: 90%;"></i-view>
                </Col>
                <Col span="8">
                    <!--弹窗组组件-->
                    <Modals></Modals>
                </Col>
            </Row>
        </div>
        <div v-if="!showPage">
            <!--表单和进度条组件-->
            <iViewTwo></iViewTwo>
        </div>
        <div class="next-button">
            <Button type="primary" @click="showPage=!showPage">
                <span v-if="showPage">下一页</span>
                <span v-if="!showPage">上一页</span>
            </Button>
        </div>
        <!--柱形图-->
        <!--<div>-->
        <!--<Row class="home-bottom">-->
        <!--<Col span="12" class="top-item">-->
        <!--<div id="panChartLeft" :style="{width: '100%', height: '100%'}"></div>-->
        <!--</Col>-->
        <!--<Col span="12" class="top-item">-->
        <!--<div id="panChartRight" :style="{width: '100%', height: '100%'}"></div>-->
        <!--</Col>-->
        <!--</Row>-->
        <!--</div>-->
    </div>
</template>

<script>
    export default {
        name: 'home1',
        data() {
            return {
                showPage: true,
            }
        },
        mounted() {
            // this.getData();
            // this.$showLoading();
        },
        methods: {
            getData() {
                this.$api.Server.homeInfo().then(res => {
                });
            },
            drawLeft(data) {
                //柱形图
                let panChartLeft = this.$echarts.init(document.getElementById('panChartLeft'));
                panChartLeft.setOption({
                    title: {
                        text: '服务使用频率Top5',
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    toolbox: {
                        show: true,
                        feature: {
                            mark: {show: true},
                            dataView: {show: true, readOnly: false},
                            magicType: {show: true, type: ['line', 'bar']},
                            restore: {show: true},
                            saveAsImage: {show: true}
                        }
                    },
                    calculable: true,
                    xAxis: [
                        {
                            type: 'category',
                            data: data.x_data
                        }
                    ],
                    yAxis: [
                        {
                            type: 'value'
                        }
                    ],
                    series: [
                        {
                            name: '使用次数',
                            type: 'bar',
                            color: '#709ed8',
                            data: data.y_data,
                            markPoint: {
                                data: [
                                    {type: 'max', name: '最大值'},
                                    {type: 'min', name: '最小值'}
                                ]
                            },
                            markLine: {
                                data: [
                                    {type: 'average', name: '平均值'}
                                ]
                            }
                        }
                    ]
                });
            },
            drawRight(data) {
                let panChartRight = this.$echarts.init(document.getElementById('panChartRight'));
                panChartRight.setOption({
                    title: {
                        text: '服务申请频率Top5',
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    toolbox: {
                        show: true,
                        feature: {
                            mark: {show: true},
                            dataView: {show: true, readOnly: false},
                            magicType: {show: true, type: ['line', 'bar']},
                            restore: {show: true},
                            saveAsImage: {show: true}
                        }
                    },
                    calculable: true,
                    xAxis: [
                        {
                            type: 'category',
                            data: data.x_data
                        }
                    ],
                    yAxis: [
                        {
                            type: 'value'
                        }
                    ],
                    series: [
                        {
                            name: '申请次数',
                            type: 'bar',
                            color: '#64a9ff',
                            data: data.y_data,
                            markPoint: {
                                data: [
                                    {type: 'max', name: '最大值'},
                                    {type: 'min', name: '最小值'}
                                ]
                            },
                            markLine: {
                                data: [
                                    {type: 'average', name: '平均值'}
                                ]
                            }
                        }
                    ]
                });
            }
        }
    }
</script>

<style scoped lang='scss'>
    #home {
        height: 100%;
        width: 100%;
        overflow-y: auto;
        padding: 10px;

        .next-button {
            position: absolute;
            z-index: 9999;
            right: 40px;
            bottom: 30px;
        }

        .home-top {
            height: 25%;
        }

        .home-bottom {
            height: 70%;
        }

        .top-item {
            padding: 10px;
            height: 100%;
            font-size: 18px;

            .item-contain {
                width: 100%;
                height: 100%;
                background-color: #1a4aa3;
            }

            .content-icon {
                font-size: 60px;
            }

            .is-left {
                float: left;
                width: 30%;
                height: 100%;
                border-top-left-radius: 10px;
                border-bottom-left-radius: 10px;
            }

            .is-right {
                float: right;
                width: 70%;
                height: 100%;
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 10px;
            }

            .first-color-left {
                background-color: #5c90d2;
                display: flex;
                align-items: center;
                justify-content: center;
            }

            .second-color-left {
                background-color: #4A9BFF;
                display: flex;
                align-items: center;
                justify-content: center;
            }

            .first-color-right {
                background-color: #709ed8;
            }

            .second-color-right {
                background-color: #64a9ff;
            }
        }

    }
</style>
