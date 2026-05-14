Bluetooth® Low Energy AT 命令集
==================================================

本章节介绍低功耗蓝牙指令集，此指令集针对不同的模组会有所不同的适配，具体差异请移步：:doc:`../instruction/other/firmware_differences`。

:ref:`基础指令 <cmd-基础指令>`：


 - :ref:`AT+BLEMAC <cmd-BLEMAC>`：查询或设置蓝牙 MAC 地址
 - :ref:`AT+BLEMODE <cmd-BLEMODE>`：查询或设置蓝牙工作模式
 - :ref:`AT+BLERFPWR <cmd-BLERFPWR>`：查询或设置蓝牙发射功率
 - :ref:`AT+BLESTATE <cmd-BLESTATE>`：查询连接状态
 - :ref:`AT+BLEDISCON <cmd-BLEDISCON>`：断开蓝牙连接
 - :ref:`AT+BLEMTU <cmd-BLEMTU>`：查询或设置蓝牙 MTU
 - :ref:`AT+BLESEND <cmd-BLESEND>`：向蓝牙透传通道发送数据
 - :ref:`AT+BLESERUUID <cmd-BLESERUUID>`：查询或设置蓝牙透传服务的 UUID
 - :ref:`AT+BLETXUUID <cmd-BLETXUUID>`：查询或设置蓝牙透传服务 TX 特征的 UUID
 - :ref:`AT+BLERXUUID <cmd-BLERXUUID>`：查询或设置蓝牙透传服务 RX 特征的 UUID
 - :ref:`AT+TRANSENTER <cmd-TRANSENTER>`：进入蓝牙透传模式

:ref:`从机指令 <cmd-从机指令>`：


 - :ref:`+DATA <cmd-DATA>`：主机模式下收到蓝牙透传数据
 - :ref:`AT+BLENAME <cmd-BLENAME>`：查询或设置蓝牙设备名称
 - :ref:`AT+BLECONINTV <cmd-BLECONINTV>`：查询或设置蓝牙连接间隔
 - :ref:`AT+BLEAUTH <cmd-BLEAUTH>`：查询或设置蓝牙配对码
 - :ref:`AT+BLEADVINTV <cmd-BLEADVINTV>`：查询或设置蓝牙广播间隔
 - :ref:`AT+BLEADVDATA <cmd-BLEADVDATA>`：查询或设置蓝牙广播数据
 - :ref:`AT+BLEADVEN <cmd-BLEADVEN>`：查询或设置蓝牙广播使能

:ref:`主机指令 <cmd-主机指令>`：


 - :ref:`AT+BLESCAN <cmd-BLESCAN>`：蓝牙主机模式下发起扫描
 - :ref:`AT+BLECONNECT <cmd-BLECONNECT>`：主机发起一次连接
 - :ref:`AT+BLEAUTOCON <cmd-BLEAUTOCON>`：设置主机自动连接从机参数
 - :ref:`AT+BLEDISAUTOCON <cmd-BLEDISAUTOCON>`：取消自动扫描连接

:ref:`iBeacon指令 <cmd-iBeacon指令>`：


 - :ref:`AT+BLEIBCNUUID <cmd-BLEIBCNUUID>`：查询或设置蓝牙 iBeacon UUID
 - :ref:`AT+BLEIBCNDATA <cmd-BLEIBCNDATA>`：设置蓝牙 iBeacon data


:ref:`BLE MESH指令 <cmd-MESH指令>`：


- :ref:`SIG-MESH 指令 <cmd-SIG指令>`：

  - :ref:`AT+PROVISION <cmd-PROVISION>`：蓝牙设置启动配网功能
  - :ref:`AT+MESHSEND <cmd-MESHSEND>`：SIG-MESH 发送数据
  - :ref:`AT+MESHADDR <cmd-MESHADDR>`：查询节点地址
  - :ref:`AT+MESHSTATE <cmd-MESHSTATE>`：查询是否配网成功

- :ref:`ALI-MESH 指令 <cmd-ALI指令>`：

  - :ref:`aliGenie_data <cmd-aliGenie_data>`：天猫精灵下发数据
  - :ref:`AT+AliGenie <cmd-MESHSEND>`：设置天猫精灵三元组
  - :ref:`AT+SEND2ALI <cmd-SEND2ALI>`：向天猫精灵平台上报数据

.. _cmd-基础指令:

基础指令
-------------------------------------------------
.. _cmd-BLEMAC:

AT+BLEMAC：查询或设置蓝牙 MAC 地址
-------------------------------------------------

描述
^^^^

- 查询或设置蓝牙 MAC 地址

执行命令
^^^^^^^^
**查询命令：**

::

    AT+BLEMAC?  

**响应：**

::

    +BLEMAC:<MAC>
    
    OK 

**设置命令：**
设置蓝牙 MAC 地址(重启后生效)

::

    AT+BLEMAC=<MAC>  

**响应：**

::

    OK 

参数
^^^^
-  MAC：要设置的蓝牙 MAC 地址，格式小写无分隔 eg:ab5f8d9ebb01

示例
^^^^

::

    AT+BLEMAC=ab5f8d9ebb01

    OK

.. _cmd-BLEMODE:

AT+BLEMODE：查询或设置蓝牙工作模式
-------------------------------------------------

描述
^^^^

- 查询或设置蓝牙工作模式
  
注意
^^^^

- 瑞昱系列(BW16/BW15)如果开启多种无线类型需要按照指定顺序开启
- 设置蓝牙模式后会立即执行，如果是启动蓝牙需要先设置好蓝牙参数后再启动蓝牙
- 如果开启 AP+STA+蓝牙三模，或者 AP+STA 混杂模式，需要先开 AP，然后连接STA 或蓝牙(蓝牙和 STA 顺序先后没有要求，但是必须先开 AP)

执行命令
^^^^^^^^
**查询命令：**
设置蓝牙工作模式

::

    AT+BLEMODE? 

**响应：**

::
    
    +BLEMODE :<mode>
    
    OK 

**设置命令：**
设置蓝牙工作模式

::

    AT+BLEMODE=<mode>  

**响应：**

::
    
    OK 

参数
^^^^
-  Mode：
      - 0：从机模式
      - 1：主机模式
      - 2：iBeacon 模式
      - 9：蓝牙关闭


示例
^^^^

::

    AT+BLEMODE=0

    OK

.. _cmd-BLERFPWR:

AT+BLERFPWR：查询或设置蓝牙发射功率
-------------------------------------------------

描述
^^^^

- 查询或设置蓝牙发射功率

注释
^^^^
- PB 系列默认当前发射功率为最大发射功率 10
- TB 系列默认当前发射功率为最大发射功率 10



执行命令
^^^^^^^^
**查询命令：**
查询蓝牙发射功率
::

    AT+BLERFPWR?  

**响应：**
::
    
    +BLERFPWR:MAX:<max_power> MIN:<min_power> CURRENT:<cur_power>
    
    OK

    - max_power：当前模组支持的蓝牙最大发射功率
    - min_power：当前模组支持的蓝牙最小发射功率
    - cur_power：当前模组设置的蓝牙发射功率 

**设置命令：**
设置蓝牙发射功率(需要在蓝牙关闭状态下设置)
::

    AT+BLERFPWR=<power>  

**响应：**

::
    
    OK 

参数
^^^^
-  power：蓝牙发射功率，取值为整数、MAX(最大发射功率)、MIN(最小发射功率)

示例
^^^^

::

    AT+BLERFPWR=10

    OK
    
.. _cmd-BLESTATE:

AT+BLESTATE：查询蓝牙连接状态
-------------------------------------------------

描述
^^^^

- 查询蓝牙连接状态

执行命令
^^^^^^^^
**命令：**

::

    AT+BLESTATE?  

**响应：**
::
    
    + BLESTATE:<status>
    
    OK

参数
^^^^
-  status：
    -  0：未连接
    -  1：已连接

示例
^^^^

::

    AT+BLESTATE?

    + BLESTATE:0
    
    OK

.. _cmd-BLEDISCON:

AT+BLEDISCON：断开蓝牙连接
-------------------------------------------------

描述
^^^^

- 断开蓝牙连接

执行命令
^^^^^^^^
**命令：**

::

    AT+BLEDISCON 

**响应：**

::
    
    OK 

示例
^^^^

::

    AT+BLEDISCON
    
    OK
    
.. _cmd-BLEMTU:

AT+BLEMTU：查询或设置蓝牙MTU
-------------------------------------------------

描述
^^^^

- 查询或设置蓝牙MTU

注释
^^^^
- PB 系列默认 MTU 为 23
- TB 系列默认 MTU 为 247



执行命令
^^^^^^^^
**查询命令：**
查询蓝牙MTU
::

    AT+BLEMTU?

**响应：**
::
    
    +BLEMTU:<MTU>
    
    OK

**设置命令：**
设置蓝牙MTU
::

    AT+BLEMTU=<mtu>  

**响应：**

::
    
    OK 

参数
^^^^
-  mtu：设置蓝牙的 MTU，取值 23~250

示例
^^^^

::

    AT+BLEMTU=247

    OK
    
.. _cmd-BLESEND:

AT+BLESEND：向蓝牙透传通道发送数据
-------------------------------------------------

描述
^^^^

- 向蓝牙透传通道发送数据

执行命令
^^^^^^^^
**命令：**

::

    AT+BLESEND=<len>,<data> 

**响应：**

::
    
    OK 

参数
^^^^
-  len:要发送的数据长度，单位为字节
-  data：要发送的数据内容，长度应与 len 一致
  
示例
^^^^

::

    AT+BLESEND=5,12345
    
    OK
    
.. _cmd-BLESERUUID:

AT+BLESERUUID：查询或者设置蓝牙透传服务 UUID
-------------------------------------------------

描述
^^^^

- 查询或者设置蓝牙透传服务 UUID

注释
^^^^
- 默认主服务 UUID: 55535343fe7d4ae58fa99fafd205e455

执行命令
^^^^^^^^
**查询命令：**
查询蓝牙透传服务的 UUID
::

    AT+BLESERUUID?

**响应：**
::
    
    +BLESERUUID:<UUID>
    
    OK

**设置命令：**
设置蓝牙透传服务 UUID(仅允许在蓝牙关闭状态下设置蓝牙名称)
::

    AT+BLESERUUID=<UUID>  

**响应：**

::
    
    OK 

参数
^^^^
-  UUID：16 字节的服务 ID，字符串长度 32 位 eg:00112233445566778899aabbccddeeff

示例
^^^^

::

    AT+BLESERUUID=55535343fe7d4ae58fa99fafd205e455

    OK
    
.. _cmd-BLETXUUID:

AT+BLETXUUID：查询或者设置蓝牙透传服务 TX 特征 UUID
----------------------------------------------------

描述
^^^^

- 查询或者设置蓝牙透传服务 TX 特征 UUID

注释
^^^^
- 默认 TX 的UUID:49535343884143f4a8d4ecbe34729bb3
- TX 对应的蓝牙服务属性为 NOTIFY

执行命令
^^^^^^^^
**查询命令：**
查询蓝牙透传服务 TX 特征的 UUID
::

    AT+BLETXUUID?

**响应：**
::
    
    +BLETXUUID:<UUID>
    
    OK

**设置命令：**
设置蓝牙透传服务 TX 特征 UUID(仅允许在蓝牙关闭状态下设置蓝牙名称)
::

    AT+BLETXUUID=<UUID>  

**响应：**

::
    
    OK 

参数
^^^^
-  UUID：16 字节的服务 ID，字符串长度 32 位 eg:00112233445566778899aabbccddeeff

示例
^^^^

::

    AT+BLETXUUID=49535343884143f4a8d4ecbe34729bb3

    OK

.. _cmd-BLERXUUID:

AT+BLERXUUID：查询或者设置蓝牙透传服务 RX 特征 UUID
----------------------------------------------------

描述
^^^^

- 查询或者设置蓝牙透传服务 RX 特征 UUID

注释
^^^^
- 默认 RX 的UUID:495353431e4d4bd9ba6123c647249616
- RX 对应的蓝牙服务属性为 NOTIFY

执行命令
^^^^^^^^
**查询命令：**
查询蓝牙透传服务 RX 特征的 UUID
::

    AT+BLERXUUID?

**响应：**
::
    
    +BLERXUUID:<UUID>
    
    OK

**设置命令：**
设置蓝牙透传服务 RX 特征 UUID(仅允许在蓝牙关闭状态下设置蓝牙名称)
::

    AT+BLERXUUID=<UUID>  

**响应：**

::
    
    OK 

参数
^^^^
-  UUID：16 字节的服务 ID，字符串长度 32 位 eg:00112233445566778899aabbccddeeff

示例
^^^^

::

    AT+BLETXUUID=495353431e4d4bd9ba6123c647249616

    OK

.. _cmd-TRANSENTER:

AT+TRANSENTER：进入蓝牙透传模式
-------------------------------------------------

描述
^^^^

- 进入蓝牙透传模式

备注
^^^^
- 输入+++后可以退出透传模式，进入 AT 指令模式
- 注释:默认连接后自动进入透传模式

执行命令
^^^^^^^^
**命令：**

::

    AT+TRANSENTER 

**响应：**

::
    
    OK 

示例
^^^^

::

    AT+TRANSENTER
    
    OK
  
.. _cmd-从机指令:

从机指令
-------------------------------------------------------
.. _cmd-DATA:

+DATA：主机模式下收到蓝牙透传 UUID 通道发送过来的数据
--------------------------------------------------------

描述
^^^^

- 主机模式下收到蓝牙透传 UUID 通道发送过来的数据


参数
^^^^
-  len: 收到的数据长度，单位为字节
-  data：收到的数据内容，长度应与 len 一致

.. _cmd-BLENAME:

AT+BLENAME：查询或设置蓝牙设备名称
-------------------------------------------------

描述
^^^^

- 查询或设置蓝牙设备名称

注释
^^^^
- 默认蓝牙名称: ai-thinker

执行命令
^^^^^^^^
**查询命令：**
查询蓝牙名称
::

    AT+BLENAME?

**响应：**
::
    
    +BLENAME :<ble name>
    
    OK

**设置命令：**
设置蓝牙设备名称(仅允许在蓝牙关闭状态下设置蓝牙名称)
::

    AT+BLENAME=<ble name> 

**响应：**

::
    
    OK 

参数
^^^^
-  ble name：蓝牙名称(UTF-8 格式，支持中文)

示例
^^^^

::

    AT+BLENAME=ai-thinker

    OK
    
.. _cmd-BLECONINTV:

AT+BLECONINTV：查询或设置蓝牙连接间隔
-------------------------------------------------

描述
^^^^

- 查询或设置蓝牙连接间隔

注释
^^^^
- PB 系列默认参数：+BLECONINTV:6,12,0,200
- TB 系列默认参数：+BLECONINTV:8,8,99,400

执行命令
^^^^^^^^
**查询命令：**
查询蓝牙连接间隔
::

    AT+BLECONINTV?

**响应：**
::
    
    +BLECONINTV:<min_interval>,< max_interval>,<latency>,< timeout>
    
    OK

**设置命令：**
设置蓝牙连接间隔(仅允许在蓝牙关闭状态下设置)
::

    AT+BLECONINTV=<min_interval>,< max_interval>,<latency>,< timeout> 

**响应：**

::
    
    OK 

参数
^^^^
-  min_interval：最小连接间隔，取值 6~3200,实际时间是 minInterval*1.25ms，要求在7.5ms ~ 4s
-  max_interval：最大连接间隔，取值 6~3200,实际时间是 minInterval*1.25ms，要求在7.5ms ~ 4s
-  Latency：延时(可以跳过几次连接)，要求在 0~499 之间
-  Timeout：超时时间，取值 10~3200,实际时间是 Timeout*10ms 即 100ms~32*1000ms且 Timeout*10>(1+Latency)*max_interval*1.25

示例
^^^^

::

    AT+BLECONINTV=6,12,0,200

    OK
    
.. _cmd-BLEAUTH:

AT+BLEAUTH：查询或设置蓝牙配对码
-------------------------------------------------

描述
^^^^

- 查询或设置蓝牙配对码

执行命令
^^^^^^^^
**查询命令：**
查询蓝牙配对码
::

    AT+BLEAUTH?

**响应：**
::
    
    +BLEAUTH:<pind>
    
    OK

**设置命令：**
设置蓝牙配对码(仅允许在蓝牙关闭状态下执行设置)
::

    AT+BLEAUTH=<pind>

**响应：**
::
    
    OK 

参数
^^^^
-  pind：启用配对码，设置 6 位数字 eg:123456
-  禁用配对码 DISENABLE

示例
^^^^

::

    AT+BLEAUTH=123456

    OK
    
.. _cmd-BLEADVINTV:

AT+BLEADVINTV：查询或设置蓝牙广播间隔
-------------------------------------------------

描述
^^^^

- 查询或设置蓝牙广播间隔

注释
^^^^
- PB 默认参数 320
- TB 默认参数 800

执行命令
^^^^^^^^
**查询命令：**
查询蓝牙广播间隔
::

    AT+BLEADVINTV?

**响应：**
::
    
    +BLEADVINTV:<intv>
    
    OK

**设置命令：**
设置蓝牙广播间隔(仅允许在蓝牙关闭状态下执行设置)
::

    AT+BLEADVINTV=<intv>

**响应：**
::
    
    OK 

参数
^^^^
-  <intv>：广播间隔，单位取值为 160~16384，广播间隔为 iNtv*0.625ms

示例
^^^^

::

    AT+BLEADVINTV=160

    OK
    
.. _cmd-BLEADVDATA:

AT+BLEADVDATA：查询或设置蓝牙广播数据
-------------------------------------------------

描述
^^^^

- 查询或设置蓝牙广播数据

注释
^^^^
- 默认参数：MAC+55e4(主服务 uuid 前四个)，例如：40154641871855e4

执行命令
^^^^^^^^
**查询命令：**
查询蓝牙广播数据
::

    AT+BLEADVDATA?

**响应：**
::
    
    +BLEADVDATA:<data>
    
    OK

**设置命令：**
设置蓝牙广播数据(仅允许在蓝牙关闭状态下执行设置)
::

    AT+BLEADVDATA=<data>

**响应：**

::
    
    OK 

参数
^^^^
-  data：设置的蓝牙数据(这个是字符串形式的hex数据，最大长度32字节eg:00112233445566778899aabbccddeeff)

示例
^^^^

::

    AT+BLEADVDATA=40154641871855e4

    OK
    
.. _cmd-BLEADVEN:

AT+BLEADVEN：查询或设置蓝牙广播使能
-------------------------------------------------

描述
^^^^

- 查询或设置蓝牙广播使能

注释
^^^^
- 默认开启

执行命令
^^^^^^^^
**查询命令：**
查询蓝牙广播使能
::

    AT+BLEADVEN?

**响应：**
::
    
    +BLEADVEN:<status>
    
    OK

**设置命令：**
设置蓝牙广播使能(仅允许在蓝牙从机状态下执行设置)
::

    AT+BLEADVEN=<status>

**响应：**

::
    
    OK 

参数
^^^^
-  status：
    -  0：关闭
    -  1：开启

示例
^^^^

::

    AT+BLEADVEN=1

    OK
    
.. _cmd-主机指令:

主机指令
-------------------------------------------------------
.. _cmd-BLESCAN:

AT+BLESCAN：蓝牙主机模式下发起扫描
-------------------------------------------------

描述
^^^^

- 蓝牙主机模式下发起扫描

注释
^^^^
- PB 系列默认扫描时间 5 秒，扫描间隔 230*0.625 mSec，扫描窗口 160*0.625 mSec
- TB 系列默认扫描时间 2 秒，扫描间隔 160*0.625 mSec，扫描窗口 160*0.625 mSec

执行命令
^^^^^^^^
**命令：**
::

    AT+BLESCAN

**响应：**
::
        
    OK //注意这里这个 OK 只是表示指令发送成功了，扫描实际并没有结束

    Devices Found:id/total //index/total 表示当前扫描到的蓝牙设备的序号和总共扫描到的数量

    name:<name> //蓝牙名称，如果没有则显示 N/A

    MAC:<MAC> //小写不加冒号

    rssi:<rssi>

    Devices Found:<id/total>

    name:<name>N/A

    MAC:<MAC>

    rssi:<rssi>

    ........
    

示例
^^^^

::

    AT+BLEMODE=1

    OK

    AT+BLESCAN

    OK

.. _cmd-BLECONNECT:

AT+BLECONNECT：蓝牙主机发起一次连接
-------------------------------------------------

描述
^^^^

- 蓝牙主机发起一次连接

执行命令
^^^^^^^^
**命令：**
::

    AT+BLECONNECT=<MAC>

**响应：**
::
    
    Connecting... ...

    OK 
    
参数
^^^^
-  MAC：连接目标 mac 地址(eg:A4C13812505C)

示例
^^^^

::

    AT+BLEMODE=1

    OK

    AT+BLECONNECT=A4C13812505C

    OK

.. _cmd-BLEAUTOCON:

AT+BLEAUTOCON：设置主机自动连接从机参数
-------------------------------------------------

描述
^^^^

- 连接指定蓝牙(仅允许在蓝牙主机状态下连接)

执行命令
^^^^^^^^
**命令：**
::

    AT+BLEAUTOCON=<MAC>,<UUID>,<save_flash>

**响应：**
::
    
    +EVENT:BLE_CONNECTED //如果连接成功则显示这条信息

    +BLEAUTOCON:Wait connect //如果当前没有扫描到指定蓝牙，则显示该消息(后台还会自动扫描，当扫描到指定连接的时候就会自动连接)

    OK 
    
参数
^^^^
-  MAC：连接目标 mac 地址(eg:A4C13812505C)
-  UUID：如果需要连接指定 UUID 则设置为目标 UUID 的末两位(eg:E455)
-  注意：MAC、UUID 两个输入任意一个就可以实现连接(两个都设置也可以)，不限制则设置为 FALSE，如果 MAC 和 UUID 都设置为 FALSE 则关闭自动连接
-  save_flash：是否保存到 flash，并设置开机自动连接，0 表示不保存，仅本次连接，1表示保存到 flash，下次开机自动连接

示例
^^^^

::

    AT+BLEAUTOCON=A4C13812505C,55535343fe7d4ae58fa99fafd205e455,1

    OK

.. _cmd-BLEDISAUTOCON:

AT+BLEDISAUTOCON：取消自动扫描连接
-------------------------------------------------

描述
^^^^

- 取消自动扫描连接

执行命令
^^^^^^^^
**命令：**

::

    AT+BLEDISAUTOCON 

**响应：**

::
    
    OK 

示例
^^^^

::

    AT+BLEDISAUTOCON
    
    OK

.. _cmd-iBeacon指令:

iBeacon指令
------------------------------------------------------------
.. _cmd-BLEIBCNUUID:

AT+BLEIBCNUUID：查询或者设置蓝牙 iBeacon UUID
----------------------------------------------------

描述
^^^^

- 查询或者设置蓝牙 iBeacon UUID

执行命令
^^^^^^^^
**查询命令：**
查询蓝牙 iBeacon UUID
::

    AT+BLEIBCNUUID?

**响应：**
::
    
    +BLEIBCNIIUD:<iBeacon>
    
    OK

**设置命令：**
设置蓝牙 iBeacon UUID(仅允许在蓝牙关闭状态下设置蓝牙 iBeacon UUID)
::

    AT+BLEIBCNUUID=<iBeacon>  

**响应：**

::
    
    OK 

参数
^^^^
-  iBeacon：要设置的 UUID：16 字节的服务 ID，字符串长度 32 位 eg:00112233445566778899aabbccddeeff

示例
^^^^

::

    AT+BLETXUUID=495353431e4d4bd9ba6123c647249616

    OK

.. _cmd-BLEIBCNDATA:

AT+BLEIBCNDATA：查询或者设置蓝牙 iBeacon data
----------------------------------------------------

描述
^^^^

- 查询或者设置蓝牙 iBeacon data

执行命令
^^^^^^^^
**查询命令：**
查询蓝牙 iBeacon data
::

    AT+BLEIBCNDATA?

**响应：**
::
    
    +BLEIBCNDATA:<companyID>,<major>,<minor>,<power>
    
    OK

**设置命令：**
设置蓝牙 iBeacon data(仅允许在蓝牙关闭状态下设置蓝牙 iBeacon UUID)
::

    AT+BLEIBCNDATA=<company ID>,<MAJOR>,<MINOR>,<POWER>  

**响应：**

::
    
    OK 

参数
^^^^
-  companyID(2 字节 16 进制数据，eg：11aa)
-  MAJOR (2 字节 16 进制数据，eg：11aa)
-  MINOR (2 字节 16 进制数据，eg：11aa)
-  POWER (1 字节 16 进制数据，eg：aa)

示例
^^^^

::

    AT+BLEIBCNDATA=4c00,2774,6b74,c5

    OK

.. _cmd-MESH指令:

BLE MESH指令
-------------------------------------------------

.. _cmd-SIG指令:

SIG-MESH指令
-------------------------------------------------
.. _cmd-PROVISION:

AT+PROVISION：蓝牙设置启动配网功能
-------------------------------------------------

描述
^^^^

- 设置蓝牙启动配网功能

执行命令
^^^^^^^^
**命令：**

::

    AT+PROVISION  

**响应：**

::
    
    OK 

备注
^^^^
-  当节点处于 unProvisioning 状态，即未配网过，此时不发送广播，网关无法扫描到此设备并进行连接，如需连接需使用 AT+PROVISION 指令使能节点，使得设备能被扫描和连接。当设备处于 Provisioning 状态，即已经与网关配网过了，无需使能节点，节点自动接入已经配网的 mesh 网络中

示例
^^^^

::

    AT+PROVISION

    OK

.. _cmd-MESHSEND:

AT+MESHSEND：SIG-MESH 发送数据
-------------------------------------------------

描述
^^^^

- SIG-MESH 发送数据

执行命令
^^^^^^^^
**命令：**

::

    AT+MESHSEND=<addr>,<opcode>,<data>  

**响应：**

::
    
    OK 

参数
^^^^
-  addr：目标的地址
-  opcode：操作码
-  目前针对我司出售的网关的操作码有如下:
-  1:set 指令，操作码 opcode 为 D18888
-  2:get 指令，操作码 opcode 为 D08888
-  3:ACK 指令，操作码 opcode 为 D38888
-  4:删除节点指令 操作码 opcode 为 D28888
-  data：数据示例：
-  {"mesh_data vendor" : { "daddr" : 3 , "saddr" : 2 , "opcode" : d38888 , "data_len" :2 , "data" : 0101(为 hex 字符串) ret : 1 }}

示例
^^^^

::

    AT+MESHSEND=FFFF,D38888,0102030405

    OK

.. _cmd-MESHADDR:

AT+MESHADDR：查询节点地址
-------------------------------------------------

描述
^^^^

- 查询节点地址

执行命令
^^^^^^^^
**命令：**

::

    AT+MESHADDR  

**响应：**
::
        
    +MESHADDR:<addr>

    OK 



示例
^^^^

::

    AT+MESHADDR

    +MESHADDR:<FFFF>

    OK

.. _cmd-MESHSTATE:

AT+MESHSTATE：查询是否配网成功
-------------------------------------------------

描述
^^^^

- 查询是否配网成功

执行命令
^^^^^^^^
**命令：**

::

    AT+MESHSTATE 

**响应：**
::
        
    +MESHSTATE:<status>

    OK 

参数
^^^^
-  status：
    -  0：失败
    -  1：成功

示例
^^^^

::

    AT+MESHSTATE

    +MESHSTATE:0

    OK

.. _cmd-ALI指令:

ALI-MESH指令
-------------------------------------------------
.. _cmd-aliGenie_data:

aliGenie_data：天猫精灵下发数据
-------------------------------------------------

描述
^^^^

- 天猫精灵下发数据

格式
^^^^
-  { "aliGenie_data" : { "daddr" : %x , "saddr" : %x , "opcode" : %x , "data_len" : %d , "data" : %s }}//数据格式为 json 字符串
-  daddr：目标地址
-  saddr：源地址
-  opcode：操作码
-  data_len：数据长度
-  data：数据内容

.. _cmd-AliGenie:

AT+AliGenie：设置天猫精灵三元组
-------------------------------------------------

描述
^^^^

- 设置天猫精灵三元组

执行命令
^^^^^^^^
**命令：**

::

    AT+AliGenie=<pid>,<mac>,<secret>

**响应：**

::
    
    OK 

参数
^^^^
-  pid：三元组产品 ID(8 位)
-  mac：三元组物理地址(12 位)
-  secret：三元组密钥（32 位）
-  注意：全部为 16 进制字符串

.. _cmd-SEND2ALI:

AT+SEND2ALI：向天猫精灵平台上报数据
-------------------------------------------------

描述
^^^^

- 向天猫精灵平台上报数据

执行命令
^^^^^^^^
**命令：**

::

    AT+SEND2ALI=<opcode>,<param>

**响应：**

::

    OK 

参数
^^^^
-  opcode：操作码，长度 6 位/4 位
-  param：上报参数，长度最多 20 位

示例
^^^^

::

    上报状态为开
    AT+SEND2ALI=8204,01


    OK

