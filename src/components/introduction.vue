<template>
  <div id="introduction" class="g-introduction">
    <div class="introduction-content">
      <div class="introduction-left">
        <div class="left-inner">
          <h4 class="animate-from-bottom">
            Introduction
          </h4>
          <!-- <strong class="animate-from-left">AquaSentry</strong> -->
          <div class="desc animate-from-bottom">
            Through innovative hardware design and cutting-edge software
            technology, it can quickly and accurately locate the drowning person
            in various water environments and automatically launch a
            self-inflating lifebuoy, which greatly improves the rescue
            efficiency and reduces the dependence on manpower.
          </div>
        </div>
        <p class="line"></p>
      </div>
      <div class="introduction-right">
        <video src="/introduction.mp4" controls autoplay muted loop></video>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import gsap from "gsap";
import { onMounted } from "vue";


onMounted(() => {
  setTimeout(() => {
    const tl = gsap.timeline({
      scrollTrigger: {
        trigger: ".g-introduction", // 监听 `.animate-from-bottom` 元素
        start: "top 75%",  // 当元素的顶部到达视口底部时触发
        end: "bottom 25%",    // 当元素的底部到达视口顶部时结束
        // markers: true, // 开启标记，便于调试
        toggleActions: "play none none none",
      },
    });
    tl.from(".animate-from-bottom", {
      duration: 1,
      y: 100, // 动画从底部移动上来
      opacity: 0, // 渐显
      //   ease: "power2.out"
    })
      .from(".introduction-right", {
        duration: 1,
        opacity: 0,
        y: 100,
      }, "<")
      // .from(".animate-from-left", {
      //   duration: 1,
      //   x: -300, // 从左边移动到原位置
      //   opacity: 0,
      //   ease: "power2.out",
      //   onComplete: () => {
      //     console.log('complete animation')
      //   }
      // })

      .from(".line", {
        opacity: 0,
        duration: 1,
      });
  }, 100);
});
</script>

<style lang="less" scoped>
.g-introduction {
  width: 100%;
  height: 600px;
  background: url("/introduction_bg.jpg") no-repeat top transparent;
  background-attachment: fixed;
}

.introduction-content {
  width: 90%;
  margin: 0 auto;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;

  .introduction-right {
    width: 560px;
    height: 360px;

    video {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  }

  .introduction-left {
    flex: 1;

    .left-inner {
      padding-right: 80px;
      //   border-bottom: 1px solid #999;
    }

    .line {
      width: 100%;
      height: 1px;
      background-color: #999;
    }

    h4 {
      font-size: 32px;
      color: #fff;
    }

    strong {
      display: block;
      font-size: 24px;
      color: #aaa;
    }

    .desc {
      font-size: 14px;
      color: #ddd;
      line-height: 1.8;
      padding-top: 50px;
      padding-bottom: 50px;
    }
  }
}
</style>
