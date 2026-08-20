MQTT AT 命令集
==================================================

本章节介绍驱动MQTT指令集，此指令集针对不同的模组会有所不同的适配，具体差异请移步：:doc:`../instruction/other/firmware_differences`。

 - :ref:`AT+MQTT <cmd-MQTT>`：MQTT 的配置和连接
 - :ref:`AT+MQTTVER <cmd-MQTTVER>`：查询和设置 MQTT 版本
 - :ref:`AT+MQTTBUF <cmd-MQTTBUF>`：查询和设置 MQTT 收发 buf 大小
 - :ref:`AT+MQTTKEEPALIVE <cmd-MQTTKEEPALIVE>`：查询和设置 MQTT 心跳间隔
 - :ref:`AT+MQTTCRET <cmd-MQTTCRET>`：查询和设置 MQTT SSL 证书
 - :ref:`AT+MQTTDISCONN <cmd-MQTTDISCONN>`：断开 MQTT 连接
 - :ref:`AT+MQTTPUB <cmd-MQTTPUB>`：发布 MQTT 消息
 - :ref:`AT+MQTTPUBRAW <cmd-MQTTPUBRAW>`：发布指定长度 MQTT 消息
 - :ref:`AT+MQTTSUB <cmd-MQTTSUB>`：订阅 MQTT 消息
 - :ref:`AT+MQTTUNSUB <cmd-MQTTUNSUB>`：取消订阅 MQTT 消息

.. _cmd-MQTT:

AT+MQTT 配置和连接
------------------------------------------


配置命令
^^^^^^^^

**命令：**

::

    //配置参数
    AT+MQTT=<key>,<data>

**响应：**

::

    OK

参数
^^^^

-  **<key>**：MQTT参数。
     -  1：设置连接的域名或 IP
     -  2：设置服务器端口号
     -  3：设置连接方式
            - 预留，暂时默认 1：使用 tcp 连接
     -  4：设置客户端ID
     -  5：设置用户名
            - 最大长度63字节
     -  6：设置登录密码
            - 最大长度63字节
     -  7：设置遗嘱消息，格式为AT+MQTT=7,<LWT_topic>,<LWT_qos>,<LWT_Retained>,<LWTpayload>
            -  LWT_topic：遗嘱主题(不需要遗嘱这里设置为"")
            -  LWT_qos：遗嘱 QOS(0/1/2)
            -  LWT_Retained：遗嘱 retained(0/1)
            -  LWTpayload：遗嘱消息内容
-  **<data>**：设置的参数。

说明
^^^^

- 配置MQTT连接参数。


执行命令
^^^^^^^^

**命令：**

::

    //启用连接
    AT+MQTT

**响应：**

::

    OK


示例
^^^^

::

    //设置域名
    AT+MQTT=1,192.168.202.10 
    OK

    //设置端口号
    AT+MQTT=2,1883
    OK
    
    //设置连接方式
    AT+MQTT=3,1
    OK
    
    //设置用户 ID
    AT+MQTT=4,client_id 
    OK

    //设置 MQTT 用户名
    AT+MQTT=5,admin
    OK

    //设置 MQTT 密码
    AT+MQTT=6,public
    OK

    //设置遗嘱主题 LWTTOPIC，qos0，开启retained，负载消息为 123456；注意：取消遗嘱消息则设置为 AT+MQTT=7,"",0,0,""
    AT+MQTT=7,"LWTTOPIC",0,1,"123456"
    OK

    //查询 MQTT 连接和配置情况
    AT+MQTT? 
    +MQTT:0,192.168.202.10,1883,1,client_id,admin,public
    OK

    //连接 MQTT
    AT+MQTT 
    OK

    //MQTT 连接成功
    +EVENT:MQTT_CONNECT


查询命令
^^^^^^^^

**命令：**

::

    AT+MQTT? 

**响应：**

::

    +MQTT:<MQTT_status>,<Host_name>,<Port>,<scheme>,<client_id>,<username>,<password>,<LWT_topic>,<LWT_qos>,<LWT_Retained>,<LWTpayload>
    OK

参数
^^^^

-   **<MQTT_status>**：MQTT 连接状态。
        - 0：初始状态
        - 1：正在连接
        - 2：正在订阅消息
        - 3：连接成功
-   **<Host_name>**：服务器域名。
-   **<Port>**：服务器端口号。
-   **<scheme>**：连接方式
        - 1：TCP 连接
-   **<client_id>**：MQTT 用户 ID。
-   **<username>**：MQTT 用户名。
-   **<password>**：MQTT 密码。
-   **<LWT_topic>**：遗嘱主题。
-   **<LWT_qos>**：遗嘱 QOS。
-   **<LWT_Retained>**：遗嘱 retained。
-   **<LWTpayload>**：遗嘱消息内容。


说明
^^^^

- 注意：执行连接前需要先设置好 MQTT 参数，如果当前 MQTT 任务已经启动再次执行会重新连接（更改服务器的话建议先删除所有订阅后重连）
- 注意：这里是异步连接，显示 OK 只是表示 MQTT 任务启动，连接状态需要通过AT+MQTT?查询或等待收到 URC 数据“+EVENT:MQTT_CONNECT


示例
^^^^

::

    AT+MQTT? //查询 MQTT 连接和配置情况
    +MQTT:0,192.168.202.10,1883,1,client_id,admin,public,LWTTOPIC,0,1,123456
    OK


.. _cmd-MQTTVER:

AT+MQTTVER 查询和设置 MQTT 版本
------------------------------------------

查询/设置命令
^^^^^^^^^^^^^^

**命令：**

::

    AT+MQTTVER=<version>
    AT+MQTTVER?

**响应：**

::

    OK
    +MQTTVER:<version>
    OK

参数
^^^^

-  **<version>**：MQTT 协议版本。
    - 3：MQTT 3.1
    - 4：MQTT 3.1.1

说明
^^^^

- 查询或设置当前 MQTT 协议版本。
- 若未设置，系统会使用默认版本。

示例
^^^^

::

    AT+MQTTVER=4
    OK

    AT+MQTTVER?
    +MQTTVER:4
    OK

.. _cmd-MQTTBUF:

AT+MQTTBUF 查询和设置 MQTT 收发 buf 大小
------------------------------------------

查询/设置命令
^^^^^^^^^^^^^^

**命令：**

::

    AT+MQTTBUF=<size>
    AT+MQTTBUF?

**响应：**

::

    OK
    +MQTTBUF:<size>
    OK

参数
^^^^

-  **<size>**：MQTT 收发缓冲区大小，单位：字节。

说明
^^^^

- 用于配置 MQTT 发送和接收数据使用的缓冲区大小。
- 该参数会影响单次收发数据的最大长度。

示例
^^^^

::

    AT+MQTTBUF=1024
    OK

    AT+MQTTBUF?
    +MQTTBUF:1024
    OK

.. _cmd-MQTTKEEPALIVE:

AT+MQTTKEEPALIVE 查询和设置 MQTT 心跳间隔
------------------------------------------

查询/设置命令
^^^^^^^^^^^^^^

**命令：**

::

    AT+MQTTKEEPALIVE=<seconds>
    AT+MQTTKEEPALIVE?

**响应：**

::

    OK
    +MQTTKEEPALIVE:<seconds>
    OK

参数
^^^^

-  **<seconds>**：MQTT 心跳保活间隔，单位：秒。

说明
^^^^

- 用于配置 MQTT 客户端的保活心跳时间。
- 若连接超时未收到心跳响应，客户端将视为连接失效。

示例
^^^^

::

    AT+MQTTKEEPALIVE=60
    OK

    AT+MQTTKEEPALIVE?
    +MQTTKEEPALIVE:60
    OK

.. _cmd-MQTTCRET:

AT+MQTTCRET 查询和设置 MQTT SSL 证书
------------------------------------------

查询/设置命令
^^^^^^^^^^^^^^

**命令：**

::

    AT+MQTTCRET=<mode>,<cert>
    AT+MQTTCRET?

**响应：**

::

    OK
    +MQTTCRET:<mode>,<cert>
    OK

参数
^^^^

-  **<mode>**：证书模式。
    - 0：关闭
    - 1：启用
-  **<cert>**：证书内容或证书索引，具体由固件实现决定。

说明
^^^^

- 用于设置 MQTT 连接时使用的 SSL/TLS 证书。
- 若设备固件支持证书加载功能，可通过此命令配置证书。

示例
^^^^

::

    AT+MQTTCRET=1,ca.pem
    OK

    AT+MQTTCRET?
    +MQTTCRET:1,ca.pem
    OK

.. _cmd-MQTTDISCONN:

AT+MQTTDISCONN 断开 MQTT 连接
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+MQTTDISCONN

**响应：**

::

    OK

说明
^^^^

- 主动断开当前 MQTT 连接。
- 连接断开后，可重新执行 :ref:`AT+MQTT <cmd-MQTT>` 进行重连。

示例
^^^^

::

    AT+MQTTDISCONN
    OK

.. _cmd-MQTTPUB:

AT+MQTTPUB 发布MQTT消息
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+MQTTPUB=<topic>,<qos>,<Retained>,<payload>

**响应：**

::

    OK

参数
^^^^

-  **<topic>**：要发布的主题。
-  **<qos>**：qos 等级(0,1,2)。
-  **<Retained>**：
    - 0：普通消息
    - 1：Retained消息
-  **<payload>**：数据内容(最大长度为1024个字节)


说明
^^^^

- 发布MQTT消息。


示例
^^^^

::
    
    AT+MQTTPUB=testtopic,1,0,456
    OK
 
.. _cmd-MQTTPUBRAW:

AT+MQTTPUBRAW 发布指定长度 MQTT 消息
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+MQTTPUBRAW=<topic>,<qos>,<Retained>,<length>

**响应：**

::

    OK

参数
^^^^

-  **<topic>**：要发布的主题。
-  **<qos>**：qos 等级(0,1,2)。
-  **<Retained>**：
    - 0：普通消息
    - 1：Retained消息
-  **<length>**：数据长度


说明
^^^^

- 发布指定长度的MQTT消息。


示例
^^^^

::


    AT+MQTTPUBRAW=testtopic,1,0,10 //向 testtopic 发送 10 字节的数据
    > //收到这个字符之后开始输入要发送的数据
    
    OK //当收到 10 字节数据后就会发送数据(可以是任意数据)，发送完成会显示 OK

.. _cmd-MQTTSUB:

AT+MQTTSUB 订阅 MQTT 消息
------------------------------------------


执行命令
^^^^^^^^

**命令：**

::

    AT+MQTTSUB=<topic>,<qos>

**响应：**

::

    OK

参数
^^^^

-  **<topic>**：要订阅的主题。(最多订阅四个主题)
-  **<qos>**：qos 等级(0,1,2)。

说明
^^^^

- 配置MQTT订阅主题。


示例
^^^^

::

    AT+MQTTSUB=testtopic0,0
    OK


查询命令
^^^^^^^^

**命令：**

::

    AT+MQTTSUB?

**响应：**

::

    <status>,<Topic>
    ... 
    OK

参数
^^^^

-   **<status>**：订阅状态。
        - 0：初始化状态
        - 1：订阅中(首次订阅)
        - 2：订阅中(断线重连后重新订阅)
        - 3：订阅成功
-   **<Topic>**：订阅的主题。


说明
^^^^

- 查询已经配置MQTT订阅主题。

示例
^^^^

::

    AT+MQTTSUB?
    3,testtopic0
    3,testtopic1
    OK

.. _cmd-MQTTUNSUB:

AT+MQTTUNSUB 取消订阅 MQTT 消息
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+MQTTUNSUB=<topic>

**响应：**

::

    OK

参数
^^^^

-  **<topic>**：取消订阅的主题。

说明
^^^^

- 取消订阅 MQTT 消息。


示例
^^^^

::

    AT+MQTTSUB=testtopic0

    OK

