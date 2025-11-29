<template>
    <!--渲染Echarts图表的容器-->
    <div id="pan" style="width: 100%; height: 400px"></div>
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
				this.$axios("/api/cars/").then((res) => {
					// this.tableData = res.data;
					this.dataMap.Alldata = res.data;
					this.Result = this.dataCount(this.dataMap);
					// console.log(this.Result);
					this.initEcharts();
				});
			},

            // 渲染Echarts图表
            initEcharts() {
                // 获取DOM元素（根据id）
                var chartDom = document.getElementById('pan');
                // 初始化
                var myChart = echarts.init(chartDom);
                // 属性
                var option = {
					tooltip: {
						trigger: 'item'
					},
					legend: {
						top: '5%',
						left: 'center'
					},
					series: [
						{
						name: 'Access From',
						type: 'pie',
						radius: ['40%', '70%'],
						avoidLabelOverlap: false,
						itemStyle: {
							borderRadius: 10,
							borderColor: '#fff',
							borderWidth: 2
						},
						label: {
							show: false,
							position: 'center'
						},
						emphasis: {
							label: {
							show: true,
							fontSize: 40,
							fontWeight: 'bold'
							}
						},
						labelLine: {
							show: false
						},
						data: [
							{ value: this.Result['宝马'], name: '宝马' },
							{ value: this.Result['丰田'], name: '本田' },
							{ value: this.Result['沃尔沃'], name: '沃尔沃' },
							{ value: this.Result['奔驰'], name: '奔驰' },
							{ value: this.Result['大众'], name: '大众' },
							// { value: 100, name: '大' },
							// { value: 100, name: '中' },
							// { value: 100, name: '小' }
						]
						}
					],
					grid:{ // 让图表占满容器
					top:"0px",
					left:"0px",
					right:"0px",
					bottom:"0px"
					}
				};

				option && myChart.setOption(option);

			},

			// 数据格式化
			dataCount(obj) {
				// const response = await this.getProfile();
				var temp = [];
				// console.log(obj)
				var brand_list = ["宝马","丰田","沃尔沃"]
				for (let i=0; i<brand_list.length; i++) {
					// console.log(type_list[i])
					var brand = brand_list[i]
					// console.log(obj["Alldata"].length)
					temp[brand] = 0
					// console.log(temp)
					for(let j=0; j<obj.Alldata.length; j++){
						// console.log(obj)
						let item = obj.Alldata[j] 
						
						if(item.brand==brand){
							temp[brand] = temp[brand]+1
						}
					}
				}

				console.log(temp.length)
				return temp;	
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