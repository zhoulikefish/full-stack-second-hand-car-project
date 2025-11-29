<template>
  <div class="register">
    <div style="background-color: rgba(245, 246, 252, 1);">
      <NavigationMenu
      :activeIndex="activeIndex"
      :backgroundColor="backgroundColor"
      :textColor="textColor"
      :activeTextColor="activeTextColor"
      />
    </div>
    <section class="form_container">
      <div class="manage_tip">
        <span class="title">用户注册</span>
      </div>
      <el-form
        :model="registerUser"
        :rules="rules"
        class="registerForm"
        ref="registerForm"
        label-width="100px"
      >
        <el-form-item label="用户名" prop="name">
          <el-input v-model="registerUser.name" placeholder="请输入用户名"></el-input>
        </el-form-item>
        <el-form-item label="电话" prop="phone">
          <el-input v-model="registerUser.phone" placeholder="请输入电话号码"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input v-model="registerUser.password" placeholder="请输入密码" type="password"></el-input>
        </el-form-item>
        <el-form-item label="确认密码" prop="password2">
          <el-input v-model="registerUser.password2" placeholder="请确认密码" type="password"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" class="submit_btn" @click="submitForm('registerForm')">注册</el-button>
        </el-form-item>
      </el-form>
    </section>
  </div>
</template>

<script>
import NavigationMenu from "@/components/NavigationMenu.vue";
export default {
  components: {
    NavigationMenu
  },
  name: "register",
  data() {
    const validatePass2 = (rule, value, callback) => {
      if (value !== this.registerUser.password) {
        callback(new Error("两次输入密码不一致!"));
      } else {
        callback();
      }
    };

    return {
      activeIndex: '1',
      backgroundColor: 'rgba(245, 246, 252, 1)',
      textColor: '#1D1E21',
      activeTextColor: 'rgba(255, 101, 27, 1)',
      registerUser: {
        name: "",
        phone: "",
        password: "",
        password2: ""
      },
      rules: {
        name: [
          { required: true, message: "用户名不能为空", trigger: "change" },
          { min: 2, max: 30, message: "长度在 2 到 30 个字符", trigger: "blur" }
        ],
        phone: [
          { required: true, message: '电话号码不能为空', trigger: 'blur' },
          {
            min: 11,
            max: 11,
            pattern: /^\d{11}$/,
            message: '电话号码长度必须为11位数字',
            trigger: 'blur'
          }
        ],
        password: [
          { required: true, message: "密码不能为空", trigger: "blur" },
          { min: 6, max: 30, message: "长度在 6 到 30 个字符", trigger: "blur" }
        ],
        password2: [
          { required: true, message: "确认密码不能为空", trigger: "blur" },
          { min: 6, max: 30, message: "长度在 6 到 30 个字符", trigger: "blur" },
          { validator: validatePass2, trigger: "blur" }
        ]
      }
    };
  },

  computed: {
    isFormValid() {
      return this.$refs.registerForm.validate().valid;
    }
  },
  
  methods: {
    // handleSelect(key, keyPath) {
    //   console.log(key, keyPath);
    // },
    submitForm(formName) {
      
      this.$refs[formName].validate(valid => {
        console.log(this.registerUser);
        if (valid) {
          this.$axios
            .post("/api/users/register", this.registerUser)
            .then(res => {
              this.$message({
                message: "注册成功！",
                type: "success"
              });
              this.$router.push("/login");
            });
        } else { 
          console.log("error submit!!");
          return false;
        }
      }); 
    }
  }
};
</script>

<style scoped>
.container {
  display: flex;
  justify-content: flex-end;
}

.navigation .el-menu-item,
.navigation .el-menu-item a {
  font-family: "Microsoft YaHei";
  font-size: 16px;
  font-weight: bold;
  text-decoration: none;
}

.register {
  position: fixed;
  width: 100%;
  height: 100%;
  background-color: rgba(245, 246, 252, 1);
  background-image: url(../assets/car.png);
  background-size: 55% 60%;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-position: 15% 60%;
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

.registerForm {
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
  position: relative;
  left: -60px;
  font-family: "Microsoft YaHei";
  font-weight: bold;
  font-size: 20px;
}
</style>
