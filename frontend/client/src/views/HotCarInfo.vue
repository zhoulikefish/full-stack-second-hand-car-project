<template>
    <el-container>
      <el-header class="right-align" style="background-color: rgba(245, 246, 252, 1);">
          <NavigationMenuAfterLogin
        :activeIndex="activeIndex"
        :backgroundColor="backgroundColor"
        :textColor="textColor"
        :activeTextColor="activeTextColor"
      />
      </el-header> 
      <el-main class="main">
        <!-- <h1 style="text-align: left; font-weight: bold; margin-left: 40px; color: #3D5278;">热门车系保值率</h1> -->
        <el-row class="parallel">
          <el-col :span="8" style="display: flex; align-items: center; justify-content: center;">
            <!-- <div class="left">
                <h1 class="title">车辆简介</h1>
                <div>
                  <h2 class="car-name">{{this.carname}}</h2> 
                  <h3 class="price-field">价格区间：{{this.pricefield}} 万</h3>
                </div>

              </div> -->
              <div class="left">
                <h1 style="text-align: left; font-weight: bold; margin-left: 30px; font-size: x-large;">热门车系保值率</h1>
                <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; margin-top: 60px;">
                  <h2 class="car-name">{{this.carname}}</h2> 
                  <h3 class="price-field">新车价格区间：</h3>
                  <p></p>
                  <p></p>
                  <h3 class="price-field">{{this.pricefield}} 万</h3>
                </div>
              </div>
          </el-col>
            <el-col :span="16" class="right">
              <!-- <div>
                <img :src="this.car_img" alt="" style="width: 80%; height: 80%;">
              </div> -->
              <div style="background-color: #ffffff; border-radius: 30px; margin-right: 25px; padding-top: 20px; padding-bottom: 20px;">
                <!-- <img src="../assets/Image.png" alt="" style="width: 80%; height: 80%;"> -->
                <img :src="car_img" alt="" style="width: 70%; height: 70%;">
                <!-- <img :src="'../assets/full/16e6e9ae1448d567d4e61cf398755fa87664e3ee.jpg'" alt="" style="width: 80%; height: 80%;"> -->
              </div>
            </el-col>
        </el-row>
        <el-row style="align-items: center; justify-content: center; background-color: #ffffff; border-radius: 30px; padding: 20px; margin-left: 25px; margin-right: 25px; margin-top: 30px;">
            <div class="echart" id="mychart" style="width: 95%; height: 400px; "></div>
        </el-row>
    </el-main>
    </el-container>
</template>

<style>
  el-container {
    display: block;
  }
  .container {
    display: flex;
    justify-content: flex-end;
    
  }
  .main{
    background-image: url("../assets/ev-bg.png");
    background-size: cover;
  }
  .parallel {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .left{
    background-color: #ffffff;
    border-radius: 30px;
    margin-left: -30px;
    /* text-align: center; */
    padding-top: 20px;
    padding-bottom: 20px;
    width: 300px;
    /* height: fit-content; */
    height: 360px;
    /* display: flex; */
  }
  .right {
    margin-left: 20px;
    /* margin-top: -30px; */
    align-items: center;
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

  .title{
    margin-left: 25px;
    font-weight: bold;
    line-height: 30px;
    font-size: large;
    /* text-align: center; */
  }
  .car-name{
    /* margin-left: 15px; */
    font-weight: bold;
    text-align: center;
    /* margin-top: 20px; */
    font-size: xx-large;
  }
  .price-field{
    font-size: x-large;
    font-weight: bold;
    color: #3D5278;
    text-align: center;
  }

</style>




<script>
  const echarts = require('echarts');
  import NavigationMenuAfterLogin from "@/components/NavigationMenuAfterLogin.vue";
  export default {
    name: 'hotcarinfo',
    props: ['targetCarModel', 'remainingCars'],
    components: {
      NavigationMenuAfterLogin
    },
    data() {
      return {
        myChart: null,
        // xData: ["1年","2年","3年","4年","5年"], 
        // yData: [23,2,3,5,10], 
        // myChartStyle: { float: "left", width: "80%", height: "400px"}, 
        dataMap: [],
        Result:  { averageData: [], cities: [] },
        carname: null,
        pricefield: null,
        targetCarModel_h: null,
        car_img: null
      };
    },
    created(){
      this.targetCarModel_h = this.$route.params.targetCarModel;
      console.log(this.$route.params.targetCarModel);
      this.getCarData();
			this.getPopular();
      this.car_img = this.$route.query.img;  
      console.log("这边");
      console.log(this.$route.query.img); 
		},
    mounted() {

      // this.targetCarModel_h = this.$route.params.targetCarModel;
      console.log(this.targetCarModel_h);
      console.log(this.Result);
      
    },

    methods: {

      getCarData() {
        this.$axios("/api/populars")
          .then((res) => {
            // const targetCarModel = "马自达2";
            this.carname = this.targetCarModel_h; 
            this.pricefield = res.data.filter(item => item.car_name === this.carname)[0].price_field;

            // const matchedData = res.data.find(item => item.car_name === this.carname);
            // if (matchedData) {
              
            //   // this.car_img = "@/assets/" + matchedData.car_img;
              
            //   this.car_img = matchedData.car_img;
            //   console.log(this.car_img);
            // }

            console.log(this.carname);
            console.log(this.pricefield);

          })
          .catch((error) => {
            console.error("Failed to fetch data:", error);
          });
      },
      getPopular() {
        // 获取表格数据
        this.$axios("/api/populars")
          .then((res) => {
            this.dataMap = res.data;
            this.Result = this.dataCount(this.dataMap);
            console.log(this.Result);
            this.initEcharts();
          })
          .catch((error) => { 
            console.error("Failed to fetch data:", error);
          });
      },
      // getImageUrl(imagePath) {
      //   this.$axios("/api/cars")
      //     .then((res) => {
      //       // const targetCarModel = "马自达2";
      //       this.carname = this.targetCarModel_h; 
      //       this.pricefield = res.data.filter(item => item.car_name === this.carname)[0].price_field;

      //       const matchedData = res.data.find(item => item.car_name === this.carname);
      //       if (matchedData) {
              
      //         // this.car_img = "@/assets/" + matchedData.car_img;
              
      //         this.car_img = matchedData.car_img;
      //         console.log(this.car_img);
      //       }

      //       console.log(this.carname);
      //       console.log(this.pricefield);

      //     })
      //     .catch((error) => {
      //       console.error("Failed to fetch data:", error);
      //     });



      //   console.log('../assets/' + imagePath);
      // },

      initEcharts() {
        const xData = Object.keys(this.Result.averageData[Object.keys(this.Result.averageData)[0]]); // x 轴数据
        const { averageData, cities } = this.Result;

        const seriesData = [];
        for (const city of cities) {
          const yData = Object.values(averageData[city]); // 获取指定城市的保值率数据
          seriesData.push({
            name: city,
            type: 'line',
            data: yData
          });
        }

        const option = {
          title: {
            text: '车辆保值率'
          },
          legend: {
            data: cities
          },
          tooltip: {
            trigger: 'axis'
          },
          toolbox: {
            feature: {
              saveAsImage: {}
            }
          },
          grid: {
            left: '3%',
            right: '5%',
            bottom: '3%',
            containLabel: true
          },
          xAxis: {
            type: 'category',
            data: xData
          },
          yAxis: {
            type: 'value',
            scale: true
          },
          series: seriesData
        };

        this.myChart = echarts.init(document.getElementById("mychart"));
        this.myChart.setOption(option);

        window.addEventListener("resize", () => {
          this.myChart.resize();
        });
      },

      dataCount(data) {
        // const targetCarModel = this.carname;
        this.carname = this.targetCarModel_h; 
        const filteredData = data.filter(item => item.car_name === this.carname);
        console.log(data)
        for (const item of filteredData) {
          for (const key in item) {
            if (key.startsWith("year")) {
              item[key] = parseFloat(item[key]);
            }
          }
        }
        console.log(filteredData);

        const cities = []; // 存储城市名称的数组
        for (const item of filteredData) {
            const city = item.city_name;
            if (!cities.includes(city)) {
              cities.push(city);
            }
        }
        
        console.log(cities);

        const averageData = {};
        for (const item of filteredData) {
          const city = item.city_name;
          if (!averageData[city]) {
            averageData[city] = {};
          }

          for (const key in item) {
            if (key.startsWith("year")) {
              const year = key;
              if (!averageData[city][year]) {
                averageData[city][year] = [];
              }
              averageData[city][year].push(item[key]);
            }
          }
        }
        console.log(averageData);

        for (const city in averageData) {
          for (const year in averageData[city]) {
            const values = averageData[city][year];
            const average = values.reduce((sum, value) => sum + value, 0) / (values.length*100);
            averageData[city][year] = average.toFixed(2);
          }
        }
        console.log(averageData);

        return { averageData, cities };
      }
    }
  }

</script>