<template>
    <!--渲染Echarts图表的容器-->
    <div id="line" style="width:10% ; height:10%"></div>
</template>

<script>

	import * as echarts from 'echarts';



	export default { 
		data() {
			return{
			} 
		},
		async created() {
			this.initEcharts();
		},
		methods:{ 

			initEcharts() {
				var chartDom = document.getElementById('line');
				var myChart = echarts.init(chartDom);
				var option;
				option = {
					// animationDuration: 10000,
					xAxis: {
						type: 'category',
						nameLocation: 'middle',
						data: ['2023-3','2023-4','2023-5','2023-6','2023-7']
					},
					yAxis: {
						name: 'Income',
					},
					series: [
						{
						data: [150, 230, 224, 218, 135, 147, 260],
						type: 'line'
						}
					],
					grid: {
						right: 140
					},
				};
				option && myChart.setOption(option);
			},

		}
	}




</script>