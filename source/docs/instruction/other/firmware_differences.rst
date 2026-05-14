固件迭代和功能差异
============================

针对已适配模组硬件的最新 Combo-AT 固件版本下载请移步到点击 :doc:`firmware_download`。

下面比较了Combo-AT固件在支持的命令集、硬件、模组方面的差异。下表列出了官方适配的 Combo-AT固件针对不同硬件的默认支持哪些命令集的差异，请见下面表格。

  .. list-table::
    :header-rows: 1

    * - 指令集
      - Ai-WB2系列
      - BW16模组
      - TB泰凌蓝牙系列
      - PB奉加蓝牙系列 

    * - 基础命令
      - 支持
      - 支持
      - 支持
      - 支持
      
    * - Wi-Fi命令集
      - 支持
      - 支持
      - 不支持
      - 不支持
      
    * - TCP/IP命令集
      - 支持
      - 支持
      - 不支持
      - 不支持
      
      
    * - Bluetooth® Low Energy命令集
      - 支持
      - 支持
      - 支持
      - 支持
      
      
    * - MQTT 命令集
      - 支持
      - 支持
      - 不支持
      - 不支持
      
    * - HTTP 命令集
      - 支持
      - 支持
      - 不支持
      - 不支持
      
    * - 外设驱动 命令集
      - 支持
      - 支持
      - 支持
      - 支持
      

    * - 云平台对接命令集
      - 支持
      - 支持
      - 不支持
      - 不支持

      
    * - UART 通讯管脚 
      - | TX: IO16
        | RX: IO7     
      - | TX: PB1
        | RX: PB2      
      - | TB-01:
        | TX: PB0
        | RX: PB1
        |
        | TB-02/TB-03F/TB-04:
        | TX:PB1
        | RX:PA0
      - | PB-01/PB-02:
        | TX: TXD
        | RX: RXD
        |
        | PB-03/PB-03F/PB-03M
        | TXD:P9
        | RXD:P10
     


下面比较了Combo-AT固件在支持各种配网协议的差异。

  .. list-table::
    :header-rows: 1

    * - 配网协议
      - Ai-WB2系列
      - BW16模组
      - TB泰凌蓝牙系列
      - PB奉加蓝牙系列 

    * - Easy WiFi Config 蓝牙配网
      - 不支持
      - 支持
      - 不支持
      - 不支持
      
    * - Blufi 蓝牙配网
      - 支持
      - 不支持
      - 不支持
      - 不支持
      
    * - SmartConfig 一键配网
      - 支持
      - 不支持
      - 不支持
      - 不支持

    * - 微信AirKiss 一键配网
      - 支持
      - 不支持
      - 不支持
      - 不支持