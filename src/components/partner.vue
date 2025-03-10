<template>
    <div id="partner" class="g-partner">
        <h3 class="partner-title">Potential Partnership</h3>
        <ul class="partner-list">
            <li>
                <img src="@/assets/image/icon_school.png" alt="">
                <span>Schools</span>
            </li>
            <li>
                <img src="@/assets/image/icon_park.png" alt="">
                <span>Parks</span>
            </li>
            <li>
                <img src="@/assets/image/icon_reser.png" alt="">
                <span>Reservoirs</span>
            </li>
        </ul>
    </div>
</template>

<script setup lang="ts">
import gsap from 'gsap';
import { onMounted } from 'vue';



onMounted(() => {
    setTimeout(() => {
        const tl = gsap.timeline({
            scrollTrigger: {
                trigger: ".g-partner", // 监听 `.animate-from-bottom` 元素
                start: "top 75%",  // 当元素的顶部到达视口底部时触发
                end: "bottom 25%",    // 当元素的底部到达视口顶部时结束
                // markers: true, // 开启标记，便于调试
                toggleActions: "play none none none",
            },
        });
        tl.from(".partner-title", {
            duration: 1,
            y: 150, // 动画从底部移动上来
            ease: "power2.out",
            opacity: 0
        })
            .from(".partner-list li", {
                duration: 2,
                scale: 0, // 动画从底部移动上来
                ease: "power2.out",
                stagger: 0.3
            })
    }, 100)

})
</script>

<style lang="less" scoped>
.g-partner {
    height: 466px;
    background: url("/cardlist_bg.png") no-repeat top transparent;
    background-attachment: fixed;
}

.partner-title {
    font-size: 26px;
    color: #fff;
    padding-top: 100px;
    padding-bottom: 80px;
    text-align: center;
}

.partner-list {
    width: 90%;
    margin: 0 auto;
    display: flex;
    padding-left: 0;
    justify-content: space-around;

    li {
        width: 300px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;

        img {
            width: 120px;
            height: 100px;
        }

        span {
            display: block;
            padding-top: 20px;
            font-size: 16px;
            color: #bbb;
        }
    }
}
</style>