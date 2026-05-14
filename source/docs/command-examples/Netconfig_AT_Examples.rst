Netconfig AT 示例
====================================

本文档主要介绍在设备上运行 :doc:`../command-set/Wi-Fi_AT_Commands` 命令的详细示例。

.. Important::
  - 此配网示例针对不同的模组会有所不同的适配，具体差异请移步查询您手上的模组指令支持情况：:doc:`../instruction/other/firmware_differences`。

.. contents::
   :local:
   :depth: 1

Easy WiFi Config 蓝牙配网
-----------------------------------------------------

1. APP下载：
   
   iOS系统的手机,可以在App Store商店搜索Easy WiFi Config 获取下载安装。

   Android系统的手机apk安装包下载:`手机apk安装包 <https://docs.ai-thinker.com/_media/rtl8710/docs/wificonfig_v2.1.6_20190529.apk.zip>`_

   .. figure:: ../../_static/Easy.png
      :alt: OTA_APP

2. 设置模块的Wi-Fi 工作模式并保存到Flash

   命令：

   .. code-block:: none

      AT+WMODE=1,1

   响应：

   .. code-block:: none

      OK

3. 开启蓝牙配网

   命令：

   .. code-block:: none

      AT+WCONFIG=2

   响应：

   .. code-block:: none

      OK  

4. APP端操作
   
   .. figure:: ../../_static/BW16config.gif
      :scale: 50 %
      :alt: OTA_APP

SmartConfig 一键配网
-----------------------------------------------------

1. APP下载：
   
   iOS系统的手机,可以在 App Store 商店搜索 Esptouch 获取下载安装。

   Android系统的手机apk安装包下载:`手机apk安装包 <https://docs.ai-thinker.com/_media/rtl8710/docs/wificonfig_v2.1.6_20190529.apk.zip>`_


2. 设置模块的Wi-Fi 工作模式并保存到Flash

   命令：

   .. code-block:: none

      AT+WMODE=1,1

   响应：

   .. code-block:: none

      OK

3. 开启一次SmartConfig配网

   命令：

   .. code-block:: none

      AT+WCONFIG=1

   响应：

   .. code-block:: none

      OK  

4. APP端操作
   
   .. figure:: ../../_static/BL602Smartconfig.gif
      :scale: 50 %
      :alt: OTA_APP

5. 配网成功后需要关闭配网模式，否则会大量占用内存

   命令：

   .. code-block:: none

      AT+WCONFIG=0

   响应：

   .. code-block:: none

      OK


微信Airkiss 一键配网
-----------------------------------------------------
Airkiss配网可使用微信公众号或微信小程序，不需要单独下载App。

1. 设置模块的 Wi-Fi 工作模式并保存到Flash

   命令：

   .. code-block:: none

      AT+WMODE=1,1

   响应：

   .. code-block:: none

      OK

2. 开启一次Airkiss配网

   命令：

   .. code-block:: none

      AT+WCONFIG=3

   响应：

   .. code-block:: none

      OK  

3. 微信公众号方式配网：关注安信可科技微信公众号，Airkiss配网接口位于应用开发>微信配网内

   .. figure:: ../../_static/Airkiss.gif
     :scale: 50 %
     :alt: OTA_APP

4. 微信小程序方式配网：搜索安信可IOT小程序：
   
   .. figure:: ../../_static/Airkiss_xiaochengxu.gif
     :scale: 50 %
     :alt: OTA_APP

5. 配网成功后需要关闭配网模式，否则会大量占用内存

   命令：

   .. code-block:: none

      AT+WCONFIG=0

   响应：

   .. code-block:: none

      OK
   

Blufi 蓝牙配网
-----------------------------------------------------
Blufi 蓝牙配网支持app、微信小程序。

1. APP下载：
   
   iOS系统的手机,可以在App Store商店搜索 EspBlufi 获取

   Android系统的手机apk安装包下载:`手机apk安装包 <https://github.com/EspressifApp/EspBlufiForAndroid/releases/download/v1.5.3/EspBluFi-1.5.3-24.apk>`_

   小程序：微信搜索 安信可IOT小程序

2. 设置模块的Wi-Fi 工作模式并保存到Flash

   命令：

   .. code-block:: none

      AT+WMODE=1,1

   响应：

   .. code-block:: none

      OK

3. 开启一次blufi配网

   命令：

   .. code-block:: none

      AT+WCONFIG=2

   响应：

   .. code-block:: none

      OK  

4. app配网方式：
      
   .. figure:: ../../_static/app_blufi.gif
     :scale: 60 %
     :alt: OTA_APP

5. 小程序配网方式：
      
   .. figure:: ../../_static/xiaochengxu_blufi.gif
     :scale: 60 %
     :alt: OTA_APP

6. 配网成功后需要关闭配网模式，否则会大量占用内存

   命令：

   .. code-block:: none

      AT+WCONFIG=0

   响应：

   .. code-block:: none

      OK
 
指令配网
-----------------------------------------------------
以目标路由器ssid：AIOT@FAE, 密码：fae12345678 为例，直接连接到此路由器。

1. 设置模块的Wi-Fi 工作模式并保存到Flash

   命令：

   .. code-block:: none

      AT+WMODE=1,1

   响应：

   .. code-block:: none

      OK

2. 连接目标路由器

   命令：

   .. code-block:: none

      AT+WJAP="AIOT@FAE","fae12345678"

   响应：

   .. code-block:: none

      OK  

3. 设置上电自动重连WiFi

   命令：

   .. code-block:: none

      AT+WAUTOCONN=1

   响应：

   .. code-block:: none

      OK  

同一个环境下有多个相同的ssid且密码相同时,如何连接信号最强的路由器
------------------------------------------------------------------
以目标路由器ssid：AIOT@FAE  密码：fae12345678 为例，连接信号最强的路由器。

通过指令AT+WSCAN=< ssid >扫描目标ssid

   .. figure:: ../../_static/SCAN.png
     :scale: 100 %
     :alt: OTA_APP

通过扫描可以知道信号强度最强的是-16dBm，bssid是9c:9d:7e:59:3e:84,AT+WJAP带上bssid参数即可连到信号最强的路由器

1. 设置模块的Wi-Fi 工作模式并保存到Flash

   命令：

   .. code-block:: none

      AT+WMODE=1,1

   响应：

   .. code-block:: none

      OK

2. 连接目标路由器

   命令：

   .. code-block:: none

      AT+WJAP="AIOT@FAE","fae12345678","9c:9d:7e:59:3e:84"

   响应：

   .. code-block:: none

      OK  

3. 设置上电自动重连WiFi

   命令：

   .. code-block:: none

      AT+WAUTOCONN=1

   响应：

   .. code-block:: none

      OK  

