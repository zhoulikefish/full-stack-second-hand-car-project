<!-- 
    * @FileDescription: 买车界面
    * @LastEditTime: 7.10
 -->



 <template>
    <div class="home">
        <div class="container">
        <!--复用组件-->
        <NavigationMenu
      :activeIndex="activeIndex"
      :backgroundColor="backgroundColor"
      :textColor="textColor"
      :activeTextColor="activeTextColor"
      />
        <!--导航菜单栏 登陆之前-->
        <!-- <el-menu
            :default-active="activeIndex"
            class="navigation"
            mode="horizontal"
            @select="handleSelect"
            background-color="rgba(245, 246, 252, 1)"
            text-color="#1D1E21"
            active-text-color="rgba(255, 101, 27, 1)">
            <el-menu-item index="1"><a href="./home">首页</a></el-menu-item>
            <el-menu-item index="2"><a href="./">我要买车</a></el-menu-item>
            <el-menu-item index="3"><a href="./sellcar">我要卖车</a></el-menu-item>
            <el-menu-item index="4"> <a href="./popularcar">热门车型</a></el-menu-item>
            <el-menu-item index="5"><a href="./">在线估值</a></el-menu-item>
            <el-menu-item index="6"><a href="./pricetimeseries">价格趋势预测</a></el-menu-item>
            <el-menu-item index="7"><a href="./login">登录/注册</a></el-menu-item>
      </el-menu> -->
      </div>
        <div class="container1">
            <p class="title1">我要买车界面</p>
        </div>
    </div>
</template>

<style scoped>
.home {
  position: fixed;
  width: 100%;
  height: 100%;
  background: url(../assets/car.png),
  url(../assets/line.png);
  background-size: 850px,200px;
  background-repeat: no-repeat;
  background-attachment:fixed;
  background-position:90% 65%, 25% 48%;
  background-color: rgba(245, 246, 252, 1);
}
.container {
  display: flex;
  justify-content: flex-end;
}
.navigation .el-menu-item {
  font-family: "Microsoft YaHei"; /* 设置文字字体 */
  font-size: 16px; /* 设置文字大小 */
  font-weight: bold; /* 设置文字加粗 */
  text-decoration: none; /* 取消文字下划线 */
}
.navigation .el-menu-item a {
  font-family: "Microsoft YaHei"; /* 设置文字字体 */
  font-size: 16px; /* 设置文字大小 */
  font-weight: bold; /* 设置文字加粗 */
  text-decoration: none; /* 取消文字下划线 */
}

.container1 {
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  padding-top: 100px;
  text-align: center;
  color: white;
}
.title1 {
  font-size: 60px;
  font-family: "Microsoft YaHei";
  font-weight: bold;
  color: #1D1E21;
  position: relative;
  right: 400px;
  top: 20px;
}
.title2 {
  font-size: 60px;
  font-family: "Microsoft YaHei";
  font-weight: bold;
  position: relative;
  color: #1D1E21;
  right: 400px;
  top: 40px;
}
.intro1 {
  font-size: 16px;
  font-family: "Microsoft YaHei";
  font-weight: bold;
  position: relative;
  color: rgba(146, 147, 149, 1);
  right: 440px;
  top: 100px;
}
.intro2 {
  font-size: 16px;
  font-family: "Microsoft YaHei";
  font-weight: bold;
  position: relative;
  color: rgba(146, 147, 149, 1);
  right: 408px;
  top: 110px;
}
</style>


<script>
import jwt_decode from "jwt-decode";
import NavigationMenu from '@/components/NavigationMenu.vue';



export default {
  name: "home",
  data() {
    return {
      activeIndex: '1',
    };
  },
  components: {
    NavigationMenu
  },
  data() {
    return {
      activeIndex: '1',
      backgroundColor: 'rgba(245, 246, 252, 1)',
      textColor: '#1D1E21',
      activeTextColor: 'rgba(255, 101, 27, 1)'
    };
  }
};
</script>