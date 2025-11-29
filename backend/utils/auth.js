// 创建一个检测登录状态的中间件
const checkAuth = (req, res, next) => {
  // 从请求头中获取 token
  const token = req.headers.authorization;

  if (token) {
    // 验证 token
    jwt.verify(
      token.replace("Bearer ", ""),
      keys.secretOrKey,
      (err, decoded) => {
        if (err) {
          // token 验证失败
          return res.status(401).json("无效的 token");
        } else {
          // token 验证成功
          req.user = decoded; // 将用户信息存储在 req 对象中
          next(); // 继续下一步操作
        }
      }
    );
  } else {
    // 没有提供 token
    return res.status(401).json("未提供 token");
  }
};



module.exports = checkAuth;
