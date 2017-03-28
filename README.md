## 计划

### 启动两个线程：server线程 、client 线程
1. server 线程
作为acceptor，负责接收client端调用，给出相应的结果

2. client 线程
启动余于3个服务，也就会启动相应的client 线程
* 每个client 线程随机发起proposol
* 发起proposor的client 同其他 server 进行 basic paxos 交互

