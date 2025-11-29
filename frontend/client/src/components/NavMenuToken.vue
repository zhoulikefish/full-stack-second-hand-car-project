<!-- 
    * @FileDescription: 页面上方的导航栏, 未登陆版本
    * @LastEditTime: 7.10
 -->




 <template>
  <div>
    <template v-if="isLoggedIn">
      <NavigationMenuAfterLogin
        :activeIndex="activeIndex"
        :backgroundColor="backgroundColor"
        :textColor="textColor"
        :activeTextColor="activeTextColor"
      />
    </template>
    <template v-else>
      <NavigationMenu
        :activeIndex="activeIndex"
        :backgroundColor="backgroundColor"
        :textColor="textColor"
        :activeTextColor="activeTextColor"
      />
    </template>
  </div>
</template>

<script>
import NavigationMenu from './NavigationMenu.vue';
import NavigationMenuAfterLogin from './NavigationMenuAfterLogin.vue';

export default {
  name: 'Navbar',
  components: {
    NavigationMenu,
    NavigationMenuAfterLogin
  },
  data() {
    return {
      activeIndex: 0, // 当前激活的菜单项索引
      backgroundColor: '#ffffff', // 背景颜色
      textColor: '#000000', // 文字颜色
      activeTextColor: '#ff0000' // 激活时的文字颜色
    };
  },
  computed: {
    isLoggedIn() {
      // 根据你的登录逻辑来计算用户的登录状态
      // 返回 true 表示已登录，返回 false 表示未登录
      // 可以根据实际情况修改下面的判断逻辑
      const token = localStorage.getItem('eletoken');
      if (token) {
        return true;
      }
      return false;
    }
  }
};
</script>

<style>
/* 根据你的需要自定义样式 */
</style>