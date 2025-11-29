const express = require("express");
const router = express.Router();
const Car = require("../../models/Car");
const checkAuth = require("../../utils/auth");

// @route  GET api/cars/test
// @desc   返回测试信息
// @access Public
router.get("/test", (req, res) => {
  res.json({ msg: "Cars route works" });
});

router.get("/count_by_province", (req, res) => {
  const r = req.query.province_name; // 获取查询参数 r
  // console.log("省份值:", r); // 打印省份值
  // 构建聚合管道
  const pipeline = [
    {
      $match: {
        province_name: r, // 匹配 province_name 字段等于参数 r 的数据
      },
    },
    {
      $group: {
        _id: null,
        count: { $sum: 1 }, // 统计匹配数据的个数
      },
    },
  ];
  // 执行聚合查询
  Car.aggregate(pipeline)
    .then((result) => {
      if (result.length > 0) {
        const count = result[0].count;
        res.json({ count });
      } else {
        res.json({ count: 0 });
        // res.json({req.query.province_name})
      }
    })
    .catch((err) => {
      res.status(500).json({ error: err.message });
    });
});


// 参数: 省份
router.get("/count_by_time", (req, res) => {
    const r = req.query.province_name; // 获取查询参数 r
  
    Car.aggregate([
      {
        $match: {
          province_name: r, // 匹配 province_name 字段等于参数 r 的数据
          update_time: { $ne: null } // 排除 update_time 为空的情况
        }
      }, 
      { 
        $group: {
          _id: {
            year: { $year: "$update_time" }, // 提取更新时间的年份
            month: { $month: "$update_time" } // 提取更新时间的月份
          },
          avgPrice: { $avg: "$price" } // 计算匹配数据的平均价格
        } 
      },
      {
        $sort: {    
          "_id.year": 1, // 按年份升序排序  
          "_id.month": 1 // 按月份升序排序    
        }
      },  
      { 
        $project: {  
          _id: 0,
        //   period: {
        //     $concat: [
        //       { $toString: "$_id.year" }, // 将年份转换为字符串
        //       "-",
        //       { $toString: "$_id.month" } // 将月份转换为字符串
        //     ]
        //   },
          avgPrice: 1
        }    
      },
    //   {
    //     $match: {
    //       period: { $ne: null } // 排除 period 为空的情况
    //     }
    //   }
    ])
      .then((result) => {
        res.json(result);
      })
      .catch((err) => {
        res.status(500).json({ error: err.message });
      });
  });
  

  function mergeData(result) {
    result.forEach((brand) => {
      const models = brand.children;
      let otherModelsValue = 0;
      const filteredModels = models.filter((model) => {
        if (model.value < 1000) {
          otherModelsValue += model.value;
          return false;
        }
        return true;
      });
      if (otherModelsValue > 0) {
        filteredModels.push({ name: "其他型号", value: otherModelsValue });
      }
      brand.children = filteredModels;
    });
    
    // 第二步：合并 brand 中子 model 和小于 1000 的节点为一个名称为“其他品牌”的节点
    let otherBrandValue = 0;
    const filteredBrands = result.filter((brand) => {
      if (brand.children) {
        const brandValue = brand.children.reduce((acc, model) => acc + model.value, 0);
        if (brandValue < 4000) {
          otherBrandValue += brandValue;
          return false;
        }
      }
      return true;
    });
    if (otherBrandValue > 0) {
      filteredBrands.push({ name: "其他品牌", value: otherBrandValue });
    }
    
    // 更新最终结果
    result = filteredBrands;
  
    return result;
  }

// sunchart 旭日图
router.get("/sunchart", (req, res) => {
  Car.aggregate([
    {
      $group: {
        _id: { brand: "$brand", model: "$model" },
        count: { $sum: 1 }
      }
    },
    {
      $group: {
        _id: "$_id.brand",     
        models: { $push: { name: "$_id.model", value: "$count" } }
      }
    },
    {
      $project: {
        _id: 0,
        name: "$_id",
        children: "$models"
      }
    }
  ])
    .then((result) => {
      res.json(mergeData(result));
      // res.json(result);
    })
    .catch((err) => {
      res.status(500).json({ error: err.message });
    });
});

router.get("/sunchart2", (req, res) => {

    Car.aggregate([
      {
        $group: {
          _id: { brand: "$brand", model: "$model" },
          count: { $sum: 1 }
        }
      },
      {
        $group: {
          _id: "$_id.brand",
          models: {
            $push: {
              $cond: [
                { $gte: ["$count", 10] }, // 判断是否数量大于等于10
                { name: "$_id.model", value: "$count" }, // 数量大于等于10，保留原始model
                { name: "其他型号", value: "$count" } // 数量小于10，归类为其他型号
              ]
            }
          },
          count: { $sum: "$count" } // 计算品牌下的总数量
        }
      },
      {
        $group: {
          _id: null,
          brands: {
            $push: {
              $cond: [
                { $gte: ["$count", 100] }, // 判断品牌总数量是否大于等于100
                { name: "$_id", children: "$models" }, // 总数量大于等于100，保留原始brand和models
                { name: "其他品牌" } // 总数量小于100，归类为其他品牌，不包含children
              ]
            }
          }
        }
      },
      {
        $project: {
          _id: 0,
          name: "品牌",
          children: "$brands"
        }
      }
    ])
      .then((result) => {
        res.json(result[0]);
      })
      .catch((err) => {
        res.status(500).json({ error: err.message });
      });
  });
  













// router.delete("/delete_by_brand", (req, res) => {
//   const brandToDelete = "二手车";

//   Car.deleteMany({ brand: brandToDelete })
//     .then(() => {
//       res.json({ message: `成功删除所有品牌为 ${brandToDelete} 的数据` });
//     })
//     .catch((err) => {
//       res.status(500).json({ error: err.message });
//     });
// });

// @route  GET api/cars
// @desc   获取所有车辆信息
// @access Public
router.get("/", (req, res) => {
  Car.find()
    .limit(1000)
    .then((cars) => {
      if (!cars || cars.length === 0) {
        //
        return res.status(404).json("No cars found");
      }
      res.json(cars);
      // res.json(cars.slice(0, 10));
    })
    .catch((err) => res.status(400).json(err));
});

router.get("/get", (req, res) => {
  const { page, pageSize } = req.query;
  const skip = (page - 1) * pageSize;

  Car.find()
    .skip(skip)
    .limit(pageSize)
    .then((cars) => {
      if (!cars || cars.length === 0) {
        return res.status(404).json("No cars found");
      }
      res.json(cars);
    })
    .catch((err) => res.status(400).json(err));
});

// @route  POST api/cars/sell
// @desc   创建新车辆信息, 同时需要添加到用户的 posts 数组中
// @access Public
router.post("/sell", (req, res) => {
  const newCar = new Car({
    url: req.body.url,  
    img_url: req.body.img_url,
    title: req.body.title,
    brand: req.body.brand, 
    model: req.body.model,
    license_time: req.body.license_time,
    update_time: req.body.update_time,
    mileage: req.body.mileage,
    transmission: req.body.transmission,
    emission_standards: req.body.emission_standards,
    displacement: req.body.displacement,
    num_of_transfer: req.body.num_of_transfer,
    location: req.body.location,
    engine: req.body.engine,
    color: req.body.color,
    fuel_standard: req.body.fuel_standard,
    drive_model: req.body.drive_model,
    price: req.body.price,
    province_name: req.body.province_name,
    poster_id: req.body.poster_id,
  });
  console.log(req.body)  
  newCar
    .save()
    .then((car) => {
      const carId = car._id; 

      // 更新用户的 post 数组，将 carId 添加到其中
      User.findByIdAndUpdate(
        req.body.poster_id, // 用户的 ID    
        { $push: { posts: carId } },
        { new: true }
      )
        .then((user) => {
          res.json({ car, user });
        })
        .catch((err) => console.log(err));
    })
    .catch((err) => console.log(err)); 
});

// @route  DELETE api/cars/:id
// @desc   删除指定id的车辆信息
// @access Public
router.delete("/:id", (req, res) => {
  Car.findByIdAndRemove(req.params.id)       
    .then(() => res.json({ success: true }))
    .catch((err) => res.status(404).json({ success: false }));
});




router.get("/test2", (req, res) => {
  res.json({ msg: "Cars route works" });
});

router.get("/count_by_brand0", (req, res) => {
  Car.aggregate([
    {
      $group: {
        _id: "$brand",
        count: { $sum: 1 }
      }
    }
  ])
    .then((result) => {
      res.json(result);  
    })
    .catch((err) => {
      res.status(500).json({ error: err.message });
    });
});

router.get("/count_by_brand", (req, res) => {

    Car.aggregate([
      {
        $group: {
          _id: { brand: "$brand", model: "$model" },
          count: { $sum: 1 }
        }
      },
      {
        $group: {
          _id: "$_id.brand",
          models: {
            $push: {
              name: "$_id.model",
              count: "$count"
            }
          },
          count: { $sum: "$count" }
        }
      }
    ])
      .then((result) => {
        res.json(result);
      })
      .catch((err) => {
        res.status(500).json({ error: err.message });
      });
  });
  








// @route  GET api/cars/:id
// @desc   获取单个信息
// @access Private
// router.get("/:id", (req, res) => {
//     Car.findById(req.params.id)
//       .then((cars) => {
//         if (!cars) {
//           return res.status(404).json("没有任何内容");
//         }
//         res.json(cars);
//       })
//       .catch((err) => res.status(404).json(err));
//   }
// );
router.get("/:id", (req, res) => {
  Car.findById(req.params.id)
    .then((car) => {
      if (!car) {
        return res.status(404).json("没有找到对应的内容");
      }
      res.json(car);
    })
    .catch((err) => res.status(500).json(err)); 
});

router.get("/test3", (req, res) => {
  res.json({ msg: "Cars route works" });
});


router.get("/filter", (req, res) => {
  // 获取查询参数
  const {
    location, // 所在地
    brand, // 品牌
    model, // 车型
    min_price, // 最低价格
    max_price, // 最高价格
    min_age, // 最小车龄
    max_age, // 最大车龄
    transmission, // 变速箱
    min_mileage, // 最小里程
    max_mileage, // 最大里程
    min_displacement, // 最小排量
    max_displacement, // 最大排量
    emission_standard, // 排放标准
    color, // 颜色
    // country, // 国别
    drive_model, // 驱动
    // seat, // 座位数  
    fuel_standard, // 燃料类型
    extra_desc, // 其他描述
  } = req.query;

  // 构建查询条件对象
  const query = {};

  // 严格查询条件
  if (location) query.location = location;
  if (brand) query.brand = brand;
  if (model) query.model = model;
  if (transmission) query.transmission = transmission;
  if (color) query.color = color;
  if (drive_model) query.drive_model = drive_model;
  if (fuel_standard) query.fuel_standard = fuel_standard;
  if (emission_standard) query.emission_standards = emission_standard;

  // 范围查询条件
  if (min_price && max_price) {
    query.price = { $gte: parseInt(min_price), $lte: parseInt(max_price) };
  }
  if (min_age && max_age) {
    query.age = { $gte: parseInt(min_age), $lte: parseInt(max_age) };
  }
  if (min_mileage && max_mileage) {
    query.mileage = {
      $gte: parseInt(min_mileage),
      $lte: parseInt(max_mileage),
    };
  }
  if (min_displacement && max_displacement) {
    query.displacement = { $gte: min_displacement, $lte: max_displacement };
  }

  // 模糊查询条件
  if (extra_desc) {
    query.$text = { $search: extra_desc };
  }

  // 查询数据库
  Car.find(query)
    .sort({ $textScore: { $meta: "textScore" } }) // 根据模糊查询的匹配度进行排序
    .then((cars) => {
      res.json(cars); // 返回筛选后的车辆信息数组，可以根据需要修改返回的数据格式
    })
    .catch((err) => {
      res.status(500).send(err.message); // 发生错误时返回错误信息
    });
});






router.get("/count2", async (req, res) => {
  try {
    const provinceName = req.query.province_name; // 获取查询参数 province_name
    console.log("省份值:", provinceName); // 打印省份值

    // 构建聚合管道
    const pipeline = [
      {
        $match: {
          province_name: provinceName, // 匹配 province_name 字段等于参数 provinceName 的数据
        },
      },
      {
        $group: {
          _id: {
            year: { $year: "$update_time" }, // 提取年份
            month: { $month: "$update_time" }, // 提取月份
          },
          count: { $sum: 1 }, // 统计匹配数据的个数
        },
      },
      {
        $project: {
          _id: 0, // 不显示 _id 字段
          yearMonth: {
            $concat: [
              { $toString: "$_id.year" },
              "-", // 年份转为字符串并拼接 "-"
              { $toString: "$_id.month" }, // 月份转为字符串
            ],
          },
          count: 1, // 保留 count 字段
        },
      },
      {
        $sort: {
          yearMonth: 1, // 按年份和月份排序
        },
      },
    ];

    // 执行聚合查询
    const result = await Car.aggregate(pipeline);

    res.json(result);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;

// const express = require('express');
// const router = express.Router();
// const Car = require('../../models/Car');

// // @route  GET api/cars/test
// // @desc   返回测试信息
// // @access Public
// router.get('/test', (req, res) => {
//   res.json({ msg: 'Cars route works' });
// });

// // @route  GET api/cars
// // @desc   获取所有车辆信息
// // @access Public
// router.get('/', (req, res) => {
//   Car.find()
//     .then(cars => {
//       if (!cars || cars.length === 0) {
//         return res.status(404).json('No cars found');
//       }
//       res.json(cars[100]);
//     })
//     .catch(err => res.status(400).json(err));
// });

// // @route  POST api/cars
// // @desc   创建新车辆信息
// // @access Public
// router.post('/', (req, res) => {
//   const newCar = new Car({
//     url: req.body.url,
//     img_url: req.body.img_url,
//     title: req.body.title,
//     brand: req.body.brand,
//     model: req.body.model,
//     license_time: req.body.license_time,
//     update_time: req.body.update_time,
//     mileage: req.body.mileage,
//     transmission: req.body.transmission,
//     emission_standards: req.body.emission_standards,
//     displacement: req.body.displacement,
//     num_of_transfer: req.body.num_of_transfer,
//     location: req.body.location,
//     engine: req.body.engine,
//     color: req.body.color,
//     fuel_standard: req.body.fuel_standard,
//     drive_model: req.body.drive_model,
//     price: req.body.price,
//     province_name: req.body.province_name
//   });

//   newCar.save()
//     .then(car => res.json(car))
//     .catch(err => console.log(err));
// });

// // @route  DELETE api/cars/:id
// // @desc   删除指定id的车辆信息
// // @access Public
// router.delete('/:id', (req, res) => {
//   Car.findByIdAndRemove(req.params.id)
//     .then(() => res.json({ success: true }))
//     .catch(err => res.status(404).json({ success: false }));
// });

// module.exports = router;
