<template>
  <div class="search">
      <!--控制导航栏和上半部分卡片的距离-->
      <!--导航栏-->
	  <el-header class="right-align" style="background-color: rgba(245, 246, 252, 1);">
      <NavigationMenuAfterLogin
        :activeIndex="activeIndex"
        :backgroundColor="backgroundColor"
        :textColor="textColor"
        :activeTextColor="activeTextColor"
      />
	  </el-header>

	
    <div style="height: 100%; display: flex" class="cab">
      <el-scrollbar style="height: 100%">
        <!--页面主体-->
        <div>
          <!--导航栏与页面-->
          <!-- <div class="header"></div> -->
          <!--控制导航栏和上半部分卡片的距离-->

          <!-- 上半部分：大矩形卡片 -->
          <el-card class="top-card" :style="{ height: '23.5rem' }">
            <el-row>
              <!-- 所在地选择 -->
              <div class="brand-container4">
                <el-cascader
                  class="location-input"
                  v-model="selectedCities"
                  :options="options"
                  size="mini"
                  @change="handleCityChange"
                  placeholder="请选择省份和城市"
                  clearable
                ></el-cascader>

                <div class="search-container">
                  <!-- 搜索框 -->
                  <el-input
                    v-model="searchKeyword"
                    size="mini"
                    placeholder=""
                    class="custom-input2"
                  ></el-input>
                  <el-button
                    type="primary"
                    icon="el-icon-search"
                    class="button1"
                    @click="search"
                    >搜索</el-button
                  >
                </div>
              </div>
            </el-row>

            <!-- 品牌选择 -->
            <el-row>
              <div class="brand-container0">
                <label class="bold-text">品牌</label>
                <ul class="brand-list">
                  <li
                    class="item"
                    :class="{ hasChecked: selectedBrand === '' }"
                    @click="selectBrand('')"
                  >
                    不限
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedBrand === '大众' }"
                    @click="selectBrand('大众')"
                  >
                    大众
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedBrand === '本田' }"
                    @click="selectBrand('本田')"
                  >
                    本田
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedBrand === '奔驰' }"
                    @click="selectBrand('奔驰')"
                  >
                    奔驰
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedBrand === '宝马' }"
                    @click="selectBrand('宝马')"
                  >
                    宝马
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedBrand === '丰田' }"
                    @click="selectBrand('丰田')"
                  >
                    丰田
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedBrand === '奥迪' }"
                    @click="selectBrand('奥迪')"
                  >
                    奥迪
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedBrand === '别克' }"
                    @click="selectBrand('别克')"
                  >
                    别克
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedBrand === '福特' }"
                    @click="selectBrand('福特')"
                  >
                    福特
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedBrand === '吉利汽车' }"
                    @click="selectBrand('吉利汽车')"
                  >
                    吉利汽车
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedBrand === '哈弗' }"
                    @click="selectBrand('哈弗')"
                  >
                    哈弗
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedBrand === '比亚迪' }"
                    @click="selectBrand('比亚迪')"
                  >
                    比亚迪
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedBrand === '马自达' }"
                    @click="selectBrand('马自达')"
                  >
                    马自达
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedBrand === '红旗' }"
                    @click="selectBrand('红旗')"
                  >
                    红旗
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedBrand === 'Jeep' }"
                    @click="selectBrand('Jeep')"
                  >
                    Jeep
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedBrand === '长安' }"
                    @click="selectBrand('长安')"
                  >
                    长安
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedBrand === '捷豹' }"
                    @click="selectBrand('捷豹')"
                  >
                    捷豹
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedBrand === 'MINI' }"
                    @click="selectBrand('MINI')"
                  >
                    MINI
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedBrand === '一汽' }"
                    @click="selectBrand('一汽')"
                  >
                    一汽
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedBrand === '三菱' }"
                    @click="selectBrand('三菱')"
                  >
                    三菱
                  </li>
                  <li
                    class="item brand-more"
                    @click="moreBrandsVisible = !moreBrandsVisible"
                  >
                    更多
                    <i
                      :class="{
                        'arrow-up': moreBrandsVisible,
                        'arrow-down': !moreBrandsVisible,
                      }"
                    ></i>
                  </li>
                  <el-dropdown
                    popper-class="dropdown-menu"
                    v-if="moreBrandsVisible"
                    trigger="click"
                  >
                    <span class="item dropdown">
                      <i class="el-icon-arrow-down el-icon--right"></i>
                    </span>
                    <el-dropdown-menu
                      slot="dropdown"
                      class="custom-dropdown-menu custom-menu"
                    >
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '东南' }"
                        @click="selectBrand('东南')"
                      >
                        东南
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '东风' }"
                        @click="selectBrand('东风')"
                      >
                        东风
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '东风风神' }"
                        @click="selectBrand('东风风神')"
                      >
                        东风风神
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '东风风行' }"
                        @click="selectBrand('东风风行')"
                      >
                        东风风行
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '中华' }"
                        @click="selectBrand('中华')"
                      >
                        中华
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '五菱汽车' }"
                        @click="selectBrand('五菱汽车')"
                      >
                        五菱汽车
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '保时捷' }"
                        @click="selectBrand('保时捷')"
                      >
                        保时捷
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '众泰' }"
                        @click="selectBrand('众泰')"
                      >
                        众泰
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '凯翼' }"
                        @click="selectBrand('凯翼')"
                      >
                        凯翼
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '凯迪拉克' }"
                        @click="selectBrand('凯迪拉克')"
                      >
                        凯迪拉克
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '法拉利' }"
                        @click="selectBrand('法拉利')"
                      >
                        法拉利
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '名爵' }"
                        @click="selectBrand('名爵')"
                      >
                        名爵
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '启辰' }"
                        @click="selectBrand('启辰')"
                      >
                        启辰
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '奇瑞' }"
                        @click="selectBrand('奇瑞')"
                      >
                        奇瑞
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '开瑞' }"
                        @click="selectBrand('开瑞')"
                      >
                        开瑞
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '思皓' }"
                        @click="selectBrand('思皓')"
                      >
                        思皓
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '斯柯达' }"
                        @click="selectBrand('斯柯达')"
                      >
                        斯柯达
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '日产' }"
                        @click="selectBrand('日产')"
                      >
                        日产
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '林肯' }"
                        @click="selectBrand('林肯')"
                      >
                        林肯
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '标致' }"
                        @click="selectBrand('标致')"
                      >
                        标致
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '江淮' }"
                        @click="selectBrand('江淮')"
                      >
                        江淮
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '沃尔沃' }"
                        @click="selectBrand('沃尔沃')"
                      >
                        沃尔沃
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '海马' }"
                        @click="selectBrand('海马')"
                      >
                        海马
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '玛莎拉蒂' }"
                        @click="selectBrand('玛莎拉蒂')"
                      >
                        玛莎拉蒂
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '现代' }"
                        @click="selectBrand('现代')"
                      >
                        现代
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '福田' }"
                        @click="selectBrand('福田')"
                      >
                        福田
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '荣威' }"
                        @click="selectBrand('荣威')"
                      >
                        荣威
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '蔚来' }"
                        @click="selectBrand('蔚来')"
                      >
                        蔚来
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '起亚' }"
                        @click="selectBrand('起亚')"
                      >
                        起亚
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '迈凯伦' }"
                        @click="selectBrand('迈凯伦')"
                      >
                        迈凯伦
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '金杯' }"
                        @click="selectBrand('金杯')"
                      >
                        金杯
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '长城' }"
                        @click="selectBrand('长城')"
                      >
                        长城
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '雪佛兰' }"
                        @click="selectBrand('雪佛兰')"
                      >
                        雪佛兰
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '雪铁龙' }"
                        @click="selectBrand('雪铁龙')"
                      >
                        雪铁龙
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '雷克萨斯' }"
                        @click="selectBrand('雷克萨斯')"
                      >
                        雷克萨斯
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '领克' }"
                        @click="selectBrand('领克')"
                      >
                        领克
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '魏牌' }"
                        @click="selectBrand('魏牌')"
                      >
                        魏牌
                      </li>
                      <li
                        class="item"
                        :class="{ hasChecked: selectedBrand === '黄海' }"
                        @click="selectBrand('黄海')"
                      >
                        黄海
                      </li>
                    </el-dropdown-menu>
                  </el-dropdown>
                </ul>
                <el-dropdown trigger="click">
                  <li
                    class="item brand-more"
                    slot="reference"
                    @click="showMoreBrands = !showMoreBrands"
                  >
                    <span class="brand-more"></span> 更多
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
                  <li
                    class="item"
                    :class="{ hasChecked: selectedModel === '' }"
                    @click="selectModel('')"
                  >
                    不限
                  </li>
                  <li
                    class="item"
                    v-for="(model, key) in visibleModelList"
                    :key="key"
                    :class="{ hasChecked: selectedModel === model }"
                    @click="selectModel(model)"
                  >
                    {{ model }}
                  </li>
                  <el-dropdown v-if="showMoreModel">
                    <li class="item hasChecked" slot="reference">
                      更多
                      <i class="el-icon-arrow-down el-icon--right"></i>
                    </li>
                    <el-dropdown-menu slot="dropdown">
                      <el-dropdown-item
                        v-for="(model, key) in modelList.slice(10)"
                        :key="key"
                        @click="selectModel(model)"
                      >
                        {{ model }}
                      </el-dropdown-item>
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
                  <li
                    class="item"
                    :class="{ hasChecked: selectedPrice === '' }"
                  >
                    <span @click="selectPrice('')">不限</span>
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedPrice === '3万以下' }"
                  >
                    <span @click="selectPrice('3万以下')">3万以下</span>
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedPrice === '3-5万' }"
                  >
                    <span @click="selectPrice('3-5万')">3-5万</span>
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedPrice === '5-8万' }"
                  >
                    <span @click="selectPrice('5-8万')">5-8万</span>
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedPrice === '8-10万' }"
                  >
                    <span @click="selectPrice('8-10万')">8-10万</span>
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedPrice === '10-15万' }"
                  >
                    <span @click="selectPrice('10-15万')">10-15万</span>
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedPrice === '15-20万' }"
                  >
                    <span @click="selectPrice('15-20万')">15-20万</span>
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedPrice === '20-30万' }"
                  >
                    <span @click="selectPrice('20-30万')">20-30万</span>
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedPrice === '30-50万' }"
                  >
                    <span @click="selectPrice('30-50万')">30-50万</span>
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedPrice === '50-100万' }"
                  >
                    <span @click="selectPrice('50-100万')">50-100万</span>
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedPrice === '100万以上' }"
                  >
                    <span @click="selectPrice('100万以上')">100万以上</span>
                  </li>
                </ul>
                <div class="input-row">
                  <el-form
                    :inline="true"
                    ref="search_data"
                    :model="search_data"
                  >
                    <el-form-item label="">
                      <el-input
                        v-model.number="search_data.minPrice"
                        size="mini"
                        placeholder="最小"
                        class="custom-input"
                      ></el-input>
                      <span> - </span>
                      <el-input
                        v-model.number="search_data.maxPrice"
                        size="mini"
                        placeholder="最大"
                        class="custom-input"
                      ></el-input>
                    </el-form-item>
                    <el-form-item>
                      <el-button
                        type="primary"
                        icon="pricesearch"
                        @click="onScreeoutMoney()"
                        class="buttonPrice"
                        >筛选</el-button
                      >
                    </el-form-item>
                  </el-form>
                </div>
              </div>
            </el-row>

            <!-- 其他选择 -->
            <el-row>
              <div class="brand-container2">
                <lable class="bold-text">其他</lable>
                <!-- 转手次数下拉菜单 -->
                <el-dropdown
                  trigger="click"
                  @command="handlenum_of_transferSelect"
                >
                  <span class="brand-more">
                    {{ num_of_transferText ? num_of_transferText : "不限"
                    }}<i class="el-icon-arrow-down el-icon--right"></i>
                  </span>
                  <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item command="">不限</el-dropdown-item>
                    <el-dropdown-item command="0">0</el-dropdown-item>
                    <el-dropdown-item command="1">1</el-dropdown-item>
                    <el-dropdown-item command="2">2</el-dropdown-item>
                    <el-dropdown-item command="3">3</el-dropdown-item>
                    <el-dropdown-item command="4">4</el-dropdown-item>
                    <el-dropdown-item command="5次及以上"
                      >5次及以上</el-dropdown-item
                    >
                  </el-dropdown-menu>
                </el-dropdown>

                <!-- 车龄下拉菜单 -->
                <el-dropdown trigger="click" @command="handleAgeSelect">
                  <span class="brand-more">
                    {{ ageText ? ageText : "不限"
                    }}<i class="el-icon-arrow-down el-icon--right"></i>
                  </span>
                  <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item command="">不限</el-dropdown-item>
                    <el-dropdown-item command="1">一年</el-dropdown-item>
                    <el-dropdown-item command="2">两年</el-dropdown-item>
                    <el-dropdown-item command="3">三年</el-dropdown-item>
                    <el-dropdown-item command="4">四年</el-dropdown-item>
                    <el-dropdown-item command="5">五年及以上</el-dropdown-item>
                  </el-dropdown-menu>
                </el-dropdown>

                <!-- 变速箱下拉菜单 -->
                <el-dropdown
                  trigger="click"
                  @command="handleTransmissionSelect"
                >
                  <span class="brand-more">
                    {{ transmissionText
                    }}<i class="el-icon-arrow-down el-icon--right"></i>
                  </span>
                  <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item command="自动">自动</el-dropdown-item>
                    <el-dropdown-item command="手动">手动</el-dropdown-item>
                  </el-dropdown-menu>
                </el-dropdown>

                <!-- 里程下拉菜单 -->
                <el-dropdown trigger="click" @command="handleMileageSelect">
                  <span class="brand-more">
                    {{ mileageText
                    }}<i class="el-icon-arrow-down el-icon--right"></i>
                  </span>
                  <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item command="1万公里以下"
                      >1万公里以下</el-dropdown-item
                    >
                    <el-dropdown-item command="1-3万公里"
                      >1-3万公里</el-dropdown-item
                    >
                    <el-dropdown-item command="3-5万公里"
                      >3-5万公里</el-dropdown-item
                    >
                    <el-dropdown-item command="5-8万公里"
                      >5-8万公里</el-dropdown-item
                    >
                    <el-dropdown-item command="8-10万公里"
                      >8-10万公里</el-dropdown-item
                    >
                    <el-dropdown-item command="10万公里以上"
                      >10万公里以上</el-dropdown-item
                    >
                  </el-dropdown-menu>
                </el-dropdown>

                <!-- 排量下拉菜单 -->
                <el-dropdown trigger="click" @command="handleEmissionsSelect">
                  <span class="brand-more">
                    {{ emissionsText
                    }}<i class="el-icon-arrow-down el-icon--right"></i>
                  </span>
                  <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item command="1.0L及以下"
                      >1.0L及以下</el-dropdown-item
                    >
                    <el-dropdown-item command="1.1L-1.6L"
                      >1.1L-1.6L</el-dropdown-item
                    >
                    <el-dropdown-item command="1.7L-2.0L"
                      >1.7L-2.0L</el-dropdown-item
                    >
                    <el-dropdown-item command="2.1L-2.5L"
                      >2.1L-2.5L</el-dropdown-item
                    >
                    <el-dropdown-item command="2.6L-3.0L"
                      >2.6L-3.0L</el-dropdown-item
                    >
                    <el-dropdown-item command="3.1L-4.0L"
                      >3.1L-4.0L</el-dropdown-item
                    >
                    <el-dropdown-item command="4.0L以上"
                      >4.0L以上</el-dropdown-item
                    >
                  </el-dropdown-menu>
                </el-dropdown>

                <!-- 排放标准下拉菜单 -->
                <el-dropdown
                  trigger="click"
                  @command="handleEmissionsstandardsSelect"
                >
                  <span class="brand-more">
                    {{ emissionsstandardsText
                    }}<i class="el-icon-arrow-down el-icon--right"></i>
                  </span>
                  <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item command="国V(国VI)"
                      >国V/国VI</el-dropdown-item
                    >
                    <el-dropdown-item command="欧III">欧III</el-dropdown-item>
                    <el-dropdown-item command="欧V+OBD"
                      >欧V+OBD</el-dropdown-item
                    >
                    <el-dropdown-item command="国IV/国V"
                      >国IV/国V</el-dropdown-item
                    >
                    <el-dropdown-item command="国IV+OBD"
                      >国IV+OBD</el-dropdown-item
                    >
                    <el-dropdown-item command="国III+OBD"
                      >国III+OBD</el-dropdown-item
                    >
                    <el-dropdown-item command="国III">国III</el-dropdown-item>
                    <el-dropdown-item command="国II">国II</el-dropdown-item>
                    <el-dropdown-item command="欧II">欧II</el-dropdown-item>
                    <el-dropdown-item command="国IV">国IV</el-dropdown-item>
                    <el-dropdown-item command="国IV(国V)+OBD"
                      >国IV/国V+OBD</el-dropdown-item
                    >
                    <el-dropdown-item command="欧IV">欧IV</el-dropdown-item>
                    <el-dropdown-item command="欧IV+OBD"
                      >欧IV+OBD</el-dropdown-item
                    >
                    <el-dropdown-item command="欧VI">欧VI</el-dropdown-item>
                    <el-dropdown-item command="国IV(国V)"
                      >国IV/国V</el-dropdown-item
                    >
                    <el-dropdown-item command="欧V">欧V</el-dropdown-item>
                    <el-dropdown-item command="国V+OBD"
                      >国V+OBD</el-dropdown-item
                    >
                    <el-dropdown-item command="国VI">国VI</el-dropdown-item>
                    <el-dropdown-item command="国V">国V</el-dropdown-item>
                  </el-dropdown-menu>
                </el-dropdown>

                <!-- 颜色下拉菜单 -->
                <el-dropdown trigger="click" @command="handleColorSelect">
                  <span class="brand-more">
                    {{ colorText
                    }}<i class="el-icon-arrow-down el-icon--right"></i>
                  </span>
                  <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item command="黑色">黑色</el-dropdown-item>
                    <el-dropdown-item command="白色">白色</el-dropdown-item>
                    <el-dropdown-item command="银/灰色"
                      >银/灰色</el-dropdown-item
                    >
                    <el-dropdown-item command="红/紫色"
                      >红/紫色</el-dropdown-item
                    >
                    <el-dropdown-item command="黄/橙色"
                      >黄/橙色</el-dropdown-item
                    >
                    <el-dropdown-item command="蓝色">蓝色</el-dropdown-item>
                    <el-dropdown-item command="绿色">绿色</el-dropdown-item>
                    <el-dropdown-item command="粉色">粉色</el-dropdown-item>
                    <el-dropdown-item command="香槟/棕色"
                      >香槟/棕色</el-dropdown-item
                    >
                    <el-dropdown-item command="其他">其他</el-dropdown-item>
                  </el-dropdown-menu>
                </el-dropdown>

                <!-- 驱动下拉菜单 -->
                <el-dropdown trigger="click" @command="handleDriveSelect">
                  <span class="brand-more">
                    {{ driveText
                    }}<i class="el-icon-arrow-down el-icon--right"></i>
                  </span>
                  <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item command="前置后驱"
                      >前置后驱</el-dropdown-item
                    >
                    <el-dropdown-item command="双电动四驱"
                      >双电动四驱</el-dropdown-item
                    >
                    <el-dropdown-item command="前置四驱"
                      >前置四驱</el-dropdown-item
                    >
                    <el-dropdown-item command="中置后驱"
                      >中置后驱</el-dropdown-item
                    >
                    <el-dropdown-item command="前置前驱"
                      >前置前驱</el-dropdown-item
                    >
                    <el-dropdown-item command="后置四驱"
                      >后置四驱</el-dropdown-item
                    >
                    <el-dropdown-item command="后置后驱"
                      >后置后驱</el-dropdown-item
                    >
                  </el-dropdown-menu>
                </el-dropdown>

                <!-- 燃料类型下拉菜单 -->
                <el-dropdown trigger="click" @command="handleFuelSelect">
                  <span class="brand-more">
                    {{ fuelText
                    }}<i class="el-icon-arrow-down el-icon--right"></i>
                  </span>
                  <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item command="插电混动"
                      >插电混动</el-dropdown-item
                    >
                    <el-dropdown-item command="增程式">增程式</el-dropdown-item>
                    <el-dropdown-item command="纯电动">纯电动</el-dropdown-item>
                  </el-dropdown-menu>
                </el-dropdown>
                <!-- 燃油标准下拉菜单 -->
                <el-dropdown
                  trigger="click"
                  @command="handleFuelStandardSelect"
                >
                  <span class="brand-more">
                    {{ fuelStandardText
                    }}<i class="el-icon-arrow-down el-icon--right"></i>
                  </span>
                  <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item command="98号">98号</el-dropdown-item>
                    <el-dropdown-item command="92号">92号</el-dropdown-item>
                    <el-dropdown-item command="89号">89号</el-dropdown-item>
                  </el-dropdown-menu>
                </el-dropdown>
              </div>
            </el-row>

            <!-- 筛选排序 -->
            <el-row>
              <div class="brand-container">
                <ul class="brand-list">
                  <li
                    class="item"
                    :class="{ hasChecked: selectedfun === '综合排序' }"
                  >
                    <span @click="selectfun('综合排序')">综合排序</span>
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedfun === '最新上架' }"
                  >
                    <span @click="selectfun('最新上架')">最新上架</span>
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedfun === '价格最高' }"
                  >
                    <span @click="selectfun('价格最高')">价格最高</span>
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedfun === '价格最低' }"
                  >
                    <span @click="selectfun('价格最低')">价格最低</span>
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedfun === '车龄最短' }"
                  >
                    <span @click="selectfun('车龄最短')">车龄最短</span>
                  </li>
                  <li
                    class="item"
                    :class="{ hasChecked: selectedfun === '里程最少' }"
                  >
                    <span @click="selectfun('里程最少')">里程最少</span>
                  </li>
                  <button class="bold-text">清空筛选</button>
                </ul>
              </div>
            </el-row>

            <!-- 已选择 -->
            <el-row>
              <div class="brand-container">
                <lable class="bold-text-yixuanze">当前选择：</lable>
                <ul class="brand-list3">
                  <span v-if="selectedBrand !== ''" class="selected-option">
                    品牌: {{ selectedBrand }}
                    <i class="el-icon-close" @click="clearSelectedBrand"></i>
                  </span>
                  <span v-if="selectedModel !== ''" class="selected-option">
                    车系: {{ selectedModel }}
                    <i class="el-icon-close" @click="clearSelectedModel"></i>
                  </span>
                  <span v-if="selectedPrice !== ''" class="selected-option">
                    价格: {{ selectedPrice }}
                    <i class="el-icon-close" @click="clearSelectedPrice"></i>
                  </span>
                  <span
                    v-if="selectedNum_of_transfer !== ''"
                    class="selected-option"
                  >
                    转手次数: {{ selectedNum_of_transfer }}
                    <i
                      class="el-icon-close"
                      @click="clearSelectedNum_of_transfer"
                    ></i>
                  </span>
                  <span v-if="selectedAge !== ''" class="selected-option">
                    车龄: {{ selectedAge }}
                    <i class="el-icon-close" @click="clearSelectedAge"></i>
                  </span>
                  <span
                    v-if="selectedTransmission !== ''"
                    class="selected-option"
                  >
                    变速箱: {{ selectedTransmission }}
                    <i
                      class="el-icon-close"
                      @click="clearSelectedTransmission"
                    ></i>
                  </span>
                  <span v-if="selectedMileage !== ''" class="selected-option">
                    里程: {{ selectedMileage }}
                    <i class="el-icon-close" @click="clearSelectedMileage"></i>
                  </span>
                  <span v-if="selectedEmission !== ''" class="selected-option">
                    排量: {{ selectedEmission }}
                    <i class="el-icon-close" @click="clearSelectedEmission"></i>
                  </span>
                  <span
                    v-if="selectedEmissionsstandards !== ''"
                    class="selected-option"
                  >
                    排量: {{ selectedEmissionsstandards }}
                    <i
                      class="el-icon-close"
                      @click="clearselectedEmissionsstandards"
                    ></i>
                  </span>
                  <span v-if="selectedColor !== ''" class="selected-option">
                    颜色: {{ selectedColor }}
                    <i class="el-icon-close" @click="clearselectedColor"></i>
                  </span>
                  <span v-if="selectedDrive !== ''" class="selected-option">
                    驱动: {{ selectedDrive }}
                    <i class="el-icon-close" @click="clearselectedDrive"></i>
                  </span>
                  <span v-if="selectedFuel !== ''" class="selected-option">
                    燃料类型: {{ selectedFuel }}
                    <i class="el-icon-close" @click="clearselectedFuel"></i>
                  </span>
                  <span
                    v-if="selectedFuelStandard !== ''"
                    class="selected-option"
                  >
                    燃油标准: {{ selectedFuelStandard }}
                    <i
                      class="el-icon-close"
                      @click="clearselectedFuelStandard"
                    ></i>
                  </span>
                </ul>
              </div>
            </el-row>
          </el-card>
          <div class="header"></div>
          <!--控制导航栏和上半部分卡片的距离-->

          <!-- 下半部分 -->

          <el-row>
            <div class="card-container">
              <el-card
                v-for="item in tableData"
                :key="item.id"
                class="card-item"
              >
                <img class="card-img" :src="item.img_url[0]" alt="image" />
                <div class="card-content">
                  <router-link :to="{ name: 'cardetails', params: { id: item._id } }">
                    <span class="title-text">{{ item.title }}</span>
                  </router-link>

                  <div class="car-info">
                    <div class="extra-info">
                      <p>{{ item.license_time }}</p>
                      <!-- 上牌时间 -->
                      <span class="separator2">/</span>
                      <p>{{ item.mileage }}</p>
                      <!-- 里程 -->
                      <span class="separator2">/</span>
                      <p>{{ item.location }}</p>
                      <!-- 所在地 -->
                    </div>
                  </div>

                  <div class="price-container">
                    <p class="price">￥{{ item.price }}万</p>
                  </div>

                  <div class="button-container">
                    <el-button
                      type="text"
                      class="buttondetails"
                      @click="onEditProfile(item)"
                    >
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
import NavigationMenuAfterLogin from "@/components/NavigationMenuAfterLogin.vue";
export default {
	components: {
		NavigationMenuAfterLogin
		},
  data() {
    return {
      //默认选项
      activeIndex: "2",
      defaultModelList: [
        "奥迪A6L",
        "宝马5系",
        "宝马3系",
        "奔驰C级",
        "奔驰E级",
        "高尔夫",
        "迈腾",
        "速腾",
        "朗逸",
        "雅阁",
        "轩逸",
        "哈弗H6",
        "福克斯",
      ],
      tableData: [],
      allTableData: [],
      num_of_transferText: "",
      searchKeyword: "",
      sortDirection: "", // 记录当前排序方式：'asc'（升序）或 'desc'（降序）
      selectedfun: "",
      selectedBrand: "", // 记录用户选择的品牌
      moreBrandsVisible: false, // 控制"更多"下拉菜单的显示
      selectedModel: "", // 记录用户选择的车系
      modelList: [], // 当前选中品牌对应的车系列表
      showMoreBrands: false,
      showMoreModel: false,
      filterTableData: [],
      selectedPrice: "",
      lowerPrice: "",
      higherPrice: "",
      isValid: true,
      areatext: "全国",
      num_of_transferText: "转手次数",
      ageText: "车龄",
      transmissionText: "变速箱",
      mileageText: "里程",
      emissionsText: "排量",
      emissionsstandardsText: "排放标准",
      colorText: "颜色",
      countryText: "国别",
      driveText: "驱动",
      seatText: "座位数",
      fuelText: "燃料类型",
      fuelStandardText: "燃油标准",

      selectedNum_of_transfer: "", // 用户选择的转手次数
      selectedAge: "", // 用户选择的车龄
      selectedTransmission: "", // 用户选择的变速箱
      selectedMileage: "",
      selectedEmission: "",
      selectedEmissionsstandards: "",
      selectedColor: "",
      selectedDrive: "",
      selectedFuel: "",
      selectedFuelStandard: "",
      form: {
        img_url: "",
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
        page_sizes: [20, 28, 36, 48, 80],
        layout: "total, sizes, prev, pager, next, jumper",
      },
      search_data: {
        minPrice: null,
        maxPrice: null,
      },
      selectedCities: [], // 用于存储选中的省份和城市的值
      filterOptions: { location: "" },
      options: [
        {
          value: "anhui",
          label: "安徽",
          children: [
            { value: "hefei", label: "合肥" },
            { value: "wuhu", label: "芜湖" },
            { value: "bangbu", label: "蚌埠" },
            { value: "huainan", label: "淮南" },
            { value: "maanshan", label: "马鞍山" },
            { value: "huaibei", label: "淮北" },
            { value: "tongling", label: "铜陵" },
            { value: "anqing", label: "安庆" },
            { value: "huangshan", label: "黄山" },
            { value: "chuzhou", label: "滁州" },
            { value: "fuyang", label: "阜阳" },
            { value: "suzhou", label: "宿州" },
            { value: "liuan", label: "六安" },
            { value: "bozhou", label: "亳州" },
            { value: "chizhou", label: "池州" },
            { value: "xuancheng", label: "宣城" },
          ],
        },
        {
          value: "beijing",
          label: "北京",
          children: [{ value: "beijing", label: "北京" }],
        },
        {
          value: "chongqing",
          label: "重庆",
          children: [{ value: "chongqing", label: "重庆" }],
        },
        {
          value: "fujian",
          label: "福建",
          children: [
            { value: "fuzhou", label: "福州" },
            { value: "xiamen", label: "厦门" },
            { value: "putian", label: "莆田" },
            { value: "sanming", label: "三明" },
            { value: "quanzhou", label: "泉州" },
            { value: "zhangzhou", label: "漳州" },
            { value: "nanping", label: "南平" },
            { value: "longyan", label: "龙岩" },
            { value: "ningde", label: "宁德" },
          ],
        },
        {
          value: "guangdong",
          label: "广东",
          children: [
            { value: "guangzhou", label: "广州" },
            { value: "shaoguan", label: "韶关" },
            { value: "shenzhen", label: "深圳" },
            { value: "zhuhai", label: "珠海" },
            { value: "shantou", label: "汕头" },
            { value: "foshan", label: "佛山" },
            { value: "jiangmen", label: "江门" },
            { value: "zhanjiang", label: "湛江" },
            { value: "maoming", label: "茂名" },
            { value: "zhaoqing", label: "肇庆" },
            { value: "huizhou", label: "惠州" },
            { value: "meizhou", label: "梅州" },
            { value: "shanwei", label: "汕尾" },
            { value: "heyuan", label: "河源" },
            { value: "yangjiang", label: "阳江" },
            { value: "qingyuan", label: "清远" },
            { value: "dongguan", label: "东莞" },
            { value: "zhongshan", label: "中山" },
            { value: "chaozhou", label: "潮州" },
            { value: "jieyang", label: "揭阳" },
            { value: "yunfu", label: "云浮" },
          ],
        },
        {
          value: "guangxi",
          label: "广西",
          children: [
            { value: "nanning", label: "南宁" },
            { value: "liuzhou", label: "柳州" },
            { value: "guilin", label: "桂林" },
            { value: "wuzhou", label: "梧州" },
            { value: "beihai", label: "北海" },
            { value: "fangchenggang", label: "防城港" },
            { value: "qinzhou", label: "钦州" },
            { value: "guigang", label: "贵港" },
            { value: "yu_lin", label: "玉林" },
            { value: "baise", label: "百色" },
            { value: "hezhou", label: "贺州" },
            { value: "hechi", label: "河池" },
            { value: "laibin", label: "来宾" },
            { value: "chongzuo", label: "崇左" },
          ],
        },
        {
          value: "guizhou",
          label: "贵州",
          children: [
            { value: "guiyang", label: "贵阳" },
            { value: "liupanshui", label: "六盘水" },
            { value: "zunyi", label: "遵义" },
            { value: "anshun", label: "安顺" },
            { value: "bijie", label: "毕节" },
            { value: "tongren", label: "铜仁" },
            { value: "qianxinan", label: "黔西南" },
            { value: "qiandongnan", label: "黔东南" },
            { value: "qiannan", label: "黔南" },
          ],
        },
        {
          value: "gansu",
          label: "甘肃",
          children: [
            { value: "lanzhou", label: "兰州" },
            { value: "jiayuguan", label: "嘉峪关" },
            { value: "jinchang", label: "金昌" },
            { value: "baiyin", label: "白银" },
            { value: "tianshui", label: "天水" },
            { value: "wuwei", label: "武威" },
            { value: "zhangye", label: "张掖" },
            { value: "pingliang", label: "平凉" },
            { value: "jiuquan", label: "酒泉" },
            { value: "qingyang", label: "庆阳" },
            { value: "dingxi", label: "定西" },
            { value: "longnan", label: "陇南" },
            { value: "linxia", label: "临夏" },
            { value: "gannan", label: "甘南" },
          ],
        },
        {
          value: "hainan",
          label: "海南",
          children: [
            { value: "haikou", label: "海口" },
            { value: "sanya", label: "三亚" },
            { value: "sansha", label: "三沙" },
            { value: "danzhou", label: "儋州" },
            { value: "wuzhishan", label: "五指山" },
            { value: "qionghai", label: "琼海" },
            { value: "wenchang", label: "文昌" },
            { value: "wanning", label: "万宁" },
            { value: "dongfang", label: "东方" },
            { value: "dingan", label: "定安" },
            { value: "tunchang", label: "屯昌" },
            { value: "chengmai", label: "澄迈" },
            { value: "lingao", label: "临高" },
            { value: "baisha", label: "白沙" },
            { value: "changjiang", label: "昌江" },
            { value: "ledong", label: "乐东" },
            { value: "lingshui", label: "陵水" },
            { value: "baoting", label: "保亭" },
            { value: "qiongzhong", label: "琼中" },
          ],
        },
        {
          value: "henan",
          label: "河南",
          children: [
            { value: "zhengzhou", label: "郑州" },
            { value: "kaifeng", label: "开封" },
            { value: "luoyang", label: "洛阳" },
            { value: "pingdingshan", label: "平顶山" },
            { value: "anyang", label: "安阳" },
            { value: "hebi", label: "鹤壁" },
            { value: "xinxiang", label: "新乡" },
            { value: "jiaozuo", label: "焦作" },
            { value: "puyang", label: "濮阳" },
            { value: "xuchang", label: "许昌" },
            { value: "luohe", label: "漯河" },
            { value: "sanmenxia", label: "三门峡" },
            { value: "nanyang", label: "南阳" },
            { value: "shangqiu", label: "商丘" },
            { value: "xinyang", label: "信阳" },
            { value: "zhoukou", label: "周口" },
            { value: "zhumadian", label: "驻马店" },
            { value: "jiyuan", label: "济源" },
          ],
        },
        {
          value: "hubei",
          label: "湖北",
          children: [
            { value: "wuhan", label: "武汉" },
            { value: "huangshi", label: "黄石" },
            { value: "shiyan", label: "十堰" },
            { value: "yichang", label: "宜昌" },
            { value: "xiangyang", label: "襄阳" },
            { value: "ezhou", label: "鄂州" },
            { value: "jingmen", label: "荆门" },
            { value: "xiaogan", label: "孝感" },
            { value: "jingzhou", label: "荆州" },
            { value: "huanggang", label: "黄冈" },
            { value: "xianning", label: "咸宁" },
            { value: "suizhou", label: "随州" },
            { value: "enshi", label: "恩施" },
            { value: "xiantao", label: "仙桃" },
            { value: "qianjiang", label: "潜江" },
            { value: "tianmen", label: "天门" },
            { value: "shennongjia", label: "神农架" },
          ],
        },
        {
          value: "hunan",
          label: "湖南",
          children: [
            { value: "changsha", label: "长沙" },
            { value: "zhuzhou", label: "株洲" },
            { value: "xiangtan", label: "湘潭" },
            { value: "hengyang", label: "衡阳" },
            { value: "shaoyang", label: "邵阳" },
            { value: "yueyang", label: "岳阳" },
            { value: "changde", label: "常德" },
            { value: "zhangjiajie", label: "张家界" },
            { value: "yiyang", label: "益阳" },
            { value: "chenzhou", label: "郴州" },
            { value: "yongzhou", label: "永州" },
            { value: "huaihua", label: "怀化" },
            { value: "loudi", label: "娄底" },
            { value: "xiangxi", label: "湘西" },
          ],
        },
        {
          value: "hebei",
          label: "河北",
          children: [
            { value: "shijiazhuang", label: "石家庄" },
            { value: "tangshan", label: "唐山" },
            { value: "qinhuangdao", label: "秦皇岛" },
            { value: "handan", label: "邯郸" },
            { value: "xingtai", label: "邢台" },
            { value: "baoding", label: "保定" },
            { value: "zhangjiakou", label: "张家口" },
            { value: "chengde", label: "承德" },
            { value: "cangzhou", label: "沧州" },
            { value: "langfang", label: "廊坊" },
            { value: "hengshui", label: "衡水" },
          ],
        },
        {
          value: "heilongjiang",
          label: "黑龙江",
          children: [
            { value: "haerbin", label: "哈尔滨" },
            { value: "qiqihaer", label: "齐齐哈尔" },
            { value: "jixi", label: "鸡西" },
            { value: "hegang", label: "鹤岗" },
            { value: "shuangyashan", label: "双鸭山" },
            { value: "daqing", label: "大庆" },
            { value: "yichun", label: "伊春" },
            { value: "jiamusi", label: "佳木斯" },
            { value: "qitaihe", label: "七台河" },
            { value: "mudanjiang", label: "牡丹江" },
            { value: "heihe", label: "黑河" },
            { value: "suihua", label: "绥化" },
            { value: "daxinganling", label: "大兴安岭" },
          ],
        },
        {
          value: "jiangsu",
          label: "江苏",
          children: [
            { value: "nanjing", label: "南京" },
            { value: "wuxi", label: "无锡" },
            { value: "xuzhou", label: "徐州" },
            { value: "changzhou", label: "常州" },
            { value: "suzhou", label: "苏州" },
            { value: "nantong", label: "南通" },
            { value: "lianyungang", label: "连云港" },
            { value: "huaian", label: "淮安" },
            { value: "yancheng", label: "盐城" },
            { value: "yangzhou", label: "扬州" },
            { value: "zhenjiang", label: "镇江" },
            { value: "tai_zhou", label: "泰州" },
            { value: "suqian", label: "宿迁" },
          ],
        },
        {
          value: "jiangxi",
          label: "江西",
          children: [
            { value: "nanchang", label: "南昌" },
            { value: "jingdezhen", label: "景德镇" },
            { value: "ping_xiang", label: "萍乡" },
            { value: "jiujiang", label: "九江" },
            { value: "xinyu", label: "新余" },
            { value: "yingtan", label: "鹰潭" },
            { value: "ganzhou", label: "赣州" },
            { value: "jian", label: "吉安" },
            { value: "yi_chun", label: "宜春" },
            { value: "fu_zhou", label: "抚州" },
            { value: "shangrao", label: "上饶" },
          ],
        },
        {
          value: "jilin",
          label: "吉林",
          children: [
            { value: "changchun", label: "长春" },
            { value: "jilinshi", label: "吉林" },
            { value: "siping", label: "四平" },
            { value: "liaoyuan", label: "辽源" },
            { value: "tonghua", label: "通化" },
            { value: "baishan", label: "白山" },
            { value: "songyuan", label: "松原" },
            { value: "baicheng", label: "白城" },
            { value: "yanbian", label: "延边" },
          ],
        },
        {
          value: "liaoning",
          label: "辽宁",
          children: [
            { value: "shenyang", label: "沈阳" },
            { value: "dalian", label: "大连" },
            { value: "anshan", label: "鞍山" },
            { value: "fushun", label: "抚顺" },
            { value: "benxi", label: "本溪" },
            { value: "dandong", label: "丹东" },
            { value: "jinzhou", label: "锦州" },
            { value: "yingkou", label: "营口" },
            { value: "fuxin", label: "阜新" },
            { value: "liaoyang", label: "辽阳" },
            { value: "panjin", label: "盘锦" },
            { value: "tieling", label: "铁岭" },
            { value: "chaoyang", label: "朝阳" },
            { value: "huludao", label: "葫芦岛" },
          ],
        },
        {
          value: "neimenggu",
          label: "内蒙古",
          children: [
            { value: "huhehaote", label: "呼和浩特" },
            { value: "baotou", label: "包头" },
            { value: "wuhai", label: "乌海" },
            { value: "chifeng", label: "赤峰" },
            { value: "tongliao", label: "通辽" },
            { value: "eerduosi", label: "鄂尔多斯" },
            { value: "hulunbeier", label: "呼伦贝尔" },
            { value: "bayannaoer", label: "巴彦淖尔" },
            { value: "wulanchabu", label: "乌兰察布" },
            { value: "xinganmeng", label: "兴安盟" },
            { value: "xilinguolemeng", label: "锡林郭勒盟" },
            { value: "alashanmeng", label: "阿拉善盟" },
          ],
        },
        {
          value: "ningxia",
          label: "宁夏",
          children: [
            { value: "yinchuan", label: "银川" },
            { value: "shizuishan", label: "石嘴山" },
            { value: "wuzhong", label: "吴忠" },
            { value: "guyuan", label: "固原" },
            { value: "zhongwei", label: "中卫" },
          ],
        },
        {
          value: "qinghai",
          label: "青海",
          children: [
            { value: "xining", label: "西宁" },
            { value: "haidong", label: "海东" },
            { value: "haibei", label: "海北" },
            { value: "huangnan", label: "黄南" },
            { value: "hai_nan", label: "海南" },
            { value: "guoluo", label: "果洛" },
            { value: "yushu", label: "玉树" },
            { value: "haixi", label: "海西" },
          ],
        },
        {
          value: "shanxi",
          label: "陕西",
          children: [
            { value: "xian", label: "西安" },
            { value: "tongchuan", label: "铜川" },
            { value: "baoji", label: "宝鸡" },
            { value: "xianyang", label: "咸阳" },
            { value: "weinan", label: "渭南" },
            { value: "yanan", label: "延安" },
            { value: "hanzhong", label: "汉中" },
            { value: "yulin", label: "榆林" },
            { value: "ankang", label: "安康" },
            { value: "shangluo", label: "商洛" },
            { value: "xixianxinqu", label: "西咸新区" },
          ],
        },
        {
          value: "sichuan",
          label: "四川",
          children: [
            { value: "chengdu", label: "成都" },
            { value: "zigong", label: "自贡" },
            { value: "panzhihua", label: "攀枝花" },
            { value: "luzhou", label: "泸州" },
            { value: "deyang", label: "德阳" },
            { value: "mianyang", label: "绵阳" },
            { value: "guangyuan", label: "广元" },
            { value: "suining", label: "遂宁" },
            { value: "neijiang", label: "内江" },
            { value: "leshan", label: "乐山" },
            { value: "nanchong", label: "南充" },
            { value: "meishan", label: "眉山" },
            { value: "yibin", label: "宜宾" },
            { value: "guangan", label: "广安" },
            { value: "dazhou", label: "达州" },
            { value: "yaan", label: "雅安" },
            { value: "bazhong", label: "巴中" },
            { value: "ziyang", label: "资阳" },
            { value: "aba", label: "阿坝" },
            { value: "ganzi", label: "甘孜" },
            { value: "liangshan", label: "凉山" },
          ],
        },
        {
          value: "shanghai",
          label: "上海",
          children: [{ value: "shanghai", label: "上海" }],
        },
        {
          value: "shanxi",
          label: "山西",
          children: [
            { value: "taiyuan", label: "太原" },
            { value: "datong", label: "大同" },
            { value: "yangquan", label: "阳泉" },
            { value: "zhangzhi", label: "长治" },
            { value: "jincheng", label: "晋城" },
            { value: "shuozhou", label: "朔州" },
            { value: "jinzhong", label: "晋中" },
            { value: "yuncheng", label: "运城" },
            { value: "xinzhou", label: "忻州" },
            { value: "linfen", label: "临汾" },
            { value: "lvliang", label: "吕梁" },
          ],
        },
        {
          value: "shandong",
          label: "山东",
          children: [
            { value: "jinan", label: "济南" },
            { value: "qingdao", label: "青岛" },
            { value: "zibo", label: "淄博" },
            { value: "zaozhuang", label: "枣庄" },
            { value: "dongying", label: "东营" },
            { value: "yantai", label: "烟台" },
            { value: "weifang", label: "潍坊" },
            { value: "jining", label: "济宁" },
            { value: "taian", label: "泰安" },
            { value: "weihai", label: "威海" },
            { value: "rizhao", label: "日照" },
            { value: "laiwu", label: "莱芜" },
            { value: "linyi", label: "临沂" },
            { value: "dezhou", label: "德州" },
            { value: "liaocheng", label: "聊城" },
            { value: "binzhou", label: "滨州" },
            { value: "heze", label: "菏泽" },
          ],
        },
        {
          value: "tianjin",
          label: "天津",
          children: [{ value: "tianjin", label: "天津" }],
        },
        {
          value: "xinjiang",
          label: "新疆",
          children: [
            { value: "wulumuqi", label: "乌鲁木齐" },
            { value: "kelamayi", label: "克拉玛依" },
            { value: "turpan", label: "吐鲁番" },
            { value: "hami", label: "哈密" },
            { value: "changji", label: "昌吉" },
            { value: "boertala", label: "博尔塔拉" },
            { value: "bayinguoleng", label: "巴音郭楞" },
            { value: "akesu", label: "阿克苏" },
            { value: "kezilesu", label: "克孜勒苏" },
            { value: "kashen", label: "喀什" },
            { value: "hetian", label: "和田" },
            { value: "yili", label: "伊犁" },
            { value: "tacheng", label: "塔城" },
            { value: "aletai", label: "阿勒泰" },
            { value: "shihezi", label: "石河子" },
            { value: "aral", label: "阿拉尔" },
            { value: "tumxuk", label: "图木舒克" },
            { value: "wujiaqu", label: "五家渠" },
            { value: "beitun", label: "北屯" },
            { value: "tiemenguan", label: "铁门关" },
            { value: "shuanghe", label: "双河" },
            { value: "kokdala", label: "可克达拉" },
            { value: "kunyu", label: "昆玉" },
          ],
        },
        {
          value: "xizang",
          label: "西藏",
          children: [
            { value: "lasa", label: "拉萨" },
            { value: "rikaze", label: "日喀则" },
            { value: "qamdo", label: "昌都" },
            { value: "nyingchi", label: "林芝" },
            { value: "shannan", label: "山南" },
            { value: "naqu", label: "那曲" },
            { value: "ali", label: "阿里" },
          ],
        },
        {
          value: "yunnan",
          label: "云南",
          children: [
            { value: "kunming", label: "昆明" },
            { value: "qujing", label: "曲靖" },
            { value: "yuxi", label: "玉溪" },
            { value: "baoshan", label: "保山" },
            { value: "zhaotong", label: "昭通" },
            { value: "lijiang", label: "丽江" },
            { value: "puer", label: "普洱" },
            { value: "lincang", label: "临沧" },
            { value: "chuxiong", label: "楚雄" },
            { value: "honghe", label: "红河" },
            { value: "wenshan", label: "文山" },
            { value: "xishuangbanna", label: "西双版纳" },
            { value: "dali", label: "大理" },
            { value: "dehong", label: "德宏" },
            { value: "nujiang", label: "怒江" },
            { value: "diqing", label: "迪庆" },
          ],
        },
        {
          value: "zhejiang",
          label: "浙江",
          children: [
            { value: "hangzhou", label: "杭州" },
            { value: "ningbo", label: "宁波" },
            { value: "wenzhou", label: "温州" },
            { value: "jiaxing", label: "嘉兴" },
            { value: "huzhou", label: "湖州" },
            { value: "shaoxing", label: "绍兴" },
            { value: "jinhua", label: "金华" },
            { value: "quzhou", label: "衢州" },
            { value: "zhoushan", label: "舟山" },
            { value: "taizhou", label: "台州" },
            { value: "lishui", label: "丽水" },
            { value: "zhoushanxinqu", label: "舟山群岛新区" },
          ],
        },
      ],
    };
  },

  mounted() {
    this.modelList = this.defaultModelList;
    // 其他初始化操作
  },

  created() {
    this.getProfile();
  },

  computed: {
    visibleModelList() {
      if (this.showMoreModel) {
        return this.modelList; // 如果显示更多车系，则直接返回全部车系列表
      } else {
        return this.modelList.slice(0, 10); // 否则只返回前15个车系
      }
    },
  },

  methods: {
    //提取排量的数字部分
    extractDisplacement(displacement) {
      const value = parseFloat(displacement);
      return isNaN(value) ? 0 : value;
    },

    selectfun(fun) {
      this.selectedfun = fun;
      switch (fun) {
        case "综合排序":
          this.tableData = this.allTableData;
          this.setPaginations();
          break;
        case "最新上架":
          this.sortDirection = ""; // 取消排序
          this.sortByUpdateTime();
          break;
        case "价格最高":
          this.sortDirection = "desc"; // 设置排序方式为降序
          this.sortByPrice();
          break;
        case "价格最低":
          this.sortDirection = "asc"; // 设置排序方式为升序
          this.sortByPrice();
          break;
        case "车龄最短":
          this.sortDirection = "";
          this.sortByAge();
          break;
        case "里程最少":
          this.sortDirection = "";
          this.sortByMileage();
          break;
        // 添加其他筛选条件的处理
        // ...
      }
    },
    //价格高低排序
    sortByPrice() {
      // 根据排序方式进行升序或降序排序
      this.allTableData.sort((a, b) => {
        if (this.sortDirection === "asc") {
          return a.price - b.price; // 价格升序排列
        }
        if (this.sortDirection === "desc") {
          return b.price - a.price; // 价格降序排列
        }
        return 0;
      });

      this.setPaginations();
    },

    //车龄排序
    sortByAge() {
      this.allTableData.sort((a, b) => {
        // 首先判断是否为未上牌车辆
        if (a.license_time === "未上牌" || b.license_time === "未上牌") {
          if (a.license_time === b.license_time) {
            return 0;
          } else if (a.license_time === "未上牌") {
            return 1; // 未上牌车辆放在最后
          } else {
            return -1; // 未上牌车辆放在最后
          }
        }

        const ageA = this.calculateAge(a.license_time);
        const ageB = this.calculateAge(b.license_time);
        return ageA - ageB;
      });
      this.setPaginations();
    },
    //里程排序
    sortByMileage() {
      this.allTableData.sort((a, b) => {
        const mileageA = this.parseMileage(a.mileage);
        const mileageB = this.parseMileage(b.mileage);
        return mileageA - mileageB;
      });
      this.setPaginations();
    },
    //计算车龄
    calculateAge(licenseTime) {
      const currentDate = new Date();
      const year = parseInt(licenseTime.substr(0, 4));
      const month = parseInt(licenseTime.substr(5, 2)) - 1; // 月份需要减1，因为JavaScript中的月份是从0开始的
      const licenseDate = new Date(year, month);

      const ageInYears = currentDate.getFullYear() - licenseDate.getFullYear();
      if (
        currentDate.getMonth() < licenseDate.getMonth() ||
        (currentDate.getMonth() === licenseDate.getMonth() &&
          currentDate.getDate() < licenseDate.getDate())
      ) {
        return ageInYears - 1;
      }
      return ageInYears;
    },

    //计算里程
    parseMileage(mileage) {
      return parseFloat(mileage.replace(/万公里/g, ""));
    },
    //最新上架
    sortByUpdateTime() {
      this.allTableData.sort((a, b) => {
        const currentTime = new Date().getTime();
        const timeA = new Date(a.update_time).getTime();
        const timeB = new Date(b.update_time).getTime();
        const diffA = currentTime - timeA; // 当前时间减去上架时间的差距
        const diffB = currentTime - timeB;
        return diffB - diffA; // 按照差距排序，差距越小表示越新上架
      });
      this.setPaginations();
    },

    /*/ 输入搜索功能
    search() {
    const keyword = this.searchKeyword.trim(); // 去掉输入关键词两端的空格

    if (keyword !== '') {
      const regex = new RegExp(keyword, 'i'); // 创建不区分大小写的正则表达式

      this.tableData = this.allTableData.filter((item) => {
        // 在每个字段中进行匹配
        return (
          regex.test(item.title) ||
          regex.test(item.brand) ||
          regex.test(item.model) ||
          regex.test(item.license_time) ||
          regex.test(item.mileage) ||
          regex.test(item.transmission) ||
          regex.test(item.emission_standards) ||
          regex.test(item.displacement) ||
          regex.test(item.num_of_transfer) ||
          regex.test(item.location) ||
          regex.test(item.engine) ||
          regex.test(item.color) ||
          regex.test(item.fuel_standard) ||
          regex.test(item.drive_model) ||
          regex.test(item.fuel_type) ||
          regex.test(item.pure_elec_range) ||
          regex.test(item.fast_charge_time) ||
          regex.test(item.battery_capacity) ||
          regex.test(item.slow_charge_time) ||
          (typeof item.update_time === 'string' && regex.test(item.update_time)) ||
          (typeof item.price === 'number' && regex.test(item.price.toString()))
        );
      });
    } else {
      this.tableData = this.allTableData; // 若关键词为空，则展示全部数据
    }

    this.setPaginations(); // 更新分页数据
    },**/

    selectModel(model) {
      this.selectedModel = model;

      if (model === "") {
        // 不限车系，显示原始数据
        this.tableData = this.allTableData;
      } else {
        this.tableData = this.allTableData.filter(
          (item) => item.model === model
        );
      }
    },
    selectBrand(brand) {
      this.selectedBrand = brand;
      this.selectedModel = "";
      console.log(this.selectedBrand, this.selectedPrice, this.selectedColor);
      // 根据选择的品牌更新车辆数据
      if (brand === "") {
        // 不限品牌，显示原始数据
        this.tableData = this.allTableData;
      } else {
        this.tableData = this.allTableData.filter(
          (item) => item.brand === brand
        );
      }
      // 根据选择的品牌更新车系选项
      if (brand === "") {
        // 不限品牌，显示原始选项
        this.modelList = [
          "奥迪A6L",
          "宝马5系",
          "宝马3系",
          "奔驰C级",
          "奔驰E级",
          "高尔夫",
          "迈腾",
          "速腾",
          "朗逸",
          "雅阁",
          "轩逸",
          "哈弗H6",
          "福克斯",
        ];
      } else if (brand === "大众") {
        // 大众品牌对应的车系列表
        this.modelList = [
          "C-TREK蔚领",
          "ID.4 CROZZ",
          "ID.4 X",
          "ID.6 CROZZ",
          "ID.6 X",
          "Passat",
          "Passat领驭",
          "Polo",
          "T-ROC探歌",
          "Tiguan",
          "一汽-大众CC",
          "凌渡",
          "凯路威",
          "夏朗",
          "大众CC",
          "大众Eos",
          "大众ID.3",
          "大众up!",
          "威然",
          "宝来",
          "宝来·纯电",
          "宝来经典",
          "尚酷",
          "帕萨特",
          "帕萨特新能源",
          "开迪",
          "捷达",
          "探岳",
          "探岳GTE插电混动",
          "探岳X",
          "探影",
          "揽境",
          "揽巡",
          "朗境",
          "朗行",
          "朗逸",
          "朗逸纯电",
          "桑塔纳",
          "桑塔纳志俊",
          "桑塔纳经典",
          "甲壳虫",
          "蔚揽",
          "蔚揽新能源",
          "辉昂",
          "辉腾",
          "迈特威",
          "迈腾",
          "迈腾(进口)",
          "迈腾GTE插电混动",
          "途安",
          "途岳",
          "途岳新能源",
          "途昂",
          "途昂X",
          "途观",
          "途观L",
          "途观L新能源",
          "途观X",
          "途铠",
          "途锐",
          "途锐新能源",
          "速腾",
          "高尔",
          "高尔夫",
          "高尔夫(进口)",
          "高尔夫·嘉旅",
          "高尔夫·纯电",
          "高尔夫新能源(进口)",
        ];
      } else if (brand === "本田") {
        // 本田品牌对应的车系列表
        this.modelList = [
          "LIFE",
          "ZR-V 致在",
          "e:NP1 极湃1",
          "享域",
          "冠道",
          "凌派",
          "哥瑞",
          "型格",
          "奥德赛",
          "思域",
          "思域(进口)",
          "思迪",
          "思铂睿",
          "时韵",
          "本田CR-V",
          "本田CR-V新能源",
          "本田CR-Z",
          "本田UR-V",
          "本田XR-V",
          "本田e:NS1",
          "杰德",
          "歌诗图",
          "皓影",
          "皓影新能源",
          "竞瑞",
          "缤智",
          "艾力绅",
          "英仕派",
          "里程",
          "锋范",
          "锋范经典",
          "雅阁",
          "飞度",
        ];
      } else if (brand === "奔驰") {
        this.modelList = [
          "AMG GT",
          "Sprinter",
          "凌特",
          "唯雅诺",
          "唯雅诺(进口)",
          "奔驰A级",
          "奔驰A级(进口)",
          "奔驰A级AMG",
          "奔驰A级AMG(进口)",
          "奔驰B级",
          "奔驰CLA",
          "奔驰CLA AMG",
          "奔驰CLK级",
          "奔驰CLS",
          "奔驰CLS AMG",
          "奔驰CL级",
          "奔驰C级",
          "奔驰C级(进口)",
          "奔驰C级AMG",
          "奔驰C级新能源",
          "奔驰EQA",
          "奔驰EQB",
          "奔驰EQC",
          "奔驰EQE",
          "奔驰EQS",
          "奔驰E级",
          "奔驰E级(进口)",
          "奔驰E级AMG",
          "奔驰E级新能源",
          "奔驰GLA",
          "奔驰GLA AMG",
          "奔驰GLA(进口)",
          "奔驰GLB",
          "奔驰GLB AMG",
          "奔驰GLC",
          "奔驰GLC AMG",
          "奔驰GLC轿跑",
          "奔驰GLC轿跑 AMG",
          "奔驰GLE",
          "奔驰GLE AMG",
          "奔驰GLE新能源",
          "奔驰GLE轿跑",
          "奔驰GLE轿跑 AMG",
          "奔驰GLE轿跑新能源",
          "奔驰GLK级",
          "奔驰GLK级(进口)",
          "奔驰GLS",
          "奔驰GLS AMG",
          "奔驰GL级",
          "奔驰GL级AMG",
          "奔驰G级",
          "奔驰G级AMG",
          "奔驰M级",
          "奔驰M级AMG",
          "奔驰R级",
          "奔驰SLC",
          "奔驰SLK级",
          "奔驰SLS级AMG",
          "奔驰SL级",
          "奔驰SL级AMG",
          "奔驰S级",
          "奔驰S级AMG",
          "奔驰S级新能源",
          "奔驰V级",
        ];
      } else if (brand === "宝马") {
        this.modelList = [
          "宝马1系",
          "宝马1系(进口)",
          "宝马1系M",
          "宝马2系",
          "宝马2系多功能旅行车",
          "宝马2系旅行车",
          "宝马2系旅行车(进口)",
          "宝马3系",
          "宝马3系(进口)",
          "宝马3系GT",
          "宝马4系",
          "宝马5系",
          "宝马5系(进口)",
          "宝马5系GT",
          "宝马5系新能源",
          "宝马6系",
          "宝马6系GT",
          "宝马7系",
          "宝马8系",
          "宝马M2",
          "宝马M3",
          "宝马M4",
          "宝马M5",
          "宝马M6",
          "宝马M8",
          "宝马X1",
          "宝马X1(进口)",
          "宝马X1新能源",
          "宝马X2",
          "宝马X2(进口)",
          "宝马X3",
          "宝马X3 M",
          "宝马X3(进口)",
          "宝马X4",
          "宝马X4 M",
          "宝马X5",
          "宝马X5 M",
          "宝马X5(进口)",
          "宝马X5新能源(进口)",
          "宝马X6",
          "宝马X6 M",
          "宝马X7",
          "宝马Z4",
          "宝马i3",
          "宝马i3(进口)",
          "宝马i4",
          "宝马i7",
          "宝马i8",
          "宝马iX",
          "宝马iX3",
        ];
      } else if (brand === "丰田") {
        this.modelList = [
          "卡罗拉",
          "雷凌",
          "汉兰达",
          "普拉多",
          "凯美瑞",
          "柯斯达",
          "锐志",
          "兰德酷路泽",
          "RAV4荣放",
          "威驰",
          "RAV4荣放EV",
          "考斯特",
          "凯美瑞新能源",
          "雅力士",
          "亚洲龙",
          "rav4荣放黑色限量版",
          "C-HR",
          "皇冠",
          "4Runner",
          "FJ酷路泽",
        ];
      } else if (brand === "奥迪") {
        this.modelList = [
          "奥迪A1",
          "奥迪A3",
          "奥迪A3(进口)",
          "奥迪A4",
          "奥迪A4(进口)",
          "奥迪A4L",
          "奥迪A5",
          "奥迪A6",
          "奥迪A6(进口)",
          "奥迪A6L",
          "奥迪A6L新能源",
          "奥迪A7",
          "奥迪A7L",
          "奥迪A8",
          "奥迪A8新能源",
          "奥迪Q2L",
          "奥迪Q2L e-tron",
          "奥迪Q3",
          "奥迪Q3 Sportback",
          "奥迪Q3(进口)",
          "奥迪Q4 e-tron",
          "奥迪Q5",
          "奥迪Q5 e-tron",
          "奥迪Q5(进口)",
          "奥迪Q5L",
          "奥迪Q5L Sportback",
          "奥迪Q6",
          "奥迪Q7",
          "奥迪Q7新能源",
          "奥迪Q8",
          "奥迪R8",
          "奥迪RS 3",
          "奥迪RS 4",
          "奥迪RS 5",
          "奥迪RS 6",
          "奥迪RS 7",
          "奥迪RS Q8",
          "奥迪RS e-tron GT",
          "奥迪S3",
          "奥迪S4",
          "奥迪S5",
          "奥迪S6",
          "奥迪S7",
          "奥迪S8",
          "奥迪SQ5",
          "奥迪TT",
          "奥迪TT RS",
          "奥迪TTS",
          "奥迪e-tron",
          "奥迪e-tron(进口)",
        ];
      } else if (brand === "别克") {
        this.modelList = [
          "VELITE 5",
          "世纪",
          "凯越",
          "别克GL6",
          "别克GL8",
          "君威",
          "君越",
          "威朗",
          "微蓝6",
          "微蓝7",
          "昂扬",
          "昂科威",
          "昂科拉",
          "昂科拉GX",
          "昂科旗",
          "昂科雷",
          "林荫大道",
          "英朗",
          "荣御",
          "阅朗",
        ];
      } else if (brand === "福特") {
        this.modelList = [
          "EVOS",
          "Mustang",
          "Ranger(进口)",
          "全顺",
          "嘉年华",
          "嘉年华(进口)",
          "探险者",
          "探险者(进口)",
          "撼路者",
          "新世代全顺",
          "福克斯",
          "福克斯(进口)",
          "福克斯Active",
          "福特E350",
          "福特F-150",
          "福特电马",
          "福睿斯",
          "经典全顺",
          "翼搏",
          "翼虎",
          "致胜",
          "蒙迪欧",
          "蒙迪欧-致胜",
          "蒙迪欧新能源",
          "途睿欧",
          "金牛座",
          "锐界",
          "锐界(进口)",
          "锐际",
          "锐际(进口)",
          "领界",
          "领睿",
          "领裕",
          "麦柯斯",
        ];
      } else if (brand === "吉利汽车") {
        this.modelList = [
          "博瑞",
          "博瑞新能源",
          "博越",
          "博越L",
          "吉利EC8",
          "吉利GC7",
          "吉利GX2",
          "吉利GX7",
          "吉利ICON",
          "吉利SC3",
          "吉利SX7",
          "嘉际",
          "嘉际新能源",
          "帝豪",
          "帝豪GL",
          "帝豪GL新能源",
          "帝豪GS",
          "帝豪GSe",
          "帝豪L",
          "帝豪L Hi·P",
          "帝豪S",
          "帝豪新能源",
          "星瑞",
          "星越",
          "星越L",
          "星越L增程电动版",
          "星越S",
          "星越新能源",
          "海景",
          "熊猫",
          "熊猫mini",
          "经典帝豪",
          "缤瑞",
          "缤越",
          "缤越新能源",
          "自由舰",
          "英伦TX4",
          "豪情SUV",
          "豪越",
          "豪越L",
          "远景",
          "远景S1",
          "远景X1",
          "远景X3",
          "远景X6",
          "金刚",
          "金刚财富",
          "金鹰",
        ];
      } else if (brand === "哈弗") {
        this.modelList = [
          "哈弗F5",
          "哈弗F7",
          "哈弗F7x",
          "哈弗H1",
          "哈弗H2",
          "哈弗H2s",
          "哈弗H3",
          "哈弗H4",
          "哈弗H5经典",
          "哈弗H6",
          "哈弗H6 Coupe",
          "哈弗H6S",
          "哈弗H6新能源",
          "哈弗H7",
          "哈弗H8",
          "哈弗H9",
          "哈弗M6",
          "哈弗初恋",
          "哈弗大狗",
          "哈弗神兽",
          "哈弗赤兔",
          "哈弗酷狗",
        ];
      } else if (brand === "比亚迪") {
        this.modelList = [
          "元",
          "元PLUS",
          "元Pro",
          "元新能源",
          "唐",
          "唐新能源",
          "宋",
          "宋MAX",
          "宋MAX新能源",
          "宋PLUS",
          "宋PLUS新能源",
          "宋Pro",
          "宋Pro新能源",
          "宋新能源",
          "思锐",
          "护卫舰07",
          "比亚迪D1",
          "比亚迪F0",
          "比亚迪F3",
          "比亚迪F3R",
          "比亚迪F6",
          "比亚迪G3",
          "比亚迪G3R",
          "比亚迪G5",
          "比亚迪G6",
          "比亚迪L3",
          "比亚迪M6",
          "比亚迪S2",
          "比亚迪S6",
          "比亚迪S7",
          "比亚迪e1",
          "比亚迪e2",
          "比亚迪e3",
          "比亚迪e5",
          "比亚迪e6",
          "比亚迪e9",
          "汉",
          "海豚",
          "海豹",
          "秦",
          "秦PLUS",
          "秦Pro",
          "秦Pro新能源",
          "秦新能源",
          "速锐",
          "驱逐舰05",
        ];
      } else if (brand === "长安") {
        this.modelList = [
          "凌轩",
          "奔奔",
          "奔奔EV",
          "奔奔MINI",
          "悦翔",
          "悦翔V3",
          "悦翔V5",
          "悦翔V7",
          "睿骋",
          "睿骋CC",
          "逸动",
          "逸动DT",
          "逸动XT",
          "逸动新能源",
          "逸达",
          "锐程CC",
          "锐程PLUS",
          "长安CS15",
          "长安CS15EV",
          "长安CS35",
          "长安CS35PLUS",
          "长安CS55",
          "长安CS55PLUS",
          "长安CS55纯电版",
          "长安CS75",
          "长安CS75 PLUS",
          "长安CS75新能源",
          "长安CS85 COUPE",
          "长安CS95",
          "长安CX20",
          "长安Lumin",
          "长安UNI-K",
          "长安UNI-K 智电iDD",
          "长安UNI-T",
          "长安UNI-V",
          "长安UNI-V 智电iDD",
          "长安奔奔E-Star",
          "长安新能源E-Pro",
        ];
      } else if (brand === "马自达") {
        this.modelList = [
          "ATENZA",
          "睿翼",
          "阿特兹",
          "马自达2",
          "马自达2劲翔",
          "马自达3",
          "马自达3 昂克赛拉",
          "马自达3(进口)",
          "马自达3星骋",
          "马自达5",
          "马自达6",
          "马自达8",
          "马自达CX-3",
          "马自达CX-30",
          "马自达CX-30 EV",
          "马自达CX-4",
          "马自达CX-5",
          "马自达CX-5(进口)",
          "马自达CX-7",
          "马自达CX-7(进口)",
          "马自达CX-8",
          "马自达MX-5",
          "马自达RX-8",
        ];
      } else if (brand === "红旗") {
        this.modelList = [
          "红旗",
          "红旗E-HS3",
          "红旗E-HS9",
          "红旗E-QM5",
          "红旗H5",
          "红旗H5经典",
          "红旗H6",
          "红旗H7",
          "红旗H9",
          "红旗HQ9",
          "红旗HS5",
          "红旗HS7",
          "红旗盛世",
        ];
      } else if (brand === "Jeep") {
        this.modelList = [
          "北京JEEP",
          "大切诺基",
          "大切诺基 SRT",
          "大切诺基(进口)",
          "大指挥官",
          "大指挥官PHEV",
          "指南者",
          "指南者(进口)",
          "指挥官",
          "指挥官PHEV",
          "指挥官经典",
          "牧马人",
          "牧马人新能源",
          "自由侠",
          "自由光",
          "自由光(进口)",
          "自由客",
          "角斗士",
        ];
      } else if (brand === "捷豹") {
        this.modelList = [
          "捷豹E-PACE",
          "捷豹F-PACE",
          "捷豹F-TYPE",
          "捷豹I-PACE",
          "捷豹S-TYPE",
          "捷豹X-TYPE",
          "捷豹XE",
          "捷豹XEL",
          "捷豹XF",
          "捷豹XFL",
          "捷豹XJ",
          "捷豹XK",
        ];
      } else if (brand === "MINI") {
        this.modelList = [
          "MINI",
          "MINI CLUBMAN",
          "MINI COUNTRYMAN",
          "MINI COUPE",
          "MINI JCW",
          "MINI JCW CLUBMAN",
          "MINI JCW COUNTRYMAN",
          "MINI JCW COUPE",
          "MINI JCW PACEMAN",
          "MINI PACEMAN",
          "MINI ROADSTER",
        ];
      } else if (brand === "一汽") {
        this.modelList = [
          "一汽蓝舰H6",
          "佳宝V80",
          "夏利",
          "夏利N5",
          "夏利N7",
          "威乐",
          "威姿",
          "威志",
          "威志V2",
          "威志V5",
          "森雅M80",
          "森雅R7",
          "森雅R9",
          "森雅S80",
          "骏派A50",
          "骏派A70",
          "骏派CX65",
          "骏派D60",
        ];
      } else if (brand === "三菱") {
        this.modelList = [
          "ASX劲炫(进口)",
          "LANCER",
          "三菱戈蓝",
          "伊柯丽斯",
          "劲炫ASX",
          "君阁",
          "奕歌",
          "帕杰罗",
          "帕杰罗(进口)",
          "帕杰罗·劲畅",
          "帕杰罗·劲畅(进口)",
          "格蓝迪",
          "欧蓝德",
          "欧蓝德(进口)",
          "欧蓝德经典",
          "翼神",
          "菱绅",
          "蓝瑟",
          "阿图柯AIRTREK",
        ];
      } else if (brand === "东南") {
        this.modelList = [
          "V3菱悦",
          "V5菱致",
          "V6菱仕",
          "东南A5翼舞",
          "东南DX3",
          "东南DX3新能源",
          "东南DX5",
          "东南DX7",
          "东南DX8S",
          "得利卡",
          "菱帅",
        ];
      } else if (brand === "东风") {
        this.modelList = [
          "俊风E11K",
          "俊风E17",
          "俊风ER30",
          "帅客",
          "帅客新能源",
          "帕拉索",
          "御轩",
          "御风P16",
          "锐骐",
          "锐骐",
        ];
      } else if (brand === "东风风神") {
        this.modelList = [
          "东风A9",
          "东风风神A30",
          "东风风神A60",
          "东风风神AX3",
          "东风风神AX4",
          "东风风神AX5",
          "东风风神AX7",
          "东风风神E70",
          "东风风神EX1",
          "东风风神H30",
          "东风风神L60",
          "东风风神S30",
          "奕炫",
          "奕炫GS",
          "奕炫MAX",
          "皓极",
        ];
      } else if (brand === "东风风行") {
        this.modelList = [
          "景逸",
          "景逸S50",
          "景逸SUV",
          "景逸X3",
          "景逸X5",
          "景逸X6",
          "景逸XV",
          "菱智",
          "菱智M5EV",
          "菱智PLUS",
          "风行CM7",
          "风行F600",
          "风行M7",
          "风行S500",
          "风行S50EV",
          "风行SX6",
          "风行T5",
          "风行T5 EVO",
          "风行T5L",
          "风行游艇",
          "风行雷霆",
        ];
      } else if (brand === "中华") {
        this.modelList = [
          "中华H230",
          "中华H3",
          "中华H330",
          "中华H530",
          "中华V3",
          "中华V5",
          "中华V6",
          "中华V7",
          "中华尊驰",
          "中华酷宝",
          "中华骏捷",
          "中华骏捷FRV",
          "中华骏捷FSV",
        ];
      } else if (brand === "五菱汽车") {
        this.modelList = [
          "PN货车",
          "五菱730",
          "五菱Air ev晴空",
          "五菱EV50",
          "五菱NanoEV",
          "五菱之光",
          "五菱之光V",
          "五菱之光小卡",
          "五菱佳辰",
          "五菱凯捷",
          "五菱宏光",
          "五菱宏光PLUS",
          "五菱宏光S3",
          "五菱宏光V",
          "五菱征程",
          "五菱征程经典",
          "五菱征途",
          "五菱星辰",
          "五菱星驰",
          "五菱缤果",
          "五菱荣光",
          "五菱荣光EV",
          "五菱荣光S",
          "五菱荣光V",
          "五菱荣光小卡",
          "五菱荣光新卡",
          "宏光MINIEV",
        ];
      } else if (brand === "保时捷") {
        this.modelList = [
          "918 Spyder",
          "Boxster",
          "Cayenne",
          "Cayenne新能源",
          "Cayman",
          "Macan",
          "Panamera",
          "Panamera新能源",
          "Taycan",
          "保时捷718",
          "保时捷911",
        ];
      } else if (brand === "众泰") {
        this.modelList = [
          "云100",
          "众泰2008",
          "众泰5008",
          "众泰E200",
          "众泰SR7",
          "众泰SR9",
          "众泰T200",
          "众泰T300",
          "众泰T500",
          "众泰T600",
          "众泰T600 Coupe",
          "众泰T700",
          "众泰T800",
          "众泰Z100",
          "众泰Z300",
          "众泰Z360",
          "众泰Z500",
          "众泰Z500新能源",
          "众泰Z560",
          "众泰Z700",
          "大迈X5",
          "大迈X7",
          "芝麻",
        ];
      } else if (brand === "凯翼") {
        this.modelList = [
          "凯翼C3",
          "凯翼C3R",
          "凯翼E3",
          "凯翼V3",
          "凯翼X3",
          "凯翼X5",
          "凯翼昆仑",
          "炫界",
          "炫界Pro",
          "炫界Pro EV",
        ];
      } else if (brand === "凯迪拉克") {
        this.modelList = [
          "LYRIQ锐歌",
          "SLS赛威",
          "凯迪拉克ATS(进口)",
          "凯迪拉克ATS-L",
          "凯迪拉克CT4",
          "凯迪拉克CT5",
          "凯迪拉克CT6",
          "凯迪拉克CT6 PLUG-IN",
          "凯迪拉克CTS",
          "凯迪拉克CTS(进口)",
          "凯迪拉克SRX",
          "凯迪拉克XLR",
          "凯迪拉克XT4",
          "凯迪拉克XT5",
          "凯迪拉克XT6",
          "凯迪拉克XTS",
          "凯雷德ESCALADE",
        ];
      } else if (brand === "名爵") {
        this.modelList = [
          "MG MULAN",
          "MG ONE",
          "MG5天蝎座",
          "MG7",
          "MG领航",
          "MG领航新能源",
          "名爵3",
          "名爵3SW",
          "名爵5",
          "名爵6",
          "名爵6新能源",
          "名爵EZS纯电动",
          "名爵HS",
          "名爵HS新能源",
          "名爵ZS",
          "锐腾",
          "锐行",
        ];
      } else if (brand === "启辰") {
        this.modelList = [
          "启辰D50",
          "启辰D60",
          "启辰D60EV",
          "启辰M50V",
          "启辰R30",
          "启辰R50",
          "启辰R50X",
          "启辰T60",
          "启辰T60EV",
          "启辰T70",
          "启辰T70X",
          "启辰T90",
          "启辰e30",
          "启辰大V",
          "启辰星",
          "晨风",
        ];
      } else if (brand === "奇瑞") {
        this.modelList = [
          "奇瑞A1",
          "奇瑞A3",
          "奇瑞A5",
          "奇瑞E3",
          "奇瑞E5",
          "奇瑞QQ",
          "奇瑞QQ3",
          "奇瑞X1",
          "旗云2",
          "旗云3",
          "欧萌达",
          "瑞虎",
          "瑞虎3",
          "瑞虎3x",
          "瑞虎5",
          "瑞虎5x",
          "瑞虎7",
          "瑞虎7 PLUS",
          "瑞虎8",
          "瑞虎8 PLUS",
          "瑞虎8 PLUS鲲鹏e+",
          "瑞虎8 PRO",
          "瑞虎9",
          "艾瑞泽3",
          "艾瑞泽5",
          "艾瑞泽5 GT",
          "艾瑞泽5 PLUS",
          "艾瑞泽7",
          "艾瑞泽7e",
          "艾瑞泽8",
          "艾瑞泽GX",
          "艾瑞泽M7",
          "风云2",
          "QQ冰淇淋",
          "大蚂蚁",
          "奇瑞eQ",
          "奇瑞无界Pro",
          "小蚂蚁",
          "瑞虎3xe",
          "瑞虎e",
          "艾瑞泽5e",
          "艾瑞泽e",
        ];
      } else if (brand === "开瑞") {
        this.modelList = [
          "优优",
          "优优EV",
          "优劲",
          "优劲EV",
          "优胜2代",
          "优雅",
          "开瑞K50",
          "开瑞K50EV",
          "开瑞K60",
          "开瑞K60EV",
          "杰虎",
          "江豚",
          "海豚EV",
        ];
      } else if (brand === "思皓") {
        this.modelList = [
          "思皓A5",
          "思皓E20X",
          "思皓E50A",
          "思皓QX",
          "思皓X4",
          "思皓X8",
          "思皓曜",
          "花仙子",
        ];
      } else if (brand === "斯柯达") {
        this.modelList = [
          "Yeti",
          "昊锐",
          "明锐",
          "昕动",
          "昕锐",
          "晶锐",
          "柯珞克",
          "柯米克",
          "柯迪亚克",
          "柯迪亚克GT",
          "速尊",
          "速派",
          "速派(进口)",
        ];
      } else if (brand === "日产") {
        this.modelList = [
          "ARIYA艾睿雅",
          "公爵王",
          "劲客",
          "天籁",
          "奇骏",
          "奇骏·荣耀",
          "帕拉丁",
          "日产350Z",
          "日产370Z",
          "日产D22",
          "日产GT-R",
          "日产NV200",
          "日产ZN厢式车",
          "楼兰",
          "玛驰",
          "碧莲",
          "纳瓦拉",
          "蓝鸟",
          "蓝鸟经典",
          "西玛",
          "贵士",
          "轩逸",
          "轩逸·纯电",
          "逍客",
          "途乐",
          "途达",
          "阳光",
          "颐达",
          "风度",
          "风雅",
          "骊威",
          "骏逸",
          "骐达TIIDA",
        ];
      } else if (brand === "林肯") {
        this.modelList = [
          "冒险家",
          "冒险家新能源",
          "城市",
          "林肯MKC",
          "林肯MKT",
          "林肯MKX",
          "林肯MKZ",
          "林肯Z",
          "林肯大陆",
          "航海家",
          "航海家(进口)",
          "领航员",
          "飞行家",
          "飞行家(进口)",
        ];
      } else if (brand === "标致") {
        this.modelList = [
          "标致2008",
          "标致206",
          "标致207",
          "标致207(进口)",
          "标致3008",
          "标致3008(进口)",
          "标致301",
          "标致307",
          "标致307(进口)",
          "标致308",
          "标致308(进口)",
          "标致308S",
          "标致4008",
          "标致4008(进口)",
          "标致408",
          "标致5008",
          "标致508",
          "标致508L新能源",
          "标致RCZ",
          "标致e2008",
        ];
      } else if (brand === "江淮") {
        this.modelList = [
          "同悦",
          "和悦",
          "和悦A13",
          "和悦A30",
          "嘉悦A5",
          "嘉悦X4",
          "嘉悦X7",
          "悦悦",
          "星锐",
          "江淮T6",
          "江淮T8",
          "江淮V7",
          "江淮iC5",
          "江淮iEV",
          "江淮iEV6E",
          "江淮iEV6S",
          "江淮iEV7",
          "江淮iEV7S",
          "江淮iEVS4",
          "瑞铃",
          "瑞风",
          "瑞风A60",
          "瑞风M2",
          "瑞风M5",
          "瑞风R3",
          "瑞风S2",
          "瑞风S3",
          "瑞风S4",
          "瑞风S5",
          "瑞风S7",
          "瑞鹰",
          "瑞风M3",
          "瑞风M4",
        ];
      } else if (brand === "沃尔沃") {
        this.modelList = [
          "XC Classic",
          "沃尔沃C30",
          "沃尔沃C40",
          "沃尔沃C70",
          "沃尔沃S40",
          "沃尔沃S60",
          "沃尔沃S60(进口)",
          "沃尔沃S60新能源",
          "沃尔沃S80",
          "沃尔沃S80L",
          "沃尔沃S90",
          "沃尔沃S90(进口)",
          "沃尔沃S90新能源",
          "沃尔沃V40",
          "沃尔沃V60",
          "沃尔沃V90",
          "沃尔沃XC40",
          "沃尔沃XC40新能源",
          "沃尔沃XC60",
          "沃尔沃XC60(进口)",
          "沃尔沃XC60新能源",
          "沃尔沃XC90",
          "沃尔沃XC90新能源",
        ];
      } else if (brand === "海马") {
        this.modelList = [
          "丘比特",
          "普力马",
          "欢动",
          "海福星",
          "海马3",
          "海马7X",
          "海马8S",
          "海马M3",
          "海马M6",
          "海马S5",
          "海马S5青春版",
          "海马S7",
          "海马V70",
          "海马爱尚EV",
          "海马骑士",
          "福仕达鸿达",
          "福美来",
          "福美来F7",
          "福美来MPV",
        ];
      } else if (brand === "法拉利") {
        this.modelList = [
          "California T",
          "F12berlinetta",
          "GTC4Lusso",
          "LaFerrari",
          "Portofino",
          "Roma",
          "SF90",
          "法拉利296",
          "法拉利458",
          "法拉利488",
          "法拉利599",
          "法拉利612",
          "法拉利812",
          "法拉利F430",
          "法拉利F8",
          "法拉利FF",
        ];
      } else if (brand === "玛莎拉蒂") {
        this.modelList = [
          "Coupe",
          "Ghibli",
          "GranCabrio",
          "GranTurismo",
          "Grecale格雷嘉",
          "Levante",
          "总裁",
          "玛莎拉蒂MC20",
        ];
      } else if (brand === "现代") {
        this.modelList = [
          "ENCINO 昂希诺",
          "H-1辉翼",
          "Veloster飞思",
          "伊兰特",
          "劳恩斯",
          "劳恩斯-酷派",
          "北京现代i30",
          "北京现代ix25",
          "北京现代ix35",
          "名图",
          "名驭",
          "帕里斯帝",
          "库斯途",
          "悦动",
          "悦纳",
          "悦纳RV",
          "捷恩斯",
          "朗动",
          "格越",
          "瑞奕",
          "瑞纳",
          "索纳塔",
          "索纳塔插电混动",
          "维拉克斯",
          "胜达",
          "胜达(进口)",
          "胜达经典",
          "菲斯塔",
          "菲斯塔纯电动",
          "途胜",
          "酷派",
          "雅尊",
          "雅科仕",
          "雅绅特",
          "领动",
          "领动插电混动",
        ];
      } else if (brand === "福田") {
        this.modelList = [
          "伽途ix5",
          "图雅诺",
          "大将军G9",
          "大将军G9SUV",
          "拓陆者",
          "祥菱M",
          "祥菱V",
          "福田风景",
          "萨普",
          "萨瓦纳",
          "蒙派克E",
          "风景G5",
          "风景G7",
          "风景G9",
          "风景V5新能源",
        ];
      } else if (brand === "荣威") {
        this.modelList = [
          "科莱威CLEVER",
          "荣威350",
          "荣威360",
          "荣威550",
          "荣威750",
          "荣威950",
          "荣威Ei5",
          "荣威MARVEL X",
          "荣威RX3",
          "荣威RX5",
          "荣威RX5 MAX",
          "荣威RX5 eMAX",
          "荣威RX5新能源",
          "荣威RX8",
          "荣威RX9",
          "荣威W5",
          "荣威e50",
          "荣威e550",
          "荣威e950",
          "荣威i5",
          "荣威i6",
          "荣威i6 MAX",
          "荣威i6 MAX新能源",
          "荣威i6新能源",
          "荣威iMAX8",
        ];
      } else if (brand === "蔚来") {
        this.modelList = [
          "蔚来EC6",
          "蔚来ES6",
          "蔚来ES7",
          "蔚来ES8",
          "蔚来ET5",
          "蔚来ET5T",
          "蔚来ET7",
        ];
      } else if (brand === "起亚") {
        this.modelList = [
          "KX3傲跑",
          "佳乐",
          "凯尊",
          "凯绅",
          "千里马",
          "奕跑",
          "智跑",
          "欧菲莱斯",
          "焕驰",
          "狮跑",
          "狮铂拓界",
          "福瑞迪",
          "秀尔",
          "索兰托",
          "赛拉图",
          "起亚K2",
          "起亚K3",
          "起亚K3S",
          "起亚K4",
          "起亚K5",
          "起亚K5新能源",
          "起亚KX5",
          "起亚KX7",
          "起亚VQ",
          "速迈",
          "锐欧",
          "霸锐",
        ];
      } else if (brand === "迈凯伦") {
        this.modelList = [
          "KX3傲跑",
          "佳乐",
          "凯尊",
          "凯绅",
          "千里马",
          "奕跑",
          "智跑",
          "欧菲莱斯",
          "焕驰",
          "狮跑",
          "狮铂拓界",
          "福瑞迪",
          "秀尔",
          "索兰托",
          "赛拉图",
          "起亚K2",
          "起亚K3",
          "起亚K3S",
          "起亚K4",
          "起亚K5",
          "起亚K5新能源",
          "起亚KX5",
          "起亚KX7",
          "起亚VQ",
          "速迈",
          "锐欧",
          "霸锐",
        ];
      } else if (brand === "金杯") {
        this.modelList = [
          "华晨金杯750",
          "小海狮X30",
          "小海狮X30 CNG",
          "新海狮EV",
          "新海狮S",
          "新海狮X30L",
          "智尚S30",
          "金杯T30",
          "金杯T32",
          "金杯T50",
          "金杯大海狮",
          "金杯快运",
          "金杯海狮",
          "金杯海狮王",
          "阁瑞斯",
        ];
      } else if (brand === "长城") {
        this.modelList = [
          "嘉誉",
          "炫丽",
          "炮",
          "酷熊",
          "金刚炮",
          "金迪尔",
          "长城C20R",
          "长城C30",
          "长城C50",
          "长城M1",
          "长城M2",
          "长城M4",
          "风骏5",
          "风骏6",
          "风骏7",
        ];
      } else if (brand === "雪佛兰") {
        this.modelList = [
          "乐风",
          "乐风RV",
          "乐骋",
          "创界",
          "创酷",
          "开拓者",
          "探界者",
          "斯帕可",
          "星迈罗",
          "景程",
          "沃兰多",
          "爱唯欧",
          "畅巡",
          "科尔维特",
          "科帕奇",
          "科帕奇(进口)",
          "科沃兹",
          "科迈罗",
          "科鲁兹",
          "科鲁泽",
          "赛欧",
          "迈锐宝",
          "迈锐宝XL",
        ];
      } else if (brand === "雪铁龙") {
        this.modelList = [
          "C4 PICASSO",
          "C4世嘉",
          "世嘉",
          "云逸 C4 AIRCROSS",
          "凡尔赛C5 X",
          "凯旋",
          "天逸 C5 AIRCROSS",
          "富康",
          "毕加索",
          "爱丽舍",
          "雪铁龙C2",
          "雪铁龙C3-XR",
          "雪铁龙C4",
          "雪铁龙C4 Aircross(进口)",
          "雪铁龙C4L",
          "雪铁龙C5",
          "雪铁龙C5(进口)",
          "雪铁龙C6",
        ];
      } else if (brand === "雷克萨斯") {
        this.modelList = [
          "雷克萨斯CT",
          "雷克萨斯ES",
          "雷克萨斯GS",
          "雷克萨斯GX",
          "雷克萨斯IS",
          "雷克萨斯LC",
          "雷克萨斯LM",
          "雷克萨斯LS",
          "雷克萨斯LX",
          "雷克萨斯NX",
          "雷克萨斯NX新能源",
          "雷克萨斯RC",
          "雷克萨斯RC F",
          "雷克萨斯RX",
          "雷克萨斯RX经典",
          "雷克萨斯RZ",
          "雷克萨斯SC",
          "雷克萨斯UX",
          "雷克萨斯UX新能源",
        ];
      } else if (brand === "领克") {
        this.modelList = [
          "领克01",
          "领克01新能源",
          "领克02",
          "领克02 Hatchback",
          "领克02新能源",
          "领克03",
          "领克03新能源",
          "领克05",
          "领克05新能源",
          "领克06",
          "领克06新能源",
          "领克09",
          "领克09新能源",
        ];
      } else if (brand === "魏牌") {
        this.modelList = [
          "拿铁DHT",
          "拿铁DHT-PHEV",
          "摩卡",
          "摩卡DHT-PHEV",
          "玛奇朵DHT",
          "玛奇朵DHT-PHEV",
          "魏牌 P8",
          "魏牌 VV5",
          "魏牌 VV6",
          "魏牌 VV7",
          "魏牌 VV7 GT",
          "魏牌 VV7新能源",
        ];
      } else if (brand === "黄海") {
        this.modelList = ["大柴神", "旗胜V3", "黄海N7", "黄海·大牛"];
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
      if (price === "不限") {
        this.selectedPrice = "";
        // 不限价格，显示原始数据
        this.tableData = this.allTableData;
        return;
      }
      this.selectedPrice = price;
      switch (price) {
        case "3万以下":
          this.search_data.minPrice = 0;
          this.search_data.maxPrice = 3;
          break;
        case "3-5万":
          this.search_data.minPrice = 3;
          this.search_data.maxPrice = 5;
          break;
        case "5-8万":
          this.search_data.minPrice = 5;
          this.search_data.maxPrice = 8;
          break;
        case "8-10万":
          this.search_data.minPrice = 8;
          this.search_data.maxPrice = 10;
          break;
        case "10-15万":
          this.search_data.minPrice = 10;
          this.search_data.maxPrice = 15;
          break;
        case "15-20万":
          this.search_data.minPrice = 15;
          this.search_data.maxPrice = 20;
          break;
        case "20-30万":
          this.search_data.minPrice = 20;
          this.search_data.maxPrice = 30;
          break;
        case "30-50万":
          this.search_data.minPrice = 30;
          this.search_data.maxPrice = 50;
          break;
        case "50-100万":
          this.search_data.minPrice = 50;
          this.search_data.maxPrice = 100;
          break;
        case "100万以上":
          this.search_data.minPrice = 100;
          this.search_data.maxPrice = 1000000000000000000000;
          break;
      }
      this.onScreeoutMoney();
    },
    onScreeoutMoney() {
      if (this.selectedPrice === "") {
        this.allTableData = this.filterTableData;
      } else if (
        this.search_data.maxPrice !== null &&
        this.search_data.minPrice !== null &&
        this.search_data.minPrice > this.search_data.maxPrice
      ) {
        // 最大值小于最小值，给出错误提示或执行其他操作
        alert("请输入有效的价格范围");
        return;
      }
      const minPrice = this.search_data.minPrice;
      const maxPrice = this.search_data.maxPrice;
      this.allTableData = this.filterTableData.filter((item) => {
        if (minPrice === null && maxPrice === null) {
          return true;
        } else if (minPrice === null) {
          return item.price <= maxPrice;
        } else if (maxPrice === null) {
          return item.price >= minprice;
        } else {
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
      this.paginations.page_size = 20; // 将page_size的值改为20
      // 设置默认分页数据
      this.tableData = this.allTableData.filter((item, index) => {
        return index < this.paginations.page_size;
      });
    },

    search() {
      // 根据用户选择的条件过滤数据
      let filteredData = this.allTableData;
      if (this.selectedBrand) {
        filteredData = filteredData.filter(
          (item) => item.brand === this.selectedBrand
        );
      }
      if (this.selectedModel) {
        filteredData = filteredData.filter(
          (item) => item.model === this.selectedModel
        );
      }
      if (this.selectedPrice) {
        const [minPrice, maxPrice] = this.selectedPrice.split("-");
        filteredData = filteredData.filter((item) => {
          const price = parseFloat(item.price);
          return price >= parseFloat(minPrice) && price <= parseFloat(maxPrice);
        });
      }

      // 更新显示的数据
      this.tableData = filteredData;
    },
    //其他中下拉选项的方法

    selectAge(age) {
      this.selectedAge = age;
      // 其他逻辑...
    },
    handleCommand(command) {
      this.$message("click on item " + command);
    },
    handleAreaSelect(command) {
      this.areatext = command;
    },
    handlenum_of_transferSelect(command) {
      this.num_of_transferText = command;
      if (command === "") {
        // 不限转手次数，显示所有数据
        this.tableData = this.allTableData;
      } else if (command === "5次及以上") {
        this.tableData = this.allTableData.filter((item) => {
          const num_of_transfer = parseInt(item.num_of_transfer.split("次")[0]);
          return num_of_transfer >= 5;
        });
      } else {
        this.tableData = this.allTableData.filter((item) => {
          const num_of_transfer = parseInt(item.num_of_transfer.split("次")[0]);
          return num_of_transfer === parseInt(command);
        });
      }
      this.selectedNum_of_transfer = this.num_of_transferText;
    },
    handleAgeSelect(command) {
      this.ageText = command;
      if (command === "") {
        // 不限车龄，显示所有数据
        this.tableData = this.allTableData;
      } else if (command === "五年及以上") {
        this.tableData = this.allTableData.filter((item) => {
          const licenseYear = parseInt(item.license_time.substr(0, 4));
          const currentYear = new Date().getFullYear();
          return currentYear - licenseYear >= 5;
        });
      } else {
        const selectedAge = parseInt(command);
        this.tableData = this.allTableData.filter((item) => {
          const licenseYear = parseInt(item.license_time.substr(0, 4));
          const currentYear = new Date().getFullYear();
          return currentYear - licenseYear === selectedAge;
        });
      }
      this.selectedAge = this.ageText;
    },
    handleTransmissionSelect(command) {
      this.transmissionText = command;
      if (command === "") {
        // 不限变速箱，显示所有数据
        this.tableData = this.allTableData;
      } else {
        this.tableData = this.allTableData.filter((item) => {
          return item.transmission.toLowerCase() === command.toLowerCase();
        });
      }
      // 将用户选择的变速箱存储在selectedTransmission变量中
      this.selectedTransmission = this.transmissionText;
    },

    handleMileageSelect(command) {
      this.mileageText = command;

      if (command === "") {
        // 不限里程，显示所有数据
        this.tableData = this.allTableData;
      } else {
        this.tableData = this.allTableData.filter((item) => {
          const mileage = this.parseMileage(item.mileage);
          switch (command) {
            case "1万公里以下":
              return mileage < 1;
            case "1-3万公里":
              return mileage >= 1 && mileage <= 3;
            case "3-5万公里":
              return mileage >= 3 && mileage <= 5;
            case "5-8万公里":
              return mileage >= 5 && mileage <= 8;
            case "8-10万公里":
              return mileage >= 8 && mileage <= 10;
            case "10万公里以上":
              return mileage > 10;
            default:
              return true;
          }
        });
      }
      this.selectedMileage = this.mileageText;
    },
    handleEmissionsSelect(command) {
      this.emissionsText = command;

      if (command === "") {
        // 不限排量，显示所有数据
        this.tableData = this.allTableData;
      } else {
        const unit = "L"; // 假设排量单位为L
        const minValue = this.extractDisplacement(command.split("-")[0]);
        const maxValue = this.extractDisplacement(command.split("-")[1]);

        this.tableData = this.allTableData.filter((item) => {
          const displacement = this.extractDisplacement(item.displacement);
          return displacement >= minValue && displacement <= maxValue;
        });
      }
      this.selectedEmission = this.emissionsText;
    },
    handleEmissionsstandardsSelect(command) {
      this.emissionsstandardsText = command;

      if (command === "") {
        // 不限排放标准，显示所有数据
        this.tableData = this.allTableData;
      } else {
        this.tableData = this.allTableData.filter((item) => {
          return item.emission_standards === command;
        });
      }
      this.selectedEmissionsstandards = this.emissionsstandardsText;
    },
    handleColorSelect(command) {
      this.colorText = command;

      if (command === "") {
        // 不限颜色，显示所有数据
        this.tableData = this.allTableData;
      } else {
        this.tableData = this.allTableData.filter((item) => {
          return item.color === command;
        });
      }
      this.selectedColor = this.colorText;
    },
    handleDriveSelect(command) {
      this.driveText = command;

      if (command === "") {
        // 不限驱动类型，显示所有数据
        this.tableData = this.allTableData;
      } else {
        this.tableData = this.allTableData.filter((item) => {
          return item.drive_model === command;
        });
      }
      this.selectedDrive = this.driveText;
    },
    handleFuelSelect(command) {
      this.fuelText = command;

      if (command === "") {
        // 不限燃料类型，显示所有数据
        this.tableData = this.allTableData;
      } else {
        this.tableData = this.allTableData.filter((item) => {
          return item.fuel_type === command;
        });
      }
      this.selectedFuel = this.fuelText;
    },

    handleFuelStandardSelect(command) {
      this.fuelStandardText = command;

      if (command === "") {
        // 不限燃料类型，显示所有数据
        this.tableData = this.allTableData;
      } else {
        this.tableData = this.allTableData.filter((item) => {
          return item.fuel_standard === command;
        });
      }
      this.selectedFuelStandard = this.fuelStandardText;
    },

    clearSelectedBrand() {
      this.selectedBrand = "";
      // 其他逻辑...
    },
    clearSelectedModel() {
      this.selectedModel = "";
      // 其他逻辑...
    },
    clearSelectedPrice() {
      this.selectedPrice = "";
      this.onScreeoutMoney();
      // 其他逻辑...
    },

    clearSelectedTransmission() {
      this.selectedTransmission = "";
      // 重置变速箱下拉菜单
      this.transmissionText = "变速箱";
      this.$nextTick(() => {
        const dropdown = document.querySelector(
          ".el-dropdown-menu__item.is-selected"
        );
        if (dropdown) {
          dropdown.classList.remove("is-selected");
        }
      });

      // 显示所有数据
      this.tableData = this.allTableData;
    },

    clearSelectedNum_of_transfer() {
      this.selectedNum_of_transfer = "";
      // 重置转手次数下拉菜单
      this.num_of_transferText = "车龄";
      this.$nextTick(() => {
        const dropdown = document.querySelector(
          ".el-dropdown-menu__item.is-selected"
        );
        if (dropdown) {
          dropdown.classList.remove("is-selected");
        }
      });

      // 显示所有数据
      this.tableData = this.allTableData;
    },

    clearSelectedAge() {
      this.selectedAge = "";
      // 重置车龄下拉菜单
      this.ageText = "车龄";
      this.$nextTick(() => {
        const dropdown = document.querySelector(
          ".el-dropdown-menu__item.is-selected"
        );
        if (dropdown) {
          dropdown.classList.remove("is-selected");
        }
      });

      // 显示所有数据
      this.tableData = this.allTableData;
    },
    clearSelectedMileage() {
      this.selectedMileage = "";
      // 重置里程下拉菜单
      this.mileageText = "里程";
      this.$nextTick(() => {
        const dropdown = document.querySelector(
          ".el-dropdown-menu__item.is-selected"
        );
        if (dropdown) {
          dropdown.classList.remove("is-selected");
        }
      });

      // 显示所有数据
      this.tableData = this.allTableData;
    },
    clearSelectedEmission() {
      this.selectedEmission = "";
      // 重置排量下拉菜单
      this.emissionsText = "排量";
      this.$nextTick(() => {
        const dropdown = document.querySelector(
          ".el-dropdown-menu__item.is-selected"
        );
        if (dropdown) {
          dropdown.classList.remove("is-selected");
        }
      });

      // 显示所有数据
      this.tableData = this.allTableData;
    },
    clearselectedEmissionsstandards() {
      this.selectedEmissionsstandards = "";
      // 重置排放标准下拉菜单
      this.emissionsstandardsText = "排放标准";
      this.$nextTick(() => {
        const dropdown = document.querySelector(
          ".el-dropdown-menu__item.is-selected"
        );
        if (dropdown) {
          dropdown.classList.remove("is-selected");
        }
      });

      // 显示所有数据
      this.tableData = this.allTableData;
    },

    clearselectedColor() {
      this.selectedColor = "";
      // 重置颜色下拉菜单
      this.colorText = "颜色";
      this.$nextTick(() => {
        const dropdown = document.querySelector(
          ".el-dropdown-menu__item.is-selected"
        );
        if (dropdown) {
          dropdown.classList.remove("is-selected");
        }
      });

      // 显示所有数据
      this.tableData = this.allTableData;
    },
    clearselectedDrive() {
      this.selectedDrive = "";
      // 重置驱动下拉菜单
      this.driveText = "驱动";
      this.$nextTick(() => {
        const dropdown = document.querySelector(
          ".el-dropdown-menu__item.is-selected"
        );
        if (dropdown) {
          dropdown.classList.remove("is-selected");
        }
      });

      // 显示所有数据
      this.tableData = this.allTableData;
    },
    clearselectedFuel() {
      this.selectedFuel = "";
      // 重置燃料类型下拉菜单
      this.fuelText = "燃料类型";
      this.$nextTick(() => {
        const dropdown = document.querySelector(
          ".el-dropdown-menu__item.is-selected"
        );
        if (dropdown) {
          dropdown.classList.remove("is-selected");
        }
      });

      // 显示所有数据
      this.tableData = this.allTableData;
    },
    clearselectedFuelStandard() {
      this.selectedFuelStandard = "";
      // 重置燃油标准下拉菜单
      this.fuelStandardText = "燃油标准";
      this.$nextTick(() => {
        const dropdown = document.querySelector(
          ".el-dropdown-menu__item.is-selected"
        );
        if (dropdown) {
          dropdown.classList.remove("is-selected");
        }
      });

      // 显示所有数据
      this.tableData = this.allTableData;
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
  background-size: 850px, 200px;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-position: 90% 65%, 25% 48%;
  background-color: rgba(245, 246, 252, 1);
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
  background-color: rgba(255, 255, 255, 1);
  margin-left: 0px;
  margin-right: 0px;
}
.bottom-row {
  margin-top: 1.5rem; /* 控制底部行与上半部分的间距 */
}

/**全国选项的颜色和样式 */
.location-input {
  width: 150px;
  font-size: 8px; /* 修改内部文字的大小为 14px */
  font-weight: bold; /* 将内部文字设为加粗 */
  margin-bottom: 0px;
}

.el-icon-arrow-down {
  font-size: 12px;
}
.bold-text {
  font-weight: bold;
  font-size: 12px; /* 设置字体大小 */
  color: #000000; /* 设置字体颜色 */
}

.bold-text-yixuanze {
  font-size: 8px; /* 设置字体大小 */
  color: rgb(37, 38, 43); /* 设置字体颜色 */
}

/**品牌部分的样式 */
.custom-menu {
  max-height: 200px; /* 设置下拉菜单的最大高度 */
  overflow-y: auto; /* 将内容超出限定高度时添加滚动轴 */
}

.dropdown-menu {
  width: auto;
  min-width: 100px;
}
.custom-dropdown-menu {
  font-size: 12px;
  line-height: 1.5;
  text-align: center;
}
.brand-container {
  margin-top: 20px; /* 调整第一个容器与上方元素的距离 */
  display: flex;
  align-items: center;
}

.brand-container4 {
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
.brand-list3 {
  display: flex;
  align-items: center;
}
.brand-list3 .item {
  margin-right: 10px; /* 设置词与词之间的空隙大小，调整数值以获得所需的间距 */
  display: inline;
  font-size: 6px; /* 设置字体大小 */
}
.brand-container .bold-text {
  margin-right: 15px; /* 添加右边距，调整"品牌"标签与文本之间的距离 */
}

.brand-container .bold-text-yixuanze {
  margin-right: 5px; /* 添加右边距，调整"品牌"标签与文本之间的距离 */
}
.brand-more {
  margin-right: 8px; /* 设置词与词之间的空隙大小，调整数值以获得所需的间距 */
  display: inline;
  font-size: 12px; /* 设置字体大小 */
}

.search-container {
  margin-left: auto; /* 使用auto将搜索框和按钮推向最右侧 */
  display: flex;
  align-items: center;
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
}

.button1 {
  margin-left: 10px;
  padding: 0.5%;
  font-size: 8px;
  background-color: rgba(53, 99, 233, 1);
  color: white;
}

.buttonPrice {
  margin-left: 10px;
  margin-top: 28px;
  padding: 7%;
  float: right;
  font-size: 8px;
  background-color: rgba(53, 99, 233, 1);
  color: white;
}
/**已选择的样式 */
.selected-option {
  font-size: 5px; /* 根据需求调整字体大小 */
  display: inline-block;
  padding: 1px;
  border: 1px solid #ccc;
  border-radius: 3px;
  margin-right: 5px;
}

.selected-option i {
  cursor: pointer;
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
  margin-bottom: 10px;
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
  margin-right: 0px;
  margin-bottom: 15px;
}

.title {
  font-size: 20px;
}

.car-info {
  margin-top: 4px;
  display: flex;
}

.price {
  float: left;
  font-size: 22px;
  color: rgba(53, 99, 233, 1);
  margin-top: -10px;
  margin-bottom: -50px;
}

.title-text{
  font-size: 22px;
  font-weight: bold;
  margin-left: 5px;
}
.extra-info {
  font-size: 15px;
  color: #999;
  margin-top: 2px;
  display: flex;
}
.separator2 {
  margin: 0 5px;
  color: #999;
  margin-top: -3px;
  font-size: 15px;
}

.buttondetails {
  width: 80px;
  height: 25px;
  padding: 1%;
  border-radius: 25px;
  float: right;
  font-size: 10px;
  background-color: rgba(53, 99, 233, 1);
  color: white;
  margin-top: -14px;
}

.price-container {
  margin-right: auto;
  margin-top: 15px;
  margin-left: -30px;
  margin-bottom: -10px;
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
  clear: both;
}
</style>
