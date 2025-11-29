<template>
  <div class="logFund">
       <el-dialog 
          :title="dialog.title" 
          :visible.sync="dialog.show"
          :close-on-click-modal='false'
          :close-on-press-escape='false'
          :modal-append-to-body="false">
          <div class="form">
              <el-form 
                  ref="form" 
                  :model="form"
                  :rules="form_rules"
                  label-width="120px" 
                  style="margin:10px;width:auto;">

                  
                  <el-form-item label="车辆类型" prop="type">
                    <el-input v-model="form.type"></el-input>
                  </el-form-item>
                  <el-form-item label="车辆描述" prop="describe">
                    <el-input v-model="form.describe"></el-input>
                  </el-form-item>
                  <el-form-item label="价格" prop="price">
                    <el-input v-model="form.price"></el-input>
                  </el-form-item>
                  <el-form-item label="车辆年龄" prop="age">
                    <el-input v-model="form.age"></el-input>
                  </el-form-item>
                  <el-form-item label="记录日期" prop="date">
                    <el-date-picker v-model="form.date" type="date" value-format="yyyy-MM-dd"></el-date-picker>
                  </el-form-item>

                  

                  <el-form-item  class="text_right">
                      <el-button @click="dialog.show = false">取 消</el-button>
                      <el-button type="primary" @click='onSubmit("form")'>提  交</el-button>
                  </el-form-item>

              </el-form>
          </div>
      </el-dialog>
  </div>
</template>

<script>
export default {
name: "logfound",
props: {
  dialog: Object,
  form: Object
},
data() {
  return {
    format_type_list: [
      // TBD
    ],
    form_rules: {
      type: [
        { required: true, message: "车辆类型不能为空！", trigger: "blur" }
      ],
      describe: [
        { required: true, message: "车辆描述不能为空！", trigger: "blur" }
      ],
      price: [
        { required: true, message: "价格不能为空！", trigger: "blur" }
      ],
      age: [
        { required: true, message: "车辆年龄不能为空！", trigger: "blur" }
      ],
      date: [{ required: true, message: "记录日期不能为空！", trigger: "blur" }]
    }
  };
},
methods: {
  onSubmit(form) {
    this.$refs[form].validate(valid => {
      if (valid) {
        // 表单数据验证完成之后，提交数据
        const url =
          this.dialog.option == "add" ? "add" : `edit/${this.form.id}`;
        this.$axios.post(`/api/profiles/${url}`, this.form).then(res => {
          // 操作成功
          this.$message({
            message: "保存成功！",
            type: "success"
          });
          this.dialog.show = true;
          this.$emit("update");
        });
      }
    });
  }
}
};
</script>
