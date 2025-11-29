<template>
  <el-container>
    <el-header>
      <div class="container">
        <el-menu class="navigation" mode="horizontal" :default-active="activeIndex" @select="handleSelect"
          background-color="rgba(245, 246, 252, 1)" text-color="#1D1E21" active-text-color="rgba(255, 101, 27, 1)">
          <el-menu-item index="1"><a href="http://localhost:8080/home">首页</a></el-menu-item>
          <el-menu-item index="2"><a>我要买车</a></el-menu-item>
          <el-menu-item index="3"><a href="http://localhost:8080/sellcar">我要卖车</a></el-menu-item>
          <el-menu-item index="4"><a href="http://localhost:8080/boardoverview">数据看板</a></el-menu-item>
          <el-menu-item index="5"><a href="http://localhost:8080/pricepredict">价格趋势预测</a></el-menu-item>
          <el-menu-item index="6"><a href="http://localhost:8080/login">登录/注册</a></el-menu-item>
        </el-menu>
      </div>
    </el-header>
    <div class="background-image">
      <img src="../assets/Image.jpg" alt="" class="background-img">
    </div>
    <el-main>
      <el-row class="parallel-container" justify="center">
        <el-col :span="11" class="center-div">
          <el-form ref="form" :model="form" style="margin-top: 20px; color: rgb(0, 0, 0)">
            <el-row class="center-row">
              <h1 class="car-info">请输入想要预测的车辆信息</h1>
            </el-row>
            <el-row>
              <el-col :span="12">
                <h3 class="third-title">品牌车型</h3>
                <el-form-item style="line-height:20px; margin-top: 10px; margin-left: 10px;">
                  <el-cascader v-model="formData.model" :options="modelOptions" @change="handleChange2" clearable
                    style="width: 200px;"></el-cascader>
                </el-form-item>
              </el-col>
              <el-col :span="8">
                <h3 class="third-title">上牌时间</h3>
                <el-form-item style="line-height:20px; margin-top: 10px; margin-left: 10px;">
                  <el-cascader v-model="formData.time" :options="timeOptions" @change="handleChange2" clearable
                    style="width: 200px;"></el-cascader>

                </el-form-item>

              </el-col>
            </el-row>



            <el-row>
              <el-col :span="12">
                <h3 class="third-title">地理位置</h3>
                <el-form-item prop="location" style="line-height: 20px; margin-left: 10px;">
                  <el-cascader v-model="formData.location" :options="locationOptions" placeholder="请选择地理位置" clearable
                    style="width: 200px;"></el-cascader>
                </el-form-item>

              </el-col>
              <el-col :span="12">
                <h3 class="third-title">转手次数</h3>
                <el-form-item prop="numberOfTransfer" style="line-height: 20px; margin-left: 10px;">
                  <el-select v-model="formData.numberOfTransfer" placeholder="请选择转手次数" clearable style="width: 200px;">
                    <el-option label="0" value=0></el-option>
                    <el-option label="1" value=1></el-option>
                    <el-option label="2" value=2></el-option>
                    <el-option label="其他" value=-1></el-option>
                  </el-select>
                </el-form-item>
                <h2 class="second-title">&nbsp;</h2>
                <h3 class="third-title" style="margin-bottom: 100px;">&nbsp;</h3>
              </el-col>

            </el-row>


            <!-- 
                        <el-col :span="8">              
                            <h2 class="second-title">&nbsp;</h2>
                            <h3 class="third-title">车系</h3>
                            <el-form-item style="line-height:20px; margin-top: 10px; margin-left: 5px;">
                                <el-cascader></el-cascader>
                            </el-form-item>
                            <h2 class="second-title">&nbsp;</h2>
                            <h3 class="third-title">月份</h3>
                            <el-form-item style="line-height:20px; margin-top: 10px; margin-left: 5px;">
                                <el-cascader></el-cascader>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <h2 class="second-title">&nbsp;</h2>
                            <h3 class="third-title">车型</h3>
                            <el-form-item style="line-height:20px; margin-top: 10px; margin-left: 5px;">
                              <el-cascader></el-cascader>
                            </el-form-item>
                            <h2 class="second-title">&nbsp;</h2>
                            <h3 class="third-title" style="margin-bottom: 180px;">&nbsp;</h3>
                        </el-col>-->


            <el-row>
              <el-form-item>
                <div class="button-div">
                  <el-button @click="onSubmit" style="background-color: #FFFFFF;  height: 50px; font-size: 18px; color: #1c1a1a; 
                                width: 200px;font-weight: bold;">
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
          <el-row class="parallel-container" style="margin-top: 50px;">
            <el-col :span="12" class="left-div">
              <e-charts class="chart" :option="option2" />
            </el-col>
            <el-col :span="12" class="left-div">
              <e-charts class="chart" :option="option1" />
            </el-col>

          </el-row>
          <el-row id="bottom-element" class="parallel-container" style="margin-top: 30px;">
            <el-col :span="24" class="bottom-div" style="background-color: #FFFFFF; border-radius: 10px; padding-top: 4px;
    padding-bottom: 20px;">
              <h1 class="h1" style="margin-left: 25px;">价格走势提醒与建议</h1>
              <h2 class="text" style="margin-left:20px; font:13px">
                1、限迁政策对该车型二手车价格走势产生了较大的影响<br>
                2、新型车型正在逐渐取代该车型，影响了该二手车型的市场价格走势<br>
                3、车辆的性能表现较好，该类型二手车相较于整体市场贬值相对缓慢<br>
              </h2>
            </el-col>
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
  font-family: "Microsoft YaHei";
  /* 设置文字字体 */
  font-size: 16px;
  /* 设置文字大小 */
  font-weight: bold;
  /* 设置文字加粗 */
  text-decoration: none;
  /* 取消文字下划线 */
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
  margin-left: 5px;
  margin-bottom: 4px;
  font-size: 16px;
  font-family: "Microsoft YaHei";
}

.third-title {
  line-height: 25px;
  margin-left: 10px;
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
  background-color: #FFFFFF;
  border-radius: 10px;
  margin-right: 20px;
  padding: 1px;
  text-align: left;
  width: 800px;
  height: 270px;
}

.right-div {
  background-color: #FFFFFF;
  border-radius: 10px;
  margin-right: 20px;
  padding: 10px;
  text-align: left;
  width: 800px;
  height: 600px;
}

.bottom-div {
  background-color: #FFFFFF;
  border-radius: 10px;
  margin-right: 20px;
  padding: 10px;
  text-align: left;
  width: auto;
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
  margin-top: 10px;
  /*height: 1000px; 调整下方内容的高度 */
  overflow: hidden;
}

.slide-enter-active,
.slide-leave-active {
  transition: all 0.5s;
}

.slide-enter,
.slide-leave-to {
  transform: translateY(200px);
  /* 调整下方内容向下滑动的距离 */
}

.chart {
  margin-top: 1px;
  height: 250px;
}
</style>




<script>
export default {
  name: 'pricepredict',
  data() {
    return {
      data: [],
      data1: [],
      data2: [],
      showingDetails: false,
      formData: {
        model: [],
        time: [],
        numberOfTransfer: '',
        location: [],
      },
      locationOptions: [
        {
          value: '安徽',
          label: '安徽',
          children: [
            { value: '合肥', label: '合肥' },
            { value: '芜湖', label: '芜湖' },
            { value: '蚌埠', label: '蚌埠' },
            { value: '淮南', label: '淮南' },
            { value: '马鞍山', label: '马鞍山' },
            { value: '淮北', label: '淮北' },
            { value: '铜陵', label: '铜陵' },
            { value: '安庆', label: '安庆' },
            { value: '黄山', label: '黄山' },
            { value: '滁州', label: '滁州' },
            { value: '阜阳', label: '阜阳' },
            { value: '宿州', label: '宿州' },
            { value: '六安', label: '六安' },
            { value: '亳州', label: '亳州' },
            { value: '池州', label: '池州' },
            { value: '宣城', label: '宣城' }
          ]
        },
        {
          value: '北京',
          label: '北京',
          children: [
            { value: '北京', label: '北京' }
          ]
        },
        {
          value: '重庆',
          label: '重庆',
          children: [
            { value: '重庆', label: '重庆' }
          ]
        },
        {
          value: '福建',
          label: '福建',
          children: [
            { value: '福州', label: '福州' },
            { value: '厦门', label: '厦门' },
            { value: '莆田', label: '莆田' },
            { value: '三明', label: '三明' },
            { value: '泉州', label: '泉州' },
            { value: '漳州', label: '漳州' },
            { value: '南平', label: '南平' },
            { value: '龙岩', label: '龙岩' },
            { value: '宁德', label: '宁德' }
          ]
        },
        {
          value: '广东',
          label: '广东',
          children: [
            { value: '广州', label: '广州' },
            { value: '韶关', label: '韶关' },
            { value: '深圳', label: '深圳' },
            { value: '珠海', label: '珠海' },
            { value: '汕头', label: '汕头' },
            { value: '佛山', label: '佛山' },
            { value: '江门', label: '江门' },
            { value: '湛江', label: '湛江' },
            { value: '茂名', label: '茂名' },
            { value: '肇庆', label: '肇庆' },
            { value: '惠州', label: '惠州' },
            { value: '梅州', label: '梅州' },
            { value: '汕尾', label: '汕尾' },
            { value: '河源', label: '河源' },
            { value: '阳江', label: '阳江' },
            { value: '清远', label: '清远' },
            { value: '东莞', label: '东莞' },
            { value: '中山', label: '中山' },
            { value: '潮州', label: '潮州' },
            { value: '揭阳', label: '揭阳' },
            { value: '云浮', label: '云浮' }
          ]
        },
        {
          value: '广西',
          label: '广西',
          children: [
            { value: '南宁', label: '南宁' },
            { value: '柳州', label: '柳州' },
            { value: '桂林', label: '桂林' },
            { value: '梧州', label: '梧州' },
            { value: '北海', label: '北海' },
            { value: '防城港', label: '防城港' },
            { value: '钦州', label: '钦州' },
            { value: '贵港', label: '贵港' },
            { value: '玉林', label: '玉林' },
            { value: '百色', label: '百色' },
            { value: '贺州', label: '贺州' },
            { value: '河池', label: '河池' },
            { value: '来宾', label: '来宾' },
            { value: '崇左', label: '崇左' }
          ]
        },
        {
          value: '贵州',
          label: '贵州',
          children: [
            { value: '贵阳', label: '贵阳' },
            { value: '六盘水', label: '六盘水' },
            { value: '遵义', label: '遵义' },
            { value: '安顺', label: '安顺' },
            { value: '毕节', label: '毕节' },
            { value: '铜仁', label: '铜仁' },
            { value: '黔西南', label: '黔西南' },
            { value: '黔东南', label: '黔东南' },
            { value: '黔南', label: '黔南' }
          ]
        },
        {
          value: '甘肃',
          label: '甘肃',
          children: [
            { value: '兰州', label: '兰州' },
            { value: '嘉峪关', label: '嘉峪关' },
            { value: '金昌', label: '金昌' },
            { value: '白银', label: '白银' },
            { value: '天水', label: '天水' },
            { value: '武威', label: '武威' },
            { value: '张掖', label: '张掖' },
            { value: '平凉', label: '平凉' },
            { value: '酒泉', label: '酒泉' },
            { value: '庆阳', label: '庆阳' },
            { value: '定西', label: '定西' },
            { value: '陇南', label: '陇南' },
            { value: '临夏', label: '临夏' },
            { value: '甘南', label: '甘南' }
          ]
        },
        {
          value: '海南', label: '海南',
          children: [
            { value: '海口', label: '海口' },
            { value: '三亚', label: '三亚' },
            { value: '三沙', label: '三沙' },
            { value: '儋州', label: '儋州' },
            { value: '五指山', label: '五指山' },
            { value: '琼海', label: '琼海' },
            { value: '文昌', label: '文昌' },
            { value: '万宁', label: '万宁' },
            { value: '东方', label: '东方' },
            { value: '定安', label: '定安' },
            { value: '屯昌', label: '屯昌' },
            { value: '澄迈', label: '澄迈' },
            { value: '临高', label: '临高' },
            { value: '白沙', label: '白沙' },
            { value: '昌江', label: '昌江' },
            { value: '乐东', label: '乐东' },
            { value: '陵水', label: '陵水' },
            { value: '保亭', label: '保亭' },
            { value: '琼中', label: '琼中' }
          ]
        },
        {
          value: '河南', label: '河南',
          children: [
            { value: '郑州', label: '郑州' },
            { value: '开封', label: '开封' },
            { value: '洛阳', label: '洛阳' },
            { value: '平顶山', label: '平顶山' },
            { value: '安阳', label: '安阳' },
            { value: '鹤壁', label: '鹤壁' },
            { value: '新乡', label: '新乡' },
            { value: '焦作', label: '焦作' },
            { value: '濮阳', label: '濮阳' },
            { value: '许昌', label: '许昌' },
            { value: '漯河', label: '漯河' },
            { value: '三门峡', label: '三门峡' },
            { value: '南阳', label: '南阳' },
            { value: '商丘', label: '商丘' },
            { value: '信阳', label: '信阳' },
            { value: '周口', label: '周口' },
            { value: '驻马店', label: '驻马店' },
            { value: '济源', label: '济源' }
          ]
        },
        {
          value: '湖北', label: '湖北',
          children: [
            { value: '武汉', label: '武汉' },
            { value: '黄石', label: '黄石' },
            { value: '十堰', label: '十堰' },
            { value: '宜昌', label: '宜昌' },
            { value: '襄阳', label: '襄阳' },
            { value: '鄂州', label: '鄂州' },
            { value: '荆门', label: '荆门' },
            { value: '孝感', label: '孝感' },
            { value: '荆州', label: '荆州' },
            { value: '黄冈', label: '黄冈' },
            { value: '咸宁', label: '咸宁' },
            { value: '随州', label: '随州' },
            { value: '恩施', label: '恩施' },
            { value: '仙桃', label: '仙桃' },
            { value: '潜江', label: '潜江' },
            { value: '天门', label: '天门' },
            { value: '神农架', label: '神农架' }
          ]
        },
        {
          value: '湖南', label: '湖南',
          children: [
            { value: '长沙', label: '长沙' },
            { value: '株洲', label: '株洲' },
            { value: '湘潭', label: '湘潭' },
            { value: '衡阳', label: '衡阳' },
            { value: '邵阳', label: '邵阳' },
            { value: '岳阳', label: '岳阳' },
            { value: '常德', label: '常德' },
            { value: '张家界', label: '张家界' },
            { value: '益阳', label: '益阳' },
            { value: '郴州', label: '郴州' },
            { value: '永州', label: '永州' },
            { value: '怀化', label: '怀化' },
            { value: '娄底', label: '娄底' },
            { value: '湘西', label: '湘西' }
          ]
        },
        {
          value: '河北', label: '河北',
          children: [
            { value: '石家庄', label: '石家庄' },
            { value: '唐山', label: '唐山' },
            { value: '秦皇岛', label: '秦皇岛' },
            { value: '邯郸', label: '邯郸' },
            { value: '邢台', label: '邢台' },
            { value: '保定', label: '保定' },
            { value: '张家口', label: '张家口' },
            { value: '承德', label: '承德' },
            { value: '沧州', label: '沧州' },
            { value: '廊坊', label: '廊坊' },
            { value: '衡水', label: '衡水' }
          ]
        },
        {
          value: '黑龙江', label: '黑龙江',
          children: [
            { value: '哈尔滨', label: '哈尔滨' },
            { value: '齐齐哈尔', label: '齐齐哈尔' },
            { value: '鸡西', label: '鸡西' },
            { value: '鹤岗', label: '鹤岗' },
            { value: '双鸭山', label: '双鸭山' },
            { value: '大庆', label: '大庆' },
            { value: '伊春', label: '伊春' },
            { value: '佳木斯', label: '佳木斯' },
            { value: '七台河', label: '七台河' },
            { value: '牡丹江', label: '牡丹江' },
            { value: '黑河', label: '黑河' },
            { value: '绥化', label: '绥化' },
            { value: '大兴安岭', label: '大兴安岭' }
          ]
        },
        {
          value: '江苏', label: '江苏',
          children: [
            { value: '南京', label: '南京' },
            { value: '无锡', label: '无锡' },
            { value: '徐州', label: '徐州' },
            { value: '常州', label: '常州' },
            { value: '苏州', label: '苏州' },
            { value: '南通', label: '南通' },
            { value: '连云港', label: '连云港' },
            { value: '淮安', label: '淮安' },
            { value: '盐城', label: '盐城' },
            { value: '扬州', label: '扬州' },
            { value: '镇江', label: '镇江' },
            { value: '泰州', label: '泰州' },
            { value: '宿迁', label: '宿迁' }
          ]
        },
        {
          value: '江西', label: '江西',
          children: [
            { value: '南昌', label: '南昌' },
            { value: '景德镇', label: '景德镇' },
            { value: '萍乡', label: '萍乡' },
            { value: '九江', label: '九江' },
            { value: '新余', label: '新余' },
            { value: '鹰潭', label: '鹰潭' },
            { value: '赣州', label: '赣州' },
            { value: '吉安', label: '吉安' },
            { value: '宜春', label: '宜春' },
            { value: '抚州', label: '抚州' },
            { value: '上饶', label: '上饶' }
          ]
        },
        {
          value: '吉林', label: '吉林',
          children: [
            { value: '长春', label: '长春' },
            { value: '吉林', label: '吉林' },
            { value: '四平', label: '四平' },
            { value: '辽源', label: '辽源' },
            { value: '通化', label: '通化' },
            { value: '白山', label: '白山' },
            { value: '松原', label: '松原' },
            { value: '白城', label: '白城' },
            { value: '延边', label: '延边' }
          ]
        },
        {
          value: '辽宁', label: '辽宁',
          children: [
            { value: '沈阳', label: '沈阳' },
            { value: '大连', label: '大连' },
            { value: '鞍山', label: '鞍山' },
            { value: '抚顺', label: '抚顺' },
            { value: '本溪', label: '本溪' },
            { value: '丹东', label: '丹东' },
            { value: '锦州', label: '锦州' },
            { value: '营口', label: '营口' },
            { value: '阜新', label: '阜新' },
            { value: '辽阳', label: '辽阳' },
            { value: '盘锦', label: '盘锦' },
            { value: '铁岭', label: '铁岭' },
            { value: '朝阳', label: '朝阳' },
            { value: '葫芦岛', label: '葫芦岛' }
          ]
        },
        {
          value: '内蒙古', label: '内蒙古',
          children: [
            { value: '呼和浩特', label: '呼和浩特' },
            { value: '包头', label: '包头' },
            { value: '乌海', label: '乌海' },
            { value: '赤峰', label: '赤峰' },
            { value: '通辽', label: '通辽' },
            { value: '鄂尔多斯', label: '鄂尔多斯' },
            { value: '呼伦贝尔', label: '呼伦贝尔' },
            { value: '巴彦淖尔', label: '巴彦淖尔' },
            { value: '乌兰察布', label: '乌兰察布' },
            { value: '兴安盟', label: '兴安盟' },
            { value: '锡林郭勒盟', label: '锡林郭勒盟' },
            { value: '阿拉善盟', label: '阿拉善盟' }
          ]
        },
        {
          value: '宁夏', label: '宁夏',
          children: [
            { value: '银川', label: '银川' },
            { value: '石嘴山', label: '石嘴山' },
            { value: '吴忠', label: '吴忠' },
            { value: '固原', label: '固原' },
            { value: '中卫', label: '中卫' }
          ]
        },
        {
          value: '青海', label: '青海',
          children: [
            { value: '西宁', label: '西宁' },
            { value: '海东', label: '海东' },
            { value: '海北', label: '海北' },
            { value: '黄南', label: '黄南' },
            { value: '海南', label: '海南' },
            { value: '果洛', label: '果洛' },
            { value: '玉树', label: '玉树' },
            { value: '海西', label: '海西' }
          ]
        },
        {
          value: '陕西',
          label: '陕西',
          children: [
            { value: '西安', label: '西安' },
            { value: '铜川', label: '铜川' },
            { value: '宝鸡', label: '宝鸡' },
            { value: '咸阳', label: '咸阳' },
            { value: '渭南', label: '渭南' },
            { value: '延安', label: '延安' },
            { value: '汉中', label: '汉中' },
            { value: '榆林', label: '榆林' },
            { value: '安康', label: '安康' },
            { value: '商洛', label: '商洛' },
            { value: '西咸新区', label: '西咸新区' }
          ]
        },
        {
          value: '四川',
          label: '四川',
          children: [
            { value: '成都', label: '成都' },
            { value: '自贡', label: '自贡' },
            { value: '攀枝花', label: '攀枝花' },
            { value: '泸州', label: '泸州' },
            { value: '德阳', label: '德阳' },
            { value: '绵阳', label: '绵阳' },
            { value: '广元', label: '广元' },
            { value: '遂宁', label: '遂宁' },
            { value: '内江', label: '内江' },
            { value: '乐山', label: '乐山' },
            { value: '南充', label: '南充' },
            { value: '眉山', label: '眉山' },
            { value: '宜宾', label: '宜宾' },
            { value: '广安', label: '广安' },
            { value: '达州', label: '达州' },
            { value: '雅安', label: '雅安' },
            { value: '巴中', label: '巴中' },
            { value: '资阳', label: '资阳' },
            { value: '阿坝', label: '阿坝' },
            { value: '甘孜', label: '甘孜' },
            { value: '凉山', label: '凉山' }
          ]
        },
        {
          value: '上海',
          label: '上海',
          children: [
            { value: '上海', label: '上海' }
          ]
        },
        {
          value: '山西',
          label: '山西',
          children: [
            { value: '太原', label: '太原' },
            { value: '大同', label: '大同' },
            { value: '阳泉', label: '阳泉' },
            { value: '长治', label: '长治' },
            { value: '晋城', label: '晋城' },
            { value: '朔州', label: '朔州' },
            { value: '晋中', label: '晋中' },
            { value: '运城', label: '运城' },
            { value: '忻州', label: '忻州' },
            { value: '临汾', label: '临汾' },
            { value: '吕梁', label: '吕梁' }
          ]
        },
        {
          value: '山东',
          label: '山东',
          children: [
            { value: '济南', label: '济南' },
            { value: '青岛', label: '青岛' },
            { value: '淄博', label: '淄博' },
            { value: '枣庄', label: '枣庄' },
            { value: '东营', label: '东营' },
            { value: '烟台', label: '烟台' },
            { value: '潍坊', label: '潍坊' },
            { value: '济宁', label: '济宁' },
            { value: '泰安', label: '泰安' },
            { value: '威海', label: '威海' },
            { value: '日照', label: '日照' },
            { value: '莱芜', label: '莱芜' },
            { value: '临沂', label: '临沂' },
            { value: '德州', label: '德州' },
            { value: '聊城', label: '聊城' },
            { value: '滨州', label: '滨州' },
            { value: '菏泽', label: '菏泽' }
          ]
        },
        {
          value: '天津',
          label: '天津',
          children: [
            { value: '天津', label: '天津' }
          ]
        },
        {
          value: '新疆',
          label: '新疆',
          children: [
            { value: '乌鲁木齐', label: '乌鲁木齐' },
            { value: '克拉玛依', label: '克拉玛依' },
            { value: '吐鲁番', label: '吐鲁番' },
            { value: '哈密', label: '哈密' },
            { value: '昌吉', label: '昌吉' },
            { value: '博尔塔拉', label: '博尔塔拉' },
            { value: '巴音郭楞', label: '巴音郭楞' },
            { value: '阿克苏', label: '阿克苏' },
            { value: '克孜勒苏', label: '克孜勒苏' },
            { value: '喀什', label: '喀什' },
            { value: '和田', label: '和田' },
            { value: '伊犁', label: '伊犁' },
            { value: '塔城', label: '塔城' },
            { value: '阿勒泰', label: '阿勒泰' },
            { value: '石河子', label: '石河子' },
            { value: '阿拉尔', label: '阿拉尔' },
            { value: '图木舒克', label: '图木舒克' },
            { value: '五家渠', label: '五家渠' },
            { value: '北屯', label: '北屯' },
            { value: '铁门关', label: '铁门关' },
            { value: '双河', label: '双河' },
            { value: '可克达拉', label: '可克达拉' },
            { value: '昆玉', label: '昆玉' }
          ]
        },
        {
          value: '西藏',
          label: '西藏',
          children: [
            { value: '拉萨', label: '拉萨' },
            { value: '日喀则', label: '日喀则' },
            { value: '昌都', label: '昌都' },
            { value: '林芝', label: '林芝' },
            { value: '山南', label: '山南' },
            { value: '那曲', label: '那曲' },
            { value: '阿里', label: '阿里' }
          ]
        },
        {
          value: '云南',
          label: '云南',
          children: [
            { value: '昆明', label: '昆明' },
            { value: '曲靖', label: '曲靖' },
            { value: '玉溪', label: '玉溪' },
            { value: '保山', label: '保山' },
            { value: '昭通', label: '昭通' },
            { value: '丽江', label: '丽江' },
            { value: '普洱', label: '普洱' },
            { value: '临沧', label: '临沧' },
            { value: '楚雄', label: '楚雄' },
            { value: '红河', label: '红河' },
            { value: '文山', label: '文山' },
            { value: '西双版纳', label: '西双版纳' },
            { value: '大理', label: '大理' },
            { value: '德宏', label: '德宏' },
            { value: '怒江', label: '怒江' },
            { value: '迪庆', label: '迪庆' }
          ]
        },
        {
          value: '浙江',
          label: '浙江',
          children: [
            { value: '杭州', label: '杭州' },
            { value: '宁波', label: '宁波' },
            { value: '温州', label: '温州' },
            { value: '嘉兴', label: '嘉兴' },
            { value: '湖州', label: '湖州' },
            { value: '绍兴', label: '绍兴' },
            { value: '金华', label: '金华' },
            { value: '衢州', label: '衢州' },
            { value: '舟山', label: '舟山' },
            { value: '台州', label: '台州' },
            { value: '丽水', label: '丽水' },
            { value: '舟山群岛新区', label: '舟山群岛新区' }
          ]
        }
      ],

      modelOptions: [

        {
          value: '大众',
          label: '大众',
          children: [
            { value: '迈腾', label: '迈腾' },
            { value: '速腾', label: '速腾' },
            { value: 'T-ROC探歌', label: 'T-ROC探歌' },
            { value: '途观L', label: '途观L' },
            { value: 'Polo', label: 'Polo' },
            { value: '探岳', label: '探岳' },
            { value: '高尔夫', label: '高尔夫' },
            { value: '帕萨特', label: '帕萨特' },
            { value: '宝来', label: '宝来' },
            { value: '一汽-大众CC', label: '一汽-大众CC' },
            { value: '迈特威', label: '迈特威' },
            { value: '甲壳虫', label: '甲壳虫' },
            { value: '途观', label: '途观' },
            { value: '途锐', label: '途锐' },
            { value: '凌渡', label: '凌渡' },
            { value: '捷达', label: '捷达' },
            { value: '途昂', label: '途昂' },
            { value: '朗逸', label: '朗逸' }
          ]
        },
        {
          value: '雪佛兰',
          label: '雪佛兰',
          children: [
            { value: '迈锐宝', label: '迈锐宝' },
            { value: '科鲁兹', label: '科鲁兹' },
            { value: '迈锐宝XL', label: '迈锐宝XL' },
            { value: '科沃兹', label: '科沃兹' }
          ]
        },
        {
          value: '雷克萨斯',
          label: '雷克萨斯',
          children: [
            { value: '雷克萨斯NX', label: '雷克萨斯NX' },
            { value: '雷克萨斯RX', label: '雷克萨斯RX' },
            { value: '雷克萨斯LX', label: '雷克萨斯LX' },
            { value: '雷克萨斯ES', label: '雷克萨斯ES' },
            { value: '雷克萨斯LS', label: '雷克萨斯LS' },
            { value: '雷克萨斯CT', label: '雷克萨斯CT' },
            { value: '雷克萨斯GX', label: '雷克萨斯GX' }
          ]
        },
        {
          value: '保时捷',
          label: '保时捷',
          children: [
            { value: 'Cayenne新能源', label: 'Cayenne新能源' },
            { value: 'Taycan', label: 'Taycan' },
            { value: 'Panamera', label: 'Panamera' },
            { value: 'Macan', label: 'Macan' },
            { value: '保时捷718', label: '保时捷718' },
            { value: 'Cayenne', label: 'Cayenne' },
            { value: '保时捷911', label: '保时捷911' }
          ]
        },
        {
          value: '凯迪拉克',
          label: '凯迪拉克',
          children: [
            { value: '凯迪拉克XT5', label: '凯迪拉克XT5' },
            { value: '凯迪拉克CT6', label: '凯迪拉克CT6' },
            { value: '凯迪拉克XTS', label: '凯迪拉克XTS' },
            { value: '凯迪拉克ATS-L', label: '凯迪拉克ATS-L' },
            { value: '凯迪拉克CT5', label: '凯迪拉克CT5' }
          ]
        },
        {
          value: '别克',
          label: '别克',
          children: [
            { value: '君越', label: '君越' },
            { value: '威朗', label: '威朗' },
            { value: '英朗', label: '英朗' },
            { value: '昂科威', label: '昂科威' },
            { value: '别克GL8', label: '别克GL8' },
            { value: '君威', label: '君威' },
            { value: '凯越', label: '凯越' }
          ]
        },
        {
          value: '三菱',
          label: '三菱',
          children: [
            { value: '欧蓝德', label: '欧蓝德' }
          ]
        },
        {
          value: '丰田',
          label: '丰田',
          children: [
            { value: 'YARiS L 致炫', label: 'YARiS L 致炫' },
            { value: '埃尔法', label: '埃尔法' },
            { value: '普拉多', label: '普拉多' },
            { value: '亚洲龙', label: '亚洲龙' },
            { value: '威尔法', label: '威尔法' },
            { value: '汉兰达', label: '汉兰达' },
            { value: 'RAV4荣放', label: 'RAV4荣放' },
            { value: '凯美瑞', label: '凯美瑞' },
            { value: '皇冠', label: '皇冠' },
            { value: '兰德酷路泽(进口)', label: '兰德酷路泽(进口)' },
            { value: '威驰', label: '威驰' },
            { value: '卡罗拉', label: '卡罗拉' },
            { value: '锐志', label: '锐志' },
            { value: '雷凌', label: '雷凌' },
            { value: '普拉多(进口)', label: '普拉多(进口)' },
            { value: '丰田', label: '丰田' }
          ]
        },
        {
          value: '吉利汽车',
          label: '吉利汽车',
          children: [
            { value: '帝豪', label: '帝豪' },
            { value: '缤越', label: '缤越' },
            { value: '帝豪新能源', label: '帝豪新能源' },
            { value: '星瑞', label: '星瑞' },
            { value: '博越', label: '博越' }
          ]
        },
        {
          value: '五菱汽车',
          label: '五菱汽车',
          children: [
            { value: '宏光MINIEV', label: '宏光MINIEV' }
          ]
        },
        {
          value: '奔驰',
          label: '奔驰',
          children: [
            { value: '奔驰CLS', label: '奔驰CLS' },
            { value: '奔驰G级', label: '奔驰G级' },
            { value: '奔驰M级', label: '奔驰M级' },
            { value: '奔驰CLA', label: '奔驰CLA' },
            { value: '奔驰GLC', label: '奔驰GLC' },
            { value: '奔驰E级', label: '奔驰E级' },
            { value: '奔驰E级(进口)', label: '奔驰E级(进口)' },
            { value: '奔驰G级AMG', label: '奔驰G级AMG' },
            { value: '奔驰C级', label: '奔驰C级' },
            { value: '奔驰V级', label: '奔驰V级' },
            { value: '奔驰C级AMG', label: '奔驰C级AMG' },
            { value: '奔驰A级AMG(进口)', label: '奔驰A级AMG(进口)' },
            { value: '迈巴赫S级', label: '迈巴赫S级' },
            { value: '威霆', label: '威霆' },
            { value: '奔驰GLA', label: '奔驰GLA' },
            { value: 'AMG GT', label: 'AMG GT' },
            { value: '奔驰S级', label: '奔驰S级' },
            { value: '奔驰A级', label: '奔驰A级' },
            { value: '奔驰GLB', label: '奔驰GLB' },
            { value: '奔驰GLS', label: '奔驰GLS' },
            { value: '奔驰GLK级', label: '奔驰GLK级' },
            { value: '奔驰C级(进口)', label: '奔驰C级(进口)' },
            { value: '奔驰GLE', label: '奔驰GLE' }
          ]
        },
        {
          value: '奥迪',
          label: '奥迪',
          children: [
            { value: '奥迪A3', label: '奥迪A3' },
            { value: '奥迪A4L', label: '奥迪A4L' },
            { value: '奥迪Q5', label: '奥迪Q5' },
            { value: '奥迪Q7', label: '奥迪Q7' },
            { value: '奥迪Q3', label: '奥迪Q3' },
            { value: '奥迪A8', label: '奥迪A8' },
            { value: '奥迪A7', label: '奥迪A7' },
            { value: '奥迪A5', label: '奥迪A5' },
            { value: '奥迪Q5L', label: '奥迪Q5L' },
            { value: '奥迪Q2L', label: '奥迪Q2L' },
            { value: '奥迪A6(进口)', label: '奥迪A6(进口)' },
            { value: '奥迪S4', label: '奥迪S4' },
            { value: '奥迪A6L', label: '奥迪A6L' }
          ]
        },
        {
          value: '宝马',
          label: '宝马',
          children: [
            { value: '宝马1系(进口)', label: '宝马1系(进口)' },
            { value: '宝马X1', label: '宝马X1' },
            { value: '宝马X6', label: '宝马X6' },
            { value: '宝马4系', label: '宝马4系' },
            { value: '宝马7系', label: '宝马7系' },
            { value: '宝马X5(进口)', label: '宝马X5(进口)' },
            { value: '宝马3系', label: '宝马3系' },
            { value: '宝马5系(进口)', label: '宝马5系(进口)' },
            { value: '宝马X7', label: '宝马X7' },
            { value: '宝马1系', label: '宝马1系' },
            { value: '宝马X3', label: '宝马X3' },
            { value: '宝马5系新能源', label: '宝马5系新能源' },
            { value: '宝马2系', label: '宝马2系' },
            { value: '宝马5系', label: '宝马5系' }
          ]
        },
        {
          value: '宾利',
          label: '宾利',
          children: [
            { value: '飞驰', label: '飞驰' },
            { value: '欧陆', label: '欧陆' }
          ]
        },
        {
          value: '广汽传祺',
          label: '广汽传祺',
          children: [
            { value: '传祺GS4', label: '传祺GS4' },
            { value: '传祺GS3', label: '传祺GS3' },
            { value: '传祺M8', label: '传祺M8' }
          ]
        },
        {
          value: '日产',
          label: '日产',
          children: [
            { value: '轩逸', label: '轩逸' },
            { value: '途乐', label: '途乐' },
            { value: '骐达TIIDA', label: '骐达TIIDA' },
            { value: '逍客', label: '逍客' },
            { value: '奇骏', label: '奇骏' },
            { value: '天籁', label: '天籁' }
          ]
        },
        {
          value: '本田',
          label: '本田',
          children: [
            { value: '本田CR-V', label: '本田CR-V' },
            { value: '冠道', label: '冠道' },
            { value: '本田XR-V', label: '本田XR-V' },
            { value: '艾力绅', label: '艾力绅' },
            { value: '思域', label: '思域' },
            { value: '飞度', label: '飞度' },
            { value: '凌派', label: '凌派' },
            { value: '雅阁', label: '雅阁' },
            { value: '缤智', label: '缤智' },
            { value: '奥德赛', label: '奥德赛' }
          ]
        },
        {
          value: '劳斯莱斯',
          label: '劳斯莱斯',
          children: [
            { value: '古思特', label: '古思特' }
          ]
        },
        {
          value: '北京',
          label: '北京',
          children: [
            { value: '北京BJ40', label: '北京BJ40' }
          ]
        },

        {
          value: '名爵',
          label: '名爵',
          children: [
            { value: '名爵6', label: '名爵6' }
          ]
        },
        {
          value: '哈弗',
          label: '哈弗',
          children: [
            { value: '哈弗H6', label: '哈弗H6' }
          ]
        },
        {
          value: '坦克',
          label: '坦克',
          children: [
            { value: '坦克300', label: '坦克300' }
          ]
        },

        {
          value: '奇瑞新能源',
          label: '奇瑞新能源',
          children: [
            { value: '小蚂蚁', label: '小蚂蚁' }
          ]
        },

        {
          value: '捷豹',
          label: '捷豹',
          children: [
            { value: '捷豹XEL', label: '捷豹XEL' }
          ]
        },
        {
          value: '斯柯达',
          label: '斯柯达',
          children: [
            { value: '明锐', label: '明锐' }
          ]
        },

        {
          value: '标致',
          label: '标致',
          children: [
            { value: '标致408', label: '标致408' }
          ]
        },
        {
          value: '欧拉',
          label: '欧拉',
          children: [
            { value: '欧拉黑猫', label: '欧拉黑猫' }
          ]
        },
        {
          value: '比亚迪',
          label: '比亚迪',
          children: [
            { value: '汉', label: '汉' },
            { value: '唐新能源', label: '唐新能源' }
          ]
        },
        {
          value: '沃尔沃',
          label: '沃尔沃',
          children: [
            { value: '沃尔沃XC60', label: '沃尔沃XC60' },
            { value: '沃尔沃S90', label: '沃尔沃S90' },
            { value: '沃尔沃S60', label: '沃尔沃S60' },
            { value: '沃尔沃XC90', label: '沃尔沃XC90' }
          ]
        },
        {
          value: '特斯拉',
          label: '特斯拉',
          children: [
            { value: 'Model 3', label: 'Model 3' },
            { value: 'Model Y', label: 'Model Y' }
          ]
        },
        {
          value: '玛莎拉蒂',
          label: '玛莎拉蒂',
          children: [
            { value: '总裁', label: '总裁' },
            { value: 'Ghibli', label: 'Ghibli' }
          ]
        },
        {
          value: '现代',
          label: '现代',
          children: [
            { value: '途胜', label: '途胜' },
            { value: '朗动', label: '朗动' },
            { value: '北京现代ix35', label: '北京现代ix35' },
            { value: '索纳塔', label: '索纳塔' },
            { value: '名图', label: '名图' },
            { value: '领动', label: '领动' }
          ]
        },
        {
          value: '福特',
          label: '福特',
          children: [
            { value: 'Mustang', label: 'Mustang' },
            { value: '福睿斯', label: '福睿斯' },
            { value: '锐界', label: '锐界' },
            { value: '蒙迪欧', label: '蒙迪欧' },
            { value: '翼虎', label: '翼虎' },
            { value: '福克斯', label: '福克斯' }
          ]
        },
        {
          value: '红旗',
          label: '红旗',
          children: [
            { value: '红旗H5经典', label: '红旗H5经典' }
          ]
        },
        {
          value: '英菲尼迪',
          label: '英菲尼迪',
          children: [
            { value: '英菲尼迪Q50L', label: '英菲尼迪Q50L' }
          ]
        },
        {
          value: '荣威',
          label: '荣威',
          children: [
            { value: '荣威RX5', label: '荣威RX5' }
          ]
        },
        {
          value: '起亚',
          label: '起亚',
          children: [
            { value: '起亚K3', label: '起亚K3' },
            { value: '智跑', label: '智跑' }
          ]
        },
        {
          value: '路虎',
          label: '路虎',
          children: [
            { value: '揽胜极光', label: '揽胜极光' },
            { value: '揽胜', label: '揽胜' },
            { value: '揽胜运动版', label: '揽胜运动版' },
            { value: '发现', label: '发现' },
            { value: '发现神行', label: '发现神行' }
          ]
        },
        {
          value: '长安',
          label: '长安',
          children: [
            { value: '逸动', label: '逸动' }
          ]
        },

        {
          value: '领克',
          label: '领克',
          children: [
            { value: '领克03', label: '领克03' }
          ]
        },
        {
          value: '马自达',
          label: '马自达',
          children: [
            { value: '马自达CX-4', label: '马自达CX-4' },
            { value: '阿特兹', label: '阿特兹' },
            { value: '马自达3 昂克赛拉', label: '马自达3 昂克赛拉' },
            { value: '马自达6', label: '马自达6' }
          ]
        },
        {
          value: '魏牌',
          label: '魏牌',
          children: [
            { value: '魏牌 VV7', label: '魏牌 VV7' }
          ]
        },
        {
          value: 'GMC',
          label: 'GMC',
          children: [
            { value: 'SAVANA', label: 'SAVANA' }
          ]
        },
        {
          value: 'Jeep',
          label: 'Jeep',
          children: [
            { value: '牧马人', label: '牧马人' }
          ]
        },
        {
          value: 'MINI',
          label: 'MINI',
          children: [
            { value: 'MINI COUNTRYMAN', label: 'MINI COUNTRYMAN' },
            { value: 'MINI', label: 'MINI' },
            { value: 'MINI CLUBMAN', label: 'MINI CLUBMAN' }
          ]
        },
        {
          value: 'RAM',
          label: 'RAM',
          children: [
            { value: 'RAM Trucks', label: 'RAM Trucks' }
          ]
        },
        {
          value: 'smart',
          label: 'smart',
          children: [
            { value: 'smart fortwo', label: 'smart fortwo' }
          ]
        },
      ],

      timeOptions: [],
      input: '',
    };
  },
  mounted() {
    this.generateTimeOptions();
  },
  computed: {
    option1() {
      if (!this.data1 || this.data1.length === 0) {
        return {
          title: {
            top: '5%',
            left: '5%',
            text: '历史价格走势'
          },
          graphic: {
            type: 'text',
            left: 'center',
            top: 'center',
            style: {
              fill: '#666',
              text: '暂无数据，如想查看历史走势请减少筛选条件后重试',
              font: 'bold 17px Microsoft YaHei',
            },
          },
        };
      }
      return {
        title: {
          top: '5%',
          left: '5%',
          text: '历史价格走势'
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: ['price']
        },
        grid: {
          left: '3%',
          right: '5%',
          bottom: '3%',
          containLabel: true
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: this.data1.map(d => d.time)
        },
        yAxis: {
          type: 'value',
          /*
          min: 0,  //取0为最小刻度
          max: 100, //取100为最大刻度

          min: 'dataMin', //取最小值为最小刻度
          max: 'dataMax', //取最大值为最大刻度

          min: function (value) {//取最小值向下取整为最小刻度
            return Math.floor(value.min)
          },
          max: function (value) {//取最大值向上取整为最大刻度
            return Math.ceil(value.max)
          },
          min: (value) => { // 百位起最小值向下取整
            return Math.floor(value.min / 100) * 100;
          },
          max: (value) => {  // 百位起最大值向上取整
            return Math.ceil(value.max / 100) * 100;
          },
          min: (value) => { //当数据位数不固定时,最小值向下取整
            let num = 10 ** (value.min.toString().length - 2)
            return Math.floor(value.min / num) * num;
          },
          max: (value) => { //当数据位数不固定时,最大值向上取整
            let num = 10 ** (value.max.toString().length - 2)
            return Math.ceil(value.max / num) * num;
          },*/
          scale: true, //自适应
        },
        series: [
          {
            name: 'price',
            type: 'line',
            stack: 'Total',
            data: this.data1.map(d => d.price)
          },
        ]
      };
    },
    option2() {
      return {
        title: {
          top: '5%',
          left: '5%',
          text: '预测价格走势'
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: ['price']
        },
        grid: {
          left: '3%',
          right: '5%',
          bottom: '3%',
          containLabel: true
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: this.data2.map(d => d.time)
        },
        yAxis: {
          type: 'value',
          /*
          min: 0,  //取0为最小刻度
          max: 100, //取100为最大刻度

          min: 'dataMin', //取最小值为最小刻度
          max: 'dataMax', //取最大值为最大刻度

          min: function (value) {//取最小值向下取整为最小刻度
            return Math.floor(value.min)
          },
          max: function (value) {//取最大值向上取整为最大刻度
            return Math.ceil(value.max)
          },
          min: (value) => { // 百位起最小值向下取整
            return Math.floor(value.min / 100) * 100;
          },
          max: (value) => {  // 百位起最大值向上取整
            return Math.ceil(value.max / 100) * 100;
          },
          min: (value) => { //当数据位数不固定时,最小值向下取整
            let num = 10 ** (value.min.toString().length - 2)
            return Math.floor(value.min / num) * num;
          },
          max: (value) => { //当数据位数不固定时,最大值向上取整
            let num = 10 ** (value.max.toString().length - 2)
            return Math.ceil(value.max / num) * num;
          }, 
          scale: true, //自适应*/
        },
        series: [
          {
            name: 'price',
            type: 'line',
            stack: 'Total',
            data: this.data2.map(d => d.price)
          },
        ]
      };
    },
  },
  methods: {
    handleChange(value) {
      console.log(value);
    },
    async onSubmit() {
      this.showingDetails = true;
      console.log('submit!');
      try {
        // use await to wait for the axios promise to resolve

        // 发起预测数据请求
        const predictRes = await this.$axios({
          url: "/api/pyscripts/predict",
          method: "get",
          params: {
            brand: this.formData.model[0],
            model: this.formData.model[1],
            location: this.formData.location[1],
            numberOfTransfer: this.formData.numberOfTransfer,
            license_year: this.formData.time[0],
            license_month: this.formData.time[1],
          }
        });
        console.log(predictRes);
        // 处理预测数据
        const predictData = predictRes.data;
        const formattedPredictData = [];
        console.log(predictData);


        predictData.forEach(item => {
          const month = item.month;
          const price = item.price;
          formattedPredictData.push({ "time": `${new Date().getFullYear()}-${month}`, "price": price });
        });

        this.data2 = formattedPredictData;

        const res = await this.$axios("/api/cars");
        const now = new Date();
        const data = res.data;
        const [brand, model] = this.formData.model;
        const [licen_year, licen_month] = this.formData.time;
        const province = this.formData.location[0];
        const number = Number(this.formData.numberOfTransfer);
        console.log(`numOfTransfer: ${province}, type: ${typeof province}`);

        const fiveMonthsAgo = new Date(now.setMonth(now.getMonth() - 6, 1));
        const pattern = /^\d{4}年\d{2}月$/;

        const recentData = data.filter(item => {
          const updateTime = new Date(item.update_time);
          const itemLicenseTime = item.license_time;
          if (!pattern.test(itemLicenseTime)) {
            return false;
          }
          const year = parseInt(itemLicenseTime.split("年")[0], 10);
          //const month = parseInt(itemLicenseTime.split("年")[1].split("月")[0], 10);

          const isRecent = updateTime > fiveMonthsAgo;

          const isMatched = brand ? item.brand === brand && item.model === model : true;

          const isSameTime = licen_year ? year === licen_year : true; //&& month === licen_month : true;

          const isSameProvince = province ? item.province_name === province : true;

          const numOfTransfer = Number.parseInt(item.num_of_transfer.match(/\d+/) || -1);

          const isSameNumber = number ? numOfTransfer === number : true;


          return isSameNumber && isRecent && isMatched && isSameTime && isSameProvince;
        });


        const groupedData = {};

        recentData.forEach(item => {

          const month = new Date(item.update_time).getMonth() + 1;

          if (!groupedData[month]) {
            groupedData[month] = {

              items: [],
              sum: 0,
              average: 0
            };
          }

          groupedData[month].items.push(item);

          groupedData[month].sum += Number(item.price);
        });
        const year = new Date().getFullYear();
        Object.keys(groupedData).forEach(month => {
          groupedData[month].average = groupedData[month].sum / groupedData[month].items.length;
        });
        this.data1 = Object.keys(groupedData).map(key => {
          return {
            time: `${year}-${key}`,
            price: groupedData[key].average
          };
        });

        this.$nextTick(() => {
          const bottomElement = document.getElementById('bottom-element');
          if (bottomElement) {
            bottomElement.scrollIntoView({ behavior: 'smooth', block: 'end' });
          }
        });

      } catch (err) {
        // handle the error
        console.log(err);
      }
    },

    handleChange2(modelValue) {
      console.log(modelValue);
    },
    generateTimeOptions() {
      const startYear = 2015;
      const endYear = 2023;

      for (let year = endYear; year >= startYear; year--) {
        const yearOption = {
          value: Number(year),
          label: year.toString(),
          children: [],
        };

        const months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];

        for (let i = 0; i < months.length; i++) {
          const monthOption = {
            value: Number(months[i]),
            label: `${i + 1}月`,
          };

          yearOption.children.push(monthOption);
        }

        this.timeOptions.push(yearOption);
      }
    },
  }
};
</script>
