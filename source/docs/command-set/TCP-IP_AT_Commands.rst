TCP/IP AT 命令集
==================================================

本章节介绍驱动TCP/IP指令集，此指令集针对不同的模组会有所不同的适配，具体差异请移步：:doc:`../instruction/other/firmware_differences`。

 - :ref:`AT+SOCKET <cmd-SOCKET>`： 创建Socket连接
 - :ref:`AT+SOCKETSEND <cmd-SOCKETSEND>`：通过 socket 发送数据(长数据模式)
 - :ref:`AT+SOCKETSENDLINE <cmd-SOCKETSENDLINE>`：通过 socket 发送数据(单行模式)
 - :ref:`AT+SOCKETREAD <cmd-SOCKETREAD>`：从 socket 读取数据
 - :ref:`AT+SOCKETDEL <cmd-SOCKETDEL>`：删除指定 socket 连接
 - :ref:`AT+SOCKETRECVCFG <cmd-SOCKETRECVCFG>`：设置 socket 接收模式
 - :ref:`AT+SOCKETTT <cmd-SOCKETTT>`：进入 socket 透传模式
 - :ref:`AT+SOCKETAUTOTT <cmd-SOCKETAUTOTT>`： 自动进入 socket 透传配置
 - :ref:`AT+SSLCRET <cmd-SSLCRET>`： AT+SSLCRET 查询和设置SSL证书
 - :ref:`AT+WDOMAIN <cmd-WDOMAIN>`： 通过DNS解析查询域名的IP地址
 - :ref:`AT+WDNS <cmd-WDNS>`： 查询/设置DNS解析服务器

.. _cmd-SOCKET:

AT+SOCKET 创建 socket 连接
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+SOCKET=<type>[,<remote host>],<port>[,<keep alive>,<conID>]

**响应：**

::

    OK

参数
^^^^

-  **<type>**：socket 类型。
     -  1：UDPServer
     -  2：UDPClient
     -  3：TCPServer
     -  4：TCPClient
     -  5：TCPSeed(占位类型，不可用，这个类型是在客户端连接的模组 tcp server 时产生的，无法主动创建)
     -  6：SSLServer
     -  7：SSLClient
     -  8：SSLSeed(占位类型，不可用，这个类型是在客户端连接的模组 ssl server 时产生的，无法主动创建)
-  **<remote host>**：当 type 为客户端的时候此参数为必选，表示需要连接的服务器的域名或者 IP，server 的时候不用设置(直接跳过，eg：AT+SOCKET=3,10086)
-  **<port>**：当 type 为客户端的时候表示要连接的服务器的端口号，type 为服务端的时候表示本地 server 需要监听的端口号
-  **<keep alive>**：TCP keep-alive 间隔
     - 0 表示禁用
     - 1~7200 表示检测间隔，单位：秒(预留功能，暂时没有实现)
-  **<conID>**：指定新连接的 ConID

说明
^^^^

- 创建Socket, 并发起连接。


示例
^^^^

::

    //UDPServer
    AT+SOCKET=1,8001

    //UDPClient
    AT+SOCKET=2,192.168.31.239,23333

    //TCPServer
    AT+SOCKET=3,8888

    //TCPClient
    AT+SOCKET=4,192.168.31.239,60000


查询命令
^^^^^^^^

**命令：**

::

    AT+SOCKET? 

**响应：**

::

    <ConID>,<type>,<status>,<remote host>,<remote port>,<local port>,<server ConID>
    OK

参数
^^^^

-  **<type>**：socket 类型。
     -  1：UDPServer
     -  2：UDPClient
     -  3：TCPServer
     -  4：TCPClient
     -  5：TCPSeed(本地创建的 TCPServer，有其他用户用 tcpclient 连接上后就会产生一个 TCPSeed)
     -  6：SSLServer
     -  7：SSLClient
     -  8：SSLSeed(有客户端连接模组的 ssl server 时产生时会创建一个 SSLSeed)
-   **<Status>**：连接状态。
     -  1：Connected
     -  2：Disconnect
     -  3：Connecting
     -  4：ConnectFail
-   **<remote host>**：client 模式连接的远程地址，server 模式暂未设置
-   **<remote port>**：client 模式连接的远程端口，server 模式暂未设置，显示默认值-1
-   **<local port>**：server 模式显示的是本地监听端口，client 模式暂未设置，显示默认值-1
-   **<server ConID>**：type 为 TCPSeed 的时候这个表示该连接是从哪个 tcp server 创建的，其它 type 默认是-1

说明
^^^^

- 注意：

示例
^^^^

::

    AT+SOCKET?
    1,4,3,192.168.31.239,60000,-1,0

    OK


.. _cmd-SOCKETSEND:

AT+SOCKETSEND 通过 socket 发送数据(长数据模式)
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

   AT+SOCKETSEND=<ConID>,<length>

**响应：**

::

    OK

参数
^^^^

-  **<ConID>**：创建 SOCKET 连接后获取到的连接 ID
    - 注意：TCPServer 的连接无法发送，只能给客户端连接到 TCPServer 后创建的 seed 才能发送数据；UDP server 必须先收到客户端数据才可以发送，发送对象为第一次收到数据的对象
-  **<length>**：要发送的数据长度
    - 指令执行完毕后会显示一个”>”收到此符号后可以开始输入要发送的数据(可以输入任意 HEX 数据，不限字符串)，当接收到 length 个数据后开始发送数据。


说明
^^^^

- 向指定连接发送数据，当指令执行完毕后会在第二行出现一个“>”符号，出现这个符号后就可以开始输入数据了(可以输入任意数据，不限定数据内容)，当接收到length 个字节的数据后就会停止接收，开始发送(如果长度超过单包最大长度数据就会分包，默认超过 1024 字节后会对数据进行分包)特点：该模式可以发送任意长度数据(超长会被分包)，并且可以接收任意字符


示例
^^^^

::

    AT+SOCKETSEND=1,3
    >123
    OK
 
.. _cmd-SOCKETSENDLINE:

AT+SOCKETSENDLINE 通过 socket 发送数据(单行模式)
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+SOCKETSENDLINE=<ConID>,<length>,<data>

**响应：**

::

    OK

参数
^^^^

-  **<ConID>**：创建 SOCKET 连接后获取到的连接 ID
    - 注意：TCPServer 的连接无法发送，只能给客户端连接到 TCPServer 后创建的 seed 才能发送数据；UDP server 必须先收到客户端数据才可以发送，发送对象为第一次收到数据的对象
-  **<length>**：要发送的数据长度。
-  **<data>**：数据内容


说明
^^^^

- 向指定连接发送数据特点：该模式使用较为简单，但是长度受限(一条 AT 指令的最大长度有限)，如果有特殊字符需要将整个参数用双引号括起来，如果参数中有双引号需要加转义字符。

示例
^^^^

::

    AT+SOCKETSENDLINE=2,10,1234567890

    OK

.. _cmd-SOCKETREAD:

AT+SOCKETREAD 从 socket 读取数据
------------------------------------------


执行命令
^^^^^^^^

**命令：**

::

    AT+SOCKETREAD=<ConID>

**响应：**

::

    OK

参数
^^^^

-  **<ConID>**：ConID：创建 SOCKET 连接后获取到的连接 ID
    - 注意 TCPServer 的连接无法收发数据，只能给客户端连接到 TCPServer 后创建的 seed 才能收发送数据；UDP Client 需要先发送一次数据之后 server 端获取到本地的端口才可以向该 upd client 发送数据。

说明
^^^^

- 从指定连接读取数据。注意：读取的时候是按包读取的，一次读取一包数据


示例
^^^^

::

    +EVENT:SocketDown,1,21
    AT+SOCKETREAD=1
    +SOCKETREAD,1,21,Hello From TCP Server
    OK


.. _cmd-SOCKETDEL:

AT+SOCKETDEL 删除指定 socket 连接
------------------------------------------


执行命令
^^^^^^^^

**命令：**

::

    AT+SOCKETDEL=<ConID>

**响应：**

::

    OK

参数
^^^^

-  **<ConID>**：要删除的连接 ID。


说明
^^^^

- 删除指定 socket 连接。 注意：seed 因为是客户端发起的，server 无法重连，所以 seed 断开后需要手动删除连接(删除连接后接收到的数据也会被清空)


示例
^^^^

::

    AT+SOCKETDEL=1

    OK


.. _cmd-SOCKETRECVCFG:

AT+SOCKETRECVCFG 设置 socket 接收模式
------------------------------------------


执行命令
^^^^^^^^

**命令：**

::

    AT+SOCKETRECVCFG=<mode>

**响应：**

::

    OK

参数
^^^^

-  **<mode>**：

   -  0：被动模式(默认)，该模式下收到数据后打印只提示+EVENT:SocketDown,<ConID>,<length> 不打印数据内容
   -  1：主动模式，该模式下收到 socket 数据直接将收到的数据以如下格式打印+EVENT:SocketDown,<ConID>,<length>,<date>


说明
^^^^

- 设置 socket 接收数据的打印模


示例
^^^^

::

    AT+SOCKETRECVCFG=0

    OK


.. _cmd-SOCKETTT:

AT+SOCKETTT 进入 socket 透传模式
------------------------------------------


执行命令
^^^^^^^^

**命令：**

::

    AT+SOCKETTT

**响应：**

::

    > //收到这个表示透传开启了，可以收发数据了
    OK //连续输入三个加号+++会退出透传，透传退出时打印\r\nOK\r\n

说明
^^^^

- 进入透传模式必须满足以下任意一个条件
    - 当前仅有一个 client 连接(通过 client 透传)
    - 仅有一个 server 和一个 seed 连接(可以通过客户端连接模组 server 后产生的seed 透传，该模式必须手动进入，无法自动进入)
    - 仅有一个 UDPClient
    - 仅有一个 UDPServer(注意，透传模式不建议使用 UDP server，默认透传对象是第一个连接的 client 端，如果有其他连接向模组发起了通信可能导致后续透传对象出错)
- 输入+++后可以退出透传模式，进入 AT 指令模式

示例
^^^^

::

    AT+SOCKET=4,192.168.31.98,18 //创建 tcp client
    connect success ConID=1
    OK

    AT+SOCKETTT //进入透传模式
    >send to module //此时发送的数据会透传到目标，目标发送的数据会透传到本地
    OK //当输入连续的三个加号后退出透传模式


执行命令
^^^^^^^^

**命令：**

::

    // UDPServerTTMode：设置 UDP server 透传模式
    AT+SOCKETTT=UDPServerTTMode

**响应：**

::

    > //收到这个表示透传开启了，可以收发数据了
    OK //连续输入三个加号+++会退出透传，透传退出时打印\r\nOK\r\n


参数
^^^^

-  **<UDPServerTTMode>**：UDP server 透传模式

   - 0：透传对象固定为第一次通讯的客户端，后续有其他客户端通信也不会改变通信对象
   - 2：透传对象会动态修改为最后一次通信的客户端


说明
^^^^

- 进入 SOCKET 透传模式。 注意：UDP server 默认的透传对象是第一次通信的 client 客户端

示例
^^^^

::

    AT+SOCKETTT=2



.. _cmd-SOCKETAUTOTT:

AT+SOCKETAUTOTT 自动进入 socket 透传配置
------------------------------------------


执行命令
^^^^^^^^

**命令：**

::

    AT+SOCKETAUTOTT=<type>[,<remote host>],<port>

**响应：**

::

    OK

参数
^^^^

-  **<type>**：socket 类型
    -  0：禁用自动进入透传模式
    -  1：自动进入 UDPServer 透传模式
    -  2：自动进入 UDPClient 透传模式
    -  3：占位类型，不可用
    -  4：自动进入 TCPClient 透传模式
    -  5：占位类型，不可用
    -  6：占位类型，不可用
    -  7：自动进入 SSLClient 透传模式
    -  8：占位类型，不可用
-  **<remote host>**：当 type 为客户端的时候此参数为必选，表示需要连接的服务器的域名或者 IP，server 的时候不用设置(跳过该参数，eg:AT+SOCKETAUTOTT=1,10086)
-  **<port>**：当 type 为客户端的时候表示要连接的服务器的端口号，type 为服务端的时候表示本地 server 需要监听的端口号


说明
^^^^

- 创建对应 socket 连接后自动进入透传模式该指令设置完成后需要配合 AT+WAUTOCONN 使用，配置完成后复位生效。上电后自动连接 Wi-Fi （AT+WAUTOCONN 配置）Wi-Fi  连接成功后自动创建 socket 连接，socket 创建成功后自动进入透传模式（本指令设置）


示例
^^^^

::

    AT+SOCKETAUTOTT=4,192.168.31.239,60000

    OK



查询命令
^^^^^^^^

**命令：**

::

    AT+SOCKETAUTOTT? 

**响应：**

::

    +SOCKETAUTOTT:<type>,<remote host>,<remote port>
    OK

参数
^^^^

-  **<type>**：socket 类型
    -  0：禁用自动进入透传模式
    -  1：自动进入 UDPServer 透传模式
    -  2：自动进入 UDPClient 透传模式
    -  3：占位类型，不可用
    -  4：自动进入 TCPClient 透传模式
    -  5：占位类型，不可用
    -  6：占位类型，不可用
    -  7：自动进入 SSLClient 透传模式
    -  8：占位类型，不可用
-  **<remote host>**：当 type 为客户端的时候此参数为必选，表示需要连接的服务器的域名或者 IP，server 的时候不用设置(跳过该参数，eg:AT+SOCKETAUTOTT=1,10086)
-  **<remote port>**：当 type 为客户端的时候表示要连接的服务器的端口号，type 为服务端的时候表示本地 server 需要监听的端口号
-  **<local port>**：server 模式显示的是本地监听端口，client 模式暂未设置，显示默认值-1


说明
^^^^

- 查询当前自动透传配置信息

示例
^^^^

::

    AT+SOCKETAUTOTT?

    +SOCKETAUTOTT:4,192.168.31.239,60000
    OK



.. _cmd-SSLCRET:

AT+SSLCRET 查询和设置SSL证书
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+SSLCRET=<type>[,<length>]

**响应：**

::

    > //收到这个符号表示可以开始写证书了
    OK

参数
^^^^

-  **<type>**：操作的证书类型。
    -  1：CA 根证书
    -  2：客户端公钥
    -  3：客户端私钥
-  **<length>**：证书长度，当省略这个参数的时候表示查询对应的证书，带该参数时设置证书长度

说明
^^^^

- 查询和设置 SSL 证书只有一个参数的时候表示查询当前设置的证书内容，有两个参数的时候表示需要设置证书. 证书为空时客户端不加载证书，自动获取


示例
^^^^

::

    //设置证书
    AT+SSLCRET=1,10
    >1234567890
    OK

    //查询证书
    AT+SSLCRET=1
    +SSLCRET:1,10,1234567890
    OK


.. _cmd-WDOMAIN:

AT+WDOMAIN 通过DNS解析查询域名的IP地址
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

   AT+WDOMAIN=<server name>

**响应：**

::
    
    +WDOMAIN:<IP>

    OK

示例
^^^^

::

    AT+WDOMAIN=www.baidu.com
    +WDOMAIN:14.119.104.189
    OK
 
.. _cmd-WDNS:

AT+WDNS  查询/设置DNS解析服务器
------------------------------------------

查询命令
^^^^^^^^

描述
^^^^

- 查询DNS解析服务器


**命令：**

::

    AT+WDNS?

**响应：**

::

    +WDNS:<DNS IP1>,<DNS IP2>
    OK


示例
^^^^

::

    AT+WDNS?
    +WDNS:192.168.3.1,0.0.0.0
    OK


执行命令
^^^^^^^^

描述
^^^^

- 设置DNS解析服务器

**命令：**

::

    AT+WDNS=<"DNS IP1">[,<"DNS IP2">]

**响应：**

::

    +WDNS:<DNS IP1>[,DNS IP2]
    OK


参数
^^^^

-  **<DNS IP1/DNS IP2>**：域名解析服务器


示例
^^^^

::

    AT+WDNS=114.114.114.114

    +WDNS:114.114.114.114
    OK 

