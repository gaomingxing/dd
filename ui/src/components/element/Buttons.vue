<template>
    <div id="Buttons">
                <h3 class="margin-bottom10">按钮</h3>
                <div class="padding-10">
                    <Button>默认</Button>
                    <Button type="primary" size="large">主按钮</Button>
                    <Button type="dashed" size="small">点点点</Button>
                    <Button type="text">文本</Button>
                    <br><br>
                    <Button type="info">通知</Button>
                    <Button type="success">成功</Button>
                    <Button type="warning">警告</Button>
                    <Button type="error">错误</Button>
                </div>
                <h3 class="margin-bottom10 margin-top10">ghost按钮</h3>
                <div class="ghost-back padding-10">
                    <Button ghost>默认</Button>
                    <Button type="primary" size="large" ghost>主按钮</Button>
                    <Button type="dashed" size="small" ghost>点点点</Button>
                    <Button type="text" ghost>文本</Button>
                    <br><br>
                    <Button type="info" ghost>通知</Button>
                    <Button type="success" ghost>成功</Button>
                    <Button type="warning" ghost>警告</Button>
                    <Button type="error" ghost>错误</Button>
                </div>
                <h3 class="margin-bottom10 margin-top10">按钮disabled</h3>
                <div class="padding-10">
                    <Button type="info" disabled>通知</Button>
                    <Button type="success" disabled>成功</Button>
                    <Button type="warning" disabled ghost>警告</Button>
                    <Button type="error" disabled ghost>错误</Button>
                </div>
                <h3 class="margin-bottom10 margin-top10">图标按钮</h3>
                <div class="padding-10">
                    <Button type="primary" icon="ios-search"></Button>
                    <Button type="primary" shape="circle" icon="ios-search"></Button>
                    <Button type="primary" disabled icon="ios-search"></Button>
                </div>
    </div>
</template>

<script>
    export default {
        name: 'Buttons'
    }
</script>

<style scoped>

</style>
