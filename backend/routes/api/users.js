//@login & register
// 注册和登录接口

const checkAuth = require('../../utils/auth');
const express = require('express');
const router = express.Router();
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const keys = require('../../config/keys');
const passport = require('passport');
const User = require('../../models/User');

// @route  GET api/users/test
// @desc   返回的请求的json数据
// @access public
router.get('/test', (req, res) => {
  res.json({ msg: 'login works' });
});


router.get('/echo', (req, res) => {
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






// @route  POST api/users/register
// @desc   返回的请求的json数据
// @access public
router.post('/register', (req, res) => {
  // 查询数据库中是否已存在该手机号
  User.findOne({ phone: req.body.phone}).then(user => {
    if (user) {
      return res.status(400).json('该手机号码已被注册!');
    } else {
      // console.log("req.body: \n");
      // console.log(req.body);
      const newUser = new User({
        name: req.body.name,
        phone: req.body.phone,
        password: req.body.password,
      });
      console.log("User: \n");
      console.log(newUser);
      bcrypt.genSalt(10, (err, salt) => {
        bcrypt.hash(newUser.password, salt, (err, hash) => {
          if (err) throw err;

          newUser.password = hash;

          newUser
            .save()
            .then(user => res.json(user))
            .catch(err => console.log(err));
        });
      });
    }
  });
});

// @route  POST api/users/login
// @desc   返回token jwt passport
// @access public
router.post('/login', (req, res) => {
  const phone = req.body.phone;
  const password = req.body.password;
  // 查询数据库
  User.findOne({ phone }).then(user => {
    if (!user) {
      return res.status(404).json('用户不存在!');
    }

    // 密码匹配
    bcrypt.compare(password, user.password).then(isMatch => {
      if (isMatch) {
        const payload = {
          id: user.id,
          name: user.name,
          // avatar: user.avatar,
          identity: user.identity
        };
        jwt.sign(payload, keys.secretOrKey, { expiresIn: 20 }, (err, token) => {
          if (err) throw err;
          res.json({
            success: true,
            token: 'Bearer ' + token
          });
        });
      } else {
        return res.status(400).json('密码错误!');
      }
    });
  });
});

// @route  GET api/users/current
// @desc   返回当前用户信息
// @access Private
router.get(
  '/current',
  passport.authenticate('jwt', { session: false }),
  (req, res) => {
    res.json({
      id: req.user.id,
      name: req.user.name,
      phone: req.user.phone,
      favorites: req.user.favorites,
      posts: req.user.posts, 
    });
  }
); 


// @route  POST api/users/edit
// @desc   编辑用户信息接口
// @access Private
router.post(
  '/edit',
  passport.authenticate('jwt', { session: false }),
  (req, res) => {
    const userFields = {};
    if (req.body.name) userFields.name = req.body.name;
    if (req.body.phone) userFields.phone = req.body.phone;
    if (req.body.password) userFields.password = req.body.password;
    if (req.body.avatar) userFields.avatar = req.body.avatar; // 添加头像字段

    User.findOneAndUpdate(
      { _id: req.user.id },
      { $set: userFields },
      { new: true }
    )
      .then(user => {
        res.json(user);
      })
      .catch(err => {
        console.log(err);
        res.status(500).json({ error: '服务器内部错误' });
      });
  }
);


 



// @route  GET api/users
// @desc   获取某一用户信息（暂时）
// @access Private
router.get(
	"/:id",
	// passport.authenticate("jwt", { session: false }),
	(req, res) => {
	  //  console.log("server id:",req)
	  User.findById(req.params.id)
		.then((cars) => {
		  if (!cars) {
			return res.status(404).json("没有任何内容");
		  }
		  res.json(cars);
		})
		.catch((err) => res.status(404).json(err));
	}
  );



// // @route  GET api/users/addfavorite
// // @desc   添加favorites用户信息
// // @access Private
// router.post('/:id', async (req, res) => {
// 	try {
// 	  const { userId, productId } = req.body;
  
// 	  // 在 users 表中查找对应的用户
// 	  const user = await User.findOne({ _id: userId });
  
// 	  // 将商品 ID 添加到用户的 favorites 数组中
// 	  if (!user.favorites.includes(productId)) {
// 		user.favorites.push(productId);
// 		await user.save();
// 	  }
  
// 	  res.status(200).json({ message: '收藏成功' });
// 	} catch (error) {
// 	  // 处理错误，如返回错误状态码等
// 	  res.status(500).json({ message: '收藏失败' });
// 	}
//   });

 

// @route  GET api/users/addfavorite
// @desc   添加favorites用户信息
// @access Private  
router.post('/addfavorite', async (req, res) => {
	try {
	  const { userId, productId } = req.body;
	  console.log(req.body)
  
	  // 在 users 表中查找对应的用户
	  const user = await User.findOne({ _id: userId });
  
	  // 将商品 ID 添加到用户的 favorites 数组中
	  if (!user.favorites.includes(productId)) {
		user.favorites.push(productId);
		await user.save();
	  }
  
	  res.status(200).json({ message: '收藏成功' });
	} catch (error) {
	  // 处理错误，如返回错误状态码等
	  res.status(500).json({ message: '收藏失败' });
	}
  });


// @route  GET api/users/addfavorite
// @desc   删除favorites用户信息
// @access Private
router.post('/removefavorite', (req, res) => {
	const { userId, productId } = req.body;

	User.findOneAndUpdate(
		{ _id: userId },
		{ $pull: { favorites: null } },
		(err) => {
			if (err) {
				return res.status(500).json({ message: 'Failed to remove null values from favorites' });
			}

			// 输出日志
			console.log("start", userId, productId);

			// 从用户收藏记录中删除商品ID
			User.findOneAndUpdate(
				{ _id: userId },
				{ $pull: { favorites: productId } },
				(err) => {
					if (err) {
						return res.status(500).json({ message: 'Failed to remove favorite' });
					}
					res.json({ message: 'Favorite removed successfully' });
				}
			);
		}
	);
});


router.post('/check', async (req, res) => {
	try {
	  const { userId, productId } = req.query;
  
	  // 在 users 表中查找对应的用户
	  const user = await User.findOne({ _id: userId });
  
	  // 检查商品是否在收藏列表中
	  const isFavorite = user.favorites.includes(productId);
  
	  res.json({ success: true, isFavorite });
	} catch (error) {
	  res.json({ success: false, error: error.message });
	} 
  });     

module.exports = router;




// //@login & register
// // 注册和登录接口


// const express = require('express');
// const router = express.Router();
// const bcrypt = require('bcrypt');
// const jwt = require('jsonwebtoken');
// const keys = require('../../config/keys');
// const passport = require('passport');
// const User = require('../../models/User');

// // @route  GET api/users/test
// // @desc   返回的请求的json数据
// // @access public
// router.get('/test', (req, res) => {
//   res.json({ msg: 'login works' });
// });

// // @route  POST api/users/register
// // @desc   返回的请求的json数据
// // @access public
// router.post('/register', (req, res) => {
//   // 查询数据库中是否已存在该手机号
//   User.findOne({ phone: req.body.phone}).then(user => {
//     if (user) {
//       return res.status(400).json('该手机号码已被注册!');
//     } else {
//       // console.log("req.body: \n");
//       console.log(req.body);
//       const newUser = new User({
//         name: req.body.name,
//         phone: req.body.phone,
//         password: req.body.password,
//       });
//       console.log("User: \n");
//       console.log(newUser);
//       bcrypt.genSalt(10, (err, salt) => {
//         bcrypt.hash(newUser.password, salt, (err, hash) => {
//           if (err) throw err;

//           newUser.password = hash;

//           newUser
//             .save()
//             .then(user => res.json(user))
//             .catch(err => console.log(err));
//         });
//       });
//     }
//   });
// });



// // @route  POST api/users/login
// // @desc   返回token jwt passport
// // @access public
// router.post('/login', (req, res) => {
//   const phone = req.body.phone;
//   const password = req.body.password;
//   // 查询数据库
//   User.findOne({ phone }).then(user => {
//     if (!user) {
//       return res.status(404).json('用户不存在!');
//     }

//     // 密码匹配
//     bcrypt.compare(password, user.password).then(isMatch => {
//       if (isMatch) {
//         const payload = {
//           id: user.id,
//           name: user.name,
//           // avatar: user.avatar,
//           identity: user.identity
//         };
//         jwt.sign(payload, keys.secretOrKey, { expiresIn: 20 }, (err, token) => {
//           if (err) throw err;
//           res.json({
//             success: true,
//             token: 'Bearer ' + token
//           });
//         });
//       } else {
//         return res.status(400).json('密码错误!');
//       }
//     });
//   });
// });

// @route  GET api/users/current
// @desc   返回当前用户信息
// @access Private
// router.get(
//   '/current',
// //   passport.authenticate('jwt', { session: false }),
//   (req, res) => {
//     res.json({
//       id: req.user.id,
//       name: req.user.name,
//       phone: req.user.phone,
// 	  favorites: req.user.favorites,
// 	  posts: req.user.posts,
//     });
//   }
// );


// // @route  POST api/users/edit
// // @desc   编辑用户信息接口
// // @access Private
// router.post(
//   '/edit',
//   passport.authenticate('jwt', { session: false }),
//   (req, res) => {
//     const userFields = {};
//     if (req.body.name) userFields.name = req.body.name;
//     if (req.body.phone) userFields.phone = req.body.phone;
//     if (req.body.password) userFields.password = req.body.password;
//     if (req.body.avatar) userFields.avatar = req.body.avatar; // 添加头像字段

//     User.findOneAndUpdate(
//       { _id: req.user.id },
//       { $set: userFields },
//       { new: true }
//     )
//       .then(user => {
//         res.json(user);
//       })
//       .catch(err => {
//         console.log(err);
//         res.status(500).json({ error: '服务器内部错误' });
//       });
//   }
// );






// // @route  GET api/users
// // @desc   获取所有用户信息
// // @access Private
// router.get(
//   '/',
//   passport.authenticate('jwt', { session: false }),
//   (req, res) => {
//     User.find()
//       .then(users => {
//         if (!users || users.length === 0) {
//           return res.status(404).json('没有任何内容');
//         }
//         res.json(users);
//       })
//       .catch(err => res.status(400).json(err));
//   }
// );

// module.exports = router;
