const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// Create Schema
const UserSchema = new Schema({
// 用户名
// 请输入用户名
// 电话
// 请输入电话号码
// 密码
// 请输入密码
// 确认密码
  phone: {
    type: String, 
    required: true 
  },
  name: {
    type: String,
    required: true
  },
  
  password: {
    type: String,
    required: true
  },
  avatar: {
    type: String,
    default: 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
  },
  // identity: {
  //   type: String,
  //   required: true
  // }, 
  date: {
    type: Date,
    default: Date.now
  },
  // 记录发布的二手车
  posts: {
    type: [String],
	default: []
  },
  // 记录收藏的二手车信息
  favorites: { 
    type: [String],
	default: []
  }
});

module.exports = User = mongoose.model('users', UserSchema);
