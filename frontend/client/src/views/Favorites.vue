<template>
  <el-container-up>
    <el-header style="background-color: rgba(245, 246, 252, 1);">
      <!--复用组件-->
      <div class="navigation-container">
        <NavigationMenuAfterLogin
        :activeIndex="activeIndex"
        :backgroundColor="backgroundColor"
        :textColor="textColor"
        :activeTextColor="activeTextColor"
      />
      </div>
    </el-header>

	<!--左侧导航栏-->
	<div class="left-box">
	<el-menu class="menu_page"  mode="vertical" :default-active="activeIndex2"
				text-color="black" active-text-color="rgba(255, 101, 27, 1)">
		<!--            <router-link to="/home">-->
		<el-menu-item index="0">
		<i class="el-icon-user-solid"></i>
		<span slot="title">个人信息</span>
		</el-menu-item>
		<el-menu-item index="1">
		<i class="el-icon-share"></i>
		<router-link to="/posts">我的发布</router-link>
		</el-menu-item>
		<!--            </router-link>-->
		<el-menu-item index="2">
		<i class="el-icon-star-on"></i>
		<router-link to="/favorites">我的收藏</router-link>
		</el-menu-item>
	</el-menu>
	</div>

  <div class="user-profile">

	<div class="main_up">
      <el-table class="info" :data="result">
        <el-table-column prop="brand" label="车型" width="200"></el-table-column>
        <el-table-column prop="location" label="车辆所在地" width="150"></el-table-column>
        <el-table-column prop="license_time" label="上牌时间" width="120"></el-table-column>
        <el-table-column prop="milesage" label="行驶里程" width="120"></el-table-column>
        <el-table-column prop="fuel_standard" label="燃油类型" width="120"></el-table-column>
        <el-table-column prop="energy" label="能源类型" width="120"></el-table-column>
        <el-table-column prop="displacement" label="排量" width="120"></el-table-column>
        <el-table-column prop="num_of_transfer" label="过户次数" width="120"></el-table-column>
        <el-table-column prop="color" label="车身颜色" width="120"></el-table-column>
        <el-table-column prop="drive_model" label="驱动方式" width="120"></el-table-column>
        <el-table-column prop="price" label="期望售价" width="120"></el-table-column>
      </el-table>
    </div>


  </div>
</el-container-up>
</template>

<script>
import NavigationMenuAfterLogin from "@/components/NavigationMenuAfterLogin.vue";
import { mapState } from "vuex";
export default {
  name: "UserProfile",
  components: {
    NavigationMenuAfterLogin,
  },
  data() {
    return {
		result: [],
	userInfo: null,
      activeIndex: "7",
      backgroundColor: "rgba(245, 246, 252, 1)",
      textColor: "#1D1E21",
      activeTextColor: "rgba(255, 101, 27, 1)",

	  favorites: null,
	  posts: null
    };
  },
  computed: {
	...mapState(["user"]),
		userId() {
			return this.user.id;
		}
  },
  methods: {
	async fetchCarData(id) {
      try {
        const response = await fetch(`api/cars/${id}`); // 调用 API 获取车辆信息
        const carData = await response.json(); // 解析 API 返回的数据
        this.result.push(carData); // 将车辆信息存储在 result 数组中
      } catch (error) {
        console.error(`获取车辆信息出错: ${error.message}`);
      }
    },
  },
  async created(){
		const ID = this.userId
		console.log(this.userId)
		const response = await this.$axios.get(`/api/users/${ID}`);
		if (response.status === 200) {
			this.userInfo = response.data;
			console.log("success!")
		} else{
			console.log(response)
		}

		for (let i = 0; i < this.userInfo.favorites.length; i++) {
			await this.fetchCarData(this.userInfo.favorites[i]); // 依次调用 API 获取所有车辆信息
		}

		console.log(this.result)
    }
};
</script>

<style scoped>
.header-align{
  display: flex;
  justify-content: flex-end;
}
.navigation-container {
  display: flex;
  justify-content: flex-end;
  align-items: center;
}
.user-profile {
  background-color: #f5f6fc;
  padding: 20px;
  background-image: url('../assets/ev-bg.png');
   background-size: cover;
   height: 100vh;
   margin-top: -30px;
}

.info-row {
  margin-top: 40px;
}

.avatar-container {
  text-align: center;
}

.avatar {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  background-color: #ccc;
}

.details {
  margin-left: 30px;
  font-size: 18px;
  color: #333;
}

.detail-item {
  margin-bottom: 15px;
}

.detail-item i {
  margin-right: 10px;
}

.detail-item span {
  font-weight: bold;
}

.user-page{
  position: fixed;
  width: 100%;
  background: url("../assets/left.jpg");
  /*  height: 100%;*/
  background-size: 110% 110%;
}
.container {
  display: flex;
  justify-content: flex-end;
  height: 40px;
}

.left-box{
  position: relative;
  width: 150px;
  margin-top: 30px;
  border-radius: 30px;
  /* margin-left: 0px; */
}
.menu_page {
  position: fixed;
  height:85%;
  width: 150px;
}
.menu_page .el-menu-item span{
  font-size: 16px; /* 设置文字大小 */
}
.menu_page .el-menu-item a{
  font-family: "Microsoft YaHei"; /* 设置文字字体 */
  font-size: 16px; /* 设置文字大小 */
  text-decoration: none; /* 取消文字下划线 */
  color: gray;
}
.main_up{
  width:100%;
  height: 200px;
  margin-left: 80px;
}
.info {
  height: 400px;
  width:1200px;
  background-color: #FFFFFF;
  border-radius: 20px;
  margin-top: 30px;
  margin-left: 120px;
}
.second-content {
  font-size: 18px;
  line-height: 40px;
  font-weight: bold;
  margin-left: 200px;
  margin-top: 40px;
  margin-bottom: 2px;
  text-align-last: justify;   /*两端对齐*/
  max-width: 90px;
}
.third-content {
  font-size: 18px;
  line-height: 40px;
  margin-left: 20px;
  margin-top: 40px;
  margin-bottom: 2px;
  text-align: left;
}

</style>