# team-manage：项目运行与AI接手

上游FastAPI Team管理与兑换邀请系统的Fork，包含数据库、管理网页和外部账户集成。

## 仓库身份

- 分类：服务与部署；类型：python。
- 默认分支：`main`；当前可见性：公开。
- 本说明针对本仓库当前文件；历史本机绝对路径与相似项目不能作为当前运行位置。

## 先读这些文件

- [README.md](<../README.md>)
- [app/main.py](<../app/main.py>)
- [app/config.py](<../app/config.py>)
- [requirements.txt](<../requirements.txt>)
- [.env.example](<../.env.example>)
- [integration_docs.md](<../integration_docs.md>)

## 安装和启动

```powershell
python -m pip install -r requirements.txt
Copy-Item .env.example .env
python -m uvicorn app.main:app --host 127.0.0.1 --port 8008
```



## 配置名称

从源码及示例提取到的环境变量名称：

`ADMIN_PASSWORD`、`APP_HOST`、`APP_NAME`、`APP_PORT`、`APP_VERSION`、`DATABASE_ECHO`、`DATABASE_URL`、`DEBUG`、`JWT_VERIFY_SIGNATURE`、`LOG_LEVEL`、`PROXY`、`PROXY_ENABLED`、`SECRET_KEY`、`TIMEZONE`。

这些只是名称，不是已配置的值；有些是工具或部署变量，并非全部必填。优先读.env.example及引用处，不把真实密钥写进源码或提交。

## 数据与搬迁

启动前在.env设置独立SECRET_KEY和管理员密码，并确认SQLite路径。数据库、加密主密钥与合法账户授权需分别备份，缺失密钥可能无法恢复加密记录。

## 怎么验证

先执行 [验证记录](VERIFICATION.md) 所列命令，再按改动检查实际页面或输出。没有测试脚本时不能把占位npm test当作通过。仅文档更改检查链接和路径；涉及数据、几何、金额或接口的修改运行相应回归测试。

- Fork保留上游来源和许可证。本轮不邀请成员、不兑换、不导入真实账号，也不触发Webhook。
- Docker、外部服务条款、账户权限和生产环境部署需由实际服务状态验证，构建/路由检查不能证明所有集成可用。

## 继续维护

先读根目录AGENTS.md；若它是CLAUDE.md的链接则直接读后者。保留已有项目约定。修改前确认分支、当前差异、数据目录与实际服务。完成后更新本说明/验证记录，提交明确的源码和文档路径，并核对GitHub远端提交。公开状态、旧版、URL与业务数据需按用户既有约定保持。
