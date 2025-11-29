<template>
  <div class="home">

      <!--复用组件-->
  <div class="right-align" style="background-color: rgba(245, 246, 252, 1);">
      <NavigationMenu
        :activeIndex="activeIndex"
        :backgroundColor="backgroundColor"
        :textColor="textColor"
        :activeTextColor="activeTextColor"
      />
    </div>


        <!--走马灯-->
    <div  style="display: flex; flex-direction: column;">
          <el-carousel trigger="click" height="500px" width="1000px" v-model="currentThumbnailIndex">
            <el-carousel-item v-for="(thumbnail, index) in thumbnails" :key="index">
              <div class="picture" >
                <img :src="thumbnail.image" alt="" style="display: flex; flex-direction: column;">
        <h3 class="hh3">{{thumbnail.title}}</h3>
              </div>
            </el-carousel-item>
          </el-carousel>
  </div>


  <div class="container1">
    <el-col :span="10">
      <p class="title1">专注品质，</p>
      <p class="title2">竭诚服务。</p>
      <!-- <p class="intro1">无论您有买车还是卖车的需求，</p>
      <p class="intro1">我们都将竭尽所能为您提供满意的服务。</p> -->
    </el-col>
    <el-col :span="10">
      <img src="../assets/car.png" class="car" width="800" height="600" alt="汽车图片"/>
    </el-col>
  </div>



  <div class = "sub-container" > 

    <el-col :span="12"> 
      <img src="../assets/images/resource/news-14.jpg" class="car2"  alt="汽车图片"/>
    </el-col>
    <el-col :span="10"> 
      <el-row >
        <div class="title">
        <i class="el-icon-info"></i>
        详尽的车辆信息
        <p> 在我们的平台上，您能够了解到发布车源的详细参数，助力您选到更加心仪的爱车。</p>
        </div>
      </el-row>
      <el-row >
        <div class="title">
        <i class="el-icon-check"></i>
        精准的车辆估值
        <p> 基于海量历史交易数据，搭建高精度的估价算法模型，为您提供出售报价建议，将您爱车的价值最大化。</p>
        </div>
      </el-row>
    </el-col>


  </div>

  <div class = "sub-container" > 

    <el-col :span="10"> 
    <el-row >
      <div class="title">
        <i class="el-icon-data-line"></i>
        前瞻的走势预测
        <p> 收集宏观经济数据，判断车辆价格走势，为您选择最佳买车时间提供参考</p>
      </div>
    </el-row>
    <el-row >
      <div class="title">
        <i class="el-icon-pie-chart"></i>
          完备的数据统计
        <p> 最受欢迎车辆、各地区车源分布等信息一目了然，帮您迅速了解二手车市场行情。</p>
      </div>
    </el-row>
    </el-col>

    <el-col :span="12"> 
    <img src="../assets/images/resource/news-10.jpg" class = "car2" alt="汽车图片" />
    </el-col>

  </div>

  <div class = "sub-container" > 

    <el-col :span="12"> 
      <img src="../assets/statistics.gif" class = "gif" alt="折线图"/>
    </el-col>

    <el-col :span="19"> 
    <el-row >
      <div class="title">
        <i class="el-icon-data-line"></i>
        马上注册，拥有您自己的账户
        <p> 发布车辆、收藏心仪车辆，助您做出更精准的购买决策</p>
      </div>
    </el-row>
    <el-row >
      <div class="title">
        <i class="el-icon-pie-chart"></i>
          联系我们
        <p> 联系我们，提供系统使用的意见或建议</p>
      </div>
    </el-row>
    </el-col>

  </div>
    



    
  <div class="call" style="background-color: rgba(245, 246, 252, 1);">
    <p>欢迎致电：0433-888888</p>
  </div>

</div>


</template>

<style scoped>
@import "../assets/css/style.css";

.navigation-container {
display: flex;
justify-content: flex-end;
align-items: center;
}

.container1 {
width: 100%;
height: 100%;
box-sizing: border-box;
padding-top: 100px;
text-align: center;
margin-bottom: 400px;
/*  background-color: rgba(245, 246, 252, 1);*/
}

.sub-container {
  margin-left: 100px;
  margin-right: 100px;
  margin-bottom: 10px;
margin-top: 200px;
  display: flex;
  justify-content: space-between;
}


.title1 {
font-size: 60px;
font-family: "Microsoft YaHei";
font-weight: bold;
color: #1D1E21;
position: relative;
right: 0px;
top: 20px;
}
.title2 {
font-size: 60px;
font-family: "Microsoft YaHei";
font-weight: bold;
position: relative;
color: #1D1E21;
right: 0px;
top: 10px;
}
.line{
position: absolute;
top: 270px; /* 调整图片的上方间距 */
left: 350px;
}
.intro1 {
font-size: 16px;
font-family: "Microsoft YaHei";
font-weight: bold;
position: relative;
color: rgba(146, 147, 149, 1);

/*background-color="rgba(130, 157, 255, 1)"*/
right: 440px;
top: 100px;
}





.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}

.hh3 {
position: absolute;
opacity: 1;
align-items: center;
font-size: 100px;
font-family: "Microsoft YaHei";
font-weight: bold;
text-align: center;
}



.picture{
  display: flex;
  justify-content: center;
  align-items: center;
}
.home {
position: relative;
width: 100%;
background-color: rgba(245, 246, 252, 1);
}

.navigation .el-menu-item a {
font-family: "Microsoft YaHei"; /* 设置文字字体 */
font-size: 16px; /* 设置文字大小 */
font-weight: bold; /* 设置文字加粗 */
text-decoration: none; /* 取消文字下划线 */
}


.car{
top: 100px; /* 调整图片的上方间距 */
left: 500px;
}
.gif{
top: 100px; /* 调整图片的上方间距 */
left: 1000px;
}
.car2{
/* -webkit-box-reflect: below; */
-webkit-box-reflect: below 6px -webkit-linear-gradient(transparent,transparent 70%,rgba(255,255,255,0.6));
width: 100%;
height: auto;
border-radius : 10px;

}



.title {
margin-top: 0px;
border-radius: 40px;
/*  min-height: 100px;*/
height: 120px;
font-size: 30px;
}
.title p{
margin-top: 20px;
font-size: 18px;
font-family: "Microsoft YaHei";
font-weight: normal;
position: relative;
color: rgba(146, 147, 149, 1);
text-align: left;
}

.call{
position: relative;
bottom: 10px; /* 设置在页面底部 */
margin-top: 100px;
background-color: rgba(245, 246, 252, 1);
font-size: 17px;
height: 2%;
text-align: center;
}

.el-carousel__item h3 {
  color:  #d3dce6;
  font-size: 180px;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
  background-color: #d3dce6;
}

/* 走马灯*/
.thumbnails-container {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  margin-top: 20px;
}
.thumbnail {
  opacity: 1;
  transition: opacity 0.3s;
  margin-right: 10px;
color:  #d3dce6;
}
.thumbnail:last-child {
  margin-right: 0;
}
.thumbnail.active {
  opacity: 1;
}
</style>

<script>
import NavigationMenu from '@/components/NavigationMenu.vue';
/*import HeadNav from "../components/HeadNav";*/
export default {
name: "home",
components: {
  NavigationMenu,
},
data() {
  return {
    activeIndex: '1',
  thumbnails: [
            { image: require("../assets/images/main-slider/image-1.jpg"), active: false, title : "车车！"},
            { image: require("../assets/images/main-slider/image-2.jpg"), active: false, title : "二手车车！"},
          //   { image: require("../assets/images/resource/image-3.png"), active: false },
          //   { image: require("../assets/images/resource/image-4.png"), active: false },
          //   { image: require("../assets/images/resource/image-5.png"), active: false }
  ],
  currentThumbnailIndex: 0, 
  };
},
};
</script>