<!-- 
    * @FileDescription: 价格时间序列页面
    * @LastEditTime: 7.10
 -->
<template>
  <el-container>
    <el-header>
      <div class="container">
        <!--复用组件-->
        <NavigationMenu
          :activeIndex="activeIndex"
          :backgroundColor="backgroundColor"
          :textColor="textColor"
          :activeTextColor="activeTextColor"
        />
      </div>
    </el-header>
    <div class="background-image">
      <img src="../assets/Image.jpg" alt="" class="background-img" />
    </div>
    <el-main>
      <el-row class="parallel-container" justify="center">
        <el-col :span="12" class="center-div">
          <!-- <el-form
      :model="carInfo"
      :rules="rules"
      ref="sellForm"
      class="sellForm"
      label-width="60px"
    > -->
          <el-form
            ref="ptsForm"
            :model="ptsInfo"
            style="margin-top: 20px; color: rgb(0, 0, 0)"
          >
            <el-row class="center-row">
              <h1 class="car-info">请输入想要预测的车辆信息</h1>
              <el-col :span="10">
                <h2 class="second-title">车型属性</h2>
                <h3 class="third-title">品牌/车系/车型</h3>
                <el-form-item
                  style="line-height: 20px; margin-top: 10px; margin-left: 20px"
                >
                  <el-cascader
                    v-model="品牌车系"
                    :options="modelOptions"
                    @change="handleChange($event, '品牌车系')"
                    style="width: 250px"
                  ></el-cascader>
                </el-form-item>
                <h2 class="second-title">上牌时间</h2>
                <h3 class="third-title">年/月</h3>
                <el-form-item
                  style="line-height: 20px; margin-top: 10px; margin-left: 20px"
                >
                  <el-cascader
                    v-model="timeValue"
                    :options="timeOptions"
                    @change="handleChange2"
                    style="width: 250px"
                  ></el-cascader>
                  <h3 class="third-title" style="margin-bottom: 90px">
                    &nbsp;
                  </h3>
                </el-form-item>
              </el-col>
            </el-row>
            <el-row></el-row>
            <el-row>
              <el-form-item>
                <div class="button-div">
                  <el-button
                    @click="onSubmit(ptsForm)"
                    style="
                      background-color: #ffffff;
                      height: 50px;
                      font-size: 18px;
                      color: #1c1a1a;
                      width: 200px;
                      font-weight: bold;
                    "
                  >
                    预测价格走向
                  </el-button>
                </div>
              </el-form-item>
            </el-row>
          </el-form>
        </el-col>
      </el-row>
      <transition name="slide">
        <div v-if="showingDetails" class="details-container">
          <el-row class="parallel-container" style="margin-top: 50px">
            <el-col :span="12" class="left-div">
              <h1 class="h1">历史价格走势</h1>
              
            </el-col>

            <el-col :span="12" class="left-div">
              <h1 class="h1">预测价格走势</h1>
            </el-col>
          </el-row>
          <el-row
            id="bottom-element"
            class="parallel-container"
            style="margin-top: 30px"
          >

          </el-row>
        </div>
      </transition>
    </el-main>
  </el-container>
</template>

<style>
/*导航菜单部分*/

.container {
  display: flex;
  justify-content: flex-end;
}
.navigation .el-menu-item a {
  active-color: "rgba(255, 101, 27, 1)";
  font-family: "Microsoft YaHei"; /* 设置文字字体 */
  font-size: 16px; /* 设置文字大小 */
  font-weight: bold; /* 设置文字加粗 */
  text-decoration: none; /* 取消文字下划线 */
}
el-container {
  display: flex;
  flex-direction: column;
  font-family: "Microsoft YaHei";
  height: 100vh;
}
.el-header {
  background-color: #ffffffe2;
  /*color: #FFFFFF;*/
  line-height: 60px;
}

.el-form {
  margin-top: 10px;
  font-family: "Microsoft YaHei";
}
.parallel-container {
  display: flex;
  font-family: "Microsoft YaHei";
}
.car-info {
  margin-left: 5px;
  margin-bottom: 20px;
  font-weight: bold;
  line-height: 30px;
  margin-top: 0px;
  font-size: larger;
  text-align: left;
  font-family: "Microsoft YaHei";
}

.second-title {
  line-height: 25px;
  font-weight: bold;
  margin-left: 25px;
  margin-bottom: 4px;
  font-size: 16px;
  font-family: "Microsoft YaHei";
}
.third-title {
  line-height: 25px;
  margin-left: 20px;
  margin-bottom: 0;
  font-size: 13px;
  font-family: "Microsoft YaHei";
}

.button-div {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 20px;
  font-family: "Microsoft YaHei";
}

.custom-descriptions .el-descriptions__title {
  margin-bottom: 0;
  line-height: 40px;
  font-family: "Microsoft YaHei";
}

.h1 {
  margin-left: 15px;
  margin-bottom: 20px;
  font-weight: bold;
  line-height: 30px;
  margin-top: 10px;
  font-size: large;
  text-align: left;
  font-family: "Microsoft YaHei";
  writing-mode: horizontal-tb;
}
.car-description-title {
  margin-left: 25px;
  margin-bottom: -5px;
  font-weight: bold;
  line-height: 30px;
  margin-top: 20px;
  font-size: large;
  text-align: left;
  font-family: "Microsoft YaHei";
  writing-mode: horizontal-tb;
}
.background-image {
  position: fixed;

  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  z-index: -1;
}

.background-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.center-div {
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: "Microsoft YaHei";
}
.center-row {
  justify-content: center;
  font-family: "Microsoft YaHei";
  align-items: center;
}

.left-div {
  background-color: #ffffff;
  border-radius: 30px;
  margin-right: 20px;
  padding: 10px;
  text-align: left;
}

.right-div {
  background-color: #ffffff;
  border-radius: 30px;
  padding: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  height: auto;
}

.section-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
  text-align: left;
}

.car-introduction {
  text-align: left;
  color: #666666;
}

.car-introduction-title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
  color: #000000;
}

.car-description {
  text-align: center;
}

.car-model-wrapper {
  margin-bottom: 20px;
}

.car-model {
  font-size: 30px;
  font-weight: bold;
  margin-bottom: 5px;
}

.car-model-subtitle {
  font-size: 18px;
  color: #999999;
  margin-bottom: 10px;
}

.car-info-item {
  display: flex;
  margin-bottom: 15px;
}

.car-info-label {
  font-weight: bold;
  margin-right: 10px;
}

.car-info-value {
  margin-right: 10px;
}
.button-container {
  text-align: center;
  margin-top: 20px;
}

.details-container {
  margin-top: 20px;
  height: 200px; /* 调整下方内容的高度 */
  overflow: hidden;
}

.slide-enter-active,
.slide-leave-active {
  transition: all 0.5s;
}

.slide-enter,
.slide-leave-to {
  transform: translateY(100px); /* 调整下方内容向下滑动的距离 */
}
</style>

<script>
export default {
  name: "pricepredict",
  data() {
    return {
      ptsInfo: {
        brand: "",
        model: "",
        license_time: "",
      },



      showingDetails: false,
      modelValue: [],
      modelOptions: [
        {
          value: "bmw",
          label: "宝马",
          children: [
            {
              value: "bmw i7",
              label: "宝马i7",
              children: [
                { value: "bmw 2019 m50", label: "2019 M50" },
                { value: "bmw 2022 m50", label: "2022 M50" },
              ],
            },
          ],
        },
      ],
      timeValue: [],
      timeOptions: [],
      input: "",
    };
  },
  created() {
    this.generateTimeOptions();
  },
  methods: {
    
    handleChange(value, type) {
    if (type === '车辆所在地') {
      // 省份-地点
      this.carInfo.province_name = value[0] || '';
      this.carInfo.location = value[1] || '';
    } else if (type === '品牌车系') {
      // 品牌-车系
      this.ptsInfo.brand= value[0] || '';
      this.ptsInfo.model = (value[1] + ' ' + value[2]) || '';
      // 上牌时间
    } 
    console.log("carInfo:\n");
    console.log(this.carInfo);
  },

    onSubmit(formName) {
      this.showingDetails = true;
      console.log("submit!");
      this.$nextTick(() => {
        const bottomElement = document.getElementById("bottom-element");
        if (bottomElement) {
          bottomElement.scrollIntoView({ behavior: "smooth", block: "end" });
        }
      });
    },
    handleChange2(modelValue) {
      console.log(modelValue);
    },
    generateTimeOptions() {
      const startYear = 2015;
      const endYear = 2023;

      for (let year = startYear; year <= endYear; year++) {
        const yearOption = {
          value: year.toString(),
          label: year.toString(),
          children: [],
        };

        const months = [
          "jan",
          "feb",
          "mar",
          "apr",
          "may",
          "jun",
          "jul",
          "aug",
          "sep",
          "oct",
          "nov",
          "dec",
        ];

        for (let i = 0; i < months.length; i++) {
          const monthOption = {
            value: months[i],
            label: `${i + 1}月`,
          };

          yearOption.children.push(monthOption);
        }

        this.timeOptions.push(yearOption);
      }
    },
  },
};
</script>
