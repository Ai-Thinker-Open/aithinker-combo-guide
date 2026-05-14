MQTT AT 示例
=============================================================

本文档主要提供在模组设备上运行 :doc:`../command-set/MQTT_AT_Commands` 命令的详细示例。

.. contents::
   :local:
   :depth: 1

.. Important::
  - 文档中所描述的例子均基于设备已连接 Wi-Fi 的前提。
  - 此示例针对不同的模组会有所不同的适配，具体差异请移步查询您手上的模组指令支持情况：:doc:`../instruction/other/firmware_differences`。


基于 TCP 的 MQTT 连接
------------------------------------------------------------------------
本例需要连接的mqtt服务器ip:192.168.31.43，端口：1883，client_id：1234，用户名：admin，密码：public

1. 设置服务器域名
  
  命令：

  .. code-block:: none

      AT+MQTT=1,192.168.31.43

  响应：

  .. code-block:: none

      OK

2. 设置服务器端口
  
  命令：

  .. code-block:: none

      AT+MQTT=2,1883

  响应：

  .. code-block:: none

      OK        

3. 设置连接方式
  
  命令：

  .. code-block:: none

      AT+MQTT=3,1

  响应：

  .. code-block:: none

      OK 

4. 设置用户ID
  
  命令:

  .. code-block:: none

      AT+MQTT=4,1234

  响应：

  .. code-block:: none

      OK 

5. 设置MQTT用户名
  
  命令:

  .. code-block:: none

      AT+MQTT=5,admin

  响应：

  .. code-block:: none

      OK        

6. 设置MQTT密码
  
  命令:

  .. code-block:: none

      AT+MQTT=6,public

  响应：

  .. code-block:: none

      OK  

7. 连接MQTT服务器
  
  命令:

  .. code-block:: none

      AT+MQTT

  响应：

  .. code-block:: none

      OK

      +EVENT:MQTT_CONNECT               


说明：

- 您输入的 MQTT域名或IP地址可能与上述命令中的不同。


8. 订阅主题

  例如订阅一个主题为“testtopic0”：

  命令:

  .. code-block:: none

      AT+MQTTSUB=testtopic0,0

  响应：

  .. code-block:: none

      OK

9. 发布主题   

发布消息数据量少且消息类型为字符串可以用指令AT+MQTTPUB，如发布消息主题为testtopic1，发布消息为HelloWorld：

  命令

  .. code-block:: none

    AT+MQTTPUB=testtopic1,1,0,HelloWorld

  响应

  .. code-block:: none

    OK

当发布消息数据量大时可以用AT+MQTTPUBRAW，AT+MQTTPUBRAW指令不限制消息类型，可以发送字符串也可以发送hex类型数据。如发布消息主题为testtopic1，发布消息为1122334455667788：


  命令

  .. code-block:: none

    AT+MQTTPUBRAW=testtopic1,1,0,8		

  响应

  .. code-block:: none

    >

  输入需要发送的数据

  .. code-block:: none

    1122334455667788
 
  响应

  .. code-block:: none

    OK

