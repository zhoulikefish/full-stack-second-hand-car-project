// 执行python脚本的路由

const checkAuth = require('../../utils/auth');
const { spawn } = require('child_process');
const express = require('express');
const router = express.Router();
// const axios = require('axios');

const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const keys = require('../../config/keys');
const passport = require('passport');

router.get('/hello', (req, res) => {
    res.json({ msg: 'Hello World!' });
});

router.get('/test', (req, res) => {
    const {
        province_name,
        location,
        brand,
        model,
        update_year,
        update_month
    } = req.query;
    res.json({
        province_name,
        location,
        brand,
        model,
        update_year,
        update_month
    });
});

router.get('/evaluate', async (req, res) => {
  try {
    // 获取前端传递的参数
    const {
      province_name,
      location,
      brand,
      model,
      update_year,
      update_month
    } = req.query;
    console.log("req.query: \n");
    console.log(req.query);
    // 执行 Python 脚本
    const pythonScript = spawn('python', ['./pyscripts/evaluate/main.py', province_name, location, brand, model, update_year, update_month]);
    // 监听脚本的输出
    pythonScript.stdout.on('data', (data) => {
      const result = data.toString().trim(); // 去除首尾的空格和换行符
      // 将结果返回给前端
      res.send(result);
    });

    pythonScript.stderr.on('data', (data) => {
      console.error(`Python script error: ${data}`);
      res.status(500).send('Internal Server Error');
    });
  } catch (error) {
    console.error(error);
    res.status(500).send('Internal Server Error');
  }
});



router.get('/predict', async (req, res) => {
  try {
    const { brand, model, location, numberOfTransfer, license_year, license_month } = req.query;



    // 执行 Python 脚本
    const pythonScript = spawn('python', [
      './pyscripts/timeseries/main_macro.py',
      brand,
      model,
      location,
      numberOfTransfer,
      license_year,
      license_month
    ]);

    let result = '';

    pythonScript.stdout.on('data', (data) => {
      result += data.toString();
    });

    pythonScript.stderr.on('data', (data) => {
      console.error(`Python script error: ${data}`);
      res.status(500).send('Internal Server Error');
    });

    pythonScript.on('close', (code) => {
      if (code === 0) {
        try {
          // 手动解析JSON字符串
          const formattedPredictData = JSON.parse(result.replace(/'/g, '"'));
          res.json(formattedPredictData);
        } catch (error) {
          console.error(`Failed to parse JSON: ${error}`);
          res.status(500).send('Internal Server Error');
        }
      } else {
        console.error(`Python script process exited with code ${code}`);
        res.status(500).send('Internal Server Error');
      }
    });
  } catch (error) {
    console.error(error);
    res.status(500).send('Internal Server Error');
  }
});


router.get('/test2', async (req, res) => {
    const { brand, model, location, numberOfTransfer, license_year, license_month } = req.query;
  res.json({
    brand,
    model,
    location,
    numberOfTransfer,
    license_year,
    license_month
  });
});




module.exports = router;
