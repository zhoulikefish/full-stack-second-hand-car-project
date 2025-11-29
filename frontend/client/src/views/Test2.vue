<template>
  <div class="login">
      <div class="container">
        <NavigationMenu
      :activeIndex="activeIndex"
      :backgroundColor="backgroundColor"
      :textColor="textColor"
      :activeTextColor="activeTextColor"
      />
    </div>
      <section class="form_container">
          <div class="manage_tip">
              <span class="title">用户登录</span>
          </div>
          <el-form :model="loginUser" :rules="rules" ref="loginForm" class="loginForm" label-width="60px">
              <el-form-item label="电话" prop="phone">
                  <el-input v-model="loginUser.phone" placeholder="请输入电话"></el-input>
              </el-form-item>
              <el-form-item label="密码" prop="password">
                  <el-input v-model="loginUser.password" placeholder="请输入密码" type="password"></el-input>
              </el-form-item>
              <el-form-item>
                  <el-button type="primary"  @click="submitForm('loginForm')" class="submit_btn">登  录</el-button>
              </el-form-item>
              <div class="tiparea">
                  <p>还没有账号？现在<router-link to='/register'>注册</router-link></p>
              </div>
          </el-form>
      </section>
  </div>
</template>

<script>
import jwt_decode from "jwt-decode";
import NavigationMenu from "@/components/NavigationMenu.vue";
export default {
components: {
  NavigationMenu
},


name: "login",
data() {
  return {
    activeIndex: '6',

    loginUser: {
      phone: "",
      password: ""
    },
    rules: {
      phone: [
        { required: true, message: '电话号码不能为空', trigger: 'blur' },
        { min: 11, max: 11, pattern: /^\d{11}$/,
          message: '电话号码长度必须为11位数字', trigger: 'blur' },
      ],
      password: [
        { required: true, message: "密码不能为空", trigger: "blur" },
        { min: 6, max: 30, message: "长度在 6 到 30 个字符", trigger: "blur" }
      ]
    }
  };
},
computed: {
  isFormValid() {
    return this.$refs.form.validate().valid;
  }
},
methods: { 
  submitForm(formName) {
    this.$refs[formName].validate(valid => {
      if (valid) {
        this.$axios.post("/api/users/login", this.loginUser).then(res => {
          // 登录成功
          const { token } = res.data;
          localStorage.setItem("eleToken", token);
          
          // 解析token
          const decode = jwt_decode(token);

          // 存储数据
          this.$store.dispatch("setIsAutnenticated", !this.isEmpty(decode));
          this.$store.dispatch("setUser", decode);

          // 页面跳转
          this.$router.push("/home");
        });
      } else {
        console.log("error submit!!");
        return false;
      }
    });
  },
  isEmpty(value) {
    return (
      value === undefined ||
      value === null ||
      (typeof value === "object" && Object.keys(value).length === 0) ||
      (typeof value === "string" && value.trim().length === 0)
    );
  }
}
};
</script>

<style scoped>
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

.login {
position: fixed;
width: 100%;
height: 100%;
background-color: rgba(245, 246, 252, 1);
background-image: url(../assets/car.png);
background-size: 55% 60%;
background-repeat: no-repeat;
background-attachment:fixed;
background-position:15% 60%;
}
.form_container {
width: 380px;
height: 210px;
position: relative;
top: 10%;
left: 65%;
padding: 25px;
border-radius: 5px;
text-align: center;
}
.form_container .manage_tip .title {
font-family: "Microsoft YaHei";
font-weight: bold;
font-size: 28px;
color: #1D1E21;
}
.loginForm {
margin-top: 20px;
background-color: #fff;
padding: 25px 40px 20px 20px;
border-radius: 5px;
box-shadow: 0px 5px 10px #cccc;
}

.submit_btn {
border: none;
width: 120%;
background: rgba(255, 101, 27, 1);
display: flex;
justify-content: center;
position:relative;
left:-50px;
font-family: "Microsoft YaHei";
font-weight: bold;
font-size: 20px;
}

.tiparea {
text-align: right;
font-size: 15px;
color: #333;
}
.tiparea p a {
color: #409eff;

}
</style>


