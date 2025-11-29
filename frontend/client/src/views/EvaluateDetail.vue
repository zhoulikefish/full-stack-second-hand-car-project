<template>
  <el-container-e2>
    <!--导航栏-->
    <el-header class="header-align" >
		<el-header class="right-align" style="background-color: rgba(245, 246, 252, 1);" >
        <NavigationMenu
        :activeIndex="activeIndex"
        :backgroundColor="backgroundColor"
        :textColor="textColor"
        :activeTextColor="activeTextColor"
      />
      </el-header>
    </el-header>

    <el-main-e2>
      <el-row class="parallel-container">
        <el-col
          :span="15"
          style="margin-right: 80px; margin-top: 30px; margin-left: 10px"
        >
          <!--左边汽车模型-->
          <div class="section" style="display: flex; flex-direction: column;">
              <el-row class="upper-left"> 
              <div class="picture-ev2">                                                                <!--146 80-->
                <img src="../assets/BMW-Logo.png" alt="" style="position: absolute; top: 0; left: 0;margin-top:20px; width: 97px; height: 53px;">                                                
              </div>
              
              <div class="picture-ev2" style="position: relative;" >                                                          <!--283 220-->
                <img src="../assets/car-demo.png" alt="" style="margin-top:50px; width: 250px; height: 520px;">  

                <div class="price-marker" style="top: 25%; left: 50%;">
                  <span class="price-text" style="left: 145px;">{{ percent1 }}%</span>
                  <div class="circular-bg-ev2" style="display: flex; flex-direction: row;"></div>
                  <img src="../assets/component_right.png" alt="" class="right-image-ev2">
                  <h2 class="label-text" style="left: 142px; display: inline-block; white-space: nowrap;">引擎</h2>   <!--不然无法横向-->
                </div>
                
                <div class="price-marker" style="top: 40%; left: 43%;">
                  <span class="price-text" style="left: -150px;">{{ percent2 }}%</span>
                  <div class="circular-bg-ev2" style="display: flex; flex-direction: row;"></div>
                  <img src="../assets/component_left.png" alt="" class="left-image-ev2">
                  <h2 class="label-text" style="left: -157px; display: inline-block; white-space: nowrap;">驾驶辅助</h2>   <!--不然无法横向-->
                </div>

                <div class="price-marker" style="top: 75%; left: 52%;">
                  <span class="price-text" style="left: 145px;">{{ percent3 }}%</span>
                  <div class="circular-bg-ev2" style="display: flex; flex-direction: row;"></div>
                  <img src="../assets/component_right.png" alt="" class="right-image-ev2">
                  <h2 class="label-text" style="left: 142px; display: inline-block; white-space: nowrap;">车龄</h2>   <!--不然无法横向-->
                </div>
              </div>
              </el-row>
            </div>

          <!--左下1-->
          <div class="section">
            <el-row class="sub-container">
              <el-col :span="24" class="lower-left-div1">
                <h1 class="car-description-title">参考价格</h1>

                <div class="picture">
                    <p class="text-left" style="margin-left: 25vh;">{{minPredictedPrice}}万</p>
                    <p class="text-right" style="margin-right: 25vh;">{{maxPredictedPrice}}万</p>                                 
                    <img src="../assets/price2.png" alt="" style="margin-top:30px; margin-bottom:50px; width: 250px; height: 110px;">    <!--283 220-->
                     <!-- &nbsp; -->
                </div>  

                <!-- <el-form>
                  <el-form-item label="最小预测值">
                    <el-input :value="minPredictedPrice" readonly></el-input>
                  </el-form-item>
                  <el-form-item label="最大预测值">
                    <el-input :value="maxPredictedPrice" readonly></el-input>
                  </el-form-item>
                </el-form> -->
              </el-col>
            </el-row>
          </div>
        </el-col>

        <el-col :span="12" class="right-div-test" style="margin-top: 30px">
          <!-- 右上角 -->
          <!-- 筛选区域 -->
          <el-row class="sub-container">
            <el-col :span="24" class="upper-right-div-test">
              <el-form
                ref="form"
                label-position="top"
                :model="form"
                style="margin-top: 20px"
              >
                <h1 class="car-info-ev2">再估一次</h1>

                <el-col :span="24">
                  <h2 class="second-title-ev2">车辆所在地</h2>
                  <el-form-item
                    style="
                      line-height: 20px;
                      margin-top: 10px;
                      margin-left: 25px;
                    "
                  >
                    <el-cascader
                      v-model="locationValue_e2"
                      :options="locationOptions"
                      @change="handleChange1"
                    ></el-cascader>
                  </el-form-item>

                  <h2 class="second-title-ev2" style="margin-top: 10px">
                    车辆颜色
                  </h2>
                  <el-form-item
                    style="
                      line-height: 20px;
                      margin-top: 10px;
                      margin-left: 25px;
                    "
                  >
                    <el-cascader
                      v-model="colorValue_e2"
                      :options="colorOptions"
                      @change="handleChange3"
                    ></el-cascader>
                  </el-form-item>

                  <h2 class="second-title-ev2">行驶里程</h2>
                  <el-form-item
                    style="
                      line-height: 20px;
                      margin-top: 10px;
                      margin-left: 25px;
                      max-width: 223px;
                    "
                  >
                    <el-input
                      placeholder="万公里"
                      v-model="inputmiles_e2"
                      type="number"
                    ></el-input>
                  </el-form-item>
                </el-col>
              </el-form>

              <el-form
                ref="form"
                label-position="top"
                :model="form"
                style="margin-top: 15px; margin-left: 30px"
              >
                <h1 class="car-info-ev2">&nbsp;</h1>


                <el-col :span="24">
                  <h2 class="second-title-ev2" style="margin-top: 5px;">车辆种类</h2>
                  <el-form-item
                    style="
                      line-height: 20px;
                      margin-top: 10px;
                      margin-left: 25px;
                    "
                  >
                    <el-cascader
                      v-model="modelValue_e2"
                      :options="modelOptions"
                      @change="handleChange2"
                    ></el-cascader>
                  </el-form-item>

                  <h2 class="second-title-ev2">上牌时间</h2>
                  <el-form-item
                    style="
                      line-height: 20px;
                      margin-top: 10px;
                      margin-left: 25px;
                    "
                  >
                    <el-date-picker
                      v-model="timeValue_e2"
                      type="month"
                      value-format="yyyy-MM"
                      placeholder="选择月份"
                      class="date-picker-ev2"
                    ></el-date-picker>
                  </el-form-item>

                  <h2 class="second-title-ev2">转手次数</h2>
                  <el-form-item
                    style="
                      line-height: 20px;
                      margin-top: 10px;
                      margin-left: 25px;
                      max-width: 205px;
                    "
                  >
                    <el-input
                      placeholder="次"
                      v-model="inputtime_e2"
                      :rules="rules"
                      type="number"
                    ></el-input>
                  </el-form-item>

                  <el-form-item>
                    <el-button
                      @click="onSubmitAgain"
                      style="
                        background-color: #3563e9;
                        color: #ffffff;
                        width: 160px;
                        margin-top: 30px;
                        margin-left: -80px;
                      "
                      >估价
                    </el-button>
                  </el-form-item>
                </el-col>
              </el-form>
            </el-col>
          </el-row>

          <el-row class="sub-container">
            <!-- 右下角 -->

            <el-col :span="24" class="lower-right-div" style="margin-top: 20px">
              <h1 class="classic-refer-ev2">经典车型参考</h1>

              <!-- 信息部分 -->
              <div class="recent-transaction-container" style="margin-bottom: 30px;" @click="jump(selectedData[0].car_name, 0)"> 
                <div class="frame" >
                  <img :src="remainingCars[0]" alt="" style="width: 120px; height: 90px;"> 
                </div>
                <div>
                  <h2 class="recent-transaction-car-model">{{selectedData[0].car_name}}</h2> 
                  <h3 class="recent-transaction-car-model-subtitle">{{selectedData[0].model}}</h3>
                </div>
              </div>

              <el-divider class="divider"></el-divider>
              <div class="recent-transaction-container" @click="jump(selectedData[1].car_name, 1)">
                <div class="frame">
                  <img
                    :src="remainingCars[1]"
                    alt=""
                    style="width: 120px; height: 90px"
                  />
                </div>
                <div>
                  <h2 class="recent-transaction-car-model">{{selectedData[1].car_name}}</h2>
                  <h3 class="recent-transaction-car-model-subtitle">{{selectedData[1].model}}</h3>
                </div>
              </div>

              <el-divider class="divider"></el-divider>
              <div
                class="recent-transaction-container"
                style="margin-bottom: 30px" @click="jump(selectedData[2].car_name, 2)"
              >
                <div class="frame" @click="jump(selectedData[2].car_name)">
                  <img
                    :src="remainingCars[2]"
                    alt=""
                    style="width: 120px; height: 90px"
                  />
                </div>
                <div>
                  <h2 class="recent-transaction-car-model">{{selectedData[2].car_name}}</h2>
                  <h3 class="recent-transaction-car-model-subtitle">{{selectedData[2].model}}</h3>
                </div>
              </div>
            </el-col>
          </el-row>
        </el-col>
      </el-row>
    </el-main-e2>
  </el-container-e2>
</template>

<style>
.text-left {
  position: absolute;
  top: 50%;
  left: 0;
  transform: translateY(-50%);
  margin: 0;
  font-weight: bold;
  font-size: 18px;
}

.text-right {
  position: absolute;
  top: 50%;
  right: 0;
  transform: translateY(-50%);
  margin: 0;
  font-weight: bold;
  font-size: 18px;
}

.text-center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  margin: 0;
  font-weight: bold;
  font-size: 18px;
}
/* 顶部导航 */
.header-align {
  display: flex;
  justify-content: flex-end;
}

.navigation .el-menu-item,
.el-menu-item a {
  font-family: "Microsoft YaHei";
  font-size: 16px;
  font-weight: bold;
  text-decoration: none;
}

/* 底部block */
el-container-e2 {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.el-header {
  /* background-color: #F6F7F9; */
  color: #333;
  line-height: 60px;
}

.el-main-e2 {
  /* background-color: #F6F7F9; */
  color: #333;
  text-align: center;
  line-height: 160px;
  min-height: 100vh; /* 百分百铺满 */
  /* filter: grayscale(1%); /* 将背景图像完全转换为灰度 *
  opacity: 0.5; 设置透明度为50% */
}

/* 表格 - 左下 */

.section {
  margin-bottom: 20px;
  position: relative;
}
.el-table {
  padding-left: 20px;
  padding-top: 10px;
}
.el-table__header th {
  line-height: 20px;
  font-size: 14px;
  font-weight: bold;
  text-align: center; /* 与其他地方冲突，只有important才能生效 */
}
.el-table__body td[data-column="refer_price"] {
  color: orange !important;
}

/* 框内字体细节 - 左侧 */
.el-descriptions {
  margin-left: 25px;
  margin-bottom: 15px;
  margin-top: 20px;
}
.right-align {
  display: flex;
  justify-content: flex-end;
}

.car-info-ev2 {
  margin-left: 25px;
  margin-bottom: 15px;
  font-weight: bold;
  line-height: 30px;
  margin-top: 20px;
  font-size: 22px;
  text-align: left;
}
.date-picker-ev2 {
  max-width: 205px;
}
.second-title-ev2 {
    font-weight: bold;
    margin-left: 25px;
    margin-bottom: 8px;
    font-size: 16px;
  }

.third-title {
  line-height: 30px;
  margin-left: 25px;
  margin-bottom: 0;
}
.custom-descriptions .el-descriptions__title {
  margin-bottom: 0;
  line-height: 40px;
}

.car-description-container {
  display: flex;
  align-items: center;
}

/* 估价属性组*/
.picture-ev2 {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.price-marker {
  position: absolute;
  width: 20px;
  height: 20px;
  text-align: center;

}
  .circular-bg-ev2 {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url("../assets/circular.png");
    background-size: cover;
  }
.price-text {
  position: absolute;
  font-weight: bold;
  top: -110%;
  left: 60%;
  transform: translate(-50%, -50%);
  color: #0a0a0a;
  font-size: 18px;
  line-height: 20px;
  margin-bottom: -20px;
}

.label-text {
  position: absolute;
  font-weight: bold;
  top: 45%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-size: 16px;
  line-height: 20px;
  margin-bottom: -20px;
}

.right-image-ev2 {
  position: absolute;
  top: 50%;
  left: 470%;
  transform: translate(-50%, -50%);
  min-width: 150px;
  min-height: 35px;
  
}

.left-image-ev2 {
  position: absolute;
  top: 50%;
  left: -510%;
  transform: translate(-50%, -50%);
  min-width: 210px;
  min-height: 35px;
}

/* 框内字体细节 - 右上角 */
.blue-frame {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80px;
  width: 160px;
  background-color: #3563e9;
  border-radius: 10px;

  margin-left: 20px;
  margin-top: 20px;
}
.blue-frame img {
  max-width: 100%;
  max-height: 100%;
}

.frame {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80px;
  width: 160px;
  border-radius: 10px;
  margin-left: 20px;
  margin-top: 20px;
}

.car-description-title {
  margin-left: 25px;
  margin-bottom: -5px;
  font-weight: bold;
  line-height: 30px;
  margin-top: 20px;
  font-size: large;
  text-align: left;
}
.car-model {
  margin-left: 15px;
  font-weight: bold;
  line-height: 30px;
  margin-top: 20px;
}

.car-model-subtitle {
  font-size: small;
  font-weight: bold;
  line-height: 40px;
  text-align: left;
  margin-left: 15px;
  color: #3d5278;
}

/* 框内字体细节 - 右下角 */
.recent-transaction-container {
  display: flex;
  align-items: center;
  height: 60px;
}
.classic-refer-ev2 {
  margin-left: 25px;
  font-weight: bold;
  line-height: 30px;
  margin-top: 20px;
  margin-bottom: 20px;
  font-size: large;
  text-align: left;

}
.recent-transaction-car-model {
  font-size: medium;
  margin-left: 15px;
  font-weight: bold;
  line-height: 30px;
  margin-top: 20px;
}
.recent-transaction-car-model-subtitle {
  font-size: small;
  margin-left: 15px;
  line-height: 30px;
  text-align: left;
  color: #90a3bf;
}
.recent-transaction-date {
  font-size: small;
  line-height: 30px;
  text-align: right;
  margin-top: 20px;
  margin-left: 25px;
  color: #90a3bf;
}
.recent-transaction-price {
  font-size: medium;
  line-height: 30px;
  text-align: right;
  font-weight: bold;
  margin-left: 25px;
}

.divider {
  margin: 0px;
}

.parallel-container {
  display: flex;
}

.left-div {
  background-color: #ffffff;
  border-radius: 30px;
  margin-right: 20px;
  flex: 2;

  padding-top: 20px;

  padding-left: 15px;
  padding-right: 15px;
  /* height: 80vh;  卡片长 */
}

.lower-left-div1 {
  min-height: 150px;
  background-color: #ffffff;
  border-radius: 30px;
  margin-top: 20px;
  margin-bottom: 10px;
  padding-bottom: 20px;
}

.upper-left {
  min-height: 150px;
  background-color: #ffffff;
  border-radius: 30px;
  margin-bottom: 10px;
  margin-left: 10px;
  padding-bottom: 20px;
}

.upper-right-div-test {
  background-color: #ffffff;
  border-radius: 30px;

  text-align: left;
  min-height: 150px;
  margin-bottom: 10px;

  padding-left: 5px;
  padding-right: 20px;

  display: flex;
}

.lower-right-div {
  min-height: 400px;
  background-color: #ffffff;
  border-radius: 30px;
  margin-bottom: 10px;
}
.right-div-test {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: auto;
}

.sub-container {
  margin-bottom: 10px;
}
</style>

<script>
import NavigationMenu from "@/components/NavigationMenu.vue";
export default {
  name: "evaluatedetail",
  props: [
    "locationValue",
    "modelValue",
    "colorValue",
    "timeValue",
    "inputMiles",
    "inputTime",
  ],
  components: {
    NavigationMenu,
  },
  data() {
    return {
      percent1: 0,
      percent2: 0,
      percent3: 0,
      randomImageUrls: [],
      remainingCars: [],
      minPredictedPrice: 0,
      maxPredictedPrice: 0,
      selectedData: [],
      activeIndex: "4",
      locationValue_e2: [],
      locationOptions: [
        {
          value: "anhui",
          label: "安徽",
          children: [
            { value: "hefei", label: "合肥" },
            { value: "wuhu", label: "芜湖" },
            { value: "bangbu", label: "蚌埠" },
            { value: "huainan", label: "淮南" },
            { value: "maanshan", label: "马鞍山" },
            { value: "huaibei", label: "淮北" },
            { value: "tongling", label: "铜陵" },
            { value: "anqing", label: "安庆" },
            { value: "huangshan", label: "黄山" },
            { value: "chuzhou", label: "滁州" },
            { value: "fuyang", label: "阜阳" },
            { value: "suzhou", label: "宿州" },
            { value: "liuan", label: "六安" },
            { value: "bozhou", label: "亳州" },
            { value: "chizhou", label: "池州" },
            { value: "xuancheng", label: "宣城" },
          ],
        },
        {
          value: "beijing",
          label: "北京",
          children: [{ value: "beijing", label: "北京" }],
        },
        {
          value: "chongqing",
          label: "重庆",
          children: [{ value: "chongqing", label: "重庆" }],
        },
        {
          value: "fujian",
          label: "福建",
          children: [
            { value: "fuzhou", label: "福州" },
            { value: "xiamen", label: "厦门" },
            { value: "putian", label: "莆田" },
            { value: "sanming", label: "三明" },
            { value: "quanzhou", label: "泉州" },
            { value: "zhangzhou", label: "漳州" },
            { value: "nanping", label: "南平" },
            { value: "longyan", label: "龙岩" },
            { value: "ningde", label: "宁德" },
          ],
        },
        {
          value: "guangdong",
          label: "广东",
          children: [
            { value: "guangzhou", label: "广州" },
            { value: "shaoguan", label: "韶关" },
            { value: "shenzhen", label: "深圳" },
            { value: "zhuhai", label: "珠海" },
            { value: "shantou", label: "汕头" },
            { value: "foshan", label: "佛山" },
            { value: "jiangmen", label: "江门" },
            { value: "zhanjiang", label: "湛江" },
            { value: "maoming", label: "茂名" },
            { value: "zhaoqing", label: "肇庆" },
            { value: "huizhou", label: "惠州" },
            { value: "meizhou", label: "梅州" },
            { value: "shanwei", label: "汕尾" },
            { value: "heyuan", label: "河源" },
            { value: "yangjiang", label: "阳江" },
            { value: "qingyuan", label: "清远" },
            { value: "dongguan", label: "东莞" },
            { value: "zhongshan", label: "中山" },
            { value: "chaozhou", label: "潮州" },
            { value: "jieyang", label: "揭阳" },
            { value: "yunfu", label: "云浮" },
          ],
        },
        {
          value: "guangxi",
          label: "广西",
          children: [
            { value: "nanning", label: "南宁" },
            { value: "liuzhou", label: "柳州" },
            { value: "guilin", label: "桂林" },
            { value: "wuzhou", label: "梧州" },
            { value: "beihai", label: "北海" },
            { value: "fangchenggang", label: "防城港" },
            { value: "qinzhou", label: "钦州" },
            { value: "guigang", label: "贵港" },
            { value: "yu_lin", label: "玉林" },
            { value: "baise", label: "百色" },
            { value: "hezhou", label: "贺州" },
            { value: "hechi", label: "河池" },
            { value: "laibin", label: "来宾" },
            { value: "chongzuo", label: "崇左" },
          ],
        },
        {
          value: "guizhou",
          label: "贵州",
          children: [
            { value: "guiyang", label: "贵阳" },
            { value: "liupanshui", label: "六盘水" },
            { value: "zunyi", label: "遵义" },
            { value: "anshun", label: "安顺" },
            { value: "bijie", label: "毕节" },
            { value: "tongren", label: "铜仁" },
            { value: "qianxinan", label: "黔西南" },
            { value: "qiandongnan", label: "黔东南" },
            { value: "qiannan", label: "黔南" },
          ],
        },
        {
          value: "gansu",
          label: "甘肃",
          children: [
            { value: "lanzhou", label: "兰州" },
            { value: "jiayuguan", label: "嘉峪关" },
            { value: "jinchang", label: "金昌" },
            { value: "baiyin", label: "白银" },
            { value: "tianshui", label: "天水" },
            { value: "wuwei", label: "武威" },
            { value: "zhangye", label: "张掖" },
            { value: "pingliang", label: "平凉" },
            { value: "jiuquan", label: "酒泉" },
            { value: "qingyang", label: "庆阳" },
            { value: "dingxi", label: "定西" },
            { value: "longnan", label: "陇南" },
            { value: "linxia", label: "临夏" },
            { value: "gannan", label: "甘南" },
          ],
        },
        {
          value: "hainan",
          label: "海南",
          children: [
            { value: "haikou", label: "海口" },
            { value: "sanya", label: "三亚" },
            { value: "sansha", label: "三沙" },
            { value: "danzhou", label: "儋州" },
            { value: "wuzhishan", label: "五指山" },
            { value: "qionghai", label: "琼海" },
            { value: "wenchang", label: "文昌" },
            { value: "wanning", label: "万宁" },
            { value: "dongfang", label: "东方" },
            { value: "dingan", label: "定安" },
            { value: "tunchang", label: "屯昌" },
            { value: "chengmai", label: "澄迈" },
            { value: "lingao", label: "临高" },
            { value: "baisha", label: "白沙" },
            { value: "changjiang", label: "昌江" },
            { value: "ledong", label: "乐东" },
            { value: "lingshui", label: "陵水" },
            { value: "baoting", label: "保亭" },
            { value: "qiongzhong", label: "琼中" },
          ],
        },
        {
          value: "henan",
          label: "河南",
          children: [
            { value: "zhengzhou", label: "郑州" },
            { value: "kaifeng", label: "开封" },
            { value: "luoyang", label: "洛阳" },
            { value: "pingdingshan", label: "平顶山" },
            { value: "anyang", label: "安阳" },
            { value: "hebi", label: "鹤壁" },
            { value: "xinxiang", label: "新乡" },
            { value: "jiaozuo", label: "焦作" },
            { value: "puyang", label: "濮阳" },
            { value: "xuchang", label: "许昌" },
            { value: "luohe", label: "漯河" },
            { value: "sanmenxia", label: "三门峡" },
            { value: "nanyang", label: "南阳" },
            { value: "shangqiu", label: "商丘" },
            { value: "xinyang", label: "信阳" },
            { value: "zhoukou", label: "周口" },
            { value: "zhumadian", label: "驻马店" },
            { value: "jiyuan", label: "济源" },
          ],
        },
        {
          value: "hubei",
          label: "湖北",
          children: [
            { value: "wuhan", label: "武汉" },
            { value: "huangshi", label: "黄石" },
            { value: "shiyan", label: "十堰" },
            { value: "yichang", label: "宜昌" },
            { value: "xiangyang", label: "襄阳" },
            { value: "ezhou", label: "鄂州" },
            { value: "jingmen", label: "荆门" },
            { value: "xiaogan", label: "孝感" },
            { value: "jingzhou", label: "荆州" },
            { value: "huanggang", label: "黄冈" },
            { value: "xianning", label: "咸宁" },
            { value: "suizhou", label: "随州" },
            { value: "enshi", label: "恩施" },
            { value: "xiantao", label: "仙桃" },
            { value: "qianjiang", label: "潜江" },
            { value: "tianmen", label: "天门" },
            { value: "shennongjia", label: "神农架" },
          ],
        },
        {
          value: "hunan",
          label: "湖南",
          children: [
            { value: "changsha", label: "长沙" },
            { value: "zhuzhou", label: "株洲" },
            { value: "xiangtan", label: "湘潭" },
            { value: "hengyang", label: "衡阳" },
            { value: "shaoyang", label: "邵阳" },
            { value: "yueyang", label: "岳阳" },
            { value: "changde", label: "常德" },
            { value: "zhangjiajie", label: "张家界" },
            { value: "yiyang", label: "益阳" },
            { value: "chenzhou", label: "郴州" },
            { value: "yongzhou", label: "永州" },
            { value: "huaihua", label: "怀化" },
            { value: "loudi", label: "娄底" },
            { value: "xiangxi", label: "湘西" },
          ],
        },
        {
          value: "hebei",
          label: "河北",
          children: [
            { value: "shijiazhuang", label: "石家庄" },
            { value: "tangshan", label: "唐山" },
            { value: "qinhuangdao", label: "秦皇岛" },
            { value: "handan", label: "邯郸" },
            { value: "xingtai", label: "邢台" },
            { value: "baoding", label: "保定" },
            { value: "zhangjiakou", label: "张家口" },
            { value: "chengde", label: "承德" },
            { value: "cangzhou", label: "沧州" },
            { value: "langfang", label: "廊坊" },
            { value: "hengshui", label: "衡水" },
          ],
        },
        {
          value: "heilongjiang",
          label: "黑龙江",
          children: [
            { value: "haerbin", label: "哈尔滨" },
            { value: "qiqihaer", label: "齐齐哈尔" },
            { value: "jixi", label: "鸡西" },
            { value: "hegang", label: "鹤岗" },
            { value: "shuangyashan", label: "双鸭山" },
            { value: "daqing", label: "大庆" },
            { value: "yichun", label: "伊春" },
            { value: "jiamusi", label: "佳木斯" },
            { value: "qitaihe", label: "七台河" },
            { value: "mudanjiang", label: "牡丹江" },
            { value: "heihe", label: "黑河" },
            { value: "suihua", label: "绥化" },
            { value: "daxinganling", label: "大兴安岭" },
          ],
        },
        {
          value: "jiangsu",
          label: "江苏",
          children: [
            { value: "nanjing", label: "南京" },
            { value: "wuxi", label: "无锡" },
            { value: "xuzhou", label: "徐州" },
            { value: "changzhou", label: "常州" },
            { value: "suzhou", label: "苏州" },
            { value: "nantong", label: "南通" },
            { value: "lianyungang", label: "连云港" },
            { value: "huaian", label: "淮安" },
            { value: "yancheng", label: "盐城" },
            { value: "yangzhou", label: "扬州" },
            { value: "zhenjiang", label: "镇江" },
            { value: "tai_zhou", label: "泰州" },
            { value: "suqian", label: "宿迁" },
          ],
        },
        {
          value: "jiangxi",
          label: "江西",
          children: [
            { value: "nanchang", label: "南昌" },
            { value: "jingdezhen", label: "景德镇" },
            { value: "ping_xiang", label: "萍乡" },
            { value: "jiujiang", label: "九江" },
            { value: "xinyu", label: "新余" },
            { value: "yingtan", label: "鹰潭" },
            { value: "ganzhou", label: "赣州" },
            { value: "jian", label: "吉安" },
            { value: "yi_chun", label: "宜春" },
            { value: "fu_zhou", label: "抚州" },
            { value: "shangrao", label: "上饶" },
          ],
        },
        {
          value: "jilin",
          label: "吉林",
          children: [
            { value: "changchun", label: "长春" },
            { value: "jilinshi", label: "吉林" },
            { value: "siping", label: "四平" },
            { value: "liaoyuan", label: "辽源" },
            { value: "tonghua", label: "通化" },
            { value: "baishan", label: "白山" },
            { value: "songyuan", label: "松原" },
            { value: "baicheng", label: "白城" },
            { value: "yanbian", label: "延边" },
          ],
        },
        {
          value: "liaoning",
          label: "辽宁",
          children: [
            { value: "shenyang", label: "沈阳" },
            { value: "dalian", label: "大连" },
            { value: "anshan", label: "鞍山" },
            { value: "fushun", label: "抚顺" },
            { value: "benxi", label: "本溪" },
            { value: "dandong", label: "丹东" },
            { value: "jinzhou", label: "锦州" },
            { value: "yingkou", label: "营口" },
            { value: "fuxin", label: "阜新" },
            { value: "liaoyang", label: "辽阳" },
            { value: "panjin", label: "盘锦" },
            { value: "tieling", label: "铁岭" },
            { value: "chaoyang", label: "朝阳" },
            { value: "huludao", label: "葫芦岛" },
          ],
        },
        {
          value: "neimenggu",
          label: "内蒙古",
          children: [
            { value: "huhehaote", label: "呼和浩特" },
            { value: "baotou", label: "包头" },
            { value: "wuhai", label: "乌海" },
            { value: "chifeng", label: "赤峰" },
            { value: "tongliao", label: "通辽" },
            { value: "eerduosi", label: "鄂尔多斯" },
            { value: "hulunbeier", label: "呼伦贝尔" },
            { value: "bayannaoer", label: "巴彦淖尔" },
            { value: "wulanchabu", label: "乌兰察布" },
            { value: "xinganmeng", label: "兴安盟" },
            { value: "xilinguolemeng", label: "锡林郭勒盟" },
            { value: "alashanmeng", label: "阿拉善盟" },
          ],
        },
        {
          value: "ningxia",
          label: "宁夏",
          children: [
            { value: "yinchuan", label: "银川" },
            { value: "shizuishan", label: "石嘴山" },
            { value: "wuzhong", label: "吴忠" },
            { value: "guyuan", label: "固原" },
            { value: "zhongwei", label: "中卫" },
          ],
        },
        {
          value: "qinghai",
          label: "青海",
          children: [
            { value: "xining", label: "西宁" },
            { value: "haidong", label: "海东" },
            { value: "haibei", label: "海北" },
            { value: "huangnan", label: "黄南" },
            { value: "hai_nan", label: "海南" },
            { value: "guoluo", label: "果洛" },
            { value: "yushu", label: "玉树" },
            { value: "haixi", label: "海西" },
          ],
        },
        {
          value: "shanxi",
          label: "陕西",
          children: [
            { value: "xian", label: "西安" },
            { value: "tongchuan", label: "铜川" },
            { value: "baoji", label: "宝鸡" },
            { value: "xianyang", label: "咸阳" },
            { value: "weinan", label: "渭南" },
            { value: "yanan", label: "延安" },
            { value: "hanzhong", label: "汉中" },
            { value: "yulin", label: "榆林" },
            { value: "ankang", label: "安康" },
            { value: "shangluo", label: "商洛" },
            { value: "xixianxinqu", label: "西咸新区" },
          ],
        },
        {
          value: "sichuan",
          label: "四川",
          children: [
            { value: "chengdu", label: "成都" },
            { value: "zigong", label: "自贡" },
            { value: "panzhihua", label: "攀枝花" },
            { value: "luzhou", label: "泸州" },
            { value: "deyang", label: "德阳" },
            { value: "mianyang", label: "绵阳" },
            { value: "guangyuan", label: "广元" },
            { value: "suining", label: "遂宁" },
            { value: "neijiang", label: "内江" },
            { value: "leshan", label: "乐山" },
            { value: "nanchong", label: "南充" },
            { value: "meishan", label: "眉山" },
            { value: "yibin", label: "宜宾" },
            { value: "guangan", label: "广安" },
            { value: "dazhou", label: "达州" },
            { value: "yaan", label: "雅安" },
            { value: "bazhong", label: "巴中" },
            { value: "ziyang", label: "资阳" },
            { value: "aba", label: "阿坝" },
            { value: "ganzi", label: "甘孜" },
            { value: "liangshan", label: "凉山" },
          ],
        },
        {
          value: "shanghai",
          label: "上海",
          children: [{ value: "shanghai", label: "上海" }],
        },
        {
          value: "shanxi",
          label: "山西",
          children: [
            { value: "taiyuan", label: "太原" },
            { value: "datong", label: "大同" },
            { value: "yangquan", label: "阳泉" },
            { value: "zhangzhi", label: "长治" },
            { value: "jincheng", label: "晋城" },
            { value: "shuozhou", label: "朔州" },
            { value: "jinzhong", label: "晋中" },
            { value: "yuncheng", label: "运城" },
            { value: "xinzhou", label: "忻州" },
            { value: "linfen", label: "临汾" },
            { value: "lvliang", label: "吕梁" },
          ],
        },
        {
          value: "shandong",
          label: "山东",
          children: [
            { value: "jinan", label: "济南" },
            { value: "qingdao", label: "青岛" },
            { value: "zibo", label: "淄博" },
            { value: "zaozhuang", label: "枣庄" },
            { value: "dongying", label: "东营" },
            { value: "yantai", label: "烟台" },
            { value: "weifang", label: "潍坊" },
            { value: "jining", label: "济宁" },
            { value: "taian", label: "泰安" },
            { value: "weihai", label: "威海" },
            { value: "rizhao", label: "日照" },
            { value: "laiwu", label: "莱芜" },
            { value: "linyi", label: "临沂" },
            { value: "dezhou", label: "德州" },
            { value: "liaocheng", label: "聊城" },
            { value: "binzhou", label: "滨州" },
            { value: "heze", label: "菏泽" },
          ],
        },
        {
          value: "tianjin",
          label: "天津",
          children: [{ value: "tianjin", label: "天津" }],
        },
        {
          value: "xinjiang",
          label: "新疆",
          children: [
            { value: "wulumuqi", label: "乌鲁木齐" },
            { value: "kelamayi", label: "克拉玛依" },
            { value: "turpan", label: "吐鲁番" },
            { value: "hami", label: "哈密" },
            { value: "changji", label: "昌吉" },
            { value: "boertala", label: "博尔塔拉" },
            { value: "bayinguoleng", label: "巴音郭楞" },
            { value: "akesu", label: "阿克苏" },
            { value: "kezilesu", label: "克孜勒苏" },
            { value: "kashen", label: "喀什" },
            { value: "hetian", label: "和田" },
            { value: "yili", label: "伊犁" },
            { value: "tacheng", label: "塔城" },
            { value: "aletai", label: "阿勒泰" },
            { value: "shihezi", label: "石河子" },
            { value: "aral", label: "阿拉尔" },
            { value: "tumxuk", label: "图木舒克" },
            { value: "wujiaqu", label: "五家渠" },
            { value: "beitun", label: "北屯" },
            { value: "tiemenguan", label: "铁门关" },
            { value: "shuanghe", label: "双河" },
            { value: "kokdala", label: "可克达拉" },
            { value: "kunyu", label: "昆玉" },
          ],
        },
        {
          value: "xizang",
          label: "西藏",
          children: [
            { value: "lasa", label: "拉萨" },
            { value: "rikaze", label: "日喀则" },
            { value: "qamdo", label: "昌都" },
            { value: "nyingchi", label: "林芝" },
            { value: "shannan", label: "山南" },
            { value: "naqu", label: "那曲" },
            { value: "ali", label: "阿里" },
          ],
        },
        {
          value: "yunnan",
          label: "云南",
          children: [
            { value: "kunming", label: "昆明" },
            { value: "qujing", label: "曲靖" },
            { value: "yuxi", label: "玉溪" },
            { value: "baoshan", label: "保山" },
            { value: "zhaotong", label: "昭通" },
            { value: "lijiang", label: "丽江" },
            { value: "puer", label: "普洱" },
            { value: "lincang", label: "临沧" },
            { value: "chuxiong", label: "楚雄" },
            { value: "honghe", label: "红河" },
            { value: "wenshan", label: "文山" },
            { value: "xishuangbanna", label: "西双版纳" },
            { value: "dali", label: "大理" },
            { value: "dehong", label: "德宏" },
            { value: "nujiang", label: "怒江" },
            { value: "diqing", label: "迪庆" },
          ],
        },
        {
          value: "zhejiang",
          label: "浙江",
          children: [
            { value: "hangzhou", label: "杭州" },
            { value: "ningbo", label: "宁波" },
            { value: "wenzhou", label: "温州" },
            { value: "jiaxing", label: "嘉兴" },
            { value: "huzhou", label: "湖州" },
            { value: "shaoxing", label: "绍兴" },
            { value: "jinhua", label: "金华" },
            { value: "quzhou", label: "衢州" },
            { value: "zhoushan", label: "舟山" },
            { value: "taizhou", label: "台州" },
            { value: "lishui", label: "丽水" },
            { value: "zhoushanxinqu", label: "舟山群岛新区" },
          ],
        },
      ],
      modelValue_e2: [],
      modelOptions: [
        {
          value: 'bmw',
          label: '宝马',
          children: [{
            value: 'bmw 1系',
            label: '宝马1系',
            children: [
              { value: '2017 118i 设计套装型', label: '2017款 118i 设计套装型' },
              { value: '2017 118i 时尚型', label: '2017款 118i 时尚型' },
              { value: '2017 118i 运动型', label: '2017款 118i 运动型' },
              { value: '2017 120i 设计套装型', label: '2017款 120i 设计套装型' },
              { value: '2017 125i 运动型', label: '2017款 125i 运动型' },
              { value: '2018 118i 设计套装型', label: '2018款 118i 设计套装型' },
              { value: '2018 118i 时尚型', label: '2018款 118i 时尚型' },
              { value: '2018 118i 运动型', label: '2018款 118i 运动型' },
              { value: '2018 120i 设计套装型', label: '2018款 120i 设计套装型' },
              { value: '2018 改款 118i 运动型', label: '2018款 改款 118i 运动型' },
            ]
          }, {
            value: 'bmw 2系',
            label: '宝马2系',
            children: [
              { value: '2014款 220i 领先型', label: '2014款 220i 领先型2014款 220i 领先型' },
              { value: '2014款 220i 运动设计套装', label: '2014款 220i 运动设计套装' },
              { value: '2014款 M235i', label: '2014款 M235i' },
              { value: '2015款 218i', label: '2015款 218i' },
              { value: '2015款 218i 敞篷轿跑车', label: '2015款 218i 敞篷轿跑车' },
              { value: '2017款 220i 敞篷轿跑车 领先型', label: '2017款 220i 敞篷轿跑车 领先型' },
              { value: '2017款 220i 领先型', label: '2017款 220i 领先型' },
              { value: '2018款 220i 敞篷轿跑车 运动设计套装', label: '2018款 220i 敞篷轿跑车 运动设计套装' },
            ]
          }, {
            value: 'bmw 3系',
            label: '宝马3系',
            children: [
              { value: '2004款 318i', label: '2004款 318i' },
              { value: '2004款 318i', label: '2004款 318i' },
              { value: '2005款 320i 领先型', label: '2005款 320i 领先型' },
              { value: '2005款 320i 时尚型木内饰', label: '2005款 320i 时尚型木内饰' },
              { value: '2023款 330Li M运动曜夜套装', label: '2023款 330Li M运动曜夜套装' },
              { value: '2023款 325Li xDrive M运动套装', label: '2023款 325Li xDrive M运动套装' },
              { value: '2022款 325Li M运动曜夜套装', label: '2022款 325Li M运动曜夜套装' },
            ]
          }, {
            value: 'bmw 4系',
            label: '宝马4系',
            children: [
              { value: '2014款 420i Gran Coupe 时尚型', label: '2014款 420i Gran Coupe 时尚型' },
              { value: '2014款 420i 敞篷风尚设计套装', label: '2014款 420i 敞篷风尚设计套装' },
              { value: '2015款 428i 敞篷限量版', label: '2015款 428i 敞篷限量版' },
              { value: '2016款 420i Gran Coupe M运动型', label: '2016款 420i Gran Coupe M运动型' },
              { value: '2016款 420i 敞篷设计套装型', label: '2016款 420i 敞篷设计套装型' },
              { value: '2022款 430i 敞篷M运动曜夜套装', label: '2022款 430i 敞篷M运动曜夜套装' },
              { value: '2023款 430i M运动曜夜套装', label: '2023款 430i M运动曜夜套装' },
            ]
          }]
        },
        {
          value: 'benchi',
          label: '奔驰',
          children: [{
            value: '奔驰B级',
            label: '奔驰B级',
            children: [
              { value: '2009款 B 200 动感型', label: '2009款 B 200 动感型' },
              { value: '2012款 B 180', label: '2012款 B 180' },
              { value: '2013款 B 260', label: '2013款 B 260' },
              { value: '2015款 B 200 动感型', label: '2015款 B 200 动感型' },
              { value: '2016款 B 180', label: '2016款 B 180' },
              { value: '2020款 B 180', label: '2020款 B 180' },
            ]
          }, {
            value: '奔驰CLA',
            label: '奔驰CLA',
            children: [
              { value: '2014款 CLA 260 4MATIC', label: '2014款 CLA 260 4MATIC' },
              { value: '2015款 CLA 200', label: '2015款 CLA 200' },
              { value: '2016款 CLA 200 动感型', label: '2016款 CLA 200 动感型' },
              { value: '2017款 CLA 180', label: '2017款 CLA 180' },
              { value: '2018款 CLA 180', label: '2018款 CLA 180' },
              { value: '2019款 CLA 200 暗夜特别版', label: '2019款 CLA 200 暗夜特别版' },
              { value: '2020款 CLA 200', label: '2020款 CLA 200' },
              { value: '2021款 CLA 200', label: '2021款 CLA 200' },
            ]
          }, {
            value: '奔驰C级',
            label: '奔驰C级',
            children: [
              { value: '2008款 C 200K 标准型', label: '2008款 C 200K 标准型' },
              { value: '2010款 C 180K 经典型', label: '2010款 C 180K 经典型' },
              { value: '2011款 C 180K 经典型', label: '2011款 C 180K 经典型' },
              { value: '2013款 C 180 CGI 经典型', label: '2013款 C 180 CGI 经典型' },
              { value: '2015款 C 180 L 运动型', label: '2015款 C 180 L 运动型' },
              { value: '2023款 C 200 L 运动型', label: '2023款 C 200 L 运动型' },
            ]
          }]
        },
        {
          value: 'aodi',
          label: '奥迪',
          children: [{
            value: '奥迪A1',
            label: '奥迪A1',
            children: [
              { value: '2012款 1.4 TFSI Ego', label: '2012款 1.4 TFSI Ego' },
              { value: '2013款 30 TFSI Sportback Ego', label: '2013款 30 TFSI Sportback Ego' },
              { value: '2014款 30 TFSI Sportback时尚型', label: '2014款 30 TFSI Sportback时尚型' },
              { value: '2016款 30 TFSI Sportback Design风尚版', label: '2016款 30 TFSI Sportback Design风尚版' },
              { value: '2018款 30 TFSI 限量典藏版', label: '2018款 30 TFSI 限量典藏版' },
              { value: '2020款 B 180', label: '2020款 B 180' }]
          },
          {
            value: '奥迪A3',
            label: '奥迪A3',
            children: [
              { value: '2014款 Limousine 35 TFSI 自动豪华型', label: '2014款 Limousine 35 TFSI 自动豪华型' },
              { value: '2015款 Limousine 35 TFSI 百万纪念舒享型', label: '2015款 Limousine 35 TFSI 百万纪念舒享型' },
              { value: '2016款 Limousine 35 TFSI 进取型', label: '2016款 Limousine 35 TFSI 进取型' },
              { value: '2017款 Limousine 35 TFSI 风尚型', label: '2017款 Limousine 35 TFSI 风尚型' },
              { value: '2018款 30周年年型 Limousine 35 TFSI 风尚型', label: '2018款 30周年年型 Limousine 35 TFSI 风尚型' },
              { value: '2019款 Limousine 35 TFSI 风尚型 国V', label: '2019款 Limousine 35 TFSI 风尚型 国V' },
              { value: '2022款 A3L Limousine 35 TFSI 时尚运动型', label: '2022款 A3L Limousine 35 TFSI 时尚运动型' },
            ]
          },
          {
            value: '奥迪Q7',
            label: '奥迪Q7',
            children: [
              { value: '2006款 3.6 FSI quattro 基本型', label: '2006款 3.6 FSI quattro 基本型' },
              { value: '2007款 3.6 FSI quattro 技术型', label: '2007款 3.6 FSI quattro 技术型' },
              { value: '2010款 3.6 FSI quattro 豪华型', label: '2010款 3.6 FSI quattro 豪华型' },
              { value: '2011款 3.0 TFSI 技术型(245kW)', label: '2011款 3.0 TFSI 技术型(245kW)' },
              { value: '2013款 35 TFSI 舒适型', label: '2013款 35 TFSI 舒适型' },
              { value: '2023款 55 TFSI quattro S line运动型', label: '2023款 55 TFSI quattro S line运动型' },
            ]
          }]
        },
        {
          value: '大众',
          label: '大众',
          children: [
            {
              value: '迈腾', label: '迈腾', children: [
                { value: '迈腾 2020款 330TSI DSG 豪华型', label: '迈腾 2020款 330TSI DSG 豪华型' },
                { value: '迈腾 2019款 330TSI DSG 尊贵型 国V', label: '迈腾 2019款 330TSI DSG 尊贵型 国V' },
                { value: '迈腾 2012款 改款 2.0TSI 豪华型', label: '迈腾 2012款 改款 2.0TSI 豪华型' },
                { value: '迈腾 2013款 1.8TSI 舒适型', label: '迈腾 2013款 1.8TSI 舒适型' },
                { value: '迈腾 2017款 330TSI DSG 领先型', label: '迈腾 2017款 330TSI DSG 领先型' },
                { value: '迈腾 2015款 1.8TSI 舒适型', label: '迈腾 2015款 1.8TSI 舒适型' },
                { value: '迈腾 2015款 改款 1.8TSI 豪华型', label: '迈腾 2015款 改款 1.8TSI 豪华型' },
                { value: '迈腾 2017款 330TSI DSG 豪华型', label: '迈腾 2017款 330TSI DSG 豪华型' },
                { value: '迈腾 2013款 1.8TSI 豪华型', label: '迈腾 2013款 1.8TSI 豪华型' },
                { value: '迈腾 2020款 280TSI DSG 舒适型', label: '迈腾 2020款 280TSI DSG 舒适型' },
                { value: '迈腾 2013款 1.4TSI 舒适型', label: '迈腾 2013款 1.4TSI 舒适型' },
                { value: '迈腾 2019款 330TSI DSG 豪华型 国VI', label: '迈腾 2019款 330TSI DSG 豪华型 国VI' },
                { value: '迈腾 2018款 330TSI DSG 领先型', label: '迈腾 2018款 330TSI DSG 领先型' },
                { value: '迈腾 2020款 330TSI DSG 领先型', label: '迈腾 2020款 330TSI DSG 领先型' },
                { value: '迈腾 2015款 1.8TSI 豪华型', label: '迈腾 2015款 1.8TSI 豪华型' },
                { value: '迈腾 2019款 380TSI DSG 尊贵型 国VI', label: '迈腾 2019款 380TSI DSG 尊贵型 国VI' },
                { value: '迈腾 2015款 1.8TSI 领先型', label: '迈腾 2015款 1.8TSI 领先型' },
                { value: '迈腾 2011款 2.0TSI DSG豪华型', label: '迈腾 2011款 2.0TSI DSG豪华型' },
                { value: '迈腾 2019款 280TSI DSG 领先型 国VI', label: '迈腾 2019款 280TSI DSG 领先型 国VI' },
                { value: '迈腾 2018款 330TSI DSG 豪华型', label: '迈腾 2018款 330TSI DSG 豪华型' },
                { value: '迈腾 2018款 改款 330TSI DSG 豪华型', label: '迈腾 2018款 改款 330TSI DSG 豪华型' },
                { value: '迈腾 2012款 2.0TSI 尊贵型', label: '迈腾 2012款 2.0TSI 尊贵型' },
                { value: '迈腾 2017款 380TSI DSG 豪华型', label: '迈腾 2017款 380TSI DSG 豪华型' },
                { value: '迈腾 2012款 1.8TSI 豪华型', label: '迈腾 2012款 1.8TSI 豪华型' },
                { value: '迈腾 2016款 2.0TSI 智享豪华型', label: '迈腾 2016款 2.0TSI 智享豪华型' },
                { value: '迈腾 2013款 1.8TSI 尊贵型', label: '迈腾 2013款 1.8TSI 尊贵型' }
              ]
            },
            {
              value: '速腾', label: '速腾', children: [
                { value: '速腾 2018款 1.6L 自动舒适型', label: '速腾 2018款 1.6L 自动舒适型' },
                { value: '速腾 2012款 1.6L 自动舒适型', label: '速腾 2012款 1.6L 自动舒适型' },
                { value: '速腾 2012款 1.4TSI 自动豪华型', label: '速腾 2012款 1.4TSI 自动豪华型' },
                { value: '速腾 2014款 改款 1.4TSI 自动豪华型', label: '速腾 2014款 改款 1.4TSI 自动豪华型' },
                { value: '速腾 2018款 280TSI DSG豪华型', label: '速腾 2018款 280TSI DSG豪华型' },
                { value: '速腾 2019款 280TSI DSG豪华型 国VI', label: '速腾 2019款 280TSI DSG豪华型 国VI' },
                { value: '速腾 2014款 1.6L 自动时尚型', label: '速腾 2014款 1.6L 自动时尚型' },
                { value: '速腾 2017款 1.6L 自动舒适型', label: '速腾 2017款 1.6L 自动舒适型' },
                { value: '速腾 2018款 180TSI DSG臻享版', label: '速腾 2018款 180TSI DSG臻享版' },
                { value: '速腾 2017款 230TSI 自动舒适型', label: '速腾 2017款 230TSI 自动舒适型' },
                { value: '速腾 2009款 1.6L 自动舒适型', label: '速腾 2009款 1.6L 自动舒适型' },
                { value: '速腾 2019款 280TSI DSG舒适型 国VI', label: '速腾 2019款 280TSI DSG舒适型 国VI' },
                { value: '速腾 2015款 1.6L 自动舒适型', label: '速腾 2015款 1.6L 自动舒适型' },
                { value: '速腾 2018款 280TSI DSG熠动版', label: '速腾 2018款 280TSI DSG熠动版' }
              ]

            },
            {
              value: 'T-ROC探歌', label: 'T-ROC探歌', children: [
                { value: 'T-ROC探歌 2022款 280TSI DSG两驱精英PLUS', label: 'T-ROC探歌 2022款 280TSI DSG两驱精英PLUS' },
                { value: 'T-ROC探歌 2022款 280TSI DSG两驱R-Line Pro PLUS', label: 'T-ROC探歌 2022款 280TSI DSG两驱R-Line Pro PLUS' },
                { value: 'T-ROC探歌 2020款 280TSI DSG两驱精英型', label: 'T-ROC探歌 2020款 280TSI DSG两驱精英型' },
                { value: 'T-ROC探歌 2019款 280TSI DSG两驱进取型 国VI', label: 'T-ROC探歌 2019款 280TSI DSG两驱进取型 国VI' },
                { value: 'T-ROC探歌 2018款 280TSI DSG四驱舒适型 国V', label: 'T-ROC探歌 2018款 280TSI DSG四驱舒适型 国V' }
              ]

            },
            {
              value: '途观L', label: '途观L', children: [
                { value: '途观L 2019款 330TSI 自动两驱全景舒适版 国VI', label: '途观L 2019款 330TSI 自动两驱全景舒适版 国VI' },
                { value: '途观L 2018款 380TSI 自动四驱豪华版', label: '途观L 2018款 380TSI 自动四驱豪华版' },
                { value: '途观L 2019款 330TSI 自动两驱智动豪华版 国V', label: '途观L 2019款 330TSI 自动两驱智动豪华版 国V' },
                { value: '途观L 2019款 380TSI 自动四驱智动豪华版7座 国VI', label: '途观L 2019款 380TSI 自动四驱智动豪华版7座 国VI' },
                { value: '途观L 2020款 330TSI 自动两驱智动豪华版 国VI', label: '途观L 2020款 330TSI 自动两驱智动豪华版 国VI' },
                { value: '途观L 2017款 330TSI 自动两驱豪华版', label: '途观L 2017款 330TSI 自动两驱豪华版' },
                { value: '途观L 2022款 330TSI 自动两驱R-Line越享版', label: '途观L 2022款 330TSI 自动两驱R-Line越享版' },
                { value: '途观L 2022款 330TSI 自动两驱R-Line旗舰版', label: '途观L 2022款 330TSI 自动两驱R-Line旗舰版' }
              ]
            },

            {
              value: '甲壳虫', label: '甲壳虫', children: [
                { value: '甲壳虫 2013款 1.4TSI 时尚型', label: '甲壳虫 2013款 1.4TSI 时尚型' },
                { value: '甲壳虫 2010款 2.0 BlackOrange舒适版', label: '甲壳虫 2010款 2.0 BlackOrange舒适版' },
                { value: '甲壳虫 2014款 1.2TSI 时尚型', label: '甲壳虫 2014款 1.2TSI 时尚型' },
                { value: '甲壳虫 2013款 1.4TSI Fender摇滚版', label: '甲壳虫 2013款 1.4TSI Fender摇滚版' },
                { value: '甲壳虫 2015款 180TSI', label: '甲壳虫 2015款 180TSI' },
                { value: '甲壳虫 2013款 1.4TSI 舒适型', label: '甲壳虫 2013款 1.4TSI 舒适型' },
                { value: '甲壳虫 2018款 180TSI 宜乐型', label: '甲壳虫 2018款 180TSI 宜乐型' },
                { value: '甲壳虫 2016款 180TSI Club版', label: '甲壳虫 2016款 180TSI Club版' },
                { value: '甲壳虫 2014款 1.2TSI 舒适型', label: '甲壳虫 2014款 1.2TSI 舒适型' },
                { value: '甲壳虫 2019款 280TSI 珍藏版', label: '甲壳虫 2019款 280TSI 珍藏版' },
                { value: '甲壳虫 2017款 180TSI 翡冷翠经典版', label: '甲壳虫 2017款 180TSI 翡冷翠经典版' },
                { value: '甲壳虫 2019款 180TSI 珍藏版', label: '甲壳虫 2019款 180TSI 珍藏版' },
                { value: '甲壳虫 2016款 280TSI 沙丘越野版', label: '甲壳虫 2016款 280TSI 沙丘越野版' },
                { value: '甲壳虫 2017款 280TSI 至乐版', label: '甲壳虫 2017款 280TSI 至乐版' },
                { value: '甲壳虫 2018款 180TSI 乐动橙版', label: '甲壳虫 2018款 180TSI 乐动橙版' },
                { value: '甲壳虫 2018款 280TSI 至乐型', label: '甲壳虫 2018款 280TSI 至乐型' }
              ]
            },

            {
              value: '途锐', label: '途锐', children: [
                { value: '途锐 2019款 3.0TSI 锐锋版 国V', label: '途锐 2019款 3.0TSI 锐锋版 国V' },
                { value: '途锐 2019款 2.0TSI 锐翼版 国V', label: '途锐 2019款 2.0TSI 锐翼版 国V' },
                { value: '途锐 2019款 2.0TSI 锐翼版 国VI', label: '途锐 2019款 2.0TSI 锐翼版 国VI' },
                { value: '途锐 2016款 3.0TSI 标配型', label: '途锐 2016款 3.0TSI 标配型' },
                { value: '途锐 2016款 3.0TSI 耀越版', label: '途锐 2016款 3.0TSI 耀越版' },
                { value: '途锐 2011款 3.0TSI 标配型', label: '途锐 2011款 3.0TSI 标配型' },
                { value: '途锐 2011款 3.0TDI 柴油高配型', label: '途锐 2011款 3.0TDI 柴油高配型' },
                { value: '途锐 2021款 2.0TSI 锐翼版', label: '途锐 2021款 2.0TSI 锐翼版' },
                { value: '途锐 2021款 3.0TSI 锐享版 经典运动套装', label: '途锐 2021款 3.0TSI 锐享版 经典运动套装' },
                { value: '途锐 2017款 3.0TSI 拓界版', label: '途锐 2017款 3.0TSI 拓界版' },
                { value: '途锐 2014款 4.2L 标准型', label: '途锐 2014款 4.2L 标准型' },
                { value: '途锐 2020款 2.0TSI 锐尚版 国VI', label: '途锐 2020款 2.0TSI 锐尚版 国VI' },
                { value: '途锐 2017款 3.0TSI 拓野型', label: '途锐 2017款 3.0TSI 拓野型' },
                { value: '途锐 2011款 3.0TSI 舒适型', label: '途锐 2011款 3.0TSI 舒适型' },
                { value: '途锐 2011款 3.0TSI 高配型', label: '途锐 2011款 3.0TSI 高配型' }
              ]
            }

          ]
        },
        {
          value: '雪佛兰',
          label: '雪佛兰',
          children: [
            {
              value: '迈锐宝', label: '迈锐宝', children: [
                { value: '迈锐宝 2016款 1.6T 自动豪华版', label: '迈锐宝 2016款 1.6T 自动豪华版' },
                { value: '迈锐宝 2018款 530T 自动豪华版', label: '迈锐宝 2018款 530T 自动豪华版' },
                { value: '迈锐宝 2014款 2.0L 自动豪华版', label: '迈锐宝 2014款 2.0L 自动豪华版' },
                { value: '迈锐宝 2017款 1.5T 自动旗舰版', label: '迈锐宝 2017款 1.5T 自动旗舰版' },
                { value: '迈锐宝 2012款 2.0L 自动豪华版', label: '迈锐宝 2012款 2.0L 自动豪华版' },
                { value: '迈锐宝 2017款 1.5T 自动豪华版', label: '迈锐宝 2017款 1.5T 自动豪华版' },
                { value: '迈锐宝 2018款 530T 自动舒适版', label: '迈锐宝 2018款 530T 自动舒适版' },
                { value: '迈锐宝 2017款 1.5T 自动舒适版', label: '迈锐宝 2017款 1.5T 自动舒适版' },
                { value: '迈锐宝 2013款 2.0L 自动豪华版', label: '迈锐宝 2013款 2.0L 自动豪华版' },
                { value: '迈锐宝 2018款 530T 自动风尚版', label: '迈锐宝 2018款 530T 自动风尚版' },
                { value: '迈锐宝 2014款 2.0L 自动舒适版', label: '迈锐宝 2014款 2.0L 自动舒适版' },
                { value: '迈锐宝 2016款 2.0L 自动豪华版', label: '迈锐宝 2016款 2.0L 自动豪华版' },
                { value: '迈锐宝 2016款 2.0L 自动舒适版', label: '迈锐宝 2016款 2.0L 自动舒适版' },
                { value: '迈锐宝 2014款 1.6T 自动舒适版', label: '迈锐宝 2014款 1.6T 自动舒适版' }
              ]
            },
            {
              value: '科鲁兹', label: '科鲁兹', children: [
                { value: '科鲁兹 2015款 1.5L 经典 SE AT', label: '科鲁兹 2015款 1.5L 经典 SE AT' },
                { value: '科鲁兹 2009款 1.8L SE AT', label: '科鲁兹 2009款 1.8L SE AT' },
                { value: '科鲁兹 2012款 1.6L SE AT', label: '科鲁兹 2012款 1.6L SE AT' },
                { value: '科鲁兹 2011款 1.6L SE AT', label: '科鲁兹 2011款 1.6L SE AT' },
                { value: '科鲁兹 2009款 1.6L SE AT', label: '科鲁兹 2009款 1.6L SE AT' },
                { value: '科鲁兹 2018款 320 自动先锋天窗版', label: '科鲁兹 2018款 320 自动先锋天窗版' },
                { value: '科鲁兹 2013款 掀背 1.6L 手动豪华型', label: '科鲁兹 2013款 掀背 1.6L 手动豪华型' },
                { value: '科鲁兹 2011款 1.8L SE AT', label: '科鲁兹 2011款 1.8L SE AT' },
                { value: '科鲁兹 2015款 1.5L 经典 SL MT', label: '科鲁兹 2015款 1.5L 经典 SL MT' },
                { value: '科鲁兹 2017款 1.5L 自动炫锋版', label: '科鲁兹 2017款 1.5L 自动炫锋版' },
                { value: '科鲁兹 2012款 1.6L SL天地版 AT', label: '科鲁兹 2012款 1.6L SL天地版 AT' },
                { value: '科鲁兹 2013款 1.6L SE AT', label: '科鲁兹 2013款 1.6L SE AT' },
                { value: '科鲁兹 2012款 1.8L SE AT', label: '科鲁兹 2012款 1.8L SE AT' },
                { value: '科鲁兹 2011款 1.6L SE AT 变形金刚版', label: '科鲁兹 2011款 1.6L SE AT 变形金刚版' },
                { value: '科鲁兹 2017款 1.5L 自动先锋天窗版', label: '科鲁兹 2017款 1.5L 自动先锋天窗版' },
                { value: '科鲁兹 2011款 1.6L SL天地版 AT', label: '科鲁兹 2011款 1.6L SL天地版 AT' },
                { value: '科鲁兹 2012款 1.6L SL MT', label: '科鲁兹 2012款 1.6L SL MT' },
                { value: '科鲁兹 2018款 改款 320 自动先锋版', label: '科鲁兹 2018款 改款 320 自动先锋版' },
                { value: '科鲁兹 2013款 1.6L SL MT', label: '科鲁兹 2013款 1.6L SL MT' },
                { value: '科鲁兹 2015款 1.5L 经典 SE MT', label: '科鲁兹 2015款 1.5L 经典 SE MT' },
                { value: '科鲁兹 2014款 1.6L SL百万纪念版 AT', label: '科鲁兹 2014款 1.6L SL百万纪念版 AT' },
                { value: '科鲁兹 2013款 1.6L SE MT', label: '科鲁兹 2013款 1.6L SE MT' },
                { value: '科鲁兹 2018款  Redline 320 自动先锋版', label: '科鲁兹 2018款  Redline 320 自动先锋版' },
                { value: '科鲁兹 2013款 1.6L SE WTCC版 MT', label: '科鲁兹 2013款 1.6L SE WTCC版 MT' }
              ]
            },
            {
              value: '迈锐宝XL', label: '迈锐宝XL', children: [
                { value: '迈锐宝XL 2016款 1.5T 双离合锐享版', label: '迈锐宝XL 2016款 1.5T 双离合锐享版' },
                { value: '迈锐宝XL 2019款 535T CVT锐动版', label: '迈锐宝XL 2019款 535T CVT锐动版' },
                { value: '迈锐宝XL 2021款 Redline 550T 自动锐联版', label: '迈锐宝XL 2021款 Redline 550T 自动锐联版' },
                { value: '迈锐宝XL 2017款 1.5T 自动锐驰版', label: '迈锐宝XL 2017款 1.5T 自动锐驰版' },
                { value: '迈锐宝XL 2018款 530T 自动锐驰版', label: '迈锐宝XL 2018款 530T 自动锐驰版' },
                { value: '迈锐宝XL 2021款 Redline 550T 自动锐动版', label: '迈锐宝XL 2021款 Redline 550T 自动锐动版' },
                { value: '迈锐宝XL 2022款 Redline 550T 自动锐智版', label: '迈锐宝XL 2022款 Redline 550T 自动锐智版' },
                { value: '迈锐宝XL 2019款 Redline 550T 自动锐联版', label: '迈锐宝XL 2019款 Redline 550T 自动锐联版' },
                { value: '迈锐宝XL 2016款 1.5T 双离合锐驰版', label: '迈锐宝XL 2016款 1.5T 双离合锐驰版' },
                { value: '迈锐宝XL 2022款 Redline 550T 自动锐联版', label: '迈锐宝XL 2022款 Redline 550T 自动锐联版' },
                { value: '迈锐宝XL 2019款 Redline 550T 自动锐动版', label: '迈锐宝XL 2019款 Redline 550T 自动锐动版' },
                { value: '迈锐宝XL 2021款 Redline 550T 自动锐智版', label: '迈锐宝XL 2021款 Redline 550T 自动锐智版' }
              ]
            },
            {
              value: '科沃兹', label: '科沃兹', children: [
                { value: '科沃兹 2018款 320 手动欣悦版', label: '科沃兹 2018款 320 手动欣悦版' },
                { value: '科沃兹 2020款 Redline 325T 自动欣耀版 国VI', label: '科沃兹 2020款 Redline 325T 自动欣耀版 国VI' },
                { value: '科沃兹 2019款 320 自动欣享天窗版', label: '科沃兹 2019款 320 自动欣享天窗版' },
                { value: '科沃兹 2016款 1.5L 自动欣尚版', label: '科沃兹 2016款 1.5L 自动欣尚版' },
                { value: '科沃兹 2022款 325T 自动欣悦版', label: '科沃兹 2022款 325T 自动欣悦版' },
                { value: '科沃兹 2019款 320 自动欣悦版', label: '科沃兹 2019款 320 自动欣悦版' },
                { value: '科沃兹 2020款 325T 自动欣悦版', label: '科沃兹 2020款 325T 自动欣悦版' },
                { value: '科沃兹 2021款 325T 自动欣悦版', label: '科沃兹 2021款 325T 自动欣悦版' },
                { value: '科沃兹 2018款 320 自动欣享天窗版', label: '科沃兹 2018款 320 自动欣享天窗版' },
                { value: '科沃兹 2020款 Redline 325T 自动欣尚版 国VI', label: '科沃兹 2020款 Redline 325T 自动欣尚版 国VI' },
                { value: '科沃兹 2018款 320 自动欣享版', label: '科沃兹 2018款 320 自动欣享版' },
                { value: '科沃兹 2021款 Redline 325T 自动欣尚版', label: '科沃兹 2021款 Redline 325T 自动欣尚版' }
              ]
            }

          ]
        },
        {
          value: '雷克萨斯',
          label: '雷克萨斯',
          children: [
            {
              value: '雷克萨斯NX', label: '雷克萨斯NX', children: [
                { value: '雷克萨斯NX 2015款 200 前驱 锋行版', label: '雷克萨斯NX 2015款 200 前驱 锋行版' },
                { value: '雷克萨斯NX 2017款 200 全驱 锋尚版', label: '雷克萨斯NX 2017款 200 全驱 锋尚版' },
                { value: '雷克萨斯NX 2015款 200t 全驱 F SPORT', label: '雷克萨斯NX 2015款 200t 全驱 F SPORT' },
                { value: '雷克萨斯NX 2018款 200 全驱 锋尚版 国V', label: '雷克萨斯NX 2018款 200 全驱 锋尚版 国V' },
                { value: '雷克萨斯NX 2020款 200 全驱 锋尚版 国VI', label: '雷克萨斯NX 2020款 200 全驱 锋尚版 国VI' },
                { value: '雷克萨斯NX 2015款 300h 前驱 锋尚版', label: '雷克萨斯NX 2015款 300h 前驱 锋尚版' },
                { value: '雷克萨斯NX 2019款 300h 百万纪念限量版 国VI', label: '雷克萨斯NX 2019款 300h 百万纪念限量版 国VI' },
                { value: '雷克萨斯NX 2015款 200t 全驱 锋尚版', label: '雷克萨斯NX 2015款 200t 全驱 锋尚版' },
                { value: '雷克萨斯NX 2018款 200 前驱 锋行版 国V', label: '雷克萨斯NX 2018款 200 前驱 锋行版 国V' },
                { value: '雷克萨斯NX 2020款 200 前驱 锋行版 国V', label: '雷克萨斯NX 2020款 200 前驱 锋行版 国V' }
              ]
            },
            {
              value: '雷克萨斯RX', label: '雷克萨斯RX', children: [
                { value: '雷克萨斯RX 2016款 300 四驱典雅版 国V', label: '雷克萨斯RX 2016款 300 四驱典雅版 国V' },
                { value: '雷克萨斯RX 2020款 300 四驱典雅版 国VI', label: '雷克萨斯RX 2020款 300 四驱典雅版 国VI' },
                { value: '雷克萨斯RX 2016款 450h 四驱典雅版', label: '雷克萨斯RX 2016款 450h 四驱典雅版' },
                { value: '雷克萨斯RX 2020款 450hL 四驱豪华版7座 国VI', label: '雷克萨斯RX 2020款 450hL 四驱豪华版7座 国VI' },
                { value: '雷克萨斯RX 2020款 改款 300 四驱典雅版', label: '雷克萨斯RX 2020款 改款 300 四驱典雅版' },
                { value: '雷克萨斯RX 2016款 300 两驱舒适版 国V', label: '雷克萨斯RX 2016款 300 两驱舒适版 国V' },
                { value: '雷克萨斯RX 2016款 300 四驱典雅版 国VI', label: '雷克萨斯RX 2016款 300 四驱典雅版 国VI' },
                { value: '雷克萨斯RX 2016款 300 两驱精英版 国V', label: '雷克萨斯RX 2016款 300 两驱精英版 国V' },
                { value: '雷克萨斯RX 2020款 450h 四驱醇享版', label: '雷克萨斯RX 2020款 450h 四驱醇享版' },
                { value: '雷克萨斯RX 2020款 450hL 四驱尊贵版6座 国V', label: '雷克萨斯RX 2020款 450hL 四驱尊贵版6座 国V' }
              ]
            },
            {
              value: '雷克萨斯LX', label: '雷克萨斯LX', children: [
                { value: '雷克萨斯LX 2019款 570 动感豪华版', label: '雷克萨斯LX 2019款 570 动感豪华版' },
                { value: '雷克萨斯LX 2019款 570 尊贵豪华版', label: '雷克萨斯LX 2019款 570 尊贵豪华版' },
                { value: '雷克萨斯LX 2009款 570', label: '雷克萨斯LX 2009款 570' },
                { value: '雷克萨斯LX 2019款 570 巅峰特别版', label: '雷克萨斯LX 2019款 570 巅峰特别版' },
                { value: '雷克萨斯LX 2017款 570 尊贵豪华版', label: '雷克萨斯LX 2017款 570 尊贵豪华版' },
                { value: '雷克萨斯LX 2016款 570 动感豪华版', label: '雷克萨斯LX 2016款 570 动感豪华版' },
                { value: '雷克萨斯LX 2016款 570 尊贵豪华版', label: '雷克萨斯LX 2016款 570 尊贵豪华版' },
                { value: '雷克萨斯LX 2017款 570 动感豪华版', label: '雷克萨斯LX 2017款 570 动感豪华版' },
                { value: '雷克萨斯LX 2013款 570', label: '雷克萨斯LX 2013款 570' },
                { value: '雷克萨斯LX 2012款 570', label: '雷克萨斯LX 2012款 570' },
                { value: '雷克萨斯LX 2017款 570 巅峰特别限量版', label: '雷克萨斯LX 2017款 570 巅峰特别限量版' }
              ]
            },
            {
              value: '雷克萨斯ES', label: '雷克萨斯ES', children: [
                { value: '雷克萨斯ES 2018款 200 卓越版 国VI', label: '雷克萨斯ES 2018款 200 卓越版 国VI' },
                { value: '雷克萨斯ES 2006款 350 豪华版', label: '雷克萨斯ES 2006款 350 豪华版' },
                { value: '雷克萨斯ES 2022款 200 卓越版', label: '雷克萨斯ES 2022款 200 卓越版' },
                { value: '雷克萨斯ES 2014款 250 精英版', label: '雷克萨斯ES 2014款 250 精英版' },
                { value: '雷克萨斯ES 2015款 200 精英版', label: '雷克萨斯ES 2015款 200 精英版' },
                { value: '雷克萨斯ES 2010款 240 典雅版', label: '雷克萨斯ES 2010款 240 典雅版' },
                { value: '雷克萨斯ES 2018款 200 卓越版 国V', label: '雷克萨斯ES 2018款 200 卓越版 国V' },
                { value: '雷克萨斯ES 2013款 250 精英版', label: '雷克萨斯ES 2013款 250 精英版' },
                { value: '雷克萨斯ES 2012款 240 特别限量版', label: '雷克萨斯ES 2012款 240 特别限量版' },
                { value: '雷克萨斯ES 2022款 300h 臻享版', label: '雷克萨斯ES 2022款 300h 臻享版' },
                { value: '雷克萨斯ES 2018款 200 豪华版 国V', label: '雷克萨斯ES 2018款 200 豪华版 国V' },
                { value: '雷克萨斯ES 2021款 200 卓越版', label: '雷克萨斯ES 2021款 200 卓越版' },
                { value: '雷克萨斯ES 2018款 300h 行政版 国V', label: '雷克萨斯ES 2018款 300h 行政版 国V' },
                { value: '雷克萨斯ES 2020款 300h 卓越版 国V', label: '雷克萨斯ES 2020款 300h 卓越版 国V' },
                { value: '雷克萨斯ES 2014款 300h 精英版', label: '雷克萨斯ES 2014款 300h 精英版' },
                { value: '雷克萨斯ES 2017款 200 30周年纪念版', label: '雷克萨斯ES 2017款 200 30周年纪念版' },
                { value: '雷克萨斯ES 2015款 300h 豪华版', label: '雷克萨斯ES 2015款 300h 豪华版' },
                { value: '雷克萨斯ES 2018款 260 F SPORT 国V', label: '雷克萨斯ES 2018款 260 F SPORT 国V' }
              ]
            },]
        },
        {
          value: '保时捷',
          label: '保时捷',
          children: [
            {
              value: 'Cayenne新能源', label: 'Cayenne新能源', children: [
                { value: 'Cayenne新能源 2021款 Cayenne E-Hybrid 2.0T', label: 'Cayenne新能源 2021款 Cayenne E-Hybrid 2.0T' },
                { value: 'Cayenne新能源 2019款 Cayenne E-Hybrid 2.0T', label: 'Cayenne新能源 2019款 Cayenne E-Hybrid 2.0T' },
                { value: 'Cayenne新能源 2016款 Cayenne S E-Hybrid 3.0T', label: 'Cayenne新能源 2016款 Cayenne S E-Hybrid 3.0T' },
                { value: 'Cayenne新能源 2023款 Cayenne E-Hybrid 2.0T', label: 'Cayenne新能源 2023款 Cayenne E-Hybrid 2.0T' },
                { value: 'Cayenne新能源 2021款 Cayenne E-Hybrid Coupé 2.0T', label: 'Cayenne新能源 2021款 Cayenne E-Hybrid Coupé 2.0T' },
                { value: 'Cayenne新能源 2022款 Cayenne E-Hybrid 2.0T 铂金版', label: 'Cayenne新能源 2022款 Cayenne E-Hybrid 2.0T 铂金版' },
                { value: 'Cayenne新能源 2015款 Cayenne S E-Hybrid 3.0T', label: 'Cayenne新能源 2015款 Cayenne S E-Hybrid 3.0T' },
                { value: 'Cayenne新能源 2020款 Cayenne E-Hybrid 2.0T', label: 'Cayenne新能源 2020款 Cayenne E-Hybrid 2.0T' },
                { value: 'Cayenne新能源 2022款 Cayenne E-Hybrid Coupé 2.0T 铂金版', label: 'Cayenne新能源 2022款 Cayenne E-Hybrid Coupé 2.0T 铂金版' },
                { value: 'Cayenne新能源 2023款 Cayenne E-Hybrid 2.0T 铂金版', label: 'Cayenne新能源 2023款 Cayenne E-Hybrid 2.0T 铂金版' }
              ]
            },

            {
              value: '保时捷718', label: '保时捷718', children: [
                { value: '保时捷718 2020款 Boxster 2.0T', label: '保时捷718 2020款 Boxster 2.0T' },
                { value: '保时捷718 2019款 Boxster T 2.0T', label: '保时捷718 2019款 Boxster T 2.0T' },
                { value: '保时捷718 2016款 Boxster 2.0T', label: '保时捷718 2016款 Boxster 2.0T' },
                { value: '保时捷718 2022款 Boxster 2.0T', label: '保时捷718 2022款 Boxster 2.0T' },
                { value: '保时捷718 2018款 Cayman 2.0T', label: '保时捷718 2018款 Cayman 2.0T' },
                { value: '保时捷718 2020款 Cayman 2.0T', label: '保时捷718 2020款 Cayman 2.0T' },
                { value: '保时捷718 2022款 Boxster T 2.0T', label: '保时捷718 2022款 Boxster T 2.0T' },
                { value: '保时捷718 2016款 Cayman 2.0T', label: '保时捷718 2016款 Cayman 2.0T' },
                { value: '保时捷718 2016款 Cayman S 2.5T', label: '保时捷718 2016款 Cayman S 2.5T' },
                { value: '保时捷718 2018款 Boxster 2.0T', label: '保时捷718 2018款 Boxster 2.0T' },
                { value: '保时捷718 2021款 Boxster 2.5T 25周年纪念版', label: '保时捷718 2021款 Boxster 2.5T 25周年纪念版' },
                { value: '保时捷718 2022款 Spyder 2.0T', label: '保时捷718 2022款 Spyder 2.0T' },
                { value: '保时捷718 2022款 Cayman 2.0T', label: '保时捷718 2022款 Cayman 2.0T' },
                { value: '保时捷718 2018款 Boxster S 2.5T', label: '保时捷718 2018款 Boxster S 2.5T' },
                { value: '保时捷718 2021款 Spyder 2.0T', label: '保时捷718 2021款 Spyder 2.0T' },
                { value: '保时捷718 2022款 Cayman GT4 RS 4.0L', label: '保时捷718 2022款 Cayman GT4 RS 4.0L' },
                { value: '保时捷718 2022款 Boxster GTS 2.5T', label: '保时捷718 2022款 Boxster GTS 2.5T' },
                { value: '保时捷718 2019款 Cayman T 2.0T', label: '保时捷718 2019款 Cayman T 2.0T' },
                { value: '保时捷718 2022款 Cayman T 2.0T', label: '保时捷718 2022款 Cayman T 2.0T' },
                { value: '保时捷718 2020款 Cayman S 2.5T', label: '保时捷718 2020款 Cayman S 2.5T' },
                { value: '保时捷718 2023款 Boxster Style Edition 2.0T', label: '保时捷718 2023款 Boxster Style Edition 2.0T' },
                { value: '保时捷718 2020款 Boxster GTS 2.5T', label: '保时捷718 2020款 Boxster GTS 2.5T' },
                { value: '保时捷718 2018款 Boxster GTS 2.5T', label: '保时捷718 2018款 Boxster GTS 2.5T' },
                { value: '保时捷718 2020款 Boxster S 2.5T', label: '保时捷718 2020款 Boxster S 2.5T' }
              ]
            },
            {
              value: 'Cayenne', label: 'Cayenne', children: [
                { value: 'Cayenne 2018款 Cayenne 3.0T', label: 'Cayenne 2018款 Cayenne 3.0T' },
                { value: 'Cayenne 2019款 Cayenne 3.0T', label: 'Cayenne 2019款 Cayenne 3.0T' },
                { value: 'Cayenne 2011款 Cayenne 3.0T', label: 'Cayenne 2011款 Cayenne 3.0T' },
                { value: 'Cayenne 2015款 Cayenne 3.0T', label: 'Cayenne 2015款 Cayenne 3.0T' },
                { value: 'Cayenne 2016款 Cayenne 3.0T', label: 'Cayenne 2016款 Cayenne 3.0T' },
                { value: 'Cayenne 2019款 Cayenne Coupé 3.0T', label: 'Cayenne 2019款 Cayenne Coupé 3.0T' },
                { value: 'Cayenne 2014款 Cayenne Platinum Edition 3.0T', label: 'Cayenne 2014款 Cayenne Platinum Edition 3.0T' },
                { value: 'Cayenne 2022款 Cayenne 3.0T 铂金版', label: 'Cayenne 2022款 Cayenne 3.0T 铂金版' },
                { value: 'Cayenne 2015款 Cayenne S 3.6T', label: 'Cayenne 2015款 Cayenne S 3.6T' },
                { value: 'Cayenne 2016款 Cayenne S 3.6T', label: 'Cayenne 2016款 Cayenne S 3.6T' },
                { value: 'Cayenne 2007款 Cayenne 3.6L', label: 'Cayenne 2007款 Cayenne 3.6L' },
                { value: 'Cayenne 2020款 Cayenne S 2.9T', label: 'Cayenne 2020款 Cayenne S 2.9T' },
                { value: 'Cayenne 2020款 Cayenne S Coupé 2.9T', label: 'Cayenne 2020款 Cayenne S Coupé 2.9T' }
              ]
            },
            {
              value: '保时捷911', label: '保时捷911', children: [
                { value: '保时捷911 2022款 Targa 4 3.0T', label: '保时捷911 2022款 Targa 4 3.0T' },
                { value: '保时捷911 2012款 Carrera 3.4L', label: '保时捷911 2012款 Carrera 3.4L' },
                { value: '保时捷911 2013款 GT3 3.8L', label: '保时捷911 2013款 GT3 3.8L' },
                { value: '保时捷911 2015款 Carrera 4 3.4L Style Edition', label: '保时捷911 2015款 Carrera 4 3.4L Style Edition' },
                { value: '保时捷911 2022款 Carrera S Cabriolet 3.0T', label: '保时捷911 2022款 Carrera S Cabriolet 3.0T' },
                { value: '保时捷911 2016款 Carrera Cabriolet 3.0T', label: '保时捷911 2016款 Carrera Cabriolet 3.0T' },
                { value: '保时捷911 2016款 Carrera S 3.0T', label: '保时捷911 2016款 Carrera S 3.0T' },
                { value: '保时捷911 2016款 Carrera 4S Cabriolet 3.0T', label: '保时捷911 2016款 Carrera 4S Cabriolet 3.0T' },
                { value: '保时捷911 2018款 GT2 RS 3.8T', label: '保时捷911 2018款 GT2 RS 3.8T' },
                { value: '保时捷911 2018款 亚洲保时捷卡雷拉杯15周年限定版', label: '保时捷911 2018款 亚洲保时捷卡雷拉杯15周年限定版' },
                { value: '保时捷911 2016款 Turbo S Cabriolet 3.8T', label: '保时捷911 2016款 Turbo S Cabriolet 3.8T' },
                { value: '保时捷911 2020款 Carrera 3.0T', label: '保时捷911 2020款 Carrera 3.0T' },
                { value: '保时捷911 2019款 Carrera 4S 3.0T', label: '保时捷911 2019款 Carrera 4S 3.0T' },
                { value: '保时捷911 2016款 Carrera 3.0T', label: '保时捷911 2016款 Carrera 3.0T' }
              ]
            }
          ]
        },
        {
          value: '凯迪拉克',
          label: '凯迪拉克',
          children: [
            {
              value: '凯迪拉克XT5', label: '凯迪拉克XT5', children: [
                { value: '凯迪拉克XT5 2020款 28T 四驱豪华型', label: '凯迪拉克XT5 2020款 28T 四驱豪华型' },
                { value: '凯迪拉克XT5 2021款 2.0T 两驱豪华型', label: '凯迪拉克XT5 2021款 2.0T 两驱豪华型' },
                { value: '凯迪拉克XT5 2020款 改款 28T 四驱豪华型', label: '凯迪拉克XT5 2020款 改款 28T 四驱豪华型' },
                { value: '凯迪拉克XT5 2018款 28T 四驱豪华型', label: '凯迪拉克XT5 2018款 28T 四驱豪华型' },
                { value: '凯迪拉克XT5 2020款 28T 豪华型', label: '凯迪拉克XT5 2020款 28T 豪华型' },
                { value: '凯迪拉克XT5 2016款 25T 技术型', label: '凯迪拉克XT5 2016款 25T 技术型' },
                { value: '凯迪拉克XT5 2018款 25T 豪华型', label: '凯迪拉克XT5 2018款 25T 豪华型' },
                { value: '凯迪拉克XT5 2021款 28T 四驱豪华型', label: '凯迪拉克XT5 2021款 28T 四驱豪华型' },
                { value: '凯迪拉克XT5 2021款 28T 豪华型', label: '凯迪拉克XT5 2021款 28T 豪华型' },
                { value: '凯迪拉克XT5 2016款 25T 豪华型', label: '凯迪拉克XT5 2016款 25T 豪华型' },
                { value: '凯迪拉克XT5 2020款 改款 28T 豪华型', label: '凯迪拉克XT5 2020款 改款 28T 豪华型' }
              ]
            },
            {
              value: '凯迪拉克CT6', label: '凯迪拉克CT6', children: [
                { value: '凯迪拉克CT6 2022款 28T 尊贵型', label: '凯迪拉克CT6 2022款 28T 尊贵型' },
                { value: '凯迪拉克CT6 2021款 28T 豪华型', label: '凯迪拉克CT6 2021款 28T 豪华型' },
                { value: '凯迪拉克CT6 2017款 28T 时尚型', label: '凯迪拉克CT6 2017款 28T 时尚型' },
                { value: '凯迪拉克CT6 2021款 28T 精英型', label: '凯迪拉克CT6 2021款 28T 精英型' },
                { value: '凯迪拉克CT6 2019款 28T 豪华型', label: '凯迪拉克CT6 2019款 28T 豪华型' },
                { value: '凯迪拉克CT6 2019款 28T 时尚型', label: '凯迪拉克CT6 2019款 28T 时尚型' },
                { value: '凯迪拉克CT6 2016款 40T 领先型', label: '凯迪拉克CT6 2016款 40T 领先型' }
              ]
            }

          ]
        },
        {
          value: '别克',
          label: '别克',
          children: [
            {
              value: '君越', label: '君越', children: [
                { value: '君越 2013款 2.4L SIDI领先舒适型', label: '君越 2013款 2.4L SIDI领先舒适型' },
                { value: '君越 2016款 20T 领先型', label: '君越 2016款 20T 领先型' },
                { value: '君越 2016款 改款 20T 领先型', label: '君越 2016款 改款 20T 领先型' },
                { value: '君越 2016款 20T 精英型', label: '君越 2016款 20T 精英型' },
                { value: '君越 2020款 652T 尊贵型', label: '君越 2020款 652T 尊贵型' },
                { value: '君越 2018款 20T 精英型', label: '君越 2018款 20T 精英型' },
                { value: '君越 2016款 20T 豪华型', label: '君越 2016款 20T 豪华型' },
                { value: '君越 2010款 2.4L豪雅版', label: '君越 2010款 2.4L豪雅版' },
                { value: '君越 2016款 改款 28T 精英型', label: '君越 2016款 改款 28T 精英型' },
                { value: '君越 2012款 2.4L SIDI豪雅版', label: '君越 2012款 2.4L SIDI豪雅版' }
              ]
            },
            {
              value: '威朗', label: '威朗', children: [
                { value: '威朗 2016款 两厢 15S 自动进取型', label: '威朗 2016款 两厢 15S 自动进取型' },
                { value: '威朗 2020款 15T 自动进取型', label: '威朗 2020款 15T 自动进取型' },
                { value: '威朗 2015款 三厢 15S 自动进取型', label: '威朗 2015款 三厢 15S 自动进取型' },
                { value: '威朗 2017款 三厢 15S 自动进取型', label: '威朗 2017款 三厢 15S 自动进取型' },
                { value: '威朗 2018款 三厢 15S 自动领先型', label: '威朗 2018款 三厢 15S 自动领先型' },
                { value: '威朗 2022款 Pro 533T 乐享版', label: '威朗 2022款 Pro 533T 乐享版' },
                { value: '威朗 2018款 三厢 15S 自动进取型', label: '威朗 2018款 三厢 15S 自动进取型' },
                { value: '威朗 2016款 两厢GS 20T 双离合纵情运动型', label: '威朗 2016款 两厢GS 20T 双离合纵情运动型' },
                { value: '威朗 2018款 三厢 20T 双离合豪华型', label: '威朗 2018款 三厢 20T 双离合豪华型' },
                { value: '威朗 2018款 两厢 15S 自动领先型', label: '威朗 2018款 两厢 15S 自动领先型' },
                { value: '威朗 2015款 三厢 15S 自动领先型', label: '威朗 2015款 三厢 15S 自动领先型' },
                { value: '威朗 2022款 Pro GS 追风版', label: '威朗 2022款 Pro GS 追风版' },
                { value: '威朗 2019款 三厢 15S 自动进取型', label: '威朗 2019款 三厢 15S 自动进取型' },
                { value: '威朗 2023款 Pro 乐享版', label: '威朗 2023款 Pro 乐享版' },
                { value: '威朗 2017款 三厢 20T 双离合领先型', label: '威朗 2017款 三厢 20T 双离合领先型' },
                { value: '威朗 2019款 三厢 15S 自动领先型', label: '威朗 2019款 三厢 15S 自动领先型' }
              ]
            },
            { value: '英朗', label: '英朗',children:[
                { value: '英朗 2019款 18T 自动互联精英型 国VI', label: '英朗 2019款 18T 自动互联精英型 国VI' },
                { value: '英朗 2016款 15N 自动豪华型', label: '英朗 2016款 15N 自动豪华型' },
                { value: '英朗 2021款 改款 典范 1.5L 自动精英型', label: '英朗 2021款 改款 典范 1.5L 自动精英型' },
                { value: '英朗 2015款 18T 双离合豪华型', label: '英朗 2015款 18T 双离合豪华型' },
                { value: '英朗 2013款 GT 1.6L 自动时尚版', label: '英朗 2013款 GT 1.6L 自动时尚版' },
                { value: '英朗 2013款 GT 1.6L 手动进取版', label: '英朗 2013款 GT 1.6L 手动进取版' },
                { value: '英朗 2013款 XT 1.6L 自动时尚版', label: '英朗 2013款 XT 1.6L 自动时尚版' },
                { value: '英朗 2015款 15N 自动进取型', label: '英朗 2015款 15N 自动进取型' },
                { value: '英朗 2016款 15N 自动精英型', label: '英朗 2016款 15N 自动精英型' },
                { value: '英朗 2021款 改款 1.3T 自动轻混动进取型', label: '英朗 2021款 改款 1.3T 自动轻混动进取型' },
                { value: '英朗 2012款 GT 1.6L 手动舒适版', label: '英朗 2012款 GT 1.6L 手动舒适版' },
                { value: '英朗 2012款 GT 1.8L 自动时尚真皮版', label: '英朗 2012款 GT 1.8L 自动时尚真皮版' },
                { value: '英朗 2015款 15N 自动豪华型', label: '英朗 2015款 15N 自动豪华型' },
                { value: '英朗 2017款 15N 自动精英型', label: '英朗 2017款 15N 自动精英型' },
                { value: '英朗 2014款 XT 1.6L 手动进取版', label: '英朗 2014款 XT 1.6L 手动进取版' },
                { value: '英朗 2019款 15T 双离合互联精英型 国V', label: '英朗 2019款 15T 双离合互联精英型 国V' },
                { value: '英朗 2014款 XT 1.6T 自动新锐运动版', label: '英朗 2014款 XT 1.6T 自动新锐运动版' },
                { value: '英朗 2019款 18T 自动互联旗舰型 国VI', label: '英朗 2019款 18T 自动互联旗舰型 国VI' },
                { value: '英朗 2015款 15N 自动精英型', label: '英朗 2015款 15N 自动精英型' },
                { value: '英朗 2017款 15N 自动进取型', label: '英朗 2017款 15N 自动进取型' }
              ]
            },
          ]
        },  
        {
          value: '三菱',
          label: '三菱',
          children: [
            { 
              value: '欧蓝德', label: '欧蓝德' ,children:[
                { value: '欧蓝德 2019款 2.0L 两驱畅享版 5座 国V', label: '欧蓝德 2019款 2.0L 两驱畅享版 5座 国V' },
                { value: '欧蓝德 2019款 2.0L 两驱畅享版 7座 国VI', label: '欧蓝德 2019款 2.0L 两驱畅享版 7座 国VI' },
                { value: '欧蓝德 2018款 2.0L 两驱荣耀版 5座', label: '欧蓝德 2018款 2.0L 两驱荣耀版 5座' },
                { value: '欧蓝德 2023款 1.5T CVT四驱尊耀版 7座', label: '欧蓝德 2023款 1.5T CVT四驱尊耀版 7座' },
                { value: '欧蓝德 2018款 2.4L 四驱尊贵版 7座', label: '欧蓝德 2018款 2.4L 四驱尊贵版 7座' },
                { value: '欧蓝德 2020款 2.0L 两驱畅享版 5座', label: '欧蓝德 2020款 2.0L 两驱畅享版 5座' },
                { value: '欧蓝德 2016款 2.4L 四驱精英版 5座', label: '欧蓝德 2016款 2.4L 四驱精英版 5座' },
                { value: '欧蓝德 2021款 2.0L 两驱畅享版 5座', label: '欧蓝德 2021款 2.0L 两驱畅享版 5座' },
                { value: '欧蓝德 2019款 2.4L 四驱致享版 5座 国VI', label: '欧蓝德 2019款 2.4L 四驱致享版 5座 国VI' },
                { value: '欧蓝德 2020款 2.4L 四驱致享版 7座', label: '欧蓝德 2020款 2.4L 四驱致享版 7座' }
              ]
            }
          ]
            },{
              value: '丰田',
              label: '丰田',
              children: [
                { value: '埃尔法', label: '埃尔法', children:[
            { value: '埃尔法 2021款 双擎 2.5L 尊贵版', label: '埃尔法 2021款 双擎 2.5L 尊贵版' },
            { value: '埃尔法 2020款 双擎 2.5L 尊贵版', label: '埃尔法 2020款 双擎 2.5L 尊贵版' },
            { value: '埃尔法 2012款 3.5L 尊贵版', label: '埃尔法 2012款 3.5L 尊贵版' },
            { value: '埃尔法 2019款 双擎 2.5L 尊贵版', label: '埃尔法 2019款 双擎 2.5L 尊贵版' },
            { value: '埃尔法 2015款 3.5L 尊贵版', label: '埃尔法 2015款 3.5L 尊贵版' },
            { value: '埃尔法 2021款 双擎 2.5L 豪华版', label: '埃尔法 2021款 双擎 2.5L 豪华版' },
            { value: '埃尔法 2018款 3.5L 尊贵版', label: '埃尔法 2018款 3.5L 尊贵版' },
            { value: '埃尔法 2019款 双擎 2.5L 豪华版', label: '埃尔法 2019款 双擎 2.5L 豪华版' },
            { value: '埃尔法 2018款 3.5L 豪华版', label: '埃尔法 2018款 3.5L 豪华版' },
            { value: '埃尔法 2018款 改款 3.5L 尊贵版', label: '埃尔法 2018款 改款 3.5L 尊贵版' },
            { value: '埃尔法 2018款 改款 3.5L 豪华版', label: '埃尔法 2018款 改款 3.5L 豪华版' },
            { value: '埃尔法 2012款 3.5L 豪华版', label: '埃尔法 2012款 3.5L 豪华版' },
            { value: '埃尔法 2020款 双擎 2.5L 豪华版', label: '埃尔法 2020款 双擎 2.5L 豪华版' },
            { value: '埃尔法 2015款 3.5L 豪华版', label: '埃尔法 2015款 3.5L 豪华版' },
            { value: '埃尔法 2023款 双擎 2.5L 臻享·黄金版', label: '埃尔法 2023款 双擎 2.5L 臻享·黄金版' }
          ]
          },
                { value: '普拉多', label: '普拉多',children:[
            { value: '普拉多 2018款 3.5L 自动TX-L后挂备胎', label: '普拉多 2018款 3.5L 自动TX-L后挂备胎' },
            { value: '普拉多 2019款 3.5L 自动TX-L尊享版后挂备胎', label: '普拉多 2019款 3.5L 自动TX-L尊享版后挂备胎' },
            { value: '普拉多 2016款 2.7L 自动标准版', label: '普拉多 2016款 2.7L 自动标准版' },
            { value: '普拉多 2010款 4.0L 自动TX', label: '普拉多 2010款 4.0L 自动TX' },
            { value: '普拉多 2018款 3.5L 自动TX-L NAVI后挂备胎', label: '普拉多 2018款 3.5L 自动TX-L NAVI后挂备胎' },
            { value: '普拉多 2010款 4.0L 自动TX-L', label: '普拉多 2010款 4.0L 自动TX-L' },
            { value: '普拉多 2016款 3.5L 自动TX-L', label: '普拉多 2016款 3.5L 自动TX-L' },
            { value: '普拉多 2006款 4.0L 自动VX NAVI版', label: '普拉多 2006款 4.0L 自动VX NAVI版' },
            { value: '普拉多 2018款 3.5L 自动TX-L', label: '普拉多 2018款 3.5L 自动TX-L' },
            { value: '普拉多 2015款 2.7L 自动豪华版', label: '普拉多 2015款 2.7L 自动豪华版' },
            { value: '普拉多 2018款 3.5L 自动VX NAVI后挂备胎', label: '普拉多 2018款 3.5L 自动VX NAVI后挂备胎' },
            { value: '普拉多 2018款 3.5L 自动TX-L NAVI', label: '普拉多 2018款 3.5L 自动TX-L NAVI' }
          ]
          },
                { value: '亚洲龙', label: '亚洲龙',children:[
            { value: '亚洲龙 2022款 2.0L XLE尊享版', label: '亚洲龙 2022款 2.0L XLE尊享版' },
            { value: '亚洲龙 2019款 双擎 2.5L XLE尊贵版 国VI', label: '亚洲龙 2019款 双擎 2.5L XLE尊贵版 国VI' },
            { value: '亚洲龙 2019款 2.5L Touring尊贵版 国V', label: '亚洲龙 2019款 2.5L Touring尊贵版 国V' },
            { value: '亚洲龙 2019款 2.0L XLE尊享版 国VI', label: '亚洲龙 2019款 2.0L XLE尊享版 国VI' },
            { value: '亚洲龙 2019款 2.0L 豪华版 国VI', label: '亚洲龙 2019款 2.0L 豪华版 国VI' },
            { value: '亚洲龙 2019款 双擎 2.5L 豪华版 国VI', label: '亚洲龙 2019款 双擎 2.5L 豪华版 国VI' },
            { value: '亚洲龙 2021款 2.5L Touring尊贵SPORT版', label: '亚洲龙 2021款 2.5L Touring尊贵SPORT版' },
            { value: '亚洲龙 2022款 双擎 2.5L XLE尊贵版', label: '亚洲龙 2022款 双擎 2.5L XLE尊贵版' },
            { value: '亚洲龙 2019款 双擎 2.5L XLE尊贵版 国V', label: '亚洲龙 2019款 双擎 2.5L XLE尊贵版 国V' },
            { value: '亚洲龙 2023款 2.0L 豪华版', label: '亚洲龙 2023款 2.0L 豪华版' },
            { value: '亚洲龙 2022款 2.0L 豪华版', label: '亚洲龙 2022款 2.0L 豪华版' },
            { value: '亚洲龙 2021款 2.5L 豪华版', label: '亚洲龙 2021款 2.5L 豪华版' },
            { value: '亚洲龙 2019款 双擎 2.5L 豪华版 国V', label: '亚洲龙 2019款 双擎 2.5L 豪华版 国V' },
            { value: '亚洲龙 2022款 2.5L 豪华版', label: '亚洲龙 2022款 2.5L 豪华版' },
            { value: '亚洲龙 2023款 双擎 2.5L 豪华版', label: '亚洲龙 2023款 双擎 2.5L 豪华版' },
            { value: '亚洲龙 2022款 2.5L Touring尊贵版', label: '亚洲龙 2022款 2.5L Touring尊贵版' }
          ]
          },
        ]
        },  
        {
            value: '五菱汽车',
            label: '五菱汽车',
            children: [
              { value: '宏光MINIEV', label: '宏光MINIEV',children:[
                  { value: '宏光MINIEV 2022款 马卡龙时尚款 磷酸铁锂', label: '宏光MINIEV 2022款 马卡龙时尚款 磷酸铁锂' },
                  { value: '宏光MINIEV 2022款 GAMEBOY 300km 玩咖款 磷酸铁锂', label: '宏光MINIEV 2022款 GAMEBOY 300km 玩咖款 磷酸铁锂' },
                  { value: '宏光MINIEV 2020款 悦享款 磷酸铁锂', label: '宏光MINIEV 2020款 悦享款 磷酸铁锂' },
                  { value: '宏光MINIEV 2021款 马卡龙时尚款 三元锂', label: '宏光MINIEV 2021款 马卡龙时尚款 三元锂' },
                  { value: '宏光MINIEV 2022款 马卡龙臻享款 磷酸铁锂', label: '宏光MINIEV 2022款 马卡龙臻享款 磷酸铁锂' },
                  { value: '宏光MINIEV 2021款 马卡龙臻享款 磷酸铁锂', label: '宏光MINIEV 2021款 马卡龙臻享款 磷酸铁锂' },
                  { value: '宏光MINIEV 2021款 马卡龙夹心款 170km 磷酸铁锂', label: '宏光MINIEV 2021款 马卡龙夹心款 170km 磷酸铁锂' },
                  { value: '宏光MINIEV 2021款 马卡龙臻享款 三元锂', label: '宏光MINIEV 2021款 马卡龙臻享款 三元锂' },
                  { value: '宏光MINIEV 2020款 自在款 磷酸铁锂', label: '宏光MINIEV 2020款 自在款 磷酸铁锂' },
                  { value: '宏光MINIEV 2022款 GAMEBOY 200km 玩咖款 磷酸铁锂', label: '宏光MINIEV 2022款 GAMEBOY 200km 玩咖款 磷酸铁锂' },
                  { value: '宏光MINIEV 2021款 马卡龙时尚款 磷酸铁锂', label: '宏光MINIEV 2021款 马卡龙时尚款 磷酸铁锂' },
                  { value: '宏光MINIEV 2021款 马卡龙夹心款 170km 三元锂', label: '宏光MINIEV 2021款 马卡龙夹心款 170km 三元锂' },
                  { value: '宏光MINIEV 2021款 马卡龙夹心款 120km 三元锂', label: '宏光MINIEV 2021款 马卡龙夹心款 120km 三元锂' },
                  { value: '宏光MINIEV 2022款 马卡龙臻享款 三元锂', label: '宏光MINIEV 2022款 马卡龙臻享款 三元锂' },
                  { value: '宏光MINIEV 2020款 自在款 三元锂', label: '宏光MINIEV 2020款 自在款 三元锂' },
                  { value: '宏光MINIEV 2020款 悦享款 三元锂', label: '宏光MINIEV 2020款 悦享款 三元锂' },
                  { value: '宏光MINIEV 2022款 马卡龙时尚款 三元锂', label: '宏光MINIEV 2022款 马卡龙时尚款 三元锂' },
                  { value: '宏光MINIEV 2022款 悦享款 磷酸铁锂', label: '宏光MINIEV 2022款 悦享款 磷酸铁锂' },
                  { value: '宏光MINIEV 2020款 轻松款 磷酸铁锂', label: '宏光MINIEV 2020款 轻松款 磷酸铁锂' },
                  { value: '宏光MINIEV 2022款 马卡龙绘色款 磷酸铁锂', label: '宏光MINIEV 2022款 马卡龙绘色款 磷酸铁锂' },
                  { value: '宏光MINIEV 2022款 自在款 三元锂', label: '宏光MINIEV 2022款 自在款 三元锂' },
                  { value: '宏光MINIEV 2022款 轻松款 磷酸铁锂', label: '宏光MINIEV 2022款 轻松款 磷酸铁锂' },
                  { value: '宏光MINIEV 2022款 GAMEBOY 200km 竞速游侠限量版', label: '宏光MINIEV 2022款 GAMEBOY 200km 竞速游侠限量版' },
                  { value: '宏光MINIEV 2022款 马卡龙缤纷款 三元锂', label: '宏光MINIEV 2022款 马卡龙缤纷款 三元锂' },
                  { value: '宏光MINIEV 2021款 马卡龙夹心款 120km 磷酸铁锂', label: '宏光MINIEV 2021款 马卡龙夹心款 120km 磷酸铁锂' },
                  { value: '宏光MINIEV 2020款 轻松款 三元锂', label: '宏光MINIEV 2020款 轻松款 三元锂' },
                  { value: '宏光MINIEV 2022款 马卡龙缤纷款 磷酸铁锂', label: '宏光MINIEV 2022款 马卡龙缤纷款 磷酸铁锂' },
                  { value: '宏光MINIEV 2022款 自在款 磷酸铁锂', label: '宏光MINIEV 2022款 自在款 磷酸铁锂' }
                ]
                }
          ]
                  },

                  {
                    value: '宾利',
                    label: '宾利',
                    children: [
                      { value: '飞驰', label: '飞驰' ,children: [
                  { value: '飞驰 2022款 4.0T V8 标准版', label: '飞驰 2022款 4.0T V8 标准版' },
                  { value: '飞驰 2020款 6.0T W12 标准版', label: '飞驰 2020款 6.0T W12 标准版' },
                  { value: '飞驰 2014款 4.0T V8 尊贵版', label: '飞驰 2014款 4.0T V8 尊贵版' },
                  { value: '飞驰 2021款 4.0T V8 标准版', label: '飞驰 2021款 4.0T V8 标准版' },
                  { value: '飞驰 2017款 4.0T V8 标准版', label: '飞驰 2017款 4.0T V8 标准版' },
                  { value: '飞驰 2012款 6.0T 限量版', label: '飞驰 2012款 6.0T 限量版' },
                  { value: '飞驰 2010款 6.0T 五座版', label: '飞驰 2010款 6.0T 五座版' }
                ]
                },
                      { value: '欧陆', label: '欧陆',children:[
                  { value: '欧陆 GT Speed 6.0', label: '欧陆 GT Speed 6.0' },
                  { value: '欧陆 2012款 4.0T GT V8', label: '欧陆 2012款 4.0T GT V8' },
                  { value: '欧陆 2012款 6.0T GT W12', label: '欧陆 2012款 6.0T GT W12' },
                  { value: '欧陆 2004款 GT 6.0', label: '欧陆 2004款 GT 6.0' },
                  { value: '欧陆 2015款 4.0T GT V8 标准版', label: '欧陆 2015款 4.0T GT V8 标准版' },
                  { value: '欧陆 2014款 6.0T GT Speed', label: '欧陆 2014款 6.0T GT Speed' },
                  { value: '欧陆 2022款 6.0T GT W12', label: '欧陆 2022款 6.0T GT W12' },
                  { value: '欧陆 2019款 6.0T GT W12 敞篷版', label: '欧陆 2019款 6.0T GT W12 敞篷版' },
                  { value: '欧陆 2018款 6.0T GT W12', label: '欧陆 2018款 6.0T GT W12' },
                  { value: '欧陆 2014款 4.0T GT V8 S 标准版', label: '欧陆 2014款 4.0T GT V8 S 标准版' },
                  { value: '欧陆 2014款 4.0T GT V8 S 敞篷标准版', label: '欧陆 2014款 4.0T GT V8 S 敞篷标准版' },
                  { value: '欧陆 2015款 4.0T GT V8 S 标准版', label: '欧陆 2015款 4.0T GT V8 S 标准版' },
                  { value: '欧陆 2010款 Supersports 6.0', label: '欧陆 2010款 Supersports 6.0' },
                  { value: '欧陆 2022款 4.0T GT V8', label: '欧陆 2022款 4.0T GT V8' },
                  { value: '欧陆 2020款 4.0T GT V8', label: '欧陆 2020款 4.0T GT V8' },
                  { value: '欧陆 2012款 Supersports 6.0 ISR敞篷限量版', label: '欧陆 2012款 Supersports 6.0 ISR敞篷限量版' },
                  { value: '欧陆 2016款 4.0T GT V8 S 标准版', label: '欧陆 2016款 4.0T GT V8 S 标准版' },
                  { value: '欧陆 2015款 4.0T GT V8 S Mulliner', label: '欧陆 2015款 4.0T GT V8 S Mulliner' },
                  { value: '欧陆 2017款 4.0T GT V8 标准版', label: '欧陆 2017款 4.0T GT V8 标准版' },
                  { value: '欧陆 2013款 6.0T GT Speed', label: '欧陆 2013款 6.0T GT Speed' },
                  { value: '欧陆 2017款 4.0T GT V8 S 标准版', label: '欧陆 2017款 4.0T GT V8 S 标准版' },
                  { value: '欧陆 2022款 4.0T GT V8 敞篷版', label: '欧陆 2022款 4.0T GT V8 敞篷版' },
                  { value: '欧陆 2016款 4.0T GT V8 标准版', label: '欧陆 2016款 4.0T GT V8 标准版' },
                  { value: '欧陆 2017款 6.0T GT W12 标准版', label: '欧陆 2017款 6.0T GT W12 标准版' },
                  { value: '欧陆 2012款 4.0T GTC V8', label: '欧陆 2012款 4.0T GTC V8' },
                  { value: '欧陆 2012款 6.0T GTC W12', label: '欧陆 2012款 6.0T GTC W12' },
                  { value: '欧陆 2014款 4.0T GT V8 S 尊贵版', label: '欧陆 2014款 4.0T GT V8 S 尊贵版' },
                  { value: '欧陆 2007款 GTC 6.0', label: '欧陆 2007款 GTC 6.0' },
                  { value: '欧陆 2010款 Supersports 6.0 敞篷版', label: '欧陆 2010款 Supersports 6.0 敞篷版' },
                  { value: '欧陆 2020款 4.0T GT V8 敞篷版', label: '欧陆 2020款 4.0T GT V8 敞篷版' },
                  { value: '欧陆 2022款 4.0T GT V8 Mulliner', label: '欧陆 2022款 4.0T GT V8 Mulliner' },
                  { value: '欧陆 2017款 4.0T GT V8 S 敞篷版', label: '欧陆 2017款 4.0T GT V8 S 敞篷版' },
                  { value: '欧陆 2015款 4.0T GT V8 敞篷版', label: '欧陆 2015款 4.0T GT V8 敞篷版' },
                  { value: '欧陆 2016款 6.0T GT W12 标准版', label: '欧陆 2016款 6.0T GT W12 标准版' },
                  { value: '欧陆 2022款 4.0T GT V8 Mulliner 敞篷版', label: '欧陆 2022款 4.0T GT V8 Mulliner 敞篷版' },
                  { value: '欧陆 2023款 4.0T GT V8 雅度版', label: '欧陆 2023款 4.0T GT V8 雅度版' },
                  { value: '欧陆 2017款 4.0T GT V8 敞篷版', label: '欧陆 2017款 4.0T GT V8 敞篷版' },
                  { value: '欧陆 2014款 4.0T GT V8 S 敞篷尊贵版', label: '欧陆 2014款 4.0T GT V8 S 敞篷尊贵版' },
                  { value: '欧陆 2023款 4.0T GT S V8', label: '欧陆 2023款 4.0T GT S V8' }

                ] }
                    ]
                  },
                  {
                    value: '奇瑞新能源',
                    label: '奇瑞新能源',
                    children: [
                      { value: '小蚂蚁', label: '小蚂蚁' ,children:[
                  { value: '小蚂蚁 2022款 甜粉款 半糖版 磷酸铁锂 30kW 301km', label: '小蚂蚁 2022款 甜粉款 半糖版 磷酸铁锂 30kW 301km' },
                  { value: '小蚂蚁 2018款 400 4座智享版', label: '小蚂蚁 2018款 400 4座智享版' },
                  { value: '小蚂蚁 2022款 甜粉款 全糖版 磷酸铁锂 30kW 301km', label: '小蚂蚁 2022款 甜粉款 全糖版 磷酸铁锂 30kW 301km' },
                  { value: '小蚂蚁 2022款 甜粉款 半糖版 三元锂 30kW 301km', label: '小蚂蚁 2022款 甜粉款 半糖版 三元锂 30kW 301km' },
                  { value: '小蚂蚁 2019款 4座智享版 35kWh', label: '小蚂蚁 2019款 4座智享版 35kWh' },
                  { value: '小蚂蚁 2021款 20万蚁粉款 才气版 磷酸铁锂 301km', label: '小蚂蚁 2021款 20万蚁粉款 才气版 磷酸铁锂 301km' },
                  { value: '小蚂蚁 2021款 15万蚁粉款 新蚁炫版 三元锂', label: '小蚂蚁 2021款 15万蚁粉款 新蚁炫版 三元锂' },
                  { value: '小蚂蚁 2021款 15万蚁粉款 新蚁酷版 磷酸铁锂', label: '小蚂蚁 2021款 15万蚁粉款 新蚁酷版 磷酸铁锂' },
                  { value: '小蚂蚁 2017款 2座智炫版', label: '小蚂蚁 2017款 2座智炫版' }
                ]
                }
                    ]
                  },

                  {
                    value: '捷豹',
                    label: '捷豹',
                    children: [
                      { value: '捷豹XEL', label: '捷豹XEL',children:[
                  { value: '捷豹XJ 2019款 3.0L 自动', label: '捷豹XJ 2019款 3.0L 自动' },
                  { value: '捷豹XJ 1994款 4.0L 自动', label: '捷豹XJ 1994款 4.0L 自动' },
                  { value: '捷豹XJ 2004款 3.0L 自动', label: '捷豹XJ 2004款 3.0L 自动' },
                  { value: '捷豹XK 2006款 4.2L 自动', label: '捷豹XK 2006款 4.2L 自动' }
                ]
                }
          ]
        },
],
      colorValue_e2: [],
      colorOptions: [
        { value: "black", label: "黑色" },
        { value: "white", label: "白色" },
        { value: "red/purple", label: "红/紫色" },
        { value: "blue", label: "蓝色" },
        { value: "silver/gray", label: "银/灰色" },
        { value: "champagne/brown", label: "香槟/棕色" },
        { value: "yellow/orange", label: "黄/橙色" },
        { value: "green", label: "绿色" },
        { value: "other", label: "其他" },
      ],
      timeValue_e2: [],

      tableData: [
        {
          car_name: "奥迪A7L2022款45TFSI quattro S-line风骑士",
          car_info: "1.50万公里/2022-06/北京",
          refer_price: "31.43-38.29万",
          operate: "查看详情",
        },
        {
          car_name: "斑马2022款1.5L舒适型双排栏板DAM15KR",
          car_info: "1.70万公里/2021-07/北京",
          refer_price: "2.38-2.96万",
          operate: "查看详情",
        },
      ],
      inputmiles_e2: "",
      inputtime_e2: "",
      form: {
        name: "",
        region: "",
        date1: "",
        date2: "",
        delivery: false,
        type: [],
        resource: "",
        desc: "",
      },
    };
  },
  created() {
    console.log("我在created里面");
    this.getPopular();
    // this.initialize();
    this.getRandomImageUrls();
    console.log(this.selectedData);
    console.log("我在created外面");
  },
  mounted() {
    this.$nextTick(() => {
      this.locationValue_e2 = this.$route.params.locationValue;
      this.modelValue_e2 = this.$route.params.modelValue;
      this.colorValue_e2 = this.$route.params.colorValue;
      this.timeValue_e2 = this.$route.params.timeValue;
      this.inputtime_e2 = this.$route.params.inputTime;
      this.inputmiles_e2 = this.$route.params.inputMiles;

      // Generate minPredictedPrice using a normal distribution with mean 15
      let minPredictedPrice = Math.abs(this.generateNormalDistribution(15, 45));
      while (minPredictedPrice < 5) {
        minPredictedPrice = Math.abs(this.generateNormalDistribution(15, 45));
      }
      minPredictedPrice = minPredictedPrice.toFixed(2); // Round to two decimal places

      // Calculate maxPredictedPrice based on minPredictedPrice
      let maxPredictedPrice = (parseFloat(minPredictedPrice) + 30).toFixed(2); // Round to two decimal places

      this.minPredictedPrice = minPredictedPrice;
      this.maxPredictedPrice = maxPredictedPrice;
      this.updatePercentages();
      this.evaluateCar();
      console.log("传递完毕");
    });
  },
  computed: {
    // 计算属性，生成随机整数百分比值
    randomPercent1() {
      return Math.floor(Math.random() * 50) + 10;
    },
    randomPercent2() {
      let maxPercent = Math.min(25, 80 - this.percent1 - 10); // 设置最大百分比为25或剩余百分比的较小值
      return Math.floor(Math.random() * maxPercent) + 10;
    },
    randomPercent3() {
      return 85 - this.percent1 - this.percent2;
    },
  },
  methods: {
    updatePercentages() {
      this.percent1 = this.randomPercent1;
      this.percent2 = this.randomPercent2;
      this.percent3 = this.randomPercent3;
    },
    generateNormalDistribution(mean, standardDeviation) {
    let u = 0,
      v = 0;
    while (u === 0) u = Math.random();
    while (v === 0) v = Math.random();
    let num = Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
    return num * standardDeviation + mean;
  },
    evaluateCar() {
    // 获取参数
    const province_name = this.locationValue_e2;
    const location = this.locationValue_e2;
    const brand = this.modelValue_e2;
    const model = this.modelValue_e2;
    const update_year = this.timeValue_e2.split("-")[0];
    const update_month = this.timeValue_e2.split("-")[1];

    // 调用路由执行 Python 脚本
    this.$axios
      .get("/api/pyscripts/evaluate", {
        params: {
          province_name,
          location,
          brand,
          model,
          update_year,
          update_month,
        },
      })
      .then((response) => {
        // 解析评估结果
        const result = response.data;
        const { min, max } = JSON.parse(result);

        // 将结果保存到对应的变量中
        this.minPredictedPrice = min;
        this.maxPredictedPrice = max;

        console.log("评估结果：", min, max);
      })
      .catch((error) => {
        console.error("评估出错：", error);
      });
  },



    async initialize() {
      await this.getPopular_test();
      console.log("我getpopular");
    },


    match_chn_char(chn) {
      for (let i = 0; i < data.length; i++) {
        let tmp_dict = data[i];
        if (tmp_dict.get("value") === chn) {
          return tmp_dict.get("label");
        }
      }
      return "Unknown";
    },
	  getPopular() {
      console.log("getpopular运行");
      this.$axios("/api/populars")
        .then((res) => {
          this.hotdata = res.data;
          // 使用 reduce 方法进行分组和筛选
          const uniqueCarNames = this.hotdata.reduce((result, item) => {
            if (
              !result.includes(item.car_name) &&
              item.car_img !== "https://imgs.icauto.com.cn/shcarimg/nofind.png"
            ) {
              result.push(item.car_name);
            }
            return result;
          }, []);

          const selectNum = 6;
          const selectedData = [];
          while (selectedData.length < selectNum) {
            const randomIndex = Math.floor(
              Math.random() * uniqueCarNames.length
            );
            const selectedCarName = uniqueCarNames[randomIndex];

            //获取整条数据，添加到数组中
            const data = this.hotdata.find(
              (item) => item.car_name === selectedCarName
            );
            selectedData.push(data);
          }

          this.selectedData = selectedData;
		  this.imgTag = '<img src="'+this.selectedData[0].car_img+'" alt="" style="width: 120px; height: 90px">';
        })
        .catch((error) => {
          console.error("Failed to fetch data:", error);
        });
    },
    jump(name, num) {
      // this.$router.push({ path: "/hotcarinfo/" + encodeURIComponent(name) });
      this.$router.push({
        path: "/hotcarinfo/" + encodeURIComponent(name),
        query: {
          img: this.remainingCars[num]
        }
      });
    },
    getRandomImageUrls() {
      this.$axios.get('/api/cars')
        .then((response) => {
          const randomCars = response.data;
          const imgUrls = randomCars.map(car => car.img_url[0]);
          console.log(imgUrls);

          const remainingCars = [];
          while (remainingCars.length < 3 && imgUrls.length > 0) { // 修改此处
            const randomIndex = Math.floor(Math.random() * imgUrls.length);
            const randomCar = imgUrls[randomIndex]; // 修改此处
            remainingCars.push(randomCar);
            imgUrls.splice(randomIndex, 1); // 修改此处
          }
          this.remainingCars = remainingCars;
          console.log(this.remainingCars);
        })
        .catch((error) => {
          console.error('Failed to get random image URLs:', error);
        });
    }
  },
  onSubmitAgain() {
    //参数
    const routeParams = {
      locationValue_2: this.locationValue_e2,
      timeValue_2: this.timeValue_e2,
      modelValue_2: this.modelValue_e2,
      input_2: this.input_e,
    };

    this.handleCreatedLogic();
    // 页面跳转
    this.$router.push({
      name: "evaluatedetail", // 跳哪
      params: routeParams,
    });
  },

  async getPopular_test() {
    return new Promise(async (resolve) => {
      console.log("getpopular运行");
      try {
        const res = await this.$axios("/api/populars");
        this.hotdata_test = res.data;
        // 分组和筛选逻辑...

        const uniqueCarNames = this.hotdata_test.reduce((result, item) => {
          if (
            !result.includes(item.car_name) &&
            item.car_img !== "https://imgs.icauto.com.cn/shcarimg/nofind.png"
          ) {
            result.push(item.car_name);
          }
          return result;
        }, []);

        const selectNum_test = 3;
        const selectedData_test = [];
        while (selectedData_test.length < selectNum_test) {
          const randomIndex = Math.floor(Math.random() * uniqueCarNames.length);
          const selectedCarName = uniqueCarNames[randomIndex];

          //获取整条数据，添加到数组中
          const data = this.hotdata_test.find(
            (item) => item.car_name === selectedCarName
          );
          selectedData_test.push(data);
        }

        // console.log(selectedData[0].car_img);
        // selectedData.forEach((data) => {
        //   console.log(data);
        // });

        this.selectedData = selectedData_test;

        console.log("异步操作已完成");
        resolve();
      } catch (error) {
        console.error("Failed to fetch data:", error);
        resolve();
      }
    });
    
  },


//   getPopular() {
//       console.log("getpopluar运行");
//       this.$axios("/api/populars")
//         .then((res) => {
//           this.hotdata = res.data;
//           // 使用 reduce 方法进行分组和筛选
//           const uniqueCarNames = this.hotdata.reduce((result, item) => {
//             if (
//               !result.includes(item.car_name) &&
//               item.car_img !== "https://imgs.icauto.com.cn/shcarimg/nofind.png"
//             ) {
//               result.push(item.car_name);
//             }
//             return result;
//           }, []);

//           const selectNum = 6;
//           const selectedData = [];
//           while (selectedData.length < selectNum) {
//             const randomIndex = Math.floor(
//               Math.random() * uniqueCarNames.length
//             );
//             const selectedCarName = uniqueCarNames[randomIndex];

//             //获取整条数据，添加到数组中
//             const data = this.hotdata.find(
//               (item) => item.car_name === selectedCarName
//             );
//             selectedData.push(data);
//           }

//           // console.log(selectedData[0].car_img);
//           // selectedData.forEach((data) => {
//           //   console.log(data);
//           // });

//           this.selectedData = selectedData;
//         })
//         .catch((error) => {
//           console.error("Failed to fetch data:", error);
//         });
//     },

};
</script>
