<template>
	<div>
		<div id="china_map" style='width:100%;height:400px;'> </div>
	</div>
</template>

<script>
import * as echarts from 'echarts';
require('../assets/board_assets/china.js');

export default {
	data() {
		return {
			// 保存原始数据
			dataMap: [],
			Result: []
		}
	},
	created(){

	},
	mounted () {
		this.getProfile();
		// 初始化echarts实例
	},
	methods: {
		async getProfile() {
			// 获取表格数据
			this.Result = await this.dataCount();
			console.log(this.Result);
			this.chinachart = echarts.init(document.getElementById('china_map'))
 
			// 进行相关配置
			this.chartOption = { 
				tooltip: { // 鼠标移到图里面的浮动提示框
				// formatter详细配置： https://echarts.baidu.com/option.html#tooltip.formatter
				formatter (params, ticket, callback) { 
					// params.data 就是series配置项中的data数据遍历
					let localValue
					if (params.data) {
						localValue = params.data.value
					} else { // 为了防止没有定义数据的时候报错写的
						localValue = 0
					}
					let htmlStr = `
						<div style='font-size:18px;'> ${params.name}</div>
						<p style='text-align:left;margin-top:-10px;'>
							区域对应数据value：${localValue}<br/>
						</p>
					`
					return htmlStr
				}
				// backgroundColor:"#ff7f50",//提示标签背景颜色
				// textStyle:{color:"#fff"} //提示标签字体颜色
				}, 
				// visualMap的详细配置解析：https://echarts.baidu.com/option.html#visualMap
				visualMap: { // 左下角的颜色区域
					type: 'piecewise', // 定义为分段型 visualMap
					min: 0,
					max: 1000,
					itemWidth: 40,
					bottom: 60,
					left: 20,
					/*background-image: linear-gradient(to right top, #bf0000, , , #807a00,
					 , #649902, , #5eb312, , #afcc00, #d7d700, 0); */
					pieces: [ // 自定义『分段式视觉映射组件（visualMapPiecewise）』的每一段的范围，以及每一段的文字，以及每一段的特别的样式
						{gt: 30000, lte: 35000, label: '很多', color: '#bf0000'}, // (900, 1000]
						{gt: 20000, lte: 30000, label: '多', color: '#af4500'}, // (500, 900]
						{gt: 10000, lte: 20000, label: '较多', color: '#648c00'}, // (310, 500]
						{gt: 6000, lte: 10000, label: '正常', color: '#62a608'}, // (200, 300]
				 		{gt: 4000, lte: 6000, label: '较少', color: '#87c000'}, // (10, 200]
						{gt: 2000, lte: 4000, label: '少', color: '#d7d700'}, 
						{gt: 0, lte: 2000, label: '很少', color: '#ffe100'}, // (10, 200]
						{value: 0, label: '无数据', color: '#999'} // [0]
					]
				},
				// geo配置详解： https://echarts.baidu.com/option.html#geo
				geo: { // 地理坐标系组件用于地图的绘制
					map: 'china', // 表示中国地图
					// roam: true, // 是否开启鼠标缩放和平移漫游
					zoom: 1.2, // 当前视角的缩放比例（地图的放大比例）
					label: {
						show: true
					},
					itemStyle: { // 地图区域的多边形 图形样式。
						borderColor: 'rgba(0, 0, 0, 0.2)',
						emphasis: { // 高亮状态下的多边形和标签样式
						shadowBlur: 20,
						shadowColor: 'rgba(0, 0, 0, 0.5)'
						}
					}
				},
				series: [
					{
						name: '', // 浮动框的标题（上面的formatter自定义了提示框数据，所以这里可不写）
						type: 'map',
						geoIndex: 0,
						label: {
						show: true
						},
						// 这是需要配置地图上的某个地区的数据，根据后台的返回的数据进行拼接（下面是我定义的假数据）
						data: []
					}
				]
			}

			this.chartOption.series[0].data = this.Result
			// 使用刚指定的配置项和数据显示地图数据
			this.chinachart.setOption(this.chartOption)
		},
		dataCount() {  
			var provinces = [
				"北京",
				"天津",
				"河北",
				"山西",
				"内蒙古",
				"辽宁",
				"吉林",
				"黑龙江",
				"上海",
				"江苏",
				"浙江",
				"安徽",
				"福建",
				"江西",
				"山东",
				"河南",
				"湖北",
				"湖南",
				"广东",
				"广西",
				"海南",
				"重庆",
				"四川",
				"贵州",
				"云南",
				"西藏",
				"陕西",
				"甘肃",
				"青海",
				"宁夏",
				"新疆",
				"台湾",
				"香港",
				"澳门"
				];
			const requests = provinces.map(region => {
				return this.$axios.get('/api/cars/count_by_province', {
				params: {
					province_name: region
				}
				}).then(response => {
			 	const count = response.data.count;
				return { name: region, value: count };
				}).catch(error => {
				console.error('请求出错:', error);
				return { name: region, value: 0 };
				});
			});

			return Promise.all(requests);
			// var temp = [];
			// for (let i=0; i<provinces.length; i++) {
			// 	let region = provinces[i];
			// 	this.$axios.get('/api/cars/count_by_province',{
			// 		province_name : region
			// 	}).then(response => {
			// 		const count = response.data.count;
			// 		temp.push({
			// 			"name":region,
			// 			"value":count
			// 		})
			// 	})
			// 	.catch(error => {
			// 		console.error('请求出错:', error);
			// 	});
			// }
		
			
			// console.log("map done!")
			// return temp;
		}
	}
}
</script>