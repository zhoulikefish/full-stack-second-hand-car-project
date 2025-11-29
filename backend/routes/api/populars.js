// @login & register
const express = require("express");
const router = express.Router();
const passport = require("passport");
const checkAuth = require('../../utils/auth');
const Popular = require("../../models/Popular");

// @route  GET api/popular/test
// @desc   返回的请求的json数据
// @access public
router.get("/test", (req, res) => {
  res.json({ msg: "popular works" });
});


// @route  GET api/Popular
// @desc   获取所有信息
// @access Private
router.get('/', (req, res) => {
  Popular.find()
    .then(populars => {
      if (!populars || populars.length === 0) {
        return res.status(404).json('No cars found');
      }
      res.json(populars);
    })
    .catch(err => res.status(400).json(err));
});


// @route  GET api/Popular/:id
// @desc   获取单个信息
// @access Private
// 通过车辆名称获取车辆信息的方法
function findCarByName(name) {
	return Popular.find(car => car.car_name === name);
  }
   

// 获取车辆信息的路由处理函数
router.get('/:id', (req, res) => {
	const name = req.query.id;
	console.log(req)

	if (name) {
		const car = findCarByName(name);
		if (car) {
			res.json(car);
		} else {
		res.status(404).json({ error: 'Car not found' });
		}
	} else {
		res.status(400).json({ error: 'Missing parameters' });
	}
}); 
 
 
module.exports = router;




