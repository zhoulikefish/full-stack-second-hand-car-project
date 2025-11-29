// @login & register
const express = require("express");
const router = express.Router();
const passport = require("passport");
const checkAuth = require('../../utils/auth');
const Like = require("../../models/Like");

// @route  GET api/Like/test
// @desc   返回的请求的json数据
// @access public
router.get("/test", (req, res) => {
  res.json({ msg: "Like works" });
});


// @route  GET api/Like
// @desc   获取所有信息
// @access Private
router.get('/', (req, res) => {
  Like.find()
    .then(Likes => {
      if (!Likes || Likes.length === 0) {
        return res.status(404).json('No logs found');
      }
      res.json(Likes );
    })
    .catch(err => res.status(400).json(err));
});


// @route  GET api/Like/:id
// @desc   获取单个信息
// @access Private
router.get(
  "/:id",
  // passport.authenticate("jwt", { session: false }),
  (req, res) => {
    Like.findById(req.params.id)
      .then((Like) => {
        if (!Like) {
          return res.status(404).json("没有任何内容");
        }
        res.json(Like);
      })
      .catch((err) => res.status(404).json(err));
  }
);



// @route  POST api/profiles/add
// @desc   创建新的信息
// @access Private
router.post(
	"/add",
	// passport.authenticate("jwt", { session: false }),
	async (req, res) => {
		try {
			const { userId, carId } = req.body;
			const newLike = new Like({ userId, carId });
		
			await newLike.save();
			res.status(200).json({ message: '收藏成功' });
		} catch (error) {
			res.status(500).json({ message: '服务器错误' });
		}
	}	
);

module.exports = router;


