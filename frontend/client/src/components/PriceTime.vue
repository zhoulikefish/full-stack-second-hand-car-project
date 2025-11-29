<template>
    <!--渲染Echarts图表的容器-->
    <div id="pricetime" style="width:100% ; height: 400px"></div>
</template>

<script>

	import * as echarts from 'echarts';



	export default { 
		data() {
			return{
				dataMap: [],
				seriesList : []
			} 
		},
		async created() {
			this.seriesList = await this.getProfiles();
			this.initEcharts();
		},
		methods:{ 
			getProfiles() {
				var cities = ["北京","上海","重庆","天津"]
				const requests = cities.map(region => {
					console.log("PriceTime!")
					return this.$axios.get('/api/cars/count_by_time', {
					params: {
						province_name: region
					}
					}).then(response => {
					const price = response.data;
					console.log(response.data)
					return {
						name: region,
						type: "line",
						stack:"Total",
						data: price.map(item => item.avgPrice)
,
					};
					}).catch(error => {
					console.error('请求出错:', error);
					return { name: region, value: 0 };
					});
				});

				return Promise.all(requests);
			},

			initEcharts() {
				var chartDom = document.getElementById('pricetime');
				var myChart = echarts.init(chartDom);
				var option;
				option = {
					animationDuration: 10000,
					tooltip: {
					order: 'valueDesc',
					trigger: 'axis'
					},
					xAxis: {
					type: 'category',
					nameLocation: 'middle',
					data: ['2023-3','2023-4','2023-5','2023-6','2023-7']
					},
					yAxis: {
					name: 'Income'
					},
					grid: {
					right: 140
					},
					series: this.seriesList
				};
				option && myChart.setOption(option);
			},


			dataCount(data) {
				// var countries = ['Australia', 'Canada', 'China', 'Cuba', 'Finland', 'France', 'Germany', 'Iceland', 'India', 'Japan', 'North Korea', 'South Korea', 'New Zealand', 'Norway', 'Poland', 'Russia', 'Turkey', 'United Kingdom', 'United States'];
				const cities = [
					'北京',
					'上海',
					'河南',
					'河北'
				
				];

				// var dailyDataList = []

				// for(const city in cities){
				// 	// 创建一个对象，用于存储每天的总价格和交易数量

				// 	const dailyData = {
				// 		name: cities[city],
				// 		type:"line",
				// 		stack:"Total",
				// 		raw_data:[]
				// 	};
				// 	dailyDataList.push(dailyData);
				// }

				// // 遍历数据集
				// for (let i = 0; i < data.length; i++) {
				// 	const row = data[i];
				// 	const city = row['province_name'];
				// 	const price = row['price'];
				// 	const date = row['update_week'];

				// 	const index = cities.indexOf(city)
				// 	if(index<0) continue

				// 	// 只处理北京城的数据
				// 	// 检查日期是否已经存在于 dailyData 对象中
				// 	try{
				// 		if (dailyDataList[index].raw_data.indexOf(date)>-1) {
				// 			// 如果存在，则更新总价格和交易数量
				// 			dailyDataList[index].raw_data[date].totalPrice += price;
				// 			dailyDataList[index].raw_data[date].transactionCount += 1;
				// 		} else {
				// 			// 如果不存在，则初始化该日期的数据
				// 			dailyDataList[index].raw_data[date] = {
				// 			totalPrice: price,
				// 			transactionCount: 1
				// 			};
				// 		}
				// 	}catch{
				// 		a=1
				// 	}
				// }

				// 创建一个数组来存储结果
				var total_result = [];

				for (const dailyData in dailyDataList) {
					const result = [];
					// 遍历 dailyData 对象，计算每天的平均价格并按照时间顺序添加到结果数组中
					for (const date in  dailyDataList[dailyData].raw_data) {
						const averagePrice = dailyDataList[dailyData].raw_data[date].totalPrice / 
											dailyDataList[dailyData].raw_data[date].transactionCount;
						result.push({
							date: date,
							averagePrice: averagePrice
						});
					}
					// 根据日期进行排序（升序）
					result.sort((a, b) => a.date.localeCompare(b.date));
					
					const data = [];
					for( var item in result){
						data.push(result[item].averagePrice)
					}
					total_result.push({
						name: dailyDataList[dailyData].name,
						type:"line",
						stack:"Total",
						data: data
					})
					
				}
				return total_result;
			
			}
		}
	}




</script>