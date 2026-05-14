基础 AT 命令集
===============================================================

本章节介绍基础 AT 命令

 - :ref:`AT <cmd-AT>`：测试 AT 启动
 - :ref:`AT+HELP <cmd-HELP>`：查看 AT 指令集
 - :ref:`AT+RST <cmd-RST>`：模块重启
 - :ref:`AT+RESTORE <cmd-RESTORE>`：恢复出厂设置
 - :ref:`ATE1 <cmd-ATE1>`：打开回显
 - :ref:`ATE0 <cmd-ATE0>`：关闭回显
 - :ref:`AT+GMR <cmd-GMR>`：查询版本信息
 - :ref:`AT+SLEEP <cmd-SLEEP>`：睡眠模式
 - :ref:`AT+UARTCFG <cmd-UARTCFG>`：串口设置
 - :ref:`AT+OTA <cmd-OTA>`：在线升级

.. _cmd-AT:

AT：测试 AT 启动
------------------------------------------

描述
^^^^

- 测试 AT 框架是否正常工作的指令


执行命令
^^^^^^^^

**命令：**

::

    AT  

**响应：**

::

    OK  

.. _cmd-HELP:

AT+HELP：查看 AT 指令集
------------------------------------------

描述
^^^^

- 查询 AT 指令集列表


执行命令
^^^^^^^^

**命令：**

::

    AT+HELP  

**响应：**

::

    <指令名称>:<注释>
    .......
    <指令名称>:<注释>
    
    OK  

.. _cmd-RST:

AT+RST：模块重启
-------------------------------------------------

描述
^^^^

- 重启模组


执行命令
^^^^^^^^

**命令：**

::

    AT+RST  

**响应：**

::

    OK  

.. _cmd-RESTORE:

AT+RESTORE：恢复出厂设置
-------------------------------------------------

描述
^^^^

- 恢复出厂模式，擦除配置信息(三元组、IO 映射除外)


执行命令
^^^^^^^^

**命令：**

::

    AT+RESTORE  

**响应：**

::

    OK 

.. _cmd-ATE1:

ATE1：打开回显
-------------------------------------------------

描述
^^^^

- 打开回显

注释
^^^^
- PB 系列默认回显打开
- TB 系列默认回显打开


执行命令
^^^^^^^^

**命令：**

::

    ATE1  

**响应：**

::

    OK 

.. _cmd-ATE0:

ATE0：关闭回显
-------------------------------------------------

描述
^^^^

- 关闭回显


执行命令
^^^^^^^^

**命令：**

::

    ATE0  

**响应：**

::

    OK 

.. _cmd-GMR:

AT+GMR：查询版本信息
-------------------------------------------------

描述
^^^^

- 查询版本信息


执行命令
^^^^^^^^

**命令：**

::

    AT+GMR  

**响应：**

::

    <at version>：AT版本信息(combo版本)
    <sdk version>：SDK版本信息
    <firmware version>：固件版本

    OK 

参数
^^^^


-  **<at version>**：AT版本信息(combo版本)
-  **<sdk version>**：SDK版本信息
-  **<firmware version>**: 固件版本信息

说明
^^^^

- 如果您在使用 Combo-AT 固件中有任何问题，请先提供 ``AT+GMR`` 版本信息。如若了解编译时间，模组重启后会自动打印出来。

示例
^^^^

::

    AT+GMR

    at version:release/V4.18_P2.19.1
    sdk version:release_bl_iot_sdk_1.6.36
    firmware version:V4.18_P1.4.4-e15d67b
    OK

.. _cmd-SLEEP:

AT+SLEEP：睡眠模式
-------------------------------------------------

描述
^^^^

- 设置睡眠模式

注释
^^^^

- PB 系列默认模式为 3，普通模式
- TB 系列默认模式为 3，普通模式
- Ai-WB2 系列支持 mode 2/3，默认为 3
- 注意：Ai-WB2 系列的 GPIO 唤醒配置时 param1 指定的引脚是没有映射的，也就是芯片实际的引脚，且仅支持 IO7 引脚(IO7 是 RX 引脚，所以串口唤醒我们一般设置 IO7 低电平环境即可，也就是 AT+SLEEP=2,2,7,0)


执行命令
^^^^^^^^

**命令：**

::

    AT+SLEEP=<mode>[,<wakeup source>,<param1>,<param2>]  

**响应：**

::
    
    OK 

参数
^^^^
-  Mode：
      - 0：进入浅睡眠，上电不自动进入浅睡眠状态
      - 1：进入浅睡眠，上电自动进入浅睡眠
      - 2：进入深度睡眠状态
      - 3：普通模式

-  wakeup source：
      - 设置唤醒源(仅 mode=0/1/2 时有效)
      - 0：定时器唤醒
      - 2：GPIO 唤醒

   param1：
      - 仅 wakeup source=0/2 时有效
      - wakeup source=0 时表示使用定时唤醒，该参数表示定时时间，单位为 ms
      - wakeup source=2 表示使用 GPIO 唤醒，该参数表示唤醒脚的序号（从模组左上角逆时针排序，引脚序号从 1 开始）

   Param2：
      - 仅 wakeup source=2 时有效，表示 GPIO 唤醒时的唤醒电平
      - 0：低电平唤醒
      - 1：高电平唤醒

示例
^^^^

::

    AT+SLEEP=2,2,7,0

    OK

.. _cmd-UARTCFG:

AT+UARTCFG：串口设置
-------------------------------------------------

描述
^^^^

- 查询/设置 AT 串口配置指令，6212,6252,8258 只支持 baudrate,流控默认为关闭状态，不可设置

注释
^^^^

- PB 系列只支持 baudrate
- TB 系列只支持 baudrate

执行命令
^^^^^^^^
**查询命令：**

::

    AT+UARTCFG?  

**响应：**
::
    
    +UARTCFG:<baudrate>,<databits>,<stopbits>,<parity>
    
    OK 

**设置命令：**

::

    AT+UARTCFG=<baudrate>,<databits>,<stopbits>,<parity>  

**响应：**

::
    
    OK 

参数
^^^^
-  baudrate：串口波特率
-  databits：数据位
      - 5：5 bit 数据位
      - 6：6 bit 数据位
      - 7：7 bit 数据位
      - 8：8 bit 数据位

   stopbits：停止位
      - 1：1 bit 停止位
      - 2：1.5 bit 停止位
      - 3：2 bit 停止位

   parity：校验位
      - 0：None
      - 1：Odd
      - 2：Even

示例
^^^^

::

    AT+UARTCFG=9600,8,1,0

    OK

.. _cmd-OTA:

AT+OTA：在线升级
-------------------------------------------------

描述
^^^^

- 开始一次 OTA 升级
- 注意：升级是异步的，显示 OK 只是表示启动任务成功，并不表示升级成功，升级成功后会重启模组，并切换到新的固件


执行命令
^^^^^^^^
**查询命令：**

::

    AT+OTA?  

**响应：**

    +OTA:<Mode>,<Host_name>,<Port>,<Route> (设置固件升级方式及固件地址)
    
    OK 

**设置命令：**

::

    AT+OTA=<Mode>,<Host_name>,<Port>,<Route> 

**响应：**

::
    
    OK 

参数
^^^^
-  Mode：下载方式
      - 1：HTTP
      - 2：HTTPS

-  Host_name：服务器域名
-  Port：服务器端口号
-  Route：要下载的资源地址


示例
^^^^

::

    1.设置模块的Wi-Fi 工作模式并保存到flash
    AT+WMODE=1,1

    OK

    2.设置模块联网，参数填写有外网的Wi-Fi 名称和Wi-Fi 密码
    AT+WJAP="Wi-Fi 名称","Wi-Fi 密码"

    +EVENT:WIFI_CONNECT

    OK

    3.设置固件升级方式及固件地址
    AT+OTA=2,chencongcc.oss-cn-beijing.aliyuncs.com,443,/bl_OTA-ComboV2.0.0.bin.xz	

    OK

    4.开始升级
    AT+OTA	

    OK







