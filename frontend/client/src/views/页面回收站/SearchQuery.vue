<template>
  <div class="fillcontain">
    <div>
      <el-form :inline="true" ref="search_data" :model="search_data">
        <el-form-item label="价格筛选:">
          <el-input v-model.number="search_data.maxPrice" placeholder="输入最大价格"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" size="small" icon="search" @click="onScreeoutMoney()">筛选</el-button>
        </el-form-item>
        <el-form-item class="btnRight">
          <el-button type="primary" size="small" icon="view" @click="onAddProfile()">添加</el-button>
        </el-form-item>
      </el-form>
    </div>
    <div class="table_container">
      <el-table :data="tableData" border style="width: 100%">
        <el-table-column type="index" label="序号" align="center" width="70"></el-table-column>
        <el-table-column prop="type" label="车辆类型" align="center" width="150"></el-table-column>
        <el-table-column prop="describe" label="描述" align="center" width="250"></el-table-column>
        <el-table-column prop="price" label="价格" align="center" width="150"></el-table-column>
        <el-table-column prop="age" label="车龄" align="center" width="150"></el-table-column>
        <el-table-column prop="date" label="发布时间" align="center" width="200" sortable></el-table-column>
        <el-table-column prop="operation" align="center" label="操作" fixed="right" width="180">
          <template slot-scope="scope">
            <el-button type="warning" icon="edit" size="small" @click="onEditProfile(scope.row)">编辑</el-button>
            <el-button type="danger" icon="delete" size="small" @click="onDeleteProfile(scope.row, scope.$index)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>

      <!-- 分页 -->
      <el-row>
        <el-col :span="24">
          <div class="pagination">
            <el-pagination
              v-if="paginations.total > 0"
              :page-sizes="paginations.page_sizes"
              :page-size="paginations.page_size"
              :layout="paginations.layout"
              :total="paginations.total"
              :current-page.sync="paginations.page_index"
              @current-change="handleCurrentChange"
              @size-change="handleSizeChange"
            ></el-pagination>
          </div>
        </el-col>
      </el-row>
    </div>
    <!-- 弹框页面 -->
    <DialogFound :dialog="dialog" :form="form" @update="getProfile"></DialogFound>
  </div>
</template>

<script>
import DialogFound from "../components/DialogFound";

export default {
  name: "fundlist",
  data() {
    return {
      tableData: [],
      allTableData: [],
      dialog: {
        show: false,
        title: "",
        option: "edit",
      },
      form: {
        type: "",
        describe: "",
        price: "",
        age: "",
        date: "",
        id: "",
      },
      // 需要给分页组件传的信息
      paginations: {
        page_index: 1, // 当前位于哪页
        total: 0, // 总数
        page_size: 5, // 1页显示多少条
        page_sizes: [5, 10, 15, 20], // 每页显示多少条
        layout: "total, sizes, prev, pager, next, jumper", // 翻页属性
      },
      search_data: {
        maxPrice: null,
      },
    };
  },
  components: {
    DialogFound,
  },
  created() {
    this.getProfile();
  },
  methods: {
    getProfile() {
      // 获取表格数据
      this.$axios("/api/cars").then((res) => {
        this.allTableData = res.data;
        this.filterTableData = res.data;
        // 设置分页数据
        this.setPaginations();
      });
    },

    onEditProfile(row) {
      // 编辑
      this.dialog = {
        show: true,
        title: "修改二手车信息",
        option: "edit",
      };
      this.form = {
        type: row.type,
        describe: row.describe,
        price: row.price,
        age: row.age,
        date: row.date,
        id: row._id,
      };
    },

    onDeleteProfile(row, index) {
      // 删除
      this.$axios.delete(`/api/profiles/delete/${row._id}`).then((res) => {
        this.$message("删除成功");
        this.getProfile();
      });
    },

    onAddProfile() {
      // 添加
      this.dialog = {
        show: true,
        title: "添加二手车信息",
        option: "add",
      };
      const today = new Date().toISOString().split("T")[0]; // 获取当前日期并转换为 yyyy-mm-dd 格式
      this.form = {
        type: "",
        describe: "",
        price: "",
        age: "",
        date: today, // 设置为当前日期
      };
    },

    handleCurrentChange(page) {
      // 当前页
      let sortnum = this.paginations.page_size * (page - 1);
      let table = this.allTableData.filter((item, index) => {
        return index >= sortnum;
      });
      // 设置默认分页数据
      this.tableData = table.filter((item, index) => {
        return index < this.paginations.page_size;
      });
    },
    handleSizeChange(page_size) {
      // 切换size
      this.paginations.page_index = 1;
      this.paginations.page_size = page_size;
      this.tableData = this.allTableData.filter((item, index) => {
        return index < page_size;
      });
    },
    setPaginations() {
      // 总页数
      this.paginations.total = this.allTableData.length;
      this.paginations.page_index = 1;
      this.paginations.page_size = 5;
      // 设置默认分页数据
      this.tableData = this.allTableData.filter((item, index) => {
        return index < this.paginations.page_size;
      });
    },
    onScreeoutMoney() {
      // 筛选
      if (!this.search_data.maxPrice) {
        this.$message({
          type: "warning",
          message: "请输入最大价格",
        });
        return;
      }
      const maxPrice = this.search_data.maxPrice;
      this.allTableData = this.filterTableData.filter((item) => {
        return item.price <= maxPrice;
      });
      // 分页数据
      this.setPaginations();
    },
  },
};
</script>

<style scoped>
.fillcontain {
  width: 100%;
  height: 100%;
  padding: 16px;
  box-sizing: border-box;
}
.btnRight {
  float: right;
}
.pagination {
  text-align: right;
  margin-top: 10px;
}
</style>
