import Vue from 'vue'
import Router from 'vue-router'

import Register from './views/Register'
import NotFound from './views/404'
import Login from './views/Login'
import Home from './views/Home'
import HomeAfterLogin from './views/HomeAfterLogin'

import UserProfile from './views/UserProfile'

import SellCar from './views/SellCar' 
import Search from './views/Search'
import CarDetails from './views/CarDetails'
import PopularCar from './views/PopularCar'
import PriceTimeSeries from './views/PriceTimeSeries'
import Search2 from './views/Search2'
import EvaluateDetail from './views/EvaluateDetail'

import Board from './views/Board'
import BoardOverview from './views/BoardOverview'
import Evaluate from './views/Evaluate'
import Posts from './views/Posts'
import Favorites from './views/Favorites'
import HotCarInfo from './views/HotCarInfo'

import Search3 from './views/Search3'
import PricePredict from './views/PricePredict'




Vue.use(Router)

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '*',
      name: '/404',
      component: NotFound
    },
    {
      path: '/',
      redirect: '/home'
    },
    {
      path: '/hotcarinfo',
      name: 'hotcarinfo',
      component: HotCarInfo,
      meta: {
        requiresAuth: true, // 添加 requiresAuth 元信息，表示需要登录才能访问的路由
      },
    },
    {
      path: '/pricepredict',
      name: 'pricepredict',
      component: PricePredict,
    },
    {
      path: '/hotcarinfo/:targetCarModel',
      name: 'hotcarinfo',
      component: HotCarInfo,
      meta: {
        requiresAuth: true, // 添加 requiresAuth 元信息，表示需要登录才能访问的路由
      },
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
      meta: {
        redirectWhenLoggedIn: true, // 添加 redirectWhenLoggedIn 元信息
      },
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: {
        redirectWhenLoggedIn: true, // 添加 redirectWhenLoggedIn 元信息
      },
    },
    {
      path: '/home',
      name: 'home',
      component: Home
    },
	{
		path: '/homeafterlogin',
		name: 'homeafterlogin',
		component: HomeAfterLogin
	  },


    {
      path: '/userprofile',
      name: 'userprofile',
      component: UserProfile,
      meta: {
        requiresAuth: true, // 添加 requiresAuth 元信息，表示需要登录才能访问的路由
      },
    },



    {
      path: '/sellcar',
      name: 'sellcar',
      component: SellCar,
      meta: {
        requiresAuth: true, // 添加 requiresAuth 元信息，表示需要登录才能访问的路由
      },
    },
    {
      path: '/cardetails/:id',
      name: 'cardetails',
      component: CarDetails,
      meta: {
        requiresAuth: true, // 添加 requiresAuth 元信息，表示需要登录才能访问的路由
      },
    },

    {
      path: '/popularcar',
      name: 'popularcar',
      component: PopularCar,
      meta: {
        requiresAuth: true, // 添加 requiresAuth 元信息，表示需要登录才能访问的路由
      },
    },
    {
      path: '/pricetimeseries',
      name: 'pricetimeseries',
      component: PriceTimeSeries,
      meta: {
        requiresAuth: true, // 添加 requiresAuth 元信息，表示需要登录才能访问的路由
      },
    },
    {
      path: '/search2',
      name: 'search2',
      component: Search2,
      meta: {
        requiresAuth: true, // 添加 requiresAuth 元信息，表示需要登录才能访问的路由
      },
    },
    {
      path: '/search',
      name: 'search',
      component: Search,
      meta: {
        requiresAuth: true, // 添加 requiresAuth 元信息，表示需要登录才能访问的路由
      },
    },

    {
      path: '/board',
      name: 'board',
      component: Board,
      meta: {
        requiresAuth: true, // 添加 requiresAuth 元信息，表示需要登录才能访问的路由
      },
    },
    {
      path: '/boardoverview',
      name: 'boardoverview',
      component: BoardOverview,
      meta: {
        requiresAuth: true, // 添加 requiresAuth 元信息，表示需要登录才能访问的路由
      },
    },
    {
      path: '/evaluatedetail',
      name: 'evaluatedetail',
      component: EvaluateDetail,
      meta: {
        requiresAuth: true, // 添加 requiresAuth 元信息，表示需要登录才能访问的路由
      },
    },
    {
      path: '/evaluate',
      name: 'evaluate',
      component: Evaluate,
      meta: {
        requiresAuth: true, // 添加 requiresAuth 元信息，表示需要登录才能访问的路由
      },
    },
    {
      path: '/search3',
      name: 'search3',
      component: Search3,
      meta: {
        requiresAuth: true, // 添加 requiresAuth 元信息，表示需要登录才能访问的路由
      },
    },
    {
      path: '/posts',
      name: 'posts',
      component: Posts,
      meta: {
        requiresAuth: true, // 添加 requiresAuth 元信息，表示需要登录才能访问的路由
      },
    },
    {
      path: '/favorites',
      name: 'favorites',
      component: Favorites,
      meta: {
        requiresAuth: true, // 添加 requiresAuth 元信息，表示需要登录才能访问的路由
      },
    }, 
    
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (about.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    // }
  ]
})

// // 添加路由守卫
// router.beforeEach((to, from, next) => {
//   // const isLogin = localStorage.eleToken ? true : false;
//   // if (to.path == "/login" || to.path == "/register") {
//   //   next();
//   // } else {
//   //   isLogin ? next() : next("/login");
//   // }
//   next();
// })

// 路由守卫函数
// 部分页面需要登录后才能查看
// router.beforeEach((to, from, next) => {
//   if (to.meta.requiresAuth) {
//     const token = localStorage.getItem('token');
//     console.log(token);
//     if (!token) {
//       // 如果未登录，重定向到登录页面
//       next('/login');
//     } else {
//       // 如果已登录，继续访问受保护页面
//       next();
//     }
//   } else {
//     // 对于非受保护页面，直接访问
//     next();
//   }
//   next()
// });
router.beforeEach((to, from, next) => {

  next();
});


// router.beforeEach((to, from, next) => {
//   const token = localStorage.getItem('eletoken');
//   console.log(token);
//   if (to.matched.some(route => route.meta.requiresAuth)) {
//     // 路由需要登录才能访问
//     if (token) {
//       // 通过令牌验证用户已登录
//       next();
//     } else {
//       // 用户未登录，跳转到登录页
//       next('/login');
//     }
//   } else {
//     if (to.matched.some(route => route.meta.redirectWhenLoggedIn)) {
//       if (token) {
//         next('/userprofile');
//       }
//       else {
//         next();
//       }
//     }
//     // 路由无需登录即可访问
//     next();
//   }
// });






// // 路由守卫函数
// router.beforeEach((to, from, next) => {
//   if (to.meta.requiresAuth) {
//     const token = localStorage.getItem('token');

//     if (1) {
//       // 如果未登录，弹出提示并跳转到登录页面
//       MessageBox.alert('您未登录，请登录后再访问此页面！', '提示', {
//         confirmButtonText: '去登录',
//         callback: action => {
//           if (action === 'confirm') {
//             next('/login');
//           }
//         },
//       });
//     } else {
//       // 如果已登录，继续访问受保护页面
//       next();
//     } 
//   } else {
//     // 对于非受保护页面，直接访问
//     next();
//   }
// });







export default router;