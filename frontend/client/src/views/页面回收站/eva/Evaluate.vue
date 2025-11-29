



<!-- 
    * @FileDescription: 估值, 一级页面
    * @LastEditTime: 7.13
 -->

<template>
  <el-container-e1>
    <!--导航栏-->
    <el-header class="right-align">
      <NavigationMenu
      :activeIndex="activeIndex"
      :backgroundColor="backgroundColor"
      :textColor="textColor"
      :activeTextColor="activeTextColor"
      />
    </el-header>

    <el-main>
      <el-row class="parallel-container">
        <el-col :span="15" style="margin-right: 80px">
          <!--左边block占页面比-->

          <!--左边选择-->
          <div class="section" style="display: flex; flex-direction: column">
            <el-col :span="18" style="margin-right: 80px" class="left_div">
              <!--列1-->
              <el-form
                ref="form"
                label-position="top"
                :model="form"
                style="margin-top: 20px"
              >
                <h1 class="car_info">车辆信息</h1>
                <h2 class="second-title">车辆所在地</h2>
                <el-form-item
                  style="line-height: 20px; margin-top: 10px; margin-left: 25px"
                >
                  <el-cascader
                    v-model="locationValue_e"
                    :options="locationOptions"
                    @change="handleChange1"
                    :props="{
                        value: 'label',
                        label: 'label',
                        children: 'children'
                      }"
                  ></el-cascader>
                </el-form-item>

                <h2 class="second_title">上牌时间</h2>
                <el-form-item
                  style="line-height: 20px; margin-top: 10px; margin-left: 25px"
                >
                  <el-date-picker
                    v-model="timeValue_e"
                    type="month"
                    value-format="yyyy-MM"
                    placeholder="选择月份"
                  ></el-date-picker>
                </el-form-item>
              </el-form>

              <!--列2-->
              <el-form
                ref="form"
                label-position="top"
                :model="form"
                style="margin-top: 20px; margin-left: 50px"
              >
                <h1 class="car_info">&nbsp;</h1>
                <h2 class="second_title" style="margin-top: 10px">车辆种类</h2>
                <el-form-item
                  style="line-height: 20px; margin-top: 10px; margin-left: 25px"
                >
                  <el-cascader
                    v-model="modelValue_e"
                    :options="modelOptions"
                    @change="handleChange2"
                    :props="{
                        value: 'label',
                        label: 'label',
                        children: 'children'
                      }"
                  ></el-cascader>
                </el-form-item>

                <h2 class="second_title">行驶里程</h2>
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
                    v-model="input_e"
                    type="number"
                  ></el-input>
                </el-form-item>

                <el-form-item>
                  <el-button
                    @click="onSubmit"
                    style="
                      background-color: #3563e9;
                      color: #ffffff;
                      width: 200px;
                      margin-top: 50px;
                      margin-left: -100px;
                    "
                    >估价
                  </el-button>
                </el-form-item>
              </el-form>
            </el-col>
          </div>

          <!--左下-->
          <div class="section">
            <el-row class="sub-container">
              <el-col :span="24" class="lower-left-div1">
                <h1 class="car-description-title">估值记录</h1>

                <el-table
                  :data="tableData"
                  style="width: 100%"
                  header-row-class-name="table-header-row"
                  row-class-name="table-row"
                >
                  <el-table-column
                    prop="car_name"
                    label="车辆名称"
                    min-width="180"
                  ></el-table-column>
                  <el-table-column
                    prop="car_info"
                    label="车辆信息"
                    min-width="180"
                  ></el-table-column>
                  <el-table-column
                    prop="refer_price"
                    label="参考价"
                    min-width="120"
                  >
                    <template slot-scope="scope">
                      <span :style="{ color: '#de8808' }">{{
                        scope.row.refer_price
                      }}</span>
                    </template>
                  </el-table-column>
                  <el-table-column
                    prop="operate"
                    label="操作"
                    min-width="120"
                  ></el-table-column>
                </el-table>
              </el-col>
            </el-row>
          </div>
        </el-col>

        <el-col :span="12" class="right-div">
          <!-- 右部概览 -->
          <el-row class="sub-container">
            <el-col :span="24" class="lower-right-div">
              <h1 class="recent-transaction-title">经典车型参考</h1>

              <!-- 信息部分 -->
              <div
                class="recent-transaction-container"
                style="margin-bottom: 30px"
              >
                <!--在底部留空白 -->
                <div class="frame">
                  <img
                    src="../assets/car.png"
                    alt=""
                    style="width: 120px; height: 40px"
                  />
                </div>
                <div>
                  <h2 class="recent-transaction-car-model">宝马i7 M50</h2>
                  <h3 class="recent-transaction-car-model-subtitle">跑车</h3>
                </div>
              </div>

              <el-divider class="divider"></el-divider>
              <div
                class="recent-transaction-container"
                style="margin-bottom: 30px"
              >
                <!--在底部留空白 -->
                <div class="frame">
                  <img
                    src="../assets/car.png"
                    alt=""
                    style="width: 120px; height: 40px"
                  />
                </div>
                <div>
                  <h2 class="recent-transaction-car-model">宝马i7 M50</h2>
                  <h3 class="recent-transaction-car-model-subtitle">跑车</h3>
                </div>
              </div>

              <el-divider class="divider"></el-divider>
              <div
                class="recent-transaction-container"
                style="margin-bottom: 30px"
              >
                <!--在底部留空白 -->
                <div class="frame">
                  <img
                    src="../assets/car.png"
                    alt=""
                    style="width: 120px; height: 40px"
                  />
                </div>
                <div>
                  <h2 class="recent-transaction-car-model">宝马i7 M50</h2>
                  <h3 class="recent-transaction-car-model-subtitle">跑车</h3>
                </div>
              </div>

              <el-divider class="divider"></el-divider>
              <div
                class="recent-transaction-container"
                style="margin-bottom: 30px"
              >
                <!--在底部留空白 -->
                <div class="frame">
                  <img
                    src="../assets/car.png"
                    alt=""
                    style="width: 120px; height: 40px"
                  />
                </div>
                <div>
                  <h2 class="recent-transaction-car-model">宝马i7 M50</h2>
                  <h3 class="recent-transaction-car-model-subtitle">跑车</h3>
                </div>
              </div>

              <el-divider class="divider"></el-divider>
              <div
                class="recent-transaction-container"
                style="margin-bottom: 30px"
              >
                <!--在底部留空白 -->
                <div class="frame">
                  <img
                    src="../assets/car.png"
                    alt=""
                    style="width: 120px; height: 40px"
                  />
                </div>
                <div>
                  <h2 class="recent-transaction-car-model">宝马i7 M50</h2>
                  <h3 class="recent-transaction-car-model-subtitle">跑车</h3>
                </div>
              </div>

              <el-divider class="divider"></el-divider>
              <div
                class="recent-transaction-container"
                style="margin-bottom: 30px"
              >
                <!--在底部留空白 -->
                <div class="frame">
                  <img
                    src="../assets/car.png"
                    alt=""
                    style="width: 120px; height: 40px"
                  />
                </div>
                <div>
                  <h2 class="recent-transaction-car-model">宝马i7 M50</h2>
                  <h3 class="recent-transaction-car-model-subtitle">跑车</h3>
                </div>
              </div>
            </el-col>
          </el-row>
        </el-col>
      </el-row>
    </el-main>
  </el-container-e1>
</template>

<style>
/* 顶部导航 */
.right-align {
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
el-container-e1 {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.el-header {
  background-color: #f6f7f9;
  color: #333;
  line-height: 60px;
}

.el-main {
  background-color: #f6f7f9;
  color: #333;
  text-align: center;
  line-height: 160px;
  min-height: 100vh; /* 百分百铺满 */
}

/* 表格 - 左下 */
.section {
  margin-bottom: 20px;
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
.car_info {
  margin-left: 25px;
  margin-bottom: 15px;
  font-weight: bold;
  line-height: 30px;
  margin-top: 20px;
  font-size: 25px;
  text-align: left;
}

.left_div {
  background-color: #ffffff;
  border-radius: 30px;
  margin-right: 30px;
  margin-left: 10px;
  text-align: left;
  padding-top: 20px;
  padding-bottom: 20px;
  padding-left: 15px;
  padding-right: 15px;
  max-height: 450px;
  display: flex;
}

.second_title {
  line-height: 30px;
  font-weight: bold;
  margin-left: 25px;
  margin-bottom: 8px;
}

.picture {
  display: flex;
  justify-content: center;
  align-items: center;
}

/* 框内字体细节 - 右上角 */
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
.recent-transaction-title {
  margin-left: 25px;
  font-weight: bold;
  line-height: 30px;
  margin-top: 20px;
  margin-bottom: 10px;
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
  margin-bottom: 10px;
}

.lower-right-div {
  min-height: 400px;
  background-color: #ffffff;
  border-radius: 30px;
  margin-bottom: 10px;
}
.right-div {
  flex: 1;
  background-color: #f6f7f9;
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
export default {
  name: "evaluatetest",
  data() {
    return {
      activeIndex: "0",
      locationValue_e: [],
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
      timeValue_e: [],

      modelValue_e: [],
      modelOptions: [
        {
          value: "bmw",
          label: "宝马",
          children: [
            {
              value: "bmw 1系",
              label: "宝马1系",
              children: [
                {
                  value: "2017 118i 设计套装型",
                  label: "2017款 118i 设计套装型",
                },
                { value: "2017 118i 时尚型", label: "2017款 118i 时尚型" },
                { value: "2017 118i 运动型", label: "2017款 118i 运动型" },
                {
                  value: "2017 120i 设计套装型",
                  label: "2017款 120i 设计套装型",
                },
                { value: "2017 125i 运动型", label: "2017款 125i 运动型" },
                {
                  value: "2018 118i 设计套装型",
                  label: "2018款 118i 设计套装型",
                },
                { value: "2018 118i 时尚型", label: "2018款 118i 时尚型" },
                { value: "2018 118i 运动型", label: "2018款 118i 运动型" },
                {
                  value: "2018 120i 设计套装型",
                  label: "2018款 120i 设计套装型",
                },
                {
                  value: "2018 改款 118i 运动型",
                  label: "2018款 改款 118i 运动型",
                },
              ],
            },
            {
              value: "bmw 2系",
              label: "宝马2系",
              children: [
                {
                  value: "2014款 220i 领先型",
                  label: "2014款 220i 领先型2014款 220i 领先型",
                },
                {
                  value: "2014款 220i 运动设计套装",
                  label: "2014款 220i 运动设计套装",
                },
                { value: "2014款 M235i", label: "2014款 M235i" },
                { value: "2015款 218i", label: "2015款 218i" },
                {
                  value: "2015款 218i 敞篷轿跑车",
                  label: "2015款 218i 敞篷轿跑车",
                },
                {
                  value: "2017款 220i 敞篷轿跑车 领先型",
                  label: "2017款 220i 敞篷轿跑车 领先型",
                },
                { value: "2017款 220i 领先型", label: "2017款 220i 领先型" },
                {
                  value: "2018款 220i 敞篷轿跑车 运动设计套装",
                  label: "2018款 220i 敞篷轿跑车 运动设计套装",
                },
              ],
            },
            {
              value: "bmw 3系",
              label: "宝马3系",
              children: [
                { value: "2004款 318i", label: "2004款 318i" },
                { value: "2005款 320i 领先型", label: "2005款 320i 领先型" },
                {
                  value: "2005款 320i 时尚型木内饰",
                  label: "2005款 320i 时尚型木内饰",
                },
                {
                  value: "2023款 330Li M运动曜夜套装",
                  label: "2023款 330Li M运动曜夜套装",
                },
                {
                  value: "2023款 325Li xDrive M运动套装",
                  label: "2023款 325Li xDrive M运动套装",
                },
                {
                  value: "2022款 325Li M运动曜夜套装",
                  label: "2022款 325Li M运动曜夜套装",
                },
              ],
            },
            {
              value: "bmw 4系",
              label: "宝马4系",
              children: [
                {
                  value: "2014款 420i Gran Coupe 时尚型",
                  label: "2014款 420i Gran Coupe 时尚型",
                },
                {
                  value: "2014款 420i 敞篷风尚设计套装",
                  label: "2014款 420i 敞篷风尚设计套装",
                },
                {
                  value: "2015款 428i 敞篷限量版",
                  label: "2015款 428i 敞篷限量版",
                },
                {
                  value: "2016款 420i Gran Coupe M运动型",
                  label: "2016款 420i Gran Coupe M运动型",
                },
                {
                  value: "2016款 420i 敞篷设计套装型",
                  label: "2016款 420i 敞篷设计套装型",
                },
                {
                  value: "2022款 430i 敞篷M运动曜夜套装",
                  label: "2022款 430i 敞篷M运动曜夜套装",
                },
                {
                  value: "2023款 430i M运动曜夜套装",
                  label: "2023款 430i M运动曜夜套装",
                },
              ],
            },
          ],
        },
        {
          value: "benchi",
          label: "奔驰",
          children: [
            {
              value: "奔驰B级",
              label: "奔驰B级",
              children: [
                { value: "2009款 B 200 动感型", label: "2009款 B 200 动感型" },
                { value: "2012款 B 180", label: "2012款 B 180" },
                { value: "2013款 B 260", label: "2013款 B 260" },
                { value: "2015款 B 200 动感型", label: "2015款 B 200 动感型" },
                { value: "2016款 B 180", label: "2016款 B 180" },
                { value: "2020款 B 180", label: "2020款 B 180" },
              ],
            },
            {
              value: "奔驰CLA",
              label: "奔驰CLA",
              children: [
                {
                  value: "2014款 CLA 260 4MATIC",
                  label: "2014款 CLA 260 4MATIC",
                },
                { value: "2015款 CLA 200", label: "2015款 CLA 200" },
                {
                  value: "2016款 CLA 200 动感型",
                  label: "2016款 CLA 200 动感型",
                },
                { value: "2017款 CLA 180", label: "2017款 CLA 180" },
                { value: "2018款 CLA 180", label: "2018款 CLA 180" },
                {
                  value: "2019款 CLA 200 暗夜特别版",
                  label: "2019款 CLA 200 暗夜特别版",
                },
                { value: "2020款 CLA 200", label: "2020款 CLA 200" },
                { value: "2021款 CLA 200", label: "2021款 CLA 200" },
              ],
            },
            {
              value: "奔驰C级",
              label: "奔驰C级",
              children: [
                {
                  value: "2008款 C 200K 标准型",
                  label: "2008款 C 200K 标准型",
                },
                {
                  value: "2010款 C 180K 经典型",
                  label: "2010款 C 180K 经典型",
                },
                {
                  value: "2011款 C 180K 经典型",
                  label: "2011款 C 180K 经典型",
                },
                {
                  value: "2013款 C 180 CGI 经典型",
                  label: "2013款 C 180 CGI 经典型",
                },
                {
                  value: "2015款 C 180 L 运动型",
                  label: "2015款 C 180 L 运动型",
                },
                {
                  value: "2023款 C 200 L 运动型",
                  label: "2023款 C 200 L 运动型",
                },
              ],
            },
          ],
        },
        {
          value: "aodi",
          label: "奥迪",
          children: [
            {
              value: "奥迪A1",
              label: "奥迪A1",
              children: [
                { value: "2012款 1.4 TFSI Ego", label: "2012款 1.4 TFSI Ego" },
                {
                  value: "2013款 30 TFSI Sportback Ego",
                  label: "2013款 30 TFSI Sportback Ego",
                },
                {
                  value: "2014款 30 TFSI Sportback时尚型",
                  label: "2014款 30 TFSI Sportback时尚型",
                },
                {
                  value: "2016款 30 TFSI Sportback Design风尚版",
                  label: "2016款 30 TFSI Sportback Design风尚版",
                },
                {
                  value: "2018款 30 TFSI 限量典藏版",
                  label: "2018款 30 TFSI 限量典藏版",
                },
                { value: "2020款 B 180", label: "2020款 B 180" },
              ],
            },
            {
              value: "奥迪A3",
              label: "奥迪A3",
              children: [
                {
                  value: "2014款 Limousine 35 TFSI 自动豪华型",
                  label: "2014款 Limousine 35 TFSI 自动豪华型",
                },
                {
                  value: "2015款 Limousine 35 TFSI 百万纪念舒享型",
                  label: "2015款 Limousine 35 TFSI 百万纪念舒享型",
                },
                {
                  value: "2016款 Limousine 35 TFSI 进取型",
                  label: "2016款 Limousine 35 TFSI 进取型",
                },
                {
                  value: "2017款 Limousine 35 TFSI 风尚型",
                  label: "2017款 Limousine 35 TFSI 风尚型",
                },
                {
                  value: "2018款 30周年年型 Limousine 35 TFSI 风尚型",
                  label: "2018款 30周年年型 Limousine 35 TFSI 风尚型",
                },
                {
                  value: "2019款 Limousine 35 TFSI 风尚型 国V",
                  label: "2019款 Limousine 35 TFSI 风尚型 国V",
                },
                {
                  value: "2022款 A3L Limousine 35 TFSI 时尚运动型",
                  label: "2022款 A3L Limousine 35 TFSI 时尚运动型",
                },
              ],
            },
            {
              value: "奥迪Q7",
              label: "奥迪Q7",
              children: [
                {
                  value: "2006款 3.6 FSI quattro 基本型",
                  label: "2006款 3.6 FSI quattro 基本型",
                },
                {
                  value: "2007款 3.6 FSI quattro 技术型",
                  label: "2007款 3.6 FSI quattro 技术型",
                },
                {
                  value: "2010款 3.6 FSI quattro 豪华型",
                  label: "2010款 3.6 FSI quattro 豪华型",
                },
                {
                  value: "2011款 3.0 TFSI 技术型(245kW)",
                  label: "2011款 3.0 TFSI 技术型(245kW)",
                },
                {
                  value: "2013款 35 TFSI 舒适型",
                  label: "2013款 35 TFSI 舒适型",
                },
                {
                  value: "2023款 55 TFSI quattro S line运动型",
                  label: "2023款 55 TFSI quattro S line运动型",
                },
              ],
            },
          ],
        },
      ],

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
      input_e: "",
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
  methods: {
    handleSelect(index) {
      this.activeIndex = index;
    },
    handleChange1(locationValue_e) {
      console.log(locationValue_e);
    },
    handleChange2(modelValue_e) {
      console.log(modelValue_e);
    },
    handleRemove(file) {
      console.log(file);
    },
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },
    handleDownload(file) {
      console.log(file);
    },
    onSubmit() {
      //参数
      const routeParams = {
        locationValue: this.locationValue_e,
        timeValue: this.timeValue_e,
        modelValue: this.modelValue_e,
        input: this.input_e,
      };

      // 页面跳转
      this.$router.push({
        name: "evaluatedetail", //跳哪
        params: routeParams,
      });
    },
  },
};
</script>
