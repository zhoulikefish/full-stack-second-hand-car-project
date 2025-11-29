// 用于处理图片上传的路由
// 相关功能还有bug, 暂时把提交卖二手车信息时的 img_URL 要求注释掉了
const checkAuth = require('../../utils/auth');
const express = require('express');
const router = express.Router();
// const multer = require('multer'); // 用于处理文件上传的中间件
const path = require('path');

// // 配置 multer 中间件
// const storage = multer.diskStorage({
//   destination: function (req, file, cb) {
//     // 指定文件保存的路径
//     cb(null, 'uploads/');
//   },
//   filename: function (req, file, cb) {
//     // 生成文件的新名称
//     const ext = path.extname(file.originalname);
//     cb(null, Date.now() + ext);
//   }
// });

// const upload = multer({ storage: storage });

// 处理图片上传的路由
// router.post('/upload', upload.single('image'), (req, res) => {
//   // 在 req.file 中可以访问上传的文件信息
//   const imageUrl = '/uploads/' + req.file.filename;
//   res.json({ imageUrl: imageUrl });
// });

module.exports = router;  
