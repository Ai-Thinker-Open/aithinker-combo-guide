云平台对接命令集
==================================================

本章节介绍对接广云物联平台指令集，此指令集针对不同的模组会有所不同的适配，具体差异请移步：:doc:`../instruction/other/firmware_differences`。

 - :ref:`AT+GWDEVICENAME <cmd-GWDEVICENAME>`：设置BLE配网设备名称
 - :ref:`AT+GWCONFIGEN <cmd-GWCONFIGEN>`：启用广云APP配网模式
 - :ref:`AT+GWCONNECTCONFIG <cmd-GWCONNECTCONFIG>`：设置广云设备密钥参数
 - :ref:`AT+GWHTTPCLIENTLINE <cmd-GWHTTPCLIENTLINE>`：启用下载证书流程
 - :ref:`AT+GWAWSCONNECT <cmd-GWAWSCONNECT>`：启用连接
 - :ref:`AT+GWAWSPUB <cmd-GWAWSPUB>`：发布数据

.. _cmd-GWDEVICENAME:

AT+GWDEVICENAME：配置配网的蓝牙名称及PID。
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+GWDEVICENAME=<“蓝牙名称”>,<厂商PID>

**响应：**

::

    OK

参数
^^^^

-  **<蓝牙名称>**:字符串类型， 配网时显示的设备名字一般以“granwin” 开头
-  **<厂商PID>**：整型，1-65535 一般由广云平台提供

说明
^^^^

- 设置BLE配网设备名称，注：需在启用配网模式前进行配置。


示例
^^^^

::

    //设置BLE配网设备名称
    AT+GWDEVICENAME="granwin_dev",137

    OK




.. _cmd-GWCONFIGEN:

AT+GWCONFIGEN：启用广云APP配网模式。
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+GWCONFIGEN

**响应：**

::

    +EVENT:BLE_CONNECT

    +EVENT:BLE_DISCONNECT

    +EVENT:BLE_CONNECT

    +EVENT:WIFI_CONNECT

    +EVENT:WIFI_GOT_IP

    +EVENT:BLE_DISCONNECT

    OK


说明
^^^^

- 启用广云APP配网模式。


示例
^^^^

::

    //进入BLE配网模式
    AT+GWCONFIGEN

    +EVENT:BLE_CONNECT

    +EVENT:BLE_DISCONNECT

    +EVENT:BLE_CONNECT

    +EVENT:WIFI_CONNECT

    +EVENT:WIFI_GOT_IP

    +EVENT:BLE_DISCONNECT



.. _cmd-GWCONNECTCONFIG:

AT+GWCONNECTCONFIG：设置广云设备密钥参数。
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+GWCONNECTCONFIG=<“clientId”>,<"Secret“>,<“productKey”>

**响应：**

::

    OK

参数
^^^^

-  **<client_id>**：客户端ID。
-  **<secret>**：设备密钥。
-  **<product_key>**：产品密钥。

说明
^^^^

- 设置广云设备密钥参数。注：该密钥参数从广云物联平台获取，需在执行下载证书及启用连接前进行配置。


示例
^^^^

::

    //设置配置连接参数
    AT+GWCONNECTCONFIG="xxxxxxxxx","xxxxxxxxx","xxxxxxxxxxxx"

    OK


.. _cmd-GWHTTPCLIENTLINE:

AT+GWHTTPCLIENTLINE：启用下载证书流程。
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+GWHTTPCLIENTLINE

**响应：**

::

    +EVENT:GET TIME:1678693267532
    +EVENT:GET TOKEN SUCCESS
    +EVENT:GET PRIVATEKEY CART SUCCESS
    +EVENT:GET DEVICE CART SUCCESSS

    OK


说明
^^^^

- 设置广云设备密钥参数。注：该密钥参数从广云物联平台获取，需在执行下载证书及启用连接前进行配置。


示例
^^^^

::

    //设置BLE配网设备名称
    AT+SECRET=KZh1eMgxxxxxxxxxx,fdjfGHe1xxxxxx,EJK6xxxxxxxx

    OK

.. _cmd-GWAWSCONNECT:

AT+GWAWSCONNECT：启用连接。
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+GWAWSCONNECT=<enable>

**响应：**

::

    OK


参数
^^^^

-  **<enable>**：
    -  0：断开连接
    -  1：建立连接


说明
^^^^

- 启用连接。注：需要完成证书后才能进行连接，完成连接后设备将默认订阅相关topic。


示例
^^^^

::

    //启用连接
    AT+GWAWSCONNECT=1

    OK


.. _cmd-GWAWSPUB:

AT+GWAWSPUB：发布数据。
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+GWAWSPUB=<type>,<payload>,<qos>

**响应：**

::

    OK


参数
^^^^

-  **<type>**：
    - 0: topic: ${productKey}/${thingName}/user/update
    - 1: topic: ${productKey}/${thingName}/user/property/query_response
    - 2: topic: ${productKey}/${thingName}/user/ota/firmware/report
-  **<payload>**：
    - json字符串
-  **<qos>**：
    -  0：qos0
    -  1：qos1
    -  2：qos2


说明
^^^^

- 发布数据。注：发布的内容为广云物联平台数据协议中json数据data对象下的内容, 涉及特殊符号"需要进行转义\\"


示例
^^^^

::

    //发布数据
    AT+GWAWSPUB=0,"{\"switch\":{\"type\":1,\"value\":1}}",0

    OK
