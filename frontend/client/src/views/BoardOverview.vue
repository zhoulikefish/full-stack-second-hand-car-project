<template>
	<div style="background-color: rgba(245, 246, 252, 1);">
	<el-header class="right-align" style="background-color: rgba(245, 246, 252, 1);">
        <NavigationMenuAfterLogin
        :activeIndex="activeIndex"
        :backgroundColor="backgroundColor"
        :textColor="textColor"
        :activeTextColor="activeTextColor"
      />
    </el-header>
	<div class="container" style="margin-top: 50px;">

	  <el-col class="left-column" >
		<el-row class="card" style="width:500px">
		  <div class="card-header">
			<h4 class="card-title">各大城市平均车辆售价折线图</h4>
		  </div>
		  <div class="card-body">
			<div id="morris_bar" style="margin-top: -20px;margin-left: -20px;width : 600px">
			  <CityTimePrice></CityTimePrice>
			</div>
		  </div>
		</el-row>
		<el-row class="card" style="width:500px" >
		  <div class="card-header">
			<h4 class="card-title">在售车辆品牌型号图</h4>
		  </div>
		  <div class="card-body">
			<div id="line_chart_2" class="morris_chart_height">
			  <Sun></Sun>
			</div>
		  </div>
		</el-row>
	</el-col>

	  <el-col class="right-column">
		<div class="card" style="width:700px">
			<div class="card-header">
				<h4 class="card-title">全国在售车辆密度图</h4>
			</div>
			<div class="card-body">
				<div id="morris_map" style="margin-top:100px" >
				<ChinaMap></ChinaMap>
				</div> 
			</div>
		</div>
	</el-col>

	</div>
</div>

</template>
  
  <style>
.right-align {
  display: flex;
  justify-content: flex-end;
}
  .container {
	margin-left: 200px;
	display: flex;
	height: 1000px;
	justify-content: space-between;
  }
  
  .left-column {
	width: 50%;
    margin-right: 20px;
	display: flex;
	flex-direction: column;
	/* justify-content: flex-start; */
	left: 0; 
	/* position: absolute;*/
  
  }

  .right-column {
	width: 10%;/* 设置一个占据页面宽度的百分比 */
	margin-left: 20px; /* 设置左边距来与左侧容器保持一定的间距 */
	display: flex;
	/* justify-content: flex-end; */
	/* align-items: flex-start;  */
  }
  .card {
	margin-bottom: 20px;
  }
  

  
  .morris_chart_height {
	height: 400px; /* 根据需要调整高度 */

  }
  </style>
  
  <script>
  import HeadNav from '../components/HeadNav';
  import LeftMenu from '../components/LeftMenu';
  import Pan from '../components/Pan';
  import ChinaMap from '../components/ChinaMap.vue';
  import CityTimePrice from '../components/PriceTime.vue';
  import Sun from '../components/Sun.vue';
  import NavigationMenuAfterLogin from '@/components/NavigationMenuAfterLogin.vue';
  

  import '../assets/board_static/css/style.css';
  export default {
	data() {
		return {
			activeIndex: "6"
		}
	},
	name: 'index',
	components: {
	  HeadNav,
	  LeftMenu,
	  Pan,
	  ChinaMap,
	  CityTimePrice,
	  Sun,
	  NavigationMenuAfterLogin,
	},
  };
  </script>
  
  <!-- <style scoped>
  .index {
	width: 100%;
	height: 100%;
	overflow: hidden;
  }
  .rightContainer {
	position: absolute;
	top: 0;
	left: calc(100% - 450px);
	width: 450px;
	height: 100%;
	overflow: auto;
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
  </style> -->