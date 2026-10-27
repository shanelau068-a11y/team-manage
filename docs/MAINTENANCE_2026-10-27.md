# 2026-10-27 维护记录

- SQLAlchemy异步依赖改为sqlalchemy[asyncio]，补上新版本必需的greenlet。
- 移除默认管理员密码及示例签名密钥，启动要求自配凭据并验证长度；新增配置回归测试。

实际结果及范围见[验证记录](VERIFICATION.md)。
