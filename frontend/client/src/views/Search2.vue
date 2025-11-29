<template>
    <div class="search">
        <div class="container">
            <div class="header"></div><!--控制导航栏和上半部分卡片的距离-->
            <!--导航栏-->
            <NavigationMenu
      :activeIndex="activeIndex"
      :backgroundColor="backgroundColor"
      :textColor="textColor"
      :activeTextColor="activeTextColor"
      />
        </div>
        <div style="height: 650px; display: flex" class="cab">
	    <el-scrollbar style="height:100%">

        <!--页面主体-->
        <div>
            <!--导航栏与页面-->
            <div class="header"></div><!--控制导航栏和上半部分卡片的距离-->
            
            <!-- 上半部分：大矩形卡片 -->
            <el-card class="top-card" :style="{ height: '18.5rem'}">
              
              <!-- 所在地选择 -->
              <el-cascader
              class="location-input"
                v-model="selectedCities"
                :options="options"
                size="mini"
                @change="handleCityChange"
                placeholder="请选择省份和城市"
                clearable
              ></el-cascader>

              <!-- 品牌选择 -->
              <el-row>
                <div class="brand-container0">
                  <label class="bold-text">品牌</label>
                  <ul class="brand-list">
                    <li class="item" :class="{ 'hasChecked': selectedBrand === '' }" @click="selectBrand('')">不限</li>
                    <li class="item" :class="{ 'hasChecked': selectedBrand === '大众' }" @click="selectBrand('大众')">大众</li>
                    <li class="item" :class="{ 'hasChecked': selectedBrand === '本田' }" @click="selectBrand('本田')">本田</li>
                    <li class="item" :class="{ 'hasChecked': selectedBrand === '奔驰' }" @click="selectBrand('奔驰')">奔驰</li>
                    <li class="item" :class="{ 'hasChecked': selectedBrand === '宝马' }" @click="selectBrand('宝马')">宝马</li>
                    <li class="item" :class="{ 'hasChecked': selectedBrand === '丰田' }" @click="selectBrand('丰田')">丰田</li>
                    <li class="item" :class="{ 'hasChecked': selectedBrand === '奥迪' }" @click="selectBrand('奥迪')">奥迪</li>
                    <li class="item" :class="{ 'hasChecked': selectedBrand === '别克' }" @click="selectBrand('别克')">别克</li>
                    <li class="item" :class="{ 'hasChecked': selectedBrand === '福特' }" @click="selectBrand('福特')">福特</li>
                    <li class="item" :class="{ 'hasChecked': selectedBrand === '吉利' }" @click="selectBrand('吉利')">吉利</li>
                    <li class="item" :class="{ 'hasChecked': selectedBrand === '哈弗' }" @click="selectBrand('哈弗')">哈弗</li>
                    <li class="item" :class="{ 'hasChecked': selectedBrand === '日系' }" @click="selectBrand('日系')">日系</li>
                    <li class="item" :class="{ 'hasChecked': selectedBrand === '比亚迪' }" @click="selectBrand('比亚迪')">比亚迪</li>
                    <li class="item" :class="{ 'hasChecked': selectedBrand === '长安' }" @click="selectBrand('长安')">长安</li>
                    <li class="item" :class="{ 'hasChecked': selectedBrand === '马自达' }" @click="selectBrand('马自达')">马自达</li>
                    <li class="item" :class="{ 'hasChecked': selectedBrand === '红星汽车' }" @click="selectBrand('红星汽车')">红星汽车</li>
                    <li class="item" :class="{ 'hasChecked': selectedBrand === '红旗' }" @click="selectBrand('红旗')">红旗</li>
                    <li class="item" :class="{ 'hasChecked': selectedBrand === 'Jeep' }" @click="selectBrand('Jeep')">Jeep</li>
                    <li class="item" :class="{ 'hasChecked': selectedBrand === '捷豹' }" @click="selectBrand('捷豹')">捷豹</li>
                    <li class="item" :class="{ 'hasChecked': selectedBrand === 'MINI' }" @click="selectBrand('MINI')">MINI</li>

                    <!-- 其他品牌选项... -->
                  </ul>
                  <el-dropdown trigger="click">
                  <li class="item brand-more" slot="reference" @click="showMoreBrands = !showMoreBrands">
                    <span class="more-txt"></span> 更多
                    <i class="el-icon-arrow-down el-icon--right"></i>
                  </li>
                  <el-dropdown-menu slot="dropdown">
                    <!-- 更多下拉菜单选项... -->
                  </el-dropdown-menu>
                </el-dropdown>
                </div>
              </el-row>

              <!-- 车系选择 -->
              <el-row>
                <div class="brand-container1">
                  <label class="bold-text">车系</label>
                  <ul class="brand-list">
                    <li class="item" :class="{ 'hasChecked': selectedSeries === '' }" @click="selectSeries('')">不限</li>
                    <li class="item" v-for="series in seriesList.slice(0, 15)" :key="series" :class="{ 'hasChecked': selectedSeries === series }" @click="selectSeries(series)">{{ series }}</li>
                    <el-dropdown>
                      <li class="item hasChecked" slot="reference" @click="showMoreSeries = !showMoreSeries">更多
                        <i class="el-icon-arrow-down el-icon--right"></i>
                      </li>
                      <el-dropdown-menu slot="dropdown">
                        <el-dropdown-item v-for="brand in seriesList.slice(15)" :key="brand" @click="selectBrand(brand)">{{ brand }}</el-dropdown-item>
                      </el-dropdown-menu>
                    </el-dropdown>
                  </ul>
                </div>
              </el-row>

                <!-- 价格选择 -->
                <el-row>
                  <div class="brand-container2">
                    <label class="bold-text">价格</label>
                    <ul class="brand-list">
                      <li class="item" :class="{ hasChecked: selectedPrice === '不限' }">
                        <span @click="selectPrice('不限')">不限</span>
                      </li>
                      <li class="item" :class="{ hasChecked: selectedPrice === '3万以下' }">
                        <span @click="selectPrice('3万以下')">3万以下</span>
                      </li>
                      <li class="item" :class="{ hasChecked: selectedPrice === '3-5万' }">
                        <span @click="selectPrice('3-5万')">3-5万</span>
                      </li>
                      <li class="item" :class="{ hasChecked: selectedPrice === '5-8万' }">
                        <span @click="selectPrice('5-8万')">5-8万</span>
                      </li>
                      <li class="item" :class="{ hasChecked: selectedPrice === '8-10万' }">
                        <span @click="selectPrice('8-10万')">8-10万</span>
                      </li>
                      <li class="item" :class="{ hasChecked: selectedPrice === '10-15万' }">
                        <span @click="selectPrice('10-15万')">10-15万</span>
                      </li>
                      <li class="item" :class="{ hasChecked: selectedPrice === '15-20万' }">
                        <span @click="selectPrice('15-20万')">15-20万</span>
                      </li>
                      <li class="item" :class="{ hasChecked: selectedPrice === '20-30万' }">
                        <span @click="selectPrice('20-30万')">20-30万</span>
                      </li>
                      <li class="item" :class="{ hasChecked: selectedPrice === '30-50万' }">
                        <span @click="selectPrice('30-50万')">30-50万</span>
                      </li>
                      <li class="item" :class="{ hasChecked: selectedPrice === '50-100万' }">
                        <span @click="selectPrice('50-100万')">50-100万</span>
                      </li>
                      <li class="item" :class="{ hasChecked: selectedPrice === '100万以上' }">
                        <span @click="selectPrice('100万以上')">100万以上</span>
                      </li>
                    </ul>
                    <div class="input-row">
                    <el-form :inline="true" ref="search_data" :model="search_data">
                      <el-form-item label="">
                        <el-input v-model.number="search_data.minPrice" size="mini" placeholder="最小" class="custom-input"></el-input>
                        <span> - </span>
                        <el-input v-model.number="search_data.maxPrice" size="mini" placeholder="最大" class="custom-input"></el-input>
                      </el-form-item>
                      <el-form-item>
                        <el-button type="primary" icon="pricesearch" @click="onScreeoutMoney()" class="buttonPrice">筛选</el-button>
                      </el-form-item>
                    </el-form>
                  </div>
                  </div>
                </el-row>

            

                <!-- 其他选择 -->
                <el-row>
                    <div class="brand-container2">
                        <lable class="bold-text">其他</lable>
                        <!-- 车型下拉菜单 -->
                        <el-dropdown trigger="click" @command="handleBrandSelect">
                            <span class="brand-more">
                            {{ brandText }}<i class="el-icon-arrow-down el-icon--right"></i>
                            </span>
                            <el-dropdown-menu slot="dropdown">
                            <el-dropdown-item command="轿车">轿车</el-dropdown-item>
                            <el-dropdown-item command="跑车">跑车</el-dropdown-item>
                            <el-dropdown-item command="皮卡车">皮卡车</el-dropdown-item>
                            <el-dropdown-item command="SUV">SUV</el-dropdown-item>
                            <el-dropdown-item command="面包车">面包车</el-dropdown-item>
                            <el-dropdown-item command="客车">客车</el-dropdown-item>
                            <el-dropdown-item command="旅游车">旅行车</el-dropdown-item>
                            <el-dropdown-item command="MPV">MPV</el-dropdown-item>
                            <el-dropdown-item command="货车">货车</el-dropdown-item>
                            </el-dropdown-menu>
                        </el-dropdown>

                        <!-- 车龄下拉菜单 -->
                        <el-dropdown trigger="click" @command="handleAgeSelect">
                            <span class="brand-more">
                            {{ ageText }}<i class="el-icon-arrow-down el-icon--right"></i>
                            </span>
                            <el-dropdown-menu slot="dropdown">
                            <el-dropdown-item command="一年">一年</el-dropdown-item>
                            <el-dropdown-item command="两年">两年</el-dropdown-item>
                            <el-dropdown-item command="三年">三年</el-dropdown-item>
                            <el-dropdown-item command="四年">四年</el-dropdown-item>
                            <el-dropdown-item command="五年及以上">五年及以上</el-dropdown-item>
                            </el-dropdown-menu>
                        </el-dropdown>
                            
                        <!-- 变速箱下拉菜单 -->
                        <el-dropdown trigger="click" @command="handleTransmissionSelect">
                            <span class="brand-more">
                            {{ transmissionText }}<i class="el-icon-arrow-down el-icon--right"></i>
                            </span>
                            <el-dropdown-menu slot="dropdown">
                            <el-dropdown-item command="自动">自动</el-dropdown-item>
                            <el-dropdown-item command="手动">手动</el-dropdown-item>
                            </el-dropdown-menu>
                        </el-dropdown>

                        <!-- 里程下拉菜单 -->
                        <el-dropdown trigger="click" @command="handleMileageSelect">
                            <span class="brand-more">
                            {{ MileageText }}<i class="el-icon-arrow-down el-icon--right"></i>
                            </span>
                            <el-dropdown-menu slot="dropdown">
                            <el-dropdown-item command="1万公里以下">1万公里以下</el-dropdown-item>
                            <el-dropdown-item command="1-3万公里">1-3万公里</el-dropdown-item>
                            <el-dropdown-item command="3-5万公里">3-5万公里</el-dropdown-item>
                            <el-dropdown-item command="5-8万公里">5-8万公里</el-dropdown-item>
                            <el-dropdown-item command="8-10万公里">8-10万公里</el-dropdown-item>
                            <el-dropdown-item command="10万公里以上">10万公里以上</el-dropdown-item>
                            </el-dropdown-menu>
                        </el-dropdown>

                        <!-- 排量下拉菜单 -->
                        <el-dropdown trigger="click" @command="handleEmissionsSelect">
                            <span class="brand-more">
                            {{ emissionsText }}<i class="el-icon-arrow-down el-icon--right"></i>
                            </span>
                            <el-dropdown-menu slot="dropdown">
                            <el-dropdown-item command="1.0L及以下">1.0L及以下</el-dropdown-item>
                            <el-dropdown-item command="1.1L-1.6L">1.1L-1.6L</el-dropdown-item>
                            <el-dropdown-item command="1.7L-2.0L">1.7L-2.0L</el-dropdown-item>
                            <el-dropdown-item command="2.1L-2.5L">2.1L-2.5L</el-dropdown-item>
                            <el-dropdown-item command="2.6L-3.0L">2.6L-3.0L</el-dropdown-item>
                            <el-dropdown-item command="3.1L-4.0L">3.1L-4.0L</el-dropdown-item>
                            <el-dropdown-item command="4.0L以上">4.0L以上</el-dropdown-item>
                            </el-dropdown-menu>
                        </el-dropdown>

                        <!-- 排放标准下拉菜单 -->
                        <el-dropdown trigger="click" @command="handleEmissionsstandardsSelect">
                            <span class="brand-more">
                            {{ emissionsstandardsText }}<i class="el-icon-arrow-down el-icon--right"></i>
                            </span>
                            <el-dropdown-menu slot="dropdown">
                              <el-dropdown-item command="国V(国VI)">国V/国VI</el-dropdown-item>
                              <el-dropdown-item command="欧III">欧III</el-dropdown-item>
                              <el-dropdown-item command="欧V+OBD">欧V+OBD</el-dropdown-item>
                              <el-dropdown-item command="国IV/国V">国IV/国V</el-dropdown-item>
                              <el-dropdown-item command="国IV+OBD">国IV+OBD</el-dropdown-item>
                              <el-dropdown-item command="国III+OBD">国III+OBD</el-dropdown-item>
                              <el-dropdown-item command="国III">国III</el-dropdown-item>
                              <el-dropdown-item command="国II">国II</el-dropdown-item>
                              <el-dropdown-item command="欧II">欧II</el-dropdown-item>
                              <el-dropdown-item command="国IV">国IV</el-dropdown-item>
                              <el-dropdown-item command="国IV(国V)+OBD">国IV/国V+OBD</el-dropdown-item>
                              <el-dropdown-item command="欧IV">欧IV</el-dropdown-item>
                              <el-dropdown-item command="欧IV+OBD">欧IV+OBD</el-dropdown-item>
                              <el-dropdown-item command="欧VI">欧VI</el-dropdown-item>
                              <el-dropdown-item command="国IV(国V)">国IV/国V</el-dropdown-item>
                              <el-dropdown-item command="欧V">欧V</el-dropdown-item>
                              <el-dropdown-item command="国V+OBD">国V+OBD</el-dropdown-item>
                              <el-dropdown-item command="国VI">国VI</el-dropdown-item>
                              <el-dropdown-item command="国V">国V</el-dropdown-item>
                            </el-dropdown-menu>
                        </el-dropdown>

                        <!-- 颜色下拉菜单 -->
                        <el-dropdown trigger="click" @command="handleColorSelect">
                            <span class="brand-more">
                            {{ colorText }}<i class="el-icon-arrow-down el-icon--right"></i>
                            </span>
                            <el-dropdown-menu slot="dropdown">
                            <el-dropdown-item command="黑色">黑色</el-dropdown-item>
                            <el-dropdown-item command="白色">白色</el-dropdown-item>
                            <el-dropdown-item command="银/灰色">银/灰色</el-dropdown-item>
                            <el-dropdown-item command="红/紫色">红/紫色</el-dropdown-item>
                            <el-dropdown-item command="黄/橙色">黄/橙色</el-dropdown-item>
                            <el-dropdown-item command="蓝色">蓝色</el-dropdown-item>
                            <el-dropdown-item command="绿色">绿色</el-dropdown-item>
                            <el-dropdown-item command="粉色">粉色</el-dropdown-item>
                            <el-dropdown-item command="香槟/棕色">香槟/棕色</el-dropdown-item>
                            <el-dropdown-item command="其他">其他</el-dropdown-item>
                            </el-dropdown-menu>
                        </el-dropdown>

                        <!-- 国别下拉菜单 -->
                        <el-dropdown trigger="click" @command="handleCountrySelect">
                            <span class="brand-more">
                            {{ countryText }}<i class="el-icon-arrow-down el-icon--right"></i>
                            </span>
                            <el-dropdown-menu slot="dropdown">
                            <el-dropdown-item command="国产">国产</el-dropdown-item>
                            <el-dropdown-item command="德系">德系</el-dropdown-item>
                            <el-dropdown-item command="日系">日系</el-dropdown-item>
                            <el-dropdown-item command="美系">美系</el-dropdown-item>
                            <el-dropdown-item command="法系">法系</el-dropdown-item>
                            <el-dropdown-item command="其他">其他</el-dropdown-item>
                            </el-dropdown-menu>
                        </el-dropdown>

                        <!-- 驱动下拉菜单 -->
                        <el-dropdown trigger="click" @command="handleDriveSelect">
                            <span class="brand-more">
                            {{ driveText }}<i class="el-icon-arrow-down el-icon--right"></i>
                            </span>
                            <el-dropdown-menu slot="dropdown">
                            <el-dropdown-item command="前驱">前驱</el-dropdown-item>
                            <el-dropdown-item command="后驱">后驱</el-dropdown-item>
                            <el-dropdown-item command="四驱">四驱</el-dropdown-item>
                            </el-dropdown-menu>
                        </el-dropdown>

                        <!-- 座位数下拉菜单 -->
                        <el-dropdown trigger="click" @command="handleSeatSelect">
                            <span class="brand-more">
                            {{ seatText }}<i class="el-icon-arrow-down el-icon--right"></i>
                            </span>
                            <el-dropdown-menu slot="dropdown">
                            <el-dropdown-item command="2座">2座</el-dropdown-item>
                            <el-dropdown-item command="4/5座">4/5座</el-dropdown-item>
                            <el-dropdown-item command="6座">6座</el-dropdown-item>
                            <el-dropdown-item command="7座及以上">7座及以上</el-dropdown-item>
                            </el-dropdown-menu>
                        </el-dropdown>
                        <!-- 燃料类型下拉菜单 -->
                        <el-dropdown trigger="click" @command="handleFuelSelect">
                            <span class="brand-more">
                            {{ fuelText }}<i class="el-icon-arrow-down el-icon--right"></i>
                            </span>
                            <el-dropdown-menu slot="dropdown">
                            <el-dropdown-item command="插电混动">插电混动</el-dropdown-item>
                            <el-dropdown-item command="增程式">增程式</el-dropdown-item>
                            <el-dropdown-item command="汽油">汽油</el-dropdown-item>
                            <el-dropdown-item command="柴油">柴油</el-dropdown-item>
                            <el-dropdown-item command="电动">电动</el-dropdown-item>
                            <el-dropdown-item command="油电混合">油电混合</el-dropdown-item>
                            <el-dropdown-item command="油改气">油改气</el-dropdown-item>
                            </el-dropdown-menu>
                        </el-dropdown>
                        
                    </div>
                </el-row>


                <!-- 筛选排序 -->
                <el-row>
                    <div class="brand-container">
                        <ul class="brand-list">
                          <li class="item" :class="{ hasChecked: selectedBrand === '综合排序' }"><span @click="selectBrand('综合排序')">综合排序</span></li>
                          <li class="item" :class="{ hasChecked: selectedfun === '最新上架' }"><span @click="selectfun('最新上架')">最新上架</span></li>
                          <li class="item" :class="{ hasChecked: selectedfun === '综合排序' }"><span @click="selectfun('价格最低')">价格最高</span></li>
                          <li class="item" :class="{ hasChecked: selectedfun === '综合排序' }"><span @click="selectfun('车龄最短')">车龄最短</span></li>
                          <li class="item" :class="{ hasChecked: selectedfun === '综合排序' }"><span @click="selectfun('里程最少')">里程最少</span></li>                  
                        </ul>            
                        <button class="bold-text">清空筛选</button>
                         <!-- 搜索框 -->
                         <el-input v-model="lowerPrice" size="mini" placeholder="" class="custom-input2"></el-input>
                        <el-button type="primary" icon="el-icon-search" class="button1">搜索</el-button>
                    </div>
                </el-row>


                <!-- 已选择 -->
                <el-row>
                    <div class="brand-container">
                            <lable class="bold-text-yixuanze">已选择:</lable>
                    </div>
                
                </el-row>


         
            </el-card>
            <div class="header"></div><!--控制导航栏和上半部分卡片的距离-->

            <!-- 下半部分 -->
            <el-row>          
                    <div class="card-container">
                        <el-card v-for="item in tableData" :key="item.id" class="card-item">
                            <img class="card-img" :src="item.img_url[0]" alt="image" >
                            <div class="card-content">
								<router-link :to="{ name: 'cardetails', params: { id: item._id } }" >
								{{ item.title }}
								</router-link>
                                <div class="car-info">
                                <div class="extra-info">
                                    <p>{{ item.license_time }}</p>  <!-- 上牌时间 -->
                                    <span class="separator2">/</span>
                                    <p>{{ item.mileage }}</p>   <!-- 里程 -->
                                    <span class="separator2">/</span>
                                    <p>{{ item.location }}</p>   <!-- 所在地 -->
                                </div>
                                </div>
                                <div class="price-container">
                                  <p class="price">￥{{ item.price }}万</p></div>
                                  <div class="button-container">
                                    <el-button type="text" class="buttondetails" @click="onEditProfile(item)">
                                    查看详情
                                    </el-button>
                                  </div>
                                
                            </div>
                        </el-card>
                    </div>
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
            </el-row>
        </div>  
        </el-scrollbar>
        </div>
    </div>  
</template>



<script>

export default {
    data() {
    return {
      tableData: [],
      allTableData: [],
      selectedfun:'',
      selectedBrand: '', // 记录用户选择的品牌
      selectedSeries: '', // 记录用户选择的车系
      seriesList: [], // 当前选中品牌对应的车系列表
      showMoreBrands: false,
      showMoreSeries: false,
      filterTableData:[],
      selectedPrice: "不限",
      lowerPrice: "",
      higherPrice: "",
      isValid: true,
      areatext:'全国',
      brandText: '车型',
      ageText: '车龄',
      transmissionText: '变速箱',
      MileageText:'里程',
      emissionsText:'排量',
      emissionsstandardsText:'排放标准',
      colorText:'颜色',
      countryText:'国别',
      driveText:'驱动',
      seatText:'座位数',
      fuelText:'燃料类型',
      form: {
        img_url:"",
        title: "",
        license_time: "",
        mileage: "",
        price: "",
        location: "",
        id: "",
      },
      paginations: {
        page_index: 1,
        total: 0,
        page_size: 20,
        page_sizes: [20,28, 36, 48,80],
        layout: "total, sizes, prev, pager, next, jumper",
      },
      search_data: {
        minPrice: null,
        maxPrice: null,
      },
      selectedCities: [], // 用于存储选中的省份和城市的值
      filterOptions: {location:''},
      options: [
        {
          value: 'anhui',
          label: '安徽',
          children: [
            { value: 'hefei', label: '合肥' },
            { value: 'wuhu', label: '芜湖' },
            { value: 'bangbu', label: '蚌埠' },
            { value: 'huainan', label: '淮南' },
            { value: 'maanshan', label: '马鞍山' },
            { value: 'huaibei', label: '淮北' },
            { value: 'tongling', label: '铜陵' },
            { value: 'anqing', label: '安庆' },
            { value: 'huangshan', label: '黄山' },
            { value: 'chuzhou', label: '滁州' },
            { value: 'fuyang', label: '阜阳' },
            { value: 'suzhou', label: '宿州' },
            { value: 'liuan', label: '六安' },
            { value: 'bozhou', label: '亳州' },
            { value: 'chizhou', label: '池州' },
            { value: 'xuancheng', label: '宣城' }
          ]
        },
        {
          value: 'beijing',
          label: '北京',
          children: [
            { value: 'beijing', label: '北京' }
          ]
        },
        {
          value: 'chongqing',
          label: '重庆',
          children: [
            { value: 'chongqing', label: '重庆' }
          ]
        },
        {
          value: 'fujian',
          label: '福建',
          children: [
            { value: 'fuzhou', label: '福州' },
            { value: 'xiamen', label: '厦门' },
            { value: 'putian', label: '莆田' },
            { value: 'sanming', label: '三明' },
            { value: 'quanzhou', label: '泉州' },
            { value: 'zhangzhou', label: '漳州' },
            { value: 'nanping', label: '南平' },
            { value: 'longyan', label: '龙岩' },
            { value: 'ningde', label: '宁德' }
          ]
        },
        {
          value: 'guangdong',
          label: '广东',
          children: [
            { value: 'guangzhou', label: '广州' },
            { value: 'shaoguan', label: '韶关' },
            { value: 'shenzhen', label: '深圳' },
            { value: 'zhuhai', label: '珠海' },
            { value: 'shantou', label: '汕头' },
            { value: 'foshan', label: '佛山' },
            { value: 'jiangmen', label: '江门' },
            { value: 'zhanjiang', label: '湛江' },
            { value: 'maoming', label: '茂名' },
            { value: 'zhaoqing', label: '肇庆' },
            { value: 'huizhou', label: '惠州' },
            { value: 'meizhou', label: '梅州' },
            { value: 'shanwei', label: '汕尾' },
            { value: 'heyuan', label: '河源' },
            { value: 'yangjiang', label: '阳江' },
            { value: 'qingyuan', label: '清远' },
            { value: 'dongguan', label: '东莞' },
            { value: 'zhongshan', label: '中山' },
            { value: 'chaozhou', label: '潮州' },
            { value: 'jieyang', label: '揭阳' },
            { value: 'yunfu', label: '云浮' }
          ]
        },
        {
          value: 'guangxi',
          label: '广西',
          children: [
            { value: 'nanning', label: '南宁' },
            { value: 'liuzhou', label: '柳州' },
            { value: 'guilin', label: '桂林' },
            { value: 'wuzhou', label: '梧州' },
            { value: 'beihai', label: '北海' },
            { value: 'fangchenggang', label: '防城港' },
            { value: 'qinzhou', label: '钦州' },
            { value: 'guigang', label: '贵港' },
            { value: 'yu_lin', label: '玉林' },
            { value: 'baise', label: '百色' },
            { value: 'hezhou', label: '贺州' },
            { value: 'hechi', label: '河池' },
            { value: 'laibin', label: '来宾' },
            { value: 'chongzuo', label: '崇左' }
          ]
        },
        {
          value: 'guizhou',
          label: '贵州',
          children: [
            { value: 'guiyang', label: '贵阳' },
            { value: 'liupanshui', label: '六盘水' },
            { value: 'zunyi', label: '遵义' },
            { value: 'anshun', label: '安顺' },
            { value: 'bijie', label: '毕节' },
            { value: 'tongren', label: '铜仁' },
            { value: 'qianxinan', label: '黔西南' },
            { value: 'qiandongnan', label: '黔东南' },
            { value: 'qiannan', label: '黔南' }
          ]
        },
        {
          value: 'gansu',
          label: '甘肃',
          children: [
            { value: 'lanzhou', label: '兰州' },
            { value: 'jiayuguan', label: '嘉峪关' },
            { value: 'jinchang', label: '金昌' },
            { value: 'baiyin', label: '白银' },
            { value: 'tianshui', label: '天水' },
            { value: 'wuwei', label: '武威' },
            { value: 'zhangye', label: '张掖' },
            { value: 'pingliang', label: '平凉' },
            { value: 'jiuquan', label: '酒泉' },
            { value: 'qingyang', label: '庆阳' },
            { value: 'dingxi', label: '定西' },
            { value: 'longnan', label: '陇南' },
            { value: 'linxia', label: '临夏' },
            { value: 'gannan', label: '甘南' }
          ]
        },
        {
          value: 'hainan', label: '海南',
          children: [
            { value: 'haikou', label: '海口' },
            { value: 'sanya', label: '三亚' },
            { value: 'sansha', label: '三沙' },
            { value: 'danzhou', label: '儋州' },
            { value: 'wuzhishan', label: '五指山' },
            { value: 'qionghai', label: '琼海' },
            { value: 'wenchang', label: '文昌' },
            { value: 'wanning', label: '万宁' },
            { value: 'dongfang', label: '东方' },
            { value: 'dingan', label: '定安' },
            { value: 'tunchang', label: '屯昌' },
            { value: 'chengmai', label: '澄迈' },
            { value: 'lingao', label: '临高' },
            { value: 'baisha', label: '白沙' },
            { value: 'changjiang', label: '昌江' },
            { value: 'ledong', label: '乐东' },
            { value: 'lingshui', label: '陵水' },
            { value: 'baoting', label: '保亭' },
            { value: 'qiongzhong', label: '琼中' }
          ]
        },
        {
          value: 'henan', label: '河南',
          children: [
            { value: 'zhengzhou', label: '郑州' },
            { value: 'kaifeng', label: '开封' },
            { value: 'luoyang', label: '洛阳' },
            { value: 'pingdingshan', label: '平顶山' },
            { value: 'anyang', label: '安阳' },
            { value: 'hebi', label: '鹤壁' },
            { value: 'xinxiang', label: '新乡' },
            { value: 'jiaozuo', label: '焦作' },
            { value: 'puyang', label: '濮阳' },
            { value: 'xuchang', label: '许昌' },
            { value: 'luohe', label: '漯河' },
            { value: 'sanmenxia', label: '三门峡' },
            { value: 'nanyang', label: '南阳' },
            { value: 'shangqiu', label: '商丘' },
            { value: 'xinyang', label: '信阳' },
            { value: 'zhoukou', label: '周口' },
            { value: 'zhumadian', label: '驻马店' },
            { value: 'jiyuan', label: '济源' }
          ]
        },
        {
          value: 'hubei', label: '湖北',
          children: [
            { value: 'wuhan', label: '武汉' },
            { value: 'huangshi', label: '黄石' },
            { value: 'shiyan', label: '十堰' },
            { value: 'yichang', label: '宜昌' },
            { value: 'xiangyang', label: '襄阳' },
            { value: 'ezhou', label: '鄂州' },
            { value: 'jingmen', label: '荆门' },
            { value: 'xiaogan', label: '孝感' },
            { value: 'jingzhou', label: '荆州' },
            { value: 'huanggang', label: '黄冈' },
            { value: 'xianning', label: '咸宁' },
            { value: 'suizhou', label: '随州' },
            { value: 'enshi', label: '恩施' },
            { value: 'xiantao', label: '仙桃' },
            { value: 'qianjiang', label: '潜江' },
            { value: 'tianmen', label: '天门' },
            { value: 'shennongjia', label: '神农架' }
          ]
        },
        {
          value: 'hunan', label: '湖南',
          children: [
            { value: 'changsha', label: '长沙' },
            { value: 'zhuzhou', label: '株洲' },
            { value: 'xiangtan', label: '湘潭' },
            { value: 'hengyang', label: '衡阳' },
            { value: 'shaoyang', label: '邵阳' },
            { value: 'yueyang', label: '岳阳' },
            { value: 'changde', label: '常德' },
            { value: 'zhangjiajie', label: '张家界' },
            { value: 'yiyang', label: '益阳' },
            { value: 'chenzhou', label: '郴州' },
            { value: 'yongzhou', label: '永州' },
            { value: 'huaihua', label: '怀化' },
            { value: 'loudi', label: '娄底' },
            { value: 'xiangxi', label: '湘西' }
          ]
        },
        {
          value: 'hebei', label: '河北',
          children: [
            {value: 'shijiazhuang', label: '石家庄'},
            {value: 'tangshan', label: '唐山'},
            {value: 'qinhuangdao', label: '秦皇岛'},
            {value: 'handan', label: '邯郸'},
            {value: 'xingtai', label: '邢台'},
            {value: 'baoding', label: '保定'},
            {value: 'zhangjiakou', label: '张家口'},
            {value: 'chengde', label: '承德'},
            {value: 'cangzhou', label: '沧州'},
            {value: 'langfang', label: '廊坊'},
            {value: 'hengshui', label: '衡水'}
          ]
        },
        {
          value: 'heilongjiang', label: '黑龙江',
          children: [
            {value: 'haerbin', label: '哈尔滨'},
            {value: 'qiqihaer', label: '齐齐哈尔'},
            {value: 'jixi', label: '鸡西'},
            {value: 'hegang', label: '鹤岗'},
            {value: 'shuangyashan', label: '双鸭山'},
            {value: 'daqing', label: '大庆'},
            {value: 'yichun', label: '伊春'},
            {value: 'jiamusi', label: '佳木斯'},
            {value: 'qitaihe', label: '七台河'},
            {value: 'mudanjiang', label: '牡丹江'},
            {value: 'heihe', label: '黑河'},
            {value: 'suihua', label: '绥化'},
            {value: 'daxinganling', label: '大兴安岭'}
          ]
        },
        {
          value: 'jiangsu', label: '江苏',
          children: [
            {value: 'nanjing', label: '南京'},
            {value: 'wuxi', label: '无锡'},
            {value: 'xuzhou', label: '徐州'},
            {value: 'changzhou', label: '常州'},
            {value: 'suzhou', label: '苏州'},
            {value: 'nantong', label: '南通'},
            {value: 'lianyungang', label: '连云港'},
            {value: 'huaian', label: '淮安'},
            {value: 'yancheng', label: '盐城'},
            {value: 'yangzhou', label: '扬州'},
            {value: 'zhenjiang', label: '镇江'},
            {value: 'tai_zhou', label: '泰州'},
            {value: 'suqian', label: '宿迁'}
          ]
        },
        {
          value: 'jiangxi', label: '江西',
          children: [
            {value: 'nanchang', label: '南昌'},
            {value: 'jingdezhen', label: '景德镇'},
            {value: 'ping_xiang', label: '萍乡'},
            {value: 'jiujiang', label: '九江'},
            {value: 'xinyu', label: '新余'},
            {value: 'yingtan', label: '鹰潭'},
            {value: 'ganzhou', label: '赣州'},
            {value: 'jian', label: '吉安'},
            {value: 'yi_chun', label: '宜春'},
            {value: 'fu_zhou', label: '抚州'},
            {value: 'shangrao', label: '上饶'}
          ]
        },
        {
          value: 'jilin', label: '吉林',
          children: [
            {value: 'changchun', label: '长春'},
            {value: 'jilinshi', label: '吉林'},
            {value: 'siping', label: '四平'},
            {value: 'liaoyuan', label: '辽源'},
            {value: 'tonghua', label: '通化'},
            {value: 'baishan', label: '白山'},
            {value: 'songyuan', label: '松原'},
            {value: 'baicheng', label: '白城'},
            {value: 'yanbian', label: '延边'}
          ]
        },
        {
          value: 'liaoning', label: '辽宁',
          children: [
            {value: 'shenyang', label: '沈阳'},
            {value: 'dalian', label: '大连'},
            {value: 'anshan', label: '鞍山'},
            {value: 'fushun', label: '抚顺'},
            {value: 'benxi', label: '本溪'},
            {value: 'dandong', label: '丹东'},
            {value: 'jinzhou', label: '锦州'},
            {value: 'yingkou', label: '营口'},
            {value: 'fuxin', label: '阜新'},
            {value: 'liaoyang', label: '辽阳'},
            {value: 'panjin', label: '盘锦'},
            {value: 'tieling', label: '铁岭'},
            {value: 'chaoyang', label: '朝阳'},
            {value: 'huludao', label: '葫芦岛'}
          ]
        },
        {
          value: 'neimenggu', label: '内蒙古',
          children: [
            {value: 'huhehaote', label: '呼和浩特'},
            {value: 'baotou', label: '包头'},
            {value: 'wuhai', label: '乌海'},
            {value: 'chifeng', label: '赤峰'},
            {value: 'tongliao', label: '通辽'},
            {value: 'eerduosi', label: '鄂尔多斯'},
            {value: 'hulunbeier', label: '呼伦贝尔'},
            {value: 'bayannaoer', label: '巴彦淖尔'},
            {value: 'wulanchabu', label: '乌兰察布'},
            {value: 'xinganmeng', label: '兴安盟'},
            {value: 'xilinguolemeng', label: '锡林郭勒盟'},
            {value: 'alashanmeng', label: '阿拉善盟'}
          ]
        },
        {
          value: 'ningxia', label: '宁夏',
          children: [
            {value: 'yinchuan', label: '银川'},
            {value: 'shizuishan', label: '石嘴山'},
            {value: 'wuzhong', label: '吴忠'},
            {value: 'guyuan', label: '固原'},
            {value: 'zhongwei', label: '中卫'}
          ]
        },
        {
          value: 'qinghai', label: '青海',
          children: [
            {value: 'xining', label: '西宁'},
            {value: 'haidong', label: '海东'},
            {value: 'haibei', label: '海北'},
            {value: 'huangnan', label: '黄南'},
            {value: 'hai_nan', label: '海南'},
            {value: 'guoluo', label: '果洛'},
            {value: 'yushu', label: '玉树'},
            {value: 'haixi', label: '海西'}
          ]
        },
        {
          value: 'shanxi',
          label: '陕西',
          children: [
            { value: 'xian', label: '西安' },
            { value: 'tongchuan', label: '铜川' },
            { value: 'baoji', label: '宝鸡' },
            { value: 'xianyang', label: '咸阳' },
            { value: 'weinan', label: '渭南' },
            { value: 'yanan', label: '延安' },
            { value: 'hanzhong', label: '汉中' },
            { value: 'yulin', label: '榆林' },
            { value: 'ankang', label: '安康' },
            { value: 'shangluo', label: '商洛' },
            { value: 'xixianxinqu', label: '西咸新区' }
          ]
        },
        {
          value: 'sichuan',
          label: '四川',
          children: [
            { value: 'chengdu', label: '成都' },
            { value: 'zigong', label: '自贡' },
            { value: 'panzhihua', label: '攀枝花' },
            { value: 'luzhou', label: '泸州' },
            { value: 'deyang', label: '德阳' },
            { value: 'mianyang', label: '绵阳' },
            { value: 'guangyuan', label: '广元' },
            { value: 'suining', label: '遂宁' },
            { value: 'neijiang', label: '内江' },
            { value: 'leshan', label: '乐山' },
            { value: 'nanchong', label: '南充' },
            { value: 'meishan', label: '眉山' },
            { value: 'yibin', label: '宜宾' },
            { value: 'guangan', label: '广安' },
            { value: 'dazhou', label: '达州' },
            { value: 'yaan', label: '雅安' },
            { value: 'bazhong', label: '巴中' },
            { value: 'ziyang', label: '资阳' },
            { value: 'aba', label: '阿坝' },
            { value: 'ganzi', label: '甘孜' },
            { value: 'liangshan', label: '凉山' }
          ]
        },
        {
          value: 'shanghai',
          label: '上海',
          children: [
            { value: 'shanghai', label: '上海' }
          ]
        },
        {
          value: 'shanxi',
          label: '山西',
          children: [
            { value: 'taiyuan', label: '太原' },
            { value: 'datong', label: '大同' },
            { value: 'yangquan', label: '阳泉' },
            { value: 'zhangzhi', label: '长治' },
            { value: 'jincheng', label: '晋城' },
            { value: 'shuozhou', label: '朔州' },
            { value: 'jinzhong', label: '晋中' },
            { value: 'yuncheng', label: '运城' },
            { value: 'xinzhou', label: '忻州' },
            { value: 'linfen', label: '临汾' },
            { value: 'lvliang', label: '吕梁' }
          ]
        },
        {
          value: 'shandong',
          label: '山东',
          children: [
            { value: 'jinan', label: '济南' },
            { value: 'qingdao', label: '青岛' },
            { value: 'zibo', label: '淄博' },
            { value: 'zaozhuang', label: '枣庄' },
            { value: 'dongying', label: '东营' },
            { value: 'yantai', label: '烟台' },
            { value: 'weifang', label: '潍坊' },
            { value: 'jining', label: '济宁' },
            { value: 'taian', label: '泰安' },
            { value: 'weihai', label: '威海' },
            { value: 'rizhao', label: '日照' },
            { value: 'laiwu', label: '莱芜' },
            { value: 'linyi', label: '临沂' },
            { value: 'dezhou', label: '德州' },
            { value: 'liaocheng', label: '聊城' },
            { value: 'binzhou', label: '滨州' },
            { value: 'heze', label: '菏泽' }
          ]
        },
        {
          value: 'tianjin',
          label: '天津',
          children: [
            { value: 'tianjin', label: '天津' }
          ]
        },
        {
          value: 'xinjiang',
          label: '新疆',
          children: [
            { value: 'wulumuqi', label: '乌鲁木齐' },
            { value: 'kelamayi', label: '克拉玛依' },
            { value: 'turpan', label: '吐鲁番' },
            { value: 'hami', label: '哈密' },
            { value: 'changji', label: '昌吉' },
            { value: 'boertala', label: '博尔塔拉' },
            { value: 'bayinguoleng', label: '巴音郭楞' },
            { value: 'akesu', label: '阿克苏' },
            { value: 'kezilesu', label: '克孜勒苏' },
            { value: 'kashen', label: '喀什' },
            { value: 'hetian', label: '和田' },
            { value: 'yili', label: '伊犁' },
            { value: 'tacheng', label: '塔城' },
            { value: 'aletai', label: '阿勒泰' },
            { value: 'shihezi', label: '石河子' },
            { value: 'aral', label: '阿拉尔' },
            { value: 'tumxuk', label: '图木舒克' },
            { value: 'wujiaqu', label: '五家渠' },
            { value: 'beitun', label: '北屯' },
            { value: 'tiemenguan', label: '铁门关' },
            { value: 'shuanghe', label: '双河' },
            { value: 'kokdala', label: '可克达拉' },
            { value: 'kunyu', label: '昆玉' }
          ]
        },
        {
          value: 'xizang',
          label: '西藏',
          children: [
            { value: 'lasa', label: '拉萨' },
            { value: 'rikaze', label: '日喀则' },
            { value: 'qamdo', label: '昌都' },
            { value: 'nyingchi', label: '林芝' },
            { value: 'shannan', label: '山南' },
            { value: 'naqu', label: '那曲' },
            { value: 'ali', label: '阿里' }
          ]
        },
        {
          value: 'yunnan',
          label: '云南',
          children: [
            { value: 'kunming', label: '昆明' },
            { value: 'qujing', label: '曲靖' },
            { value: 'yuxi', label: '玉溪' },
            { value: 'baoshan', label: '保山' },
            { value: 'zhaotong', label: '昭通' },
            { value: 'lijiang', label: '丽江' },
            { value: 'puer', label: '普洱' },
            { value: 'lincang', label: '临沧' },
            { value: 'chuxiong', label: '楚雄' },
            { value: 'honghe', label: '红河' },
            { value: 'wenshan', label: '文山' },
            { value: 'xishuangbanna', label: '西双版纳' },
            { value: 'dali', label: '大理' },
            { value: 'dehong', label: '德宏' },
            { value: 'nujiang', label: '怒江' },
            { value: 'diqing', label: '迪庆' }
          ]
        },
        {
          value: 'zhejiang',
          label: '浙江',
          children: [
            { value: 'hangzhou', label: '杭州' },
            { value: 'ningbo', label: '宁波' },
            { value: 'wenzhou', label: '温州' },
            { value: 'jiaxing', label: '嘉兴' },
            { value: 'huzhou', label: '湖州' },
            { value: 'shaoxing', label: '绍兴' },
            { value: 'jinhua', label: '金华' },
            { value: 'quzhou', label: '衢州' },
            { value: 'zhoushan', label: '舟山' },
            { value: 'taizhou', label: '台州' },
            { value: 'lishui', label: '丽水' },
            { value: 'zhoushanxinqu', label: '舟山群岛新区' }
          ]
        }
      ],
      };
    },

    created() {
      this.getProfile();
    },
    methods: {
      	selectSeries(series) {
      	// 处理车系的选择操作...
		},
		selectBrand(brand) {
		this.selectedBrand = brand;
		this,this.showMoreSeries = false;
		// 根据选择的品牌更新车系选项
		if (brand === '') {
			// 不限品牌，显示原始选项
			this.seriesList = ['奥迪A6L', '宝马5系', '宝马3系', '奔驰C级', '奔驰E级', '高尔夫', '迈腾', '速腾', '朗逸', '雅阁', '轩逸', '哈弗H6', '福克斯'];
		} else if (brand === '大众') {
			// 大众品牌对应的车系列表
			this.seriesList = ['速腾','高尔夫','大众POLO','朗逸','迈腾','宝来','帕萨特','凌渡','途观L','途观','大众CC','桑塔纳','探岳','甲壳虫','T-ROC探歌','捷达','途昂','高尔夫·嘉旅','ID.4 CROZZ','朗行','蔚领','途铠','途岳','途锐','ID.4 X','大众ID.3','','','','','','','','','','','','','','','','','','','','','','','','','','','']
		} else if (brand === '本田') {
			// 本田品牌对应的车系列表
			this.seriesList = ['雅阁', 'CR-V', '思域', '奥德赛', '艾力绅', 'Inspire', '里程', '飞度', '锋范', '凌派', '飞思', '竞瑞']
		} else if (brand === '奔驰') {
			this.seriesList = ['C级', 'E级', 'S级', 'GLC', 'GLE', 'GLA', 'GLB', 'GLS', 'A级', 'B级', 'CLA级', 'CLS级', 'AMG GT', 'SLC', 'SL级']
		} else if (brand === '宝马') {
			this.seriesList = ['3系', '5系', '7系', 'X1', 'X3', 'X5', 'X6', 'X7', 'i3', 'i8']
		} else if (brand === '丰田') {
			this.seriesList = ['卡罗拉', '雷凌', '汉兰达', '普拉多', '凯美瑞', '柯斯达', '锐志', '兰德酷路泽', 'RAV4荣放', '威驰', 'RAV4荣放EV', '考斯特', '凯美瑞新能源', '雅力士', '亚洲龙', 'rav4荣放黑色限量版', 'C-HR', '皇冠', '4Runner', 'FJ酷路泽']
		} else if (brand === '奥迪') {
			this.seriesList = ['A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'Q2', 'Q3', 'Q5', 'Q7', 'Q8', 'TT', 'R8', 'E-TRON']
		} else if (brand === '别克') {
			this.seriesList = ['昂科威', '君越', '英朗', 'GL8', 'VELITE 7', '昂科拉', '威朗', 'GL6', '探岳', 'ENCORE', '林荫大道', '阅朗']
		} else if (brand === '福特') {
			this.seriesList = ['福克斯', '蒙迪欧', '翼虎', '锐界', '探险者', '翼搏', '全顺', '金牛座', '撼路者', 'Mustang', 'F-150', '嘉年华', '麦柯斯']
		} else if (brand === '吉利') {
			this.seriesList = ['博越', '星越', '远景X3', '缤瑞', '远景X5', '帝豪', '博瑞', '远景L', '嘉际', 'ICON', '远景S1', '凯越', '嘉悦', '远景X1', '远景SUV', '远景i5', '大迈X7', '远景S2', '杰士达']
		} else if (brand === '哈弗') {
			this.seriesList = ['H6', 'H9', 'F7', 'H2', 'F5', 'H4', 'H5', 'H2s', 'H1', 'M6', 'F7x']
		} else if (brand === '日系') {
			this.seriesList = ['雅阁', 'RAV4', '思域', '凯美瑞', 'CR-V', '皇冠', 'RAV4荣放', '汉兰达', '逍客', '锐志', '思铂睿', '奥德赛', '39', 'C-HR', 'CROWN皇冠', 'Excelle', 'VIOS凯美瑞', '全新MARITIME', '皇冠新SUV', 'X-TRAIL', '缤智']
		} else if (brand === '比亚迪') {
			this.seriesList = ['元EV', '唐', '宋Pro', '汉']
		} else if (brand === '长安') {
			this.seriesList = ['悦翔', '逸动', '奔奔', 'CS35', 'CS75', '和悦', '悦豪', '睿骋', 'UNI-T', '逸动DT']
		} else if (brand === '马自达') {
			this.seriesList = ['马自达3', '马自达6', 'CX-4', 'CX-5', 'CX-8', 'CX-9', '阿特兹', '马自达2']
		} else if (brand === '红星汽车') {
			this.seriesList = ['红旗E-HS3', '红旗E-HS9']
		} else if (brand === '红旗') {
			this.seriesList = ['红旗E-HS3', '红旗E-HS9']
		} else if (brand === 'Jeep') {
			this.seriesList = ['大切诺基', '自由光', '指南者', '牧马人', '自由侠']
		} else if (brand === '捷豹') {
			this.seriesList = ['E-PACE', 'F-PACE', 'F-TYPE']
		} else if (brand === 'MINI') {
			this.seriesList = ['MINI 3门', 'MINI 5门', 'MINI CLUBMAN', 'MINI COUNTRYMAN']
		}
		// 判断品牌列表的长度，如果超过15个则触发“更多”下拉菜单
		if (this.seriesList.length > 10) {
			this.showMoreBrands = true;
		}
		},


		getProfile() {
			// 获取表格数据
			this.$axios("/api/cars").then((res) => {
				this.allTableData = res.data;
				this.tableTableData = res.data;
				this.filterTableData = res.data;
				// 设置分页数据
				this.setPaginations();
			});
		},

		selectPrice(price) {
		this.selectedPrice = price;
		switch (price) {
			case '不限':
			this.search_data.minPrice = null;
			this.search_data.maxPrice = null;
			break;
			case '3万以下':
			this.search_data.minPrice = 0;
			this.search_data.maxPrice = 3;
			break;
			case '3-5万':
			this.search_data.minPrice = 3;
			this.search_data.maxPrice = 5;
			break;
			case '5-8万':
			this.search_data.minPrice = 5;
			this.search_data.maxPrice = 8;
			break;
			case '8-10万':
			this.search_data.minPrice = 8;
			this.search_data.maxPrice = 10;
			break;
			case '10-15万':
			this.search_data.minPrice = 10;
			this.search_data.maxPrice = 15;
			break;
			case '15-20万':
			this.search_data.minPrice = 15;
			this.search_data.maxPrice = 20;
			break;
			case '20-30万':
			this.search_data.minPrice = 20;
			this.search_data.maxPrice = 30;
			break;
			case '30-50万':
			this.search_data.minPrice = 30;
			this.search_data.maxPrice = 50;
			break;
			case '50-100万':
			this.search_data.minPrice = 50;
			this.search_data.maxPrice = 100;
			break;
			case '100万以上':
			this.search_data.minPrice = 100;
			this.search_data.maxPrice = 1000000000000000000000;
			break;

		}
		this.onScreeoutMoney();
		},
		onScreeoutMoney() {
		if (this.search_data.maxPrice !== null && this.search_data.minPrice !== null && this.search_data.minPrice > this.search_data.maxPrice) {
			// 最大值小于最小值，给出错误提示或执行其他操作
			alert('请输入有效的价格范围');
			return;
			};
		const minPrice = this.search_data.minPrice;
		const maxPrice = this.search_data.maxPrice;
		this.allTableData = this.filterTableData.filter((item) => {
			if(minPrice === null && maxPrice === null){
			return true;
			}else if (minPrice === null) {
			return item.price <= maxPrice;
			}else if (maxPrice === null) {
			return item.price >= minprice;
			} else{
			return item.price >= minPrice && item.price <= maxPrice;
			}
		});
		this.setPaginations();
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
		this.paginations.page_size = 20;   // 将page_size的值改为20
		// 设置默认分页数据
		this.tableData = this.allTableData.filter((item, index) => {
			return index < this.paginations.page_size;
		});
		},
		//其他中下拉选项的方法
		handleCommand(command) {
		this.$message('click on item ' + command);
		},
		handleAreaSelect(command) {
		this.areatext = command;
		},
		handleBrandSelect(command) {
		this.brandText = command;
		},
		handleAgeSelect(command) {
		this.ageText = command;
		},
		handleTransmissionSelect(command) {
		this.transmissionText = command;
		},
		handleMileageSelect(command) {
		this.MileageText = command;
		},
		handleEmissionsSelect(command) {
		this.emissionsText = command;
		},
		handleEmissionsstandardsSelect(command) {
		this.emissionsstandardsText = command;
		},
		handleColorSelect(command) {
		this.colorText = command;
		},
		handleCountrySelect(command) {
		this.countryText = command;
		},
		handleDriveSelect(command) {
		this.driveText = command;
		},
		handleSeatSelect(command) {
		this.seatText = command;
		},
		handleFuelSelect(command) {
		this.fuelText = command;
		},


  },
};



</script>



<style scoped>
    .pagination {
      text-align: right;
      margin-top: 10px;
    }
    .search {
    position: fixed;
    width: 100%;
    height: 100%;
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

    .header {
    height: 1rem; /* 设置间隔高度，可根据需要调整数值 */
    }

    /*上半部分背景卡片的颜色 */
    .top-card {
    background-color:rgba(255, 255, 255, 1);
    margin-left: 0px;
    margin-right:0px;
    }
    .bottom-row {
    margin-top: 1.5rem; /* 控制底部行与上半部分的间距 */
    }

    /**全国选项的颜色和样式 */
    .location-input {
      width: 150px;
      font-size: 8px; /* 修改内部文字的大小为 14px */
      font-weight: bold; /* 将内部文字设为加粗 */
      margin-bottom:0px;
    }

    .el-icon-arrow-down {
        font-size: 12px;
    }
    .bold-text {
    font-weight: bold;
    font-size: 12px; /* 设置字体大小 */
    color: #000000; /* 设置字体颜色（示例为红色） */
    }

    .bold-text-yixuanze {
    font-size: 10px; /* 设置字体大小 */
    color:rgb(0, 0, 0); /* 设置字体颜色（示例为红色） */
    }

    .project-dropdown{
    height:300px;
    overflow: auto;
    }
    .project-dropdown::-webkit-scrollbar
    {
        width: 5px;
        height: 5px;
        background-color: #F5F5F5;
    }
    .project-dropdown::-webkit-scrollbar-track
    {
        border-radius: 10px;
        background-color: #F5F5F5;
    }

    

    /**品牌部分的样式 */
    .brand-container {
    margin-top: 20px; /* 调整第一个容器与上方元素的距离 */
    display: flex;
    align-items: center;
    }

    .brand-container0 {
    margin-top: 20px; /* 调整品牌与上方元素的距离 */
    display: flex;
    align-items: center;
    }
    .brand-container0 .bold-text {
    margin-right: 15px; /* 添加右边距，调整"品牌"标签与文本之间的距离 */
    }

    .brand-container1 {
    margin-top: 23px; /* 调整车系与上方元素的距离 */
    display: flex;
    align-items: center;
    }
    .brand-container1 .bold-text {
    margin-right: 15px; /* 添加右边距，调整"品牌"标签与文本之间的距离 */
    }

    .brand-container2 {
    margin-top: -10px; /* 调整价格与上方元素的距离 */
    display: flex;
    align-items: center;
    }
    .brand-container2 .bold-text {
    margin-right: 15px; /* 添加右边距，调整"品牌"标签与文本之间的距离 */
    }

    .brand-list {
    display: flex;
    align-items: center;
    }
    .brand-list .item {
    margin-right: 15px; /* 设置词与词之间的空隙大小，调整数值以获得所需的间距 */
    display: inline;
    font-size: 12px; /* 设置字体大小 */
    }
    .brand-container .bold-text {
    margin-right: 15px; /* 添加右边距，调整"品牌"标签与文本之间的距离 */
    }
    .brand-more {
        margin-right: 8px; /* 设置词与词之间的空隙大小，调整数值以获得所需的间距 */
        display: inline;
        font-size: 12px; /* 设置字体大小 */
    }

    /**价格样式--输入框 */
    /**给选中的字体设置悬停和选中样式 */
    .item:hover {
      color: rgba(53, 99, 233, 1);
    }

    .hasChecked {
      background-color: rgb(24, 126, 199);
      color: white;
      padding: 2px;
    }
    .input-row {
        overflow: hidden; /* 清除浮动 */
        margin-bottom: 0px;
    }
    .input-row el-input {
    float: left;
    margin-right: 10px; /* 可选，用于设置输入框间的水平间距 */
    }
    .custom-input {
        width: 60px;
        font-size: 6px;
        margin-top: 18px;
    }

    .custom-input2 {
        width: 250px;
        height: 30px;
        font-size: 6px;
        margin-left: 20px;
    }


    .unit {
        margin-left: 5px;
        font-size: 12px;
        
    }
    .error {
        display: block;
        color: #f56c6c;
        margin-top: 5px;
    }
    .button1 {
        margin-left: 10px;
        padding: 0.5%;
        float: right;
        font-size: 8px;
        background-color: rgba(53, 99, 233, 1);
        color: white;
    }

    .buttonPrice {
        margin-left: 10px;
        margin-top: 28px;
        padding: 10%;
        float: right;
        font-size: 8px;
        background-color: rgba(53, 99, 233, 1);
        color: white;
    }
    .separator1 {
        margin: 0 10px; /* 可调整分隔符与输入框的距离 */
    }

      /**下半部分卡片的样式 */
      .card-container {
        display: flex; /* 使用 flexbox 布局 */
        flex-wrap: wrap; /* 超出容器宽度时换行 */
        justify-content: space-between; /* 在容器内水平分布子元素 */
      }
      

      .card-item {
        width: calc(25% - 10px); /* 确保一行显示四个卡片，减去 margin 的宽度 */
        margin-bottom: 20px; /* 调整卡片之间的间距 */
      }


    .card-content {
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .card-content .title {
    white-space: nowrap; /* 强制在一行内展示文本 */
    overflow: hidden; /* 隐藏溢出的部分 */
    text-overflow: ellipsis; /* 用省略号表示溢出的部分 */
    }

    .card-img {
      max-width: 100%; /* 图片最大宽度为卡片宽度 */
      max-height: 100%; /* 图片最大高度为卡片高度 */
      margin-bottom:10px;
    }
    .bottom-card {
    background-color: rgba(255, 255, 255, 1);
    }

    .card-column {
    padding-left: 2px; /* 调整卡片列的左内间距 */
    padding-right: 2px;
  
    }
    .card-row {
        margin-left: 0px;
        margin-right:0px;
        margin-bottom: 15px;
    }

    .title {
    font-size: 15px;
    }

    .car-info {
    margin-top: 4px;
    display: flex;
    }

    .price {
    float: left;
    font-size: 18px;
    color:rgba(53, 99, 233, 1);
    margin-top: 4px;
    }

    .extra-info {
    font-size: 10px;
    color: #999;
    margin-top: 2px;
    display: flex;
    }
    .separator2 {
      margin: 0 5px;
      color: #999;
    }
  
    .buttondetails {
      width:70px;
    padding: 1%;
    float: right;
    font-size: 10px;
    background-color: rgba(53, 99, 233, 1);
    color: white;
    margin-top:-14px;
    }
    
    .price-container {
        margin-right: auto;
        margin-top: 10px;
    }
    .button-container {
        margin-left: auto;
    }
    .clearfix:before,
    .clearfix:after {
        display: table;
        content: "";
    }
    
    .clearfix:after {
        clear: both
    }
</style>