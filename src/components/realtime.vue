<template>
  <div id="aboutus" class="g-realtime">
    <div class="realtime-inner">
      <div class="realtime-left">
        <video src="/realtime.mp4" controls autoplay muted loop></video>
      </div>
      <div class="realtime-right">
        <h4 class="realtime-title">Abount Us</h4>
        <p>
          We five have been friends for a long time and come from the same robotics team. We trust each other and enjoy
          working together. We also share a common ideal, which is to help others with our robots building capabilities.
        </p>
        <p>
          Ryan, our CEO with comprehensive experiences in FRC, possesses a strong sense of social responsibility and
          business acumen. After a tragic incident of his relative drowning in a lake occurred, he put forward the idea
          of building a robot for lake’s emergency water rescues, and it quickly caught our attention. Hence, we formed
          the HydroFalcon.
        </p>
        <p>
          Stanley, CTO, has more than five years of robots building experience in 8011, focuses on software
          and hardware engineering of AquaSentry along with Sam, CDO.
        </p>
        <p>
          Pai, responsible for market-related work as CMO, is
          good at economics and business.
        </p>
        <p>
          Harper is sensitive to numbers, so she serves as CFO to finish works related to
          financial calculation.
        </p>

      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import gsap from 'gsap';
import { onMounted } from 'vue';

onMounted(() => {
  setTimeout(() => {
    const tl = gsap.timeline({
      scrollTrigger: {
        trigger: ".realtime-inner", // 监听 `.animate-from-bottom` 元素
        start: "top 75%",  // 当元素的顶部到达视口底部时触发
        end: "bottom 25%",    // 当元素的底部到达视口顶部时结束
        // markers: true, // 开启标记，便于调试
        toggleActions: "play none none none",
      },
    });
    tl.from(".realtime-left", {
      ease: "power2.out",
      duration: 1,
      opacity: 0,
      y: 100,
    })
    .from(".realtime-title", {
      ease: "power2.out",
      duration: 1,
      opacity: 0,
      y: 100,
    }, "<")
      .fromTo(
        ".realtime-right p",  // 选择每一行的 div 元素
        {
          opacity: 0,  // 初始状态：文字透明
          y: 50,  // 初始偏移：向下偏移
        },
        {
          opacity: 1,  // 动画结束状态：文字完全可见
          y: 0,  // 恢复原位置
          duration: 1,  // 每行动画持续时间
          stagger: 0.5,  // 每行之间的间隔
          ease: "power2.out",  // 缓动效果
        }
      );
   
  }, 100)
})
</script>

<style lang="less" scoped>
.g-realtime {
  // height: 500px;
  background: #101010;
  padding: 80px 0;

  .realtime-inner {
    width: 90%;
    display: flex;
    margin: 0 auto;
    align-items: center;
    // height: 320px;

    .realtime-left {
      width: 550px;
      height: 400px;
      margin-right: 80px;

      video {
        width: 100%;
        height: 100%;
        object-fit: cover;
      }
    }

    .realtime-right {
      // display: flex;
      // justify-content: center;
      // align-items: center;
      
      flex: 1;
      height: 100%;
      font-size: 14px;
      color: #ddd;
      line-height: 1.8;
      h4 {
        font-size: 30px;
        color: #fff;
        margin-bottom: 40px;
        text-align: center;
        margin-top: -20px;
      }
    }
  }

  ;
}
</style>
