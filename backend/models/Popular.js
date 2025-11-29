const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// Create Schema
// 热门二手车信息
const PopularSchema = new Schema({
  car_name: {
    type: String
  },
 price_field: {
    type: String
  },
  city_name: {
    type: String,
    required: true
  },
  year1: {
    type: String,
    required: true
  },
  year2: {
    type: String,
    required: true
  },
  year3: {
    type: String,
    required: true
  },
  year4: {
    type: String,
    required: true
  },
  year5: {
    type: String,
    required: true
  },

});

module.exports = Popular = mongoose.model('populars', PopularSchema);