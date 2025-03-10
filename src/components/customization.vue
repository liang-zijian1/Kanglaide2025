<template>
    <div id="advantages" class="g-customization">
        <h4 class="custom-title">Main Advantages</h4>
        <ul class="custom-list">
            <li class="custom-item">
                <img style="width: 40px; height: 40px;" src="@/assets/image/icon_automation.png" alt="">
                <div class="item-txt">
                    <strong>High Degree of Automation</strong>
                    <div class="desc">
                        With the advanced YOLOv11 algorithm and PID control system, AquaSentry can automatically
                        identify the drowning person and accurately launch the lifebuoy without any human intervention.
                    </div>
                </div>
            </li>
            <li class="custom-item">
                <img src="@/assets/image/icon_adaptability.png" alt="">
                <div class="item-txt">
                    <strong>Portability & Multi-Scenario Adaptability</strong>
                    <div class="desc">
                        It adopts a detachable design and weighs only 9 kg, making it convenient to carry and deploy.
                        It can be applied efficiently whether in indoor pools, outdoor lakes or post-disaster emergency
                        rescues.
                    </div>
                </div>
            </li>
            <li class="custom-item">
                <img src="@/assets/image/icon_precision.png" alt="">
                <div class="item-txt">
                    <strong>Low Latency & High Precision</strong>
                    <div class="desc">
                        The combination of hardware and software ensures that the rescue task can be completed
                        accurately even under high-pressure environments, far surpassing similar products.
                    </div>
                </div>
            </li>
        </ul>
    </div>
</template>

<script lang="ts" setup>
import gsap from 'gsap';
import { onMounted } from 'vue';

onMounted(() => {
    setTimeout(() => {
        const tl = gsap.timeline({
            scrollTrigger: {
                trigger: ".g-customization", // 监听 `.animate-from-bottom` 元素
                start: "top 75%",  // 当元素的顶部到达视口底部时触发
                end: "bottom 25%",    // 当元素的底部到达视口顶部时结束
                // markers: true, // 开启标记，便于调试
                toggleActions: "play none none none",
            },
        });
        tl.from(".custom-title", {
            duration: 1,
            y: 150, // 动画从底部移动上来
            ease: "power2.out",
            opacity: 0
        })
            .from(".custom-item", {
                duration: 2,
                y: 100, // 动画从底部移动上来
                ease: "power2.out",
                stagger: 0.5,
                opacity: 0
            })
    }, 100);
})
</script>

<style scoped lang="less">
.g-customization {
    height: 500px;
    background: #101010;

    h4 {
        font-size: 26px;
        color: #fff;
        padding-top: 100px;
        padding-bottom: 80px;
        text-align: center;
    }
}

.custom-list {
    width: 96%;
    margin: 0 auto;
    display: flex;
    padding-left: 0;

    .custom-item {
        flex: 1;
        margin: 0 20px;
        display: flex;

        .item-txt {
            flex: 1;
        }

        strong {
            display: block;
            font-size: 16px;
            color: #eee;
            margin-bottom: 24px;
            line-height: 1.5;
            max-width: 100%;
            overflow: hidden;
            text-overflow: ellipsis;
            ;
            white-space: nowrap;
        }

        .desc {
            font-size: 14px;
            color: #bbb;
            line-height: 1.8;
        }

        img {
            width: 36px;
            height: 36px;
            margin-right: 20px;

        }
    }
}
</style>