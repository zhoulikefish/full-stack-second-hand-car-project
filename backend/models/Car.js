const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// 定义Car模型的数据结构
const CarSchema = new Schema({
  // url: {
  //   type: String,
  //   required: true,
  // },
  img_url: {
    type: [String],
    // required: true,
  },
  title: {
    type: String,
    required: true,
  },
  brand: {
    type: String,
    required: true,
  },
  model: {
    type: String,
    // required: true,
  },
  license_time: {
    type: String,
    required: true,
  },
  update_time: {
    type: Date,
    default: Date.now,
  },  
  mileage: {
    type: String,
    required: true,
  },
  transmission: {
    type: String,
    required: true,
  },
  emission_standards: {
    type: String,
    required: true,
  },
  displacement: {
    type: String,
  },
  num_of_transfer: {
    type: String,
    required: true,
  },
  location: {
    type: String,
    required: true,
  },
  engine: {
    type: String,

  },
  color: {
    type: String,
    required: true,
  },
  fuel_standard: {
    type: String,
    required: true,
  },
  drive_model: {
    type: String,
    required: true,
  },
  price: {
    type: Number,
    required: true,
  },
  province_name: {
    type: String,
    // required: true,
  },

});

// 创建Car模型并导出
module.exports = Car = mongoose.model('cars', CarSchema);


