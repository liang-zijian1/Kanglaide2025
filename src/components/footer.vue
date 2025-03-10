<template>
    <div class="g-footer">
        <div class="keyworld">
            <h2><span>Aqua</span>Sentry</h2>
        </div>
        <ul class="link-method">
            <li>
                <label>
                    <img src="@/assets/image/icon_phone.png" alt="">
                    <i>Phone：</i>
                </label>
                <span>13922228880</span>
            </li>
            <li>
                <label>
                    <img src="@/assets/image/icon_email.png" alt="">
                    <i>Eamil：</i>
                </label>
                <span>zhuangjr.ryan@gmail.com</span>
            </li>
            <!-- <li>
                <label>
                    <img src="@/assets/image/icon_qq.png" alt="">
                    <i>QQ：</i>
                </label>
                <span>zhuangjr.ryan2023@gdhfi.com</span>
            </li> -->
            <!-- <li>
                <label>
                    <img src="@/assets/image/icon_weibo.png" alt="">
                    <i>微博：</i>
                </label>
                <span>一剪梅</span>
            </li> -->
            <li>
                <label>
                    <img src="@/assets/image/icon_address.png" alt="">
                    <i>Address：</i>
                </label>
                <span>Tianhe District, Guangzhou City, Guangdong Province</span>
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
                trigger: ".g-footer", // 监听 `.animate-from-bottom` 元素
                start: "top 85%",  // 当元素的顶部到达视口底部时触发
                end: "bottom 25%",    // 当元素的底部到达视口顶部时结束
                // markers: true, // 开启标记，便于调试
                toggleActions: "play none none none",
            },
        });
        tl.from(".keyworld h2", {
            opacity: 0,
            xPercent: -100,
            duration: 2,
        })
            .from(
                ".link-method li",
                {
                    opacity: 0,
                    y: 100,
                    duration: 2,
                    stagger: 0.3
                },
                "<"
            )
    }, 100);

})
</script>

<style lang="less" scoped>
.g-footer {
    background: #101010;
    padding-bottom: 60px;

    .keyworld {
        padding: 70px 0;
        margin: 0 auto;
        width: 90%;
        border-bottom: 1px solid #666;

        h2 {
            color: #fff;
            font-size: 34px;
            font-family: "Microsoft YaHei";

            span {
                color: #c40000;
            }
        }
    }

    .link-method {
        margin-top: 60px;
        margin-left: 20%;
        border-left: 1px solid #999;
        padding-left: 60px;
        display: flex;
        flex-wrap: wrap;

        li {
            width: 50%;
            height: 50px;
            display: flex;
            align-items: center;
            color: #ccc;
            i {
                font-style: normal;
            }

            img {
                width: 24px;
                height: 24px;
                margin-right: 5px;
            }
        }
    }
}
</style>