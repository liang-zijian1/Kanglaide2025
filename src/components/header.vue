<template>
    <div class="g-header">
        <h2 class="header-title"><span>Aqua</span>Sentry</h2>
        <ul>
            <li><a href="#introduction">Introduction</a></li>
            <li><a href="#advantages">Advantages</a></li>
            <li><a href="#mechanism">Mechanism</a></li>
            <li><a href="#aboutus">About us</a></li>
            <li><a href="#partner">Partnership</a></li>
        </ul>
    </div>
</template>

<script lang="ts" setup>
</script>

<style lang="less" scoped>
.g-header {
    position: absolute;
    left: 0;
    top: 0;
    display: flex;
    padding-left: 60px;
    padding-right: 60px;
    z-index: 99;
    justify-content: space-between;
    width: 100%;
    h2 {
        color: #fff;
        font-size: 34px;
        font-family: "Microsoft YaHei";
        padding-top: 60px;
        span {
            color: #c40000;
        }
    }
    ul {
        display: flex;
        font-size: 20px;
        color: #ddd;
        display: flex;
        list-style: none;
        padding-top: 36px;
        li a {
            color: #ddd;
            margin-left: 20px;
            cursor: pointer;
            text-decoration: none;
            &:hover {
                color: #c40000;
            }
        }
    }
}
</style>