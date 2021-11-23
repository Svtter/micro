# Features

0. Production-level framework.
1. All service defined in one process.
2. Provide different port for service.

编写 service 的时候，如果想要测试，应该继承 client，进行编写；
我们可以隔离代码 service 和 client 的代码；
client 不依赖于 service 存在。

## Security

1. Based on HTTPS.
