Bluetooth LE AT 示例
=================================

本文档主要介绍 :doc:`../command-set/BLE_AT_Commands` 命令的详细示例。

.. contents::
   :local:
   :depth: 1

.. Important::
  - 此示例针对不同的模组会有所不同的适配，具体差异请移步查询您手上的模组指令支持情况：:doc:`../instruction/other/firmware_differences`。


以下示例同时使用两块开发板，其中一块做从机，另一块做主机。


说明：

  ``备注可选项的指令可以设置也可以不设置，根据自己的实际情况来决定是否设置``。

基于Gatt的BLE通信
------------------------------------------------------------------------

**从机：**

1. 设置蓝牙名称，如果不设置默认是ai-thinker。（可选项，需要在开启从机模式前设置）

  命令：

  .. code-block:: none
    
    AT+BLENAME=ai-thinker

  响应

  .. code-block:: none

    OK

2. 开启从机模式

  命令：

  .. code-block:: none
    
    AT+BLEMODE=0

  响应

  .. code-block:: none

    OK

**主机：**

1. 开启主机模式

  命令：

  .. code-block:: none
    
    AT+BLEMODE=1

  响应

  .. code-block:: none

    OK

2. 扫描附近设备（可选项，需要在开启主机模式后设置）

  命令：

  .. code-block:: none
    
    AT+BLESCAN=1

  响应

  .. code-block:: none

    OK

    Devices Found:1/5
    name:ai-thinker
    MAC:a81710d8f4e4
    rssi:-23

    Devices Found:2/5
    name:N/A
    MAC:03f3e35771ce
    rssi:-73

    Devices Found:3/5
    name:N/A
    MAC:45797518112f
    rssi:-71

    Devices Found:4/5
    name:N/A
    MAC:53e4da7c288f
    rssi:-82

    Devices Found:5/5
    name:PB02-LIGHT
    MAC:bb02bbbbbb0d
    rssi:-89    

说明：

- 您所处环境中存在的蓝牙设备不同扫描响应也不同。

3. 连接从机

  命令：

  .. code-block:: none
    
    AT+BLECONNECT=a81710d8f4e4

  响应

  .. code-block:: none

    OK
    >

说明：

``ble连接上之后默认进入了透传模式，串口接收到任何数据都会直接往对侧设备发送。如果需要发送其他指令或者需要接收其他连接（如tcp连接）的数据，需要先退出透传模式，退出透传模式的指令是+++（不带回车换行），如果退出透传后需要发送ble数据可以用指令AT+BLESEND来发送，或者发送指令AT+TRANSENTER重新进入透传。``

**动图演示**

``请点开大图查看。左边窗口主机，右边窗口从机``

.. only:: format_html

   .. figure:: ../../_static/ble_connect_example.gif
       :scale: 50 %
       :align: center
       :alt: ble连接通信

.. only:: format_latex

   .. figure:: ../../_static/ble_connect_example.png
       :scale: 50 %
       :align: center
       :alt: ble连接通信





------------------------------------------------------------------------


BLE iBeacon
------------------------------------------------------------------------
1. 设置蓝牙iBeacon UUID (可选，开启iBeacon前设置)

  命令：

  .. code-block:: none
    
    AT+BLEIBCNUUID=00112233445566778899aabbccddeeff

  响应

  .. code-block:: none

    OK

2. 设置蓝牙 iBeacon data (可选，开启iBeacon前设置)

  命令：

  .. code-block:: none
    
    AT+BLEIBCNDATA=1122,3344,5566,14

  响应

  .. code-block:: none

    OK

3. 开启iBeacon

  命令：

  .. code-block:: none
    
    AT+BLEMODE=2

  响应

  .. code-block:: none

    OK

