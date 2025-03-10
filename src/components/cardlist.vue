<template>
  <div id="mechanism" class="g-cardlist">
    <div class="cardlist-inner">
      <div class="cardlist-left">
        <div class="cardlist-left-media">
          <img src="/cardlist_left.png" alt="" />
        </div>
        <div class="cardlist-left-txt cardlist-txt">
          <div class="animation-cardlist-txt">
            <h4>
              Two-degree-of-freedom Structure & High-speed Friction Launch
              Mechanism
            </h4>
            <div class="desc">
              It has two degrees of freedom of pitch and yaw rotation. Combined
              with the four-roller high-speed friction launch mechanism driven
              by two brushless motors, it can flexibly adjust the launch angle
              and achieve long-distance and accurate launch of the
              self-inflating lifebuoy.
            </div>
          </div>
        </div>
      </div>
      <ul class="cardlist-right">
        <li class="cardlist-right-item" style="height: 240px">
          <div class="cardlist-right-txt cardlist-txt">
            <div class="animation-cardlist-txt">
              <h4>High-precision Sensing and Tracking System</h4>
              <div class="desc">
                Equipped with a high-definition and ultra-high-speed industrial
                camera sensor and matched with the PID control algorithm, it can
                real-time accurately locate and automatically track the drowning
                person in various environments, providing reliable support for
                the rescue.
              </div>
            </div>
          </div>
          <div class="cardlist-right-media">
            <video src="/cardlist_right1.mp4" controls autoplay muted loop></video>
          </div>
        </li>
        <li class="cardlist-right-item">
          <div class="cardlist-right-txt cardlist-txt">
            <div class="animation-cardlist-txt">
              <h4>Efficient Software Algorithm Optimization</h4>
              <div class="desc">
                Based on 12,000 labeled drowning images and data augmentation
                technology, an exclusive YOLOv11 model has been successfully
                trained, achieving a 98.7% recognition accuracy and 1.12% packet
                loss rate. AquaSentry uses the NVIDIA GeForce RTX 3060 Laptop
                GPU for local offline inference, with an inference time of only
                2 ms per frame.
              </div>
            </div>
          </div>
          <div class="cardlist-right-media">
            <video src="/cardlist_right2.mp4" controls autoplay muted loop></video>
          </div>
        </li>
        <li class="cardlist-right-item" style="height: 210px">
          <div class="cardlist-right-txt cardlist-txt">
            <div class="animation-cardlist-txt">
              <h4>High-precision Control & Multi-protocol Communication</h4>
              <div class="desc">
                The control system is based on the STM32 self-developed
                development board and high-precision IMU inertial navigation
                chip. It supports multiple communication protocols and ensures
                the accurate positioning and control during the launch process.
              </div>
            </div>
          </div>
          <div class="cardlist-right-media">
            <img src="/cardlist_right3.jpg" alt="" />
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script lang="ts" setup>
import gsap from "gsap";
import { onMounted } from "vue";

onMounted(() => {
  setTimeout(() => {
    const tl = gsap.timeline({
    scrollTrigger: {
      trigger: ".g-cardlist", // 监听 `.animate-from-bottom` 元素
      start: "top 75%",  // 当元素的顶部到达视口底部时触发
      end: "bottom 25%",    // 当元素的底部到达视口顶部时结束
      // markers: true, // 开启标记，便于调试
      toggleActions: "play none none none",
    },
  });
    tl.from(".cardlist-left", {
      opacity: 0,
      xPercent: -100,
      duration: 2,
    })
      .from(
        ".cardlist-right-item",
        {
          opacity: 0,
          xPercent: 100,
          duration: 2,
          stagger: 0.5,
        },
        "<"
      )
      .from(".animation-cardlist-txt", {
        opacity: 0,
        y: 100,
        duration: 1,
      });
  }, 100);
});
</script>

<style lang="less" scoped>
.g-cardlist {
  display: flex;
  height: 930px;
  align-items: center;
  background: url("/cardlist_bg.png") no-repeat top transparent;
  background-attachment: fixed;

  .cardlist-inner {
    width: 95%;
    margin: 0 auto;
    display: flex;
  }
}

.cardlist-left {
  flex: 1;
  width: 0;
  margin-right: 30px;
  max-height: 774px;
  display: flex;
  flex-direction: column;

  .cardlist-left-media {
    width: 100%;
    height: 524px;

    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  }

  .cardlist-left-txt {
    flex: 1;
  }
}

.cardlist-right {
  flex: 1;
  min-width: 800px;

  .cardlist-right-item {
    display: flex;
    height: 260px;
    margin-bottom: 30px;
    align-items: center;

    &:last-child {
      margin-bottom: 0;
    }

    .cardlist-right-txt {
      flex: 3;
      width: 0;
      height: 100%;
      border: 10px solid #181818;
      padding: 20px;

      h4 {
        margin-bottom: 20px;
      }
    }

    .cardlist-right-media {
      flex: 2;
      height: 100%;

      img,
      video {
        width: 100%;
        height: 100%;
        object-fit: cover;
      }
    }
  }
}

.cardlist-txt {
  padding: 30px;
  background-color: #161616;
  border: 20px solid #181818;
  overflow: hidden;

  h4 {
    font-size: 16px;
    color: #eee;
    margin-bottom: 24px;
    line-height: 1.5;
    max-width: 100%;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .desc {
    font-size: 14px;
    color: #bbb;
    line-height: 1.8;
  }
}
</style>
