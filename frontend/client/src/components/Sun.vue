<template>
    <!--渲染Echarts图表的容器-->
    <div id="main" style="width: 100%; height: 400px"></div>
</template>

<script>
    // 引入Echarts
    import * as echarts from 'echarts';

    export default {
        name: 'App',	
		props: {
			item: {
				type: Object,
			},
		},
        // 属性
        data() {
            return {
                // 保存原始数据
                dataMap: [],
				Result: []
            }
        },
		created(){
			this.getProfile();
			// console.log(this.dataMap);
		},
        // 生命周期函数
        mounted() {
            // 渲染图表
			// console.log(this.Result)
            // this.initEcharts();
        },
        // 方法定义
        methods: {
			getProfile() {
				// 获取表格数据
				// this.$axios("/api/cars/").then((res) => {
				// 	// this.tableData = res.data;
				// 	this.dataMap.Alldata = res.data;
				// 	this.Result = this.dataCount(this.dataMap.Alldata);
				// 	// console.log(this.Result);
				// 	this.initEcharts();
				// });
				this.$axios("/api/cars/sunchart").then((res) => {
					// this.tableData = res.data;
					this.Result = res.data;
					// this.Result = this.dataCount(this.dataMap.Alldata);
					// console.log(this.Result);
					this.initEcharts();
				});
			},

            // 渲染Echarts图表
            initEcharts() {
                // 获取DOM元素（根据id）
                var chartDom = document.getElementById('main');
                // 初始化
                var myChart = echarts.init(chartDom);
                // 属性
				var option = {
					series: {
						type: 'sunburst',
						data: this.Result,
						radius: [60, '90%'],
						itemStyle: {
						borderRadius: 7,
						borderWidth: 2
						},
						label: {
							show: true,
							formatter: function(params) {
								return params.name + '\n' + params.value;
							}
						}
					}

					
				},
						
				grid = { // 让图表占满容器
					top:"0px",
					left:"0px",
					right:"0px",
					bottom:"0px"
				}
			

				option && myChart.setOption(option);

			},

			// 数据格式化
			dataCount(dataFrame) {

				// 递归函数，用于构建嵌套的字典结构 key = model/title
				function buildDictionary(data, key) {
					var brandlist = ["奔驰","宝马","本田"]
					var dict = {};
					data.forEach(function (item) {
						// console.log(item)
						var value = item[key];
						if((key=='brand' & brandlist.indexOf(value)>=0)||
						(key=='model')){
							if (!dict[value]) {
							dict[value] = [];
							}
							dict[value].push(item);
						}
					});

					var result = [];
					for (var prop in dict) {
						if(key=='brand'){
							var children = buildDictionary(dict[prop], 'model');
							result.push({ name: prop, value: dict[prop].length, children: children });
						}else if(dict[prop].length>200){
						
						result.push({ name: prop, value: dict[prop].length});
						}
					}
					return result;
				}

				// 构建字典
				var result = buildDictionary(dataFrame, 'brand');

				// 将结果转换为JSON格式
				// var json = JSON.stringify(result);

				// 输出结果
				console.log(result);

				return result;
            },

        },

		watch: {
			"item.width"() {
			this.barChart.resize({
				width: this.item.width,
				height: this.item.height,
			});
			},
			"item.height"() {
			this.barChart.resize({
				width: this.item.width,
				height: this.item.height,
			});
			},
		},

    }
</script>

<style>
    #main{
        width: 800px;
        height: 500px;
    }
</style>