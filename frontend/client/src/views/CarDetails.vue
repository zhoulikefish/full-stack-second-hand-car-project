<!-- 
    * @FileDescription: 车辆细节信息页面
    * @LastEditTime: 7.10
 -->

<template>
    <el-container>
      <!--导航栏-->
      <el-header class="right-align" style="background-color: rgba(245, 246, 252, 1);">
        <NavigationMenuAfterLogin
        :activeIndex=2
        :backgroundColor="backgroundColor"
        :textColor="textColor"
        :activeTextColor="activeTextColor"
      />
      </el-header>
  
      <el-main>
        <el-row class="parallel-container">
          <el-col :span="12" style="margin-right: 80px;">   <!--左边block占页面比-->
  
            <!--走马灯-->
            <div class="section" style="display: flex; flex-direction: column;">
              <el-carousel trigger="click" height="450px" width="350px" v-model="currentThumbnailIndex">
                <el-carousel-item v-for="(item, index) in this.thumbnails" :key="index">
                  <div class="picture">
                    <img :src="item.image" alt="carousel-image">
                  </div>
                </el-carousel-item>
              </el-carousel>
            </div>
  
            <!--缩略图 待改进-->
            <div class="thumbnails-container" style="margin-top: -20px;">
              <div v-for="(thumbnail, index) in thumbnails" :key="index" class="thumbnail" :class="{ active: index === currentThumbnailIndex }">
                <img :src="thumbnail.image" alt="" style="margin-top:15px; margin-left:10px; width: 180px; height: 100px;" @click="changeCurrentThumbnail(index)">
              </div>
            </div>
  
          </el-col>
  
          <el-col :span="12" class="right-div">  <!-- 右上角 -->
            <!-- 车辆信息 -->
            <el-row class="sub-container1"> 
              <el-col :span="24" class="upper-right-div ">
  
              <h1 class="car-title">{{ this.car.title }}</h1>
              <el-col :span="6"> 
                  <h2 class="second">上牌时间</h2>
                  <h2 class="second">里程</h2>
                  <h2 class="second">标准/排量</h2>
                  <h2 class="second">所在地</h2>
                  <h2 class="second">转手次数</h2>
                  <h2 class="price">报价</h2>
              </el-col>

              <el-col :span="18"> 
                  <h3 class="third">{{ this.car.license_time }}</h3>
                  <h3 class="third">{{ this.car.mileage }}</h3>
                  <h3 class="third">{{ this.car.emission_standards }} / {{ this.car.displacement }}</h3>
                  <h3 class="third">{{ this.car.location }}</h3>
                  <h3 class="third">{{this.car.num_of_transfer}}</h3>
                  <h3 class="price">{{this.car.price}} 万</h3>
            </el-col>
            <h2 class="second">&nbsp;</h2>
              <el-row class="temp_d">
                <el-button @click="onSubmit" style="background-color: #3563E9; color: #FFFFFF; width: 150px; margin-left:50px;  font-size: 18px;">
                  <a href="mailto:maob@sem.tsinghua.edu.cn" style="color: #FFFFFF; text-decoration: none;">联系车商</a>
                </el-button>

                <el-button @click="toggleFavorite" style="background-color: #3563E9; color: #FFFFFF; 
                    width: 150px; margin-left:50px; font-size: 18px; ">{{ isFavorite ? '取消收藏' : '添加收藏' }}
                </el-button>
              </el-row>

              </el-col>
            </el-row>
          </el-col>
        </el-row>
  
        <!--购买流程-->
        <el-row class="sub-container" style="margin-top: 10px;">
          <el-col :span="24" class="lower-left-div1">
            <h1 class="detail_info " >购买流程</h1>
            <img src="../assets/process1.png" alt="购买流程" width="1200px" height="150px">
          </el-col>
        </el-row>

        <el-row class="sub-container"> 
          <el-col :span="24" class="lower-left-detail" >
            <h1 class="detail_info" >车辆档案</h1>
  
              <!-- 左边 -->
            <el-col :span="6" > 
              <h2 class="second-content">上牌时间</h2>
              <h2 class="second-content">里程</h2>
              <h2 class="second-content">标准/排量</h2>
              <h2 class="second-content">车辆所在地</h2>
              <h2 class="second-content">转手次数</h2>
              <h2 class="second-content">&nbsp;</h2>
            </el-col>
  
            <el-col :span="6"> 
              <h3 class="third-content">{{ this.car.license_time }}</h3>
              <h3 class="third-content">{{ this.car.mileage }}</h3>
              <h3 class="third-content">{{ this.car.emission_standards }} / {{ this.car.displacement }}</h3>
              <h3 class="third-content">{{ this.car.location }}</h3>
              <h3 class="third-content">{{ this.car.num_of_transfer }}</h3>
            </el-col>
     
            <!-- 右边 -->
            <el-col :span="6"> 
              <h2 class="second-content">发动机</h2>
              <h2 class="second-content">车辆级别</h2>
              <h2 class="second-content">车身颜色</h2>
              <h2 class="second-content">燃油标号</h2>
              <h2 class="second-content">驱动方式</h2>
            </el-col>
  
            <el-col :span="6"> 
              <h3 class="third-content">{{ this.car.engine }}</h3>
              <h3 class="third-content">中大型车</h3>
              <h3 class="third-content">{{ this.car.color }}</h3>
              <h3 class="third-content">{{ this.car.fuel_standard }}</h3>
              <h3 class="third-content">{{ this.car.drive_model }}</h3>
            </el-col>
          </el-col>
        </el-row>
        
  
  
  
  
      </el-main>
    </el-container>
  </template>
  
  <style>


  /* 顶部导航 */
    .right-align {
      display: flex;
      justify-content: flex-end;
    }
  
    .navigation .el-menu-item, .el-menu-item a{
      font-family: "Microsoft YaHei"; 
      font-size: 16px; 
      font-weight: bold; 
      text-decoration: none; 
    }
  
  /* 底部block */
    el-container {
      display: flex;
      flex-direction: column;
      height: 100vh; 
    }
  
    .el-header {
      background-color: #F6F7F9;
      color: #333;
      line-height: 60px;
    }
  
    .el-main {
      background-color: #F6F7F9;
      color: #333;
      text-align: center;
      line-height: 160px;
      min-height: 100vh;  /* 百分百铺满 */
    }
  
    .section {
      margin-bottom: 20px;
    }
  
  /* 框内字体细节 - 右侧 */
    .car-title{
      font-size: 24px !important;
      margin-left: 30px;
      margin-bottom: 25px;
      font-weight: bold;
      line-height: 30px;
      margin-top: 30px;
      font-family: Arial, Helvetica, sans-serif; /*字体不一样*/ 
      text-align: left;
    }
  
    .second {
      font-size: 18px;
      line-height: 40px;
      font-weight: bold;
      margin-left: 30px;
      margin-bottom: 2px;
      
      text-align-last: justify;   /*两端对齐*/
      max-width: 90px;
  
    }
  
    .third {
      font-size: 18px;
      line-height: 40px;
      margin-left: 30px;
      margin-bottom: 2px;
  
  
    }
    .temp_d{
      margin-top: 10px;
    }
  
    .sub-container {
      margin-left: 10px;
      margin-right: 10px;
      margin-bottom: 10px;
      display: flex;
      justify-content: space-between;
    }
  
    .second-content {
      font-size: 18px;
      line-height: 40px;
      font-weight: bold;
      margin-left: 200px;
      margin-bottom: 2px;
     
      text-align-last: justify;   /*两端对齐*/
      max-width: 90px;
  
    }
  
    .third-content {
      font-size: 18px;
      line-height: 40px;
      margin-left: 20px;
      margin-bottom: 2px;
      text-align: left;
    }
  
    .price {
      color:chocolate;    
      line-height: 30px;
      font-weight: bold;
      font-size: 24px;
      margin-top: 20px;
      margin-left: 30px;
      margin-bottom: -10px;
    }
  
    .car-description-container {
      display: flex;
      align-items: center;
    }
  
    .detail_info {
      font-size: 20px;
      margin-left: 30px;
      margin-bottom: 25px;
      font-weight: bold;
      line-height: 20px;
      margin-top: 25px;
    }
    .picture{
      display: flex;
      justify-content: center;
      align-items: center;
    }
  /* 走马灯*/
    .thumbnails-container {
      display: flex;
      justify-content: flex-start;
      align-items: center;
      margin-top: 20px;
    }
    .thumbnail {
      opacity: 0.5;
      transition: opacity 0.3s;
      margin-right: 10px;
    }
    .thumbnail:last-child {
      margin-right: 0;
    }
    .thumbnail.active {
      opacity: 1;
    }
    
  
  
  
  
    .parallel-container {
      display: flex;
    }
  
    .lower-div1 {
      background-color: #FFFFFF;
      border-radius: 30px;
      margin-bottom: 10px;
      padding-bottom: 20px;
      margin-left: 25px;
    }
  
    .lower-div2 {
      margin-left: 10px;
      height: 180px;
      background-color: #FFFFFF;
      border-radius: 10px;
      margin-bottom: 10px;
      padding-bottom: 20px;
    }
  
    .lower-left-detail {
      min-height: 150px;
      background-color: #ffffff;
      border-radius: 30px;
      margin-top: 20px;
      margin-bottom: 10px;
      padding-bottom: 20px;
    }
    .upper-right-div {
      height: 36  0px;
      background-color: #FFFFFF;
      border-radius: 30px;
      margin-bottom: 10px;
      text-align: left;
      padding-left: 5px;
      padding-right: 20px;
    }
  
    .right-div {
      flex: 1;
      background-color: #F6F7F9;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 300px; 
    }
    
    .sub-container1 {
      margin-left: 10px;
      margin-right: 10px;
      height: 320px;
    }
  </style>
  
  <script>
    import NavigationMenuAfterLogin from "@/components/NavigationMenuAfterLogin.vue";
	import { mapState } from "vuex";
    export default {
		components: {
		NavigationMenuAfterLogin
		},
		data() {
		return {
			car: null,
			isFavorite: false,
			activeIndex: '1',
			backgroundColor: 'rgba(245, 246, 252, 1)',
			textColor: '#1D1E21',
			activeTextColor: 'rgba(255, 101, 27, 1)',

			currentImage: "",
			thumbnails: null,
			currentThumbnailIndex: 0,


			input: '',
			form: {
				name: '',
				region: '',
				date1: '',
				date2: '',
				delivery: false,
				type: [],
				resource: '',
				desc: ''
			}
		}
		},
		computed: {
			...mapState(["user"]),
			userId() {
				return this.user.id;
			}
		},
		methods: {
			handleChange(value) {
			console.log(value);
			},
			onSubmit() {
			console.log('submit!');
			},
			changeCurrentThumbnail(index)  {
			this.currentThumbnailIndex = index;
			},
			toggleFavorite() {
				if (this.isFavorite) {
					this.removeFavorite();
				} else {
					this.addFavorite();
				}
			},
			async addFavorite() {
			try {
					// console.log("start!")
					const response = await this.$axios.post('/api/users/addfavorite', {
						userId: this.userId, // 当前登录用户的 ID
						productId: this.$route.params.id, // 当前商品的 ID
					});

					if (response.status === 200) {
						this.$message({
						message: "收藏成功！",
						type: "success"
						})
					// 收藏成功，进行相应提示或处理
						this.isFavorite = true;
					}
				} catch (error) {
					// 处理错误
				}
				
			},
			async removeFavorite() {
				try {
					console.log("start!")
					const response2 = await this.$axios.post('/api/users/removefavorite', {
						userId: this.userId, // 当前登录用户的 ID
						productId: this.$route.params.id, // 当前商品的 ID
					});
					console.log(response2)
					if (response2.status === 200) {
						this.$message({
						message: "取消成功！",
						type: "success"
					})
					// 收藏成功，进行相应提示或处理
					this.isFavorite = false;
					}
				} catch (error) {
					// 处理错误
				}
				
			},

		},

		mounted() {
			
		},

		// 将$route.params.id对应的车辆信息存储到data中
		async created() {
			const productId = this.$route.params.id; 
			console.log(productId)// 假设商品 ID 从路由参数中获取
			// try {
			const response = await this.$axios.get(`/api/cars/${productId}`);
			if (response.status === 200) {
				this.car = response.data;
				console.log("success!")
			} else{
				console.log("fail!")
			}
			// } catch (error) {
			// // 处理错误
			// }
			this.thumbnails = [
			{ image: this.car.img_url[0], active: false },
			{ image: this.car.img_url[1], active: false },
			{ image: this.car.img_url[2], active: false },
			{ image: this.car.img_url[3], active: false },
			{ image: this.car.img_url[4], active: false }
			]

			console.log("1")

			try {
					console.log("start!")
					const response1 = await this.$axios.post('/api/users/check', {
						userId: this.userId, // 当前登录用户的 ID
						productId: productId
					});
					console.log("checkfavorite:",response1)
					// 收藏成功，进行相应提示或处理
					if(response1.data == True){
						this.isFavorite = false;
					}else{
						this.isFavorite = true;
					}
			} catch (error) {
				// 处理错误
			}
		}

	}
      
  </script>



  
