<!-- 
    * @FileDescription: 页面上方的导航栏, 已登陆版本
    * @LastEditTime: 7.10
 -->



 
 <template>
  <el-menu
    :default-active="activeIndex"
    class="navigation"
    mode="horizontal"
    @select="handleSelect"
    :background-color="backgroundColor"
    :text-color="textColor"
    :active-text-color="activeTextColor"
  >
  <el-menu-item index="1">
      <router-link to="/home" :class="{ 'active': activeIndex === '1' }">首页</router-link>
    </el-menu-item>
    <el-menu-item index="2">
      <router-link to="/search" :class="{ 'active': activeIndex === '2' }">我要买车</router-link>
    </el-menu-item>
    <el-menu-item index="3">
      <router-link to="/sellcar" :class="{ 'active': activeIndex === '3' }">我要卖车</router-link>
    </el-menu-item>
    <el-menu-item index="4">
      <router-link to="/evaluate" :class="{ 'active': activeIndex === '4' }">车辆估价</router-link>
    </el-menu-item>
    <el-menu-item index="5">
      <router-link to="/pricetimeseries" :class="{ 'active': activeIndex === '5' }">价格趋势</router-link>
    </el-menu-item>
    <el-menu-item index="6">
      <router-link to="/boardoverview" :class="{ 'active': activeIndex === '6' }">数据看板</router-link>
    </el-menu-item>
    <el-menu-item index="7">
      <router-link to="/userprofile" :class="{ 'active': activeIndex === '7' }">个人界面</router-link>
    </el-menu-item>
  </el-menu>
</template>











<!-- <template>
    <el-menu
      :default-active="activeIndex"
      class="navigation"
      mode="horizontal"
      @select="handleSelect"
      :background-color="backgroundColor"
      :text-color="textColor"
      :active-text-color="activeTextColor"
    >
      <el-menu-item index="1">
        <router-link to="./home">首页</router-link>
      </el-menu-item>
      <el-menu-item index="2">
        <router-link to="/">我要买车</router-link>
      </el-menu-item>
      <el-menu-item index="3">
        <router-link to="/sellcar">我要卖车</router-link>
      </el-menu-item>
      <el-menu-item index="4">
        <router-link to="/popularcar">热门车型</router-link>
      </el-menu-item>
      <el-menu-item index="5">
        <router-link to="/">在线估值</router-link>
      </el-menu-item>
      <el-menu-item index="6">
        <router-link to="/pricetimeseries">价格趋势预测</router-link>
      </el-menu-item>
      <el-menu-item index="7">
        <router-link to="/login">登录/注册</router-link>
      </el-menu-item>
    </el-menu>
  </template> -->







  
  
  <script>
  export default {
    name: 'NavigationMenu',
    props: {
      activeIndex: {
        type: String,
        default: '1'
      },
      backgroundColor: {
        type: String,
        default: 'rgba(245, 246, 252, 1)'
      },
      textColor: {
        type: String,
        default: '#1D1E21'
      },
      activeTextColor: {
        type: String,
        default: 'rgba(255, 101, 27, 1)'
      }
    },
    methods: {
      handleSelect(index) {
        // 处理菜单项选择的逻辑
      }
    }
  }
  </script>
  
  <style scoped>

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
  

  </style>
  
  
  <!-- <script>
  import jwt_decode from "jwt-decode";
  
  export default {
    name: "home",
    data() {
      return {
        activeIndex: '1',
      };
    },
  };
  </script> -->