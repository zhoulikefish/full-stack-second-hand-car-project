<!-- 
    * @FileDescription: 热门车型保值界面
    * @LastEditTime: 7.10
 -->



 <template>
    <el-container>
      <el-header>
        <div class="right-align" style="background-color: rgba(245, 246, 252, 1);">
          <NavigationMenu
        :activeIndex="activeIndex"
        :backgroundColor="backgroundColor"
        :textColor="textColor"
        :activeTextColor="activeTextColor"
        />
      </div>
      </el-header>
      <el-main>
        <el-row class="parallel-container">
            <el-col :span="8" class="left-div"> 
                <h1 class="car-description-title">车辆简介</h1>
              <div class="car-description-container">
                <div class="blue-frame">
                  <img src="../assets/car.png" alt="" style="width: 120px; height: 40px;"> 
                </div>
                <div>
                  <h2 class="car-model">宝马i7 M50</h2> 
                  <h3 class="car-model-subtitle">跑车</h3>
                </div>
              </div>
              <el-descriptions class="custom-descriptions" :column="2">
                <el-descriptions-item label="车辆种类">跑车</el-descriptions-item>
                <el-descriptions-item label="容量">2人</el-descriptions-item>
                <el-descriptions-item label="操舵">手动</el-descriptions-item>
                <el-descriptions-item label="汽油">70升</el-descriptions-item>
                <el-descriptions-item label="特点">配备先进的信息娱乐系统和触摸屏显示</el-descriptions-item>
              </el-descriptions>
            </el-col>
            <el-col :span="16" class="right-div">
                <div>
                  <img src="../assets/PopularCarImage.png" alt="" style="max-width: 100%; max-height: 100%;"> 
                </div>
            </el-col>
        </el-row>
        <el-row>
          <div class="echart" id="mychart" :style="myChartStyle"></div>

        </el-row>
    </el-main>
    </el-container>
</template>

<style>
  el-container {
    display: flex;

    height: 100vh; 
  }
  .el-header {
    background-color: rgba(245, 246, 252, 1);
    line-height: 60px;
  }
  .container {
    display: flex;
    justify-content: flex-end;
    
  }
  .navigation .el-menu-item {
    font-family: "Microsoft YaHei"; /* 设置文字字体 */
    font-size: 16px; /* 设置文字大小 */
    font-weight: bold; /* 设置文字加粗 */
    text-decoration: none; /* 取消文字下划线 */
  }
  .navigation .el-menu-item a {
    font-family: "Microsoft YaHei"; /* 设置文字字体 */
    font-size: 16px; /* 设置文字大小 */
    font-weight: bold; /* 设置文字加粗 */
    text-decoration: none; /* 取消文字下划线 */
  }


  .left-div{
    background-color: #FFFFFF;
    border-radius: 30px;
    margin-left: 20px;
    text-align: left;
    padding-top: 10px;
    padding-bottom: 10px;
    flex: 1;
  }
  .right-div {
    flex: 1;
  }
  
  .data{
    background-color: #FFFFFF;
    border-radius: 30px;
    margin-left: 20px;
    margin-top: 30px;
    text-align: left;
    padding-top: 10px;
    padding-bottom: 10px;
    margin-right: 20px;
  }


  h1 {
    margin-left: 25px;
    margin-bottom: -5px;
    font-weight: bold;
    line-height: 30px;
    margin-top: 20px;
    font-size: large;
    text-align: left;
  }
  .car-model{
    margin-left: 15px;
    font-weight: bold;
    line-height: 30px;
    margin-top: 20px;
    font-size: medium;
  }
  .car-model-subtitle{
    font-size: small;
    font-weight: bold;
    line-height: 40px;
    text-align: left;
    margin-left: 15px;
    color: #3D5278;
  }

  .custom-descriptions .el-descriptions__title {
    margin-bottom: 0; 
    line-height: 40px;
  }
  .car-description-container {
    display: flex;
    align-items: center;
  }


</style>




<script>
  import NavigationMenu from "../components/NavigationMenu.vue";
  const echarts = require('echarts');

  export default {
    components: {
    NavigationMenu 
  },
  data() {
    return {
      activeIndex: '1',
      backgroundColor: 'rgba(245, 246, 252, 1)',
      textColor: '#1D1E21',
      activeTextColor: 'rgba(255, 101, 27, 1)'
    };
  },
    name: 'hotcarinfo',
    data() {
      return {
        myChart: null,
        // xData: ["1年","2年","3年","4年","5年"], 
        // yData: [23,2,3,5,10], 
        myChartStyle: { float: "left", width: "100%", height: "400px" }, 
        dataMap: [],
        Result: []
      };
    },
    created(){
			this.getProfile();
		},
    mounted() {
			console.log(this.Result);
    },
    methods: {
      getProfile() {
        // 获取表格数据
        this.$axios("/api/profiles")
          .then((res) => {
            this.dataMap = res.data; // 将数据赋值给 dataMap
            console.log(this.dataMap.length);
            this.Result = this.dataCount(this.dataMap);
            console.log(this.Result);
            this.initEcharts();
          })
          .catch((error) => {
            console.error("Failed to fetch data:", error);
          });
      },
      initEcharts() {
        const xData = Object.keys(this.Result); // x 轴数据
        const yData = Object.values(this.Result); // y 轴数据
        const option = {
          tooltip: {
						trigger: 'item'
					},
          xAxis: {
            type: 'category',
            data: xData
          },
          yAxis: {
            type: 'value'
          },
          series: [{
            data: yData,
            type: 'line'
          }]
          
        };
        this.myChart = echarts.init(document.getElementById("mychart"));
        this.myChart.setOption(option);
        // option && myChart.setOption(option);
        // 监听窗口大小变化，自适应调整图表大小
        window.addEventListener("resize", () => {
          this.myChart.resize();
        });
      },
      dataCount(data) {
        const brands = ["奔驰", "MINI", "宝马"];
        const brandData = {}; // 存储每个品牌的价格数据

        // 初始化品牌数据对象
        for (const brand of brands) {
          brandData[brand] = [];
        }

        // 抽取符合品牌的价格数据
        // for (const item of data) {
        //   if (brands.includes(item.brand)) {
        //     brandData[item.brand].push(item.price);
        //   }
        // }

        for (const item of data) {
          if (brands.includes(item.brand)) {
            const price = parseFloat(item.price); // 将价格转为数值
            if (!isNaN(price)) {
              brandData[item.brand].push(price);
            }
          }
        }

        // 计算每个品牌的平均价格
        const averageData = {};
        for (const brand in brandData) {
          const prices = brandData[brand];
          if (prices.length > 0) {
            let sum = 0;
            for (let i = 0; i < prices.length; i++) {
              sum += prices[i];
            }
            averageData[brand] = sum / prices.length;
            // const averagePrice = prices.reduce((sum, price) => sum + price, 0) / prices.length;
            // averageData[brand] = averagePrice.toFixed(2); // 保留两位小数
          }
        // console.log(averageData);
        }
        return averageData;
      }
    }
  }

</script>