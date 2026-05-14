Sleep AT 示例
==================================
本文档简要介绍并举例说明使用AT命令设置睡眠模式。

.. contents::
   :local:
   :depth: 1

简介
----

当前，Combo-AT支持以下两种功耗模式：
1. 浅休眠模式：目前仅仅支持蓝牙从机模式下设置，可以选择上电进入或上电不进入浅休眠，休眠期间保持蓝牙广播。
2. 深度休眠模式：有定时唤醒和GPIO唤醒两种唤醒方式，进入休眠后，蓝牙和Wi-Fi都停止工作。

测量方法
^^^^^^^^^^^^^^^^^^^^

为避免功耗测试过程中出现一些不必要的干扰，建议对单模组进行测试。


在蓝牙连接态下设置为浅休眠模式
-----------------------------------------------------
#.初始化为角色为蓝牙从机。

    命令：

    .. code-block:: none

      AT+BLEMODE=1

    响应：

    .. code-block:: none

      OK

#.开始广播。(默认开启)

    命令：

    .. code-block:: none

      AT+BLEADVEN=1

    响应：

    .. code-block:: none

      OK  

#.更新蓝牙连接参数。设置蓝牙连接间隔为10ms。

    命令：

    .. code-block:: none

      AT+BLECONINTV=8,8,99,400

    响应：

    .. code-block:: none

      OK


#.设置休眠模式为浅休眠模式。

    命令：

    .. code-block:: none

      AT+SLEEP=0

    响应：

    .. code-block:: none

      OK

  
#.等待连接。

    如果连接建立成功，则 AT 将会提示：

    .. code-block:: none

      +EVENT:BLE_CONNECTED //蓝牙连接成功
  

      OK

设置为深度休眠模式
-----------------------

#. 设置休眠模式为深度休眠模式,GPIO唤醒。

   命令：

   .. code-block:: none

     AT+SLEEP=2,2,7,0

     OK

   响应：

   .. code-block:: none

     OK

   说明：

   - Ai-WB2 系列只支持IO7引脚唤醒，即串口接收数据时自动唤醒


#. 设置休眠模式为深度休眠模式,定时5秒唤醒。

   命令：

   .. code-block:: none

     AT+SLEEP=2,0,5000

     OK

   响应：

   .. code-block:: none

     OK

   