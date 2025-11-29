<template>
  <div class="my-favorite">
    <!--  导航菜单  -->
    <div class="container">
      <el-menu class="navigation" mode="horizontal" :default-active="activeIndex"
          background-color="rgba(245, 246, 252, 1)" text-color="#1D1E21" active-text-color="rgba(255, 101, 27, 1)">
        <el-menu-item index="1"><a href="http://localhost:8080/home">首页</a></el-menu-item>
        <el-menu-item index="2"><a>我要买车</a></el-menu-item>
        <el-menu-item index="3"><a href="http://localhost:8080/sellcar">我要卖车</a></el-menu-item>
        <el-menu-item index="4"><a href="http://localhost:8080/boardoverview">数据看板</a></el-menu-item>
        <el-menu-item index="5"><a href="http://localhost:8080/pricepredict">价格趋势预测</a></el-menu-item>
        <el-menu-item index="6"><a href="http://localhost:8080/login">登录/注册</a></el-menu-item>
      </el-menu>
    </div>

    <!--左侧导航栏-->
    <div class="left-box">
      <el-menu class="menu_page"  mode="vertical" :default-active="activeIndex2"
               text-color="black" active-text-color="rgba(255, 101, 27, 1)">
        <el-menu-item index="0">
          <i class="el-icon-user-solid"></i>
          <a href="http://localhost:8080/person">个人信息</a>
        </el-menu-item>
        <el-menu-item index="1">
          <i class="el-icon-share"></i>
          <a href="http://localhost:8080/leftmenu">我的发布</a>
        </el-menu-item>
        <el-menu-item index="2">
          <i class="el-icon-star-on"></i>
          <span slot="title">我的收藏</span>
        </el-menu-item>
      </el-menu>
    </div>

    <!--中间主要body-->
    <div class="main">
      <el-table class="info" :data="tableData">
        <el-table-column fixed prop="model" label="车型" width="200"></el-table-column>
        <el-table-column prop="location" label="车辆所在地" width="150"></el-table-column>
        <el-table-column prop="time" label="上牌时间" width="120"></el-table-column>
        <el-table-column prop="miles" label="行驶里程" width="120"></el-table-column>
        <el-table-column prop="fuel" label="燃油类型" width="120"></el-table-column>
        <el-table-column prop="energy" label="能源类型" width="120"></el-table-column>
        <el-table-column prop="type" label="变速箱" width="120"></el-table-column>
        <el-table-column prop="times" label="过户次数" width="120"></el-table-column>
        <el-table-column prop="color" label="车身颜色" width="120"></el-table-column>
        <el-table-column prop="drive" label="驱动方式" width="120"></el-table-column>
        <el-table-column prop="price" label="期望售价" width="120"></el-table-column>
      </el-table>
    </div>

  </div>
</template>

<style scoped>
.my-favorite{
  position: fixed;
  width: 100%;
  background: url("../assets/left.jpg");
  background-size: 100% 100%;
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
  margin-left: 30px;
}
.menu_page {
  position: fixed;
  height:85%;
  width: 150px;
}
.menu_page .el-menu-item span{
  font-family: "Microsoft YaHei"; /* 设置文字字体 */
  font-size: 16px; /* 设置文字大小 */
  text-decoration: none; /* 取消文字下划线 */
}
.menu_page .el-menu-item a{
  font-family: "Microsoft YaHei"; /* 设置文字字体 */
  font-size: 16px; /* 设置文字大小 */
  text-decoration: none; /* 取消文字下划线 */
  color: gray;
}
.main{
  margin-top: 30px;
  width:86%;
  min-height: 660px;
  margin-left: 20px;
}

.info{
  left: 185px;
  height: 610px;
  width: 1220px;
  font-family: "Microsoft YaHei"; /* 设置文字字体 */
  font-size: 16px; /* 设置文字大小 */
}

</style>

<script>
export default {
  name: "user-page",
  data() {
    return {
      activeIndex2: '2',
      /*      tableData: [待从接口传入]*/
    };
  }
};
</script>