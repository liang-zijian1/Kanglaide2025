<template>
  <div class="g-top">
    <!-- <Header /> -->
    <a-carousel arrows :autoplay="true" :autoplaySpeed="5000">
      <template #prevArrow>
        <div class="custom-slick-arrow" style="left: 10px; z-index: 1">
          <LeftOutlined :style="{ fontSize: '30px', color: '#fff' }" />
        </div>
      </template>
      <template #nextArrow>
        <div class="custom-slick-arrow" style="right: 10px">
          <RightOutlined :style="{ fontSize: '30px', color: '#fff' }" />
        </div>
      </template>
      <div v-for="item in items" :key="item.id">
        <div class="banner-item" :style="{ height: '100vh' }">
          <div class="banner-item-inner">
            <img :src="item.media" />
          </div>
        </div>
      </div>
    </a-carousel>
  </div>
</template>
<script lang="ts" setup>
import { LeftOutlined, RightOutlined } from "@ant-design/icons-vue";
import { onMounted, ref } from "vue";
// import Header from "./components/header.vue";
// import video1 from "@/assets/video/banner-1.mp4";
// import video2 from "@/assets/video/banner-2.mp4";
import banner1 from "@/assets/image/banner-1.png";
import banner2 from "@/assets/image/banner-2.jpg";
import banner3 from "@/assets/image/banner-3.jpg";
import banner4 from "@/assets/image/banner-4.png";

// const getImgUrl = (imagePath: string) => new URL(imagePath, import.meta.url).href

const bannerHeight = ref(window.innerHeight);
const items = ref([
  { id: 1, media: banner1 },
  { id: 2, media: banner2 },
  { id: 3, media: banner3 },
  { id: 4, media: banner4 }
]);

onMounted(() => {
  bannerHeight.value = window.innerHeight;
});
</script>
<style scoped lang="less">
/* For demo */
:deep(.slick-slide) {
  text-align: center;
  /* height: 160px;
  line-height: 160px; */
  // background: #364d79;
  overflow: hidden;
}

:deep(.slick-arrow.custom-slick-arrow) {
  width: 70px;
  height: 70px;
  font-size: 25px;
  color: #fff;
  transition: ease all 0.3s;
  opacity: 0.3;
  z-index: 1;
  border-radius: 6px;
  line-height: 70px;
  text-align: center;

  &:hover {
    background-color: rgba(0, 0, 0, .3);
  }
}

:deep(.slick-arrow.custom-slick-arrow:before) {
  display: none;
}

:deep(.slick-arrow.custom-slick-arrow:hover) {
  color: #fff;
  opacity: 0.5;
}

:deep(.slick-slide h3) {
  color: #fff;
}

.g-top {
  position: relative;
}

.banner-item {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(0, 0, 0, 0.4);
  background: url(/public/banner_bg1.png);
  transition: background-image 2s ease-in-out;

  .banner-item-inner {
    width: 830px;
    height: 420px;
    // border: 5px solid #999;
    line-height: 420px;
    color: #ddd;
    text-align: center;
    font-size: 42px;

    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  }
}
</style>
