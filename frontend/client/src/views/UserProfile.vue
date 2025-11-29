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
			<div class="info">
					<div class="avatar">
					<img src="./assets/default.jpeg" alt="Avatar">
					</div>
			<div style="position: absolute; margin-top: 280px; margin-left: 475px;">
 
					<h2>{{ userInfo.name }}</h2>
					<ul>
						<li><i class="fa fa-envelope"></i> {{ userInfo.date }}</li>
						<li><i class="fa fa-phone" style=" margin-left: -85px;"></i> {{ userInfo.phone }}</li>
					</ul>
			</div>

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
	align-items: center;
	/* position: relative;  */
	
  }
  

  
  .avatar {
	display: flex;
	justify-content: center;
	align-items: center;
	width: 150px;
	height: 150px;
	border-radius: 50%;
	object-fit: cover;
	background-color: #ccc;
	margin-left: 500px;
	margin-top: 100px;
	position: absolute; 
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

  .info {
	height: 400px;
	width:1200px;
	background-color: #FFFFFF;
	border-radius: 20px;
	margin-top: 10px;
	margin-left: 200px;
	align-items: center;
	text-align: center;
  }
  .profile {
  display: flex;
  align-items: center;
  /* padding: 20px; */
  /* border: 1px solid #ccc; */
  border-radius: 8px;
  /* width: 300px; */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}




h2 {
  margin: 0;
  font-size: 24px;
  color: #333;
  text-align: center;
}

p {
  margin: 5px 0;
  font-size: 14px;
  color: #666;
  text-align: center;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

ul li {
  /* display: flex; */
  align-items: center;
  text-align: center;
}

ul li i {
  margin-right: 5px;
  font-size: 16px;
  color: #999;
}
  
  </style>