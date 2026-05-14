Wi-Fi AT 命令集
==================================================

本章节介绍驱动 Wi-Fi 指令集，此指令集针对不同的模组会有所不同的适配，具体差异请移步：:doc:`../instruction/other/firmware_differences`。

 - :ref:`AT+WMODE <cmd-WMODE>`：Wi-Fi工作模式
 - :ref:`AT+WSCAN <cmd-WSCAN>`：扫描Wi-Fi列表
 - :ref:`AT+WSDHCP <cmd-WSDHCP>`：STA模式下DHCP参数
 - :ref:`AT+WJAP <cmd-WJAP>`：连接AP
 - :ref:`AT+WDISCONNECT <cmd-WDISCONNECT>`：断开当前的AP连接
 - :ref:`AT+WAUTOCONN <cmd-WAUTOCONN>`：上电自动连接Wi-Fi
 - :ref:`AT+WAPDHCP <cmd-WAPDHCP>`：AP模式下DHCP参数
 - :ref:`AT+WAP <cmd-WAP>`：AP模式Wi-Fi参数
 - :ref:`AT+PING <cmd-PING>`：进行Ping操作
 - :ref:`AT+CIPSTAMAC_DEF <cmd-CIPSTAMAC_DEF>`：Wi-Fi station MAC地址
 - :ref:`AT+WCOUNTRY <cmd-WCOUNTRY>`：Wi-Fi国家码
 - :ref:`AT+WCONFIG <cmd-WCONFIG>`：手机配网
 - :ref:`AT+WSCANOPT <cmd-WSCANOPT>`：筛选Wi-Fi扫描显示信息
 - :ref:`AT+WRSSI <cmd-WRSSI>`：Wi-Fi连接信号强度

.. _cmd-WMODE:

AT+WMODE 查询或设置Wi-Fi工作模式
------------------------------------------


设置命令
^^^^^^^^

**命令：**

::

    AT+WMODE=<MODE>,<save_flash> 

**响应：**

::

    OK

参数
^^^^

 - **<MODE>**：Wi-Fi工作模式
    -  0：未初始化或者关闭Wi-Fi
    -  1：STA
    -  2：AP
    -  3：AP+STA
 - **<save_flash>**：是否保存到flash
    -  0：不保存
    -  1：保存


说明
^^^^

- 设置Wi-Fi工作模式


示例
^^^^

::

    AT+WMODE=1,1  //设置STA模式，保存到FLASH
    OK

查询命令
^^^^^^^^

**命令：**

::

    AT+WMODE?

**响应：**

::

    +WMODE:<MODE>
    OK

参数
^^^^

- **<MODE>**：Wi-Fi工作模式
    -  0：未初始化或者关闭Wi-Fi
    -  1：STA
    -  2：AP
    -  3：AP+STA

示例
^^^^

::

    AT+WMODE? //查询Wi-Fi工作模式
    +WMODE:<1>
    OK


.. _cmd-WSCAN:

AT+WSCAN 扫描Wi-Fi列表
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+WSCAN

**响应：**

::

   +WSCAN:index SSID,CH,SECURITY,RSSI,BSSID
   <index> <SSID>,<CH>,<SECURITY>,<RSSI>,<BSSID>
   ...
   OK

参数
^^^^

-  **<index>**：扫描序列id
-  **<SSID>**：Wi-Fi SSID
-  **<CH>**：Wi-Fi信道
-  **<SECURITY>**：安全模式
-  **<RSSI>**：Wi-Fi接收信号强度
-  **<BSSID>**：Wi-Fi BSSID


说明
^^^^

- 需在STA模式下。


示例
^^^^

::

   AT+WSCAN
   +WSCAN:index SSID,CH,SECURITY,RSSI,BSSID
   1 IoT-Connect,9,WPA/WPA2 Mixed,-19,cc:81:da:1f:45:80
   2 IoT-Connect_5G,44,WPA/WPA2 Mixed,-30,cc:81:da:1f:45:88
   3 super_2G,1,WPA/WPA2 AES,-32,54:75:95:4f:74:5e
   ... 
   30 ChinaNet-uL5X,1,WPA/WPA2 Mixed,-71,ca:50:e9:8b:5a:0c

   OK

设置命令
^^^^^^^^

**命令：**

::

    AT+WSCAN=[<ssid>,<mac>,<channel>,<rssi>]   带过滤参数进行 Wi-Fi 扫描

**响应：**

::
    
    +WSCAN:index SSID,CH,SECURITY,RSSI,BSSID
    <index> <SSID>,<CH>,<SECURITY>,<RSSI>,<BSSID>
    ...
    OK

参数
^^^^

-  **<ssid>**：扫描指定的SSID
-  **<mac>**：扫描指定的mac地址
-  **<channel>**：扫描指定的通道号
-  **<rssi>**：过滤掉信号强度低于rssi参数值的AP，单位：dBm，默认值：-100，范围：[-100,40]

说明
^^^^

- 1，为空代表跳过参数。
- 2，可与 AT+WSCANOPT 组合使用。

示例
^^^^

::

   AT+WSCAN=AXK
   +WSCAN:index,SSID,CH,SECURITY,RSSI,BSSID
   1,AXK,149,WPA/WPA2 Mixed,-50,f8:8c:21:b4:40:22
   2,AXK,48,WPA/WPA2 Mixed,-57,f8:8c:21:b4:4a:39
   3,AXK,161,WPA/WPA2 Mixed,-75,f8:8c:21:b4:3f:62
   4,AXK,157,WPA/WPA2 Mixed,-84,f8:8c:21:b4:2d:89
   OK

.. _cmd-WSDHCP:

AT+WSDHCP 查询或设置STA模式下DHCP参数
------------------------------------------

设置命令
^^^^^^^^

**命令：**

::

   AT+WSDHCP=<MODE>[,<IP>,<MASK>,<GATEWAY>]

**响应：**

::

    OK

参数
^^^^

-  **<MODE>**：IP获取模式
    - 0：禁用DHCP，使用静态IP
    - 1：使用DHCP获取IP
-  **<IP>**：模块的IP地址，静态IP时需设置
-  **<MASK>**：子网掩码,静态IP时需设置
-  **<GATEWAY>**：网关，静态IP时需设置


示例
^^^^

::

    AT+WSDHCP=0,192.168.31.199,255.255.255.0,192.168.31.1

    OK  

查询命令
^^^^^^^^

**命令：**

::

   AT+WSDHCP?

**响应：**

::

   +WSDHCP:<MODE>[,<IP>,<MASK>,<GATEWAY>]
   OK

参数
^^^^

-  **<MODE>**：IP获取模式
    - 0：禁用DHCP，使用静态IP
    - 1：使用DHCP获取IP
-  **<IP>**：模块的IP地址，静态IP时需设置
-  **<MASK>**：子网掩码,静态IP时需设置
-  **<GATEWAY>**：网关，静态IP时需设置

示例
^^^^

::

   AT+WSDHCP?
   +WSDHCP:0,192.168.31.199,255.255.255.0,192.168.31.1
   OK

.. _cmd-WJAP:

AT+WJAP 连接AP
------------------------------------------


设置命令
^^^^^^^^

**命令：**

::

    AT+WJAP=<ssid>,<pwd>[,<bssid>]

**响应：**

::

    OK

参数
^^^^

-  **<ssid>**：连接的AP的SSID(最大长度为32字节)
-  **<pwd>**：连接的AP的密码(最大长度为32字节)
-  **<bssid>**：连接的AP的BSSID


示例
^^^^

::

   AT+WJAP=super_2G,123456798
   OK


查询命令
^^^^^^^^

**命令：**

::

    AT+WJAP?

**响应：**
  
::

     +WJAP:<status>,<ssid>,<pwd>,<bssid>,<Security>,<MAC>,<ch>,<IP>,<gateway>
     Client Num: <client number>  
     Client <id> MAC:<xx:xx:xx:xx:xx:xx> 
     OK

参数
^^^^

-  **<status>**：连接状态
       - 0：没有连接Wi-Fi(初始状态或者STA模式没有开启)
       - 1：正在连接Wi-Fi或者Wi-Fi重连中
       - 2：连接了Wi-Fi，还没有获取到IP
       - 3：连接到Wi-Fi，并且已经获取到了IP
       - 4：Wi-Fi连接失败（超过了重连次数还没有连接成功的状态）
-  **<ssid>**：连接的AP的SSID
-  **<pwd>**：连接的AP的密码
-  **<bssid>**：连接的AP的BSSID
-  **<Security>**：加密方式
 -  Open //开放网络
 -  WEP
 -  WPA TKIP
 -  WPA AES
 -  WPA Mixed
 -  WPA2 AES
 -  WPA2 TKIP
 -  WPA2 Mixed
 -  WPA/WPA2 TKIP
 -  WPA/WPA2 AES
 -  WPA/WPA2 Mixed
 -  WPA2 Enterprise
 -  WPA/WPA2 Enterprise
 -  WPA3-ASE AES
 -  UnknownType  //未知类型
-  **<MAC>**：Wi-Fi模组的MAC地址(小写字符，冒号分隔)
-  **<ch>**：连接信道
-  **<IP>**：IP地址(点分格式)
-  **<gateway>**：网关地址(点分格式)


说明
^^^^

- 查询Wi-Fi联网信息(这个是从硬件获取的当前状态，不是直接读取我们的设置值)

.. _cmd-WDISCONNECT:

AT+WDISCONNECT 断开当前的AP连接
------------------------------------------


设置命令
^^^^^^^^

**命令：**

::

    AT+WDISCONNECT

**响应：**

::

    OK

示例
^^^^

::

AT+WDTSCONNECT

+EVENT:WIFI DISCONNECT


OK


查询命令
^^^^^^^^

**暂不支持**

.. _cmd-WAUTOCONN:

AT+WAUTOCONN 上电自动重连Wi-Fi
------------------------------------------

设置命令
^^^^^^^^

**命令：**

::

    AT+WAUTOCONN=<status>

**响应：**

::

    OK

参数
^^^^

-  **<status>**：
    - 0：禁用
    - 1：使能


说明
^^^^

- 使能/禁用上电自动连接功能
- 注意：先连接成功路由器后，再发此指令。

示例
^^^^

::

    AT+WAUTOCONN=1

    OK

查询命令
^^^^^^^^

**命令：**

::

    AT+WAUTOCONN?

**响应：**
  
::

    +WAUTOCONN:<status> 
    OK

参数
^^^^

-  **<status>**：
      -  0：禁用
      -  1：使能


 .. _cmd-WAPDHCP:

AT+WAPDHCP AP模式下DHCP参数
------------------------------------------

设置命令
^^^^^^^^

**命令：**

::

    AT+WAPDHCP=<MODE>,<start_ip>,<end_ip>,<GATEWAY>

**响应：**

::

    OK

参数
^^^^

-  **<MODE>**：
    - 0：禁用DHCP
    - 1：使能DHCP
-  **<start_ip>**：DHCP起始地址。eg：192.168.43.100
-  **<end_ip>**：DHCP结束地址。eg：192.168.43.200
-  **<GATEWAY>**：网关IP(使用DHCP时模组IP就是网关IP)，使能DHCP时需设置。eg：192.168.43.1

说明
^^^^

- 设置AP模式下的DHCP参数


示例
^^^^

::

    AT+WAPDHCP=1,192.168.43.100,192.168.43.200,192.168.43.1

    OK

查询命令
^^^^^^^^

**命令：**

::

   AT+WAPDHCP?

**响应：**
  
::

    +WAPDHCP:<MODE>[,<start_ip>,<end_ip>,<GATEWAY>]
    OK   
参数
^^^^

-  **<MODE>**：
    - 0：禁用DHCP
    - 1：使能DHCP
-  **<start_ip>**：DHCP起始地址。eg：192.168.43.100
-  **<end_ip>**：DHCP结束地址。eg：192.168.43.200
-  **<GATEWAY>**：网关IP(使用DHCP时模组IP就是网关IP)，使能DHCP时需设置。eg：192.168.43.1

.. _cmd-WAP:

AT+WAP AP模式Wi-Fi参数
------------------------------------------


设置命令
^^^^^^^^

**命令：**

::

    AT+WAP=<ssid>,<pwd>,<channel>,<max conn>,<ssid hidden>

**响应：**

::

    OK

参数
^^^^

-  **<ssid>**：Wi-Fi名称(最大长度为32字节)
-  **<pwd>**：Wi-Fi密码，空字符串表示无密码(最大长度为32字节)
-  **<channel>**：Wi-Fi 信道
-  **<max conn>**：最大连接数量(不写默认是3)
-  **<ssid hidden>**：是否隐藏SSID，0不隐藏，1隐藏

示例
^^^^

::

    AT+WAP=MY_Wi-Fi,12345678,1,3,0
    OK


查询命令
^^^^^^^^

**命令：**

::

    AT+WAP?

**响应：**
  
::

    +WAP:<ssid>,<pwd>,<security>,<channel>,<max conn>,<ssid hidden>,<mac>,<IP>,<Gateway>
    OK

参数
^^^^

-  **<ssid>**：AP的SSID
-  **<pwd>**：AP的密码
-  **<Security>**：加密方式
 -  Open //开放网络
 -  WEP
 -  WPA TKIP
 -  WPA AES
 -  WPA Mixed
 -  WPA2 AES
 -  WPA2 TKIP
 -  WPA2 Mixed
 -  WPA/WPA2 TKIP
 -  WPA/WPA2 AES
 -  WPA/WPA2 Mixed
 -  WPA2 Enterprise
 -  WPA/WPA2 Enterprise
 -  WPA3-ASE AES
 -  UnknownType  //未知类型
-  **<channel>**：AP的信道
-  **<max conn>**：AP的最大支持的连接STA个数
-  **<ssid hidden>**：AP的SSID是否隐藏
-  **<mac>**：开启AP热点的网卡MAC地址
-  **<IP>**：AP的IP地址(点分格式)
-  **<Gateway>**：网关地址(点分格式)


说明
^^^^

- 查询AP参数信息(这个是从硬件获取的当前状态，不是直接读取我们的设置值)

.. _cmd-PING:

AT+PING 进行PING操作
------------------------------------------


设置命令
^^^^^^^^

**命令：**

::

   AT+PING=<addr>[,<count>]

**响应：**

::
   
   //成功
   +PING:<time>
   OK
   //失败
   +PING:TIMEOUT
   ERROR
   //返回值描述
   time：平均延时ms

参数
^^^^

-  **<addr>**：ip地址或者域名
-  **<count>**：ping次数，默认3次，loop表示一直ping不返回(此时只能重启模组)

示例
^^^^

::

    AT+PING=192.168.4.134
    +PING:<30>
    OK

.. _cmd-CIPSTAMAC_DEF:

AT+CIPSTAMAC_DEF   Wi-Fi station MAC地址
------------------------------------------


设置命令
^^^^^^^^

**命令：**

::

    AT+CIPSTAMAC_DEF=<MAC>

**响应：**

::
   
   OK

参数
^^^^

-  **<MAC>**：要设置的MAC地址，MAC格式84f3ebdd9e63(小写无分隔)

示例
^^^^

::

   AT+CIPSTAMAC_DEF=84f3ebdd9e63

   OK

查询命令
^^^^^^^^

**命令：**

::

    AT+CIPSTAMAC_DEF?

**响应：**

::

    +CIPSTAMAC_DEF:<MAC> 
    OK

参数
^^^^

-  **<MAC>**：要设置的MAC地址，MAC格式84f3ebdd9e63(小写无分隔)

示例
^^^^

::

    AT+CIPSTAMAC_DEF
    +CIPSTAMAC_DEF:84f3ebdd9e63
    OK

.. _cmd-WCOUNTRY:

AT+WCOUNTRY  Wi-Fi国家码
------------------------------------------

设置命令
^^^^^^^^

**命令：**

::

    AT+WCOUNTRY=<country_code>

**响应：**

::
   
   OK

参数
^^^^

-  **<country_code>**：Wi-Fi国家码
    - 0：不指定国家码，使用SDK默认配置
    - 1：JP日本
    - 2：AS美属萨摩亚
    - 3：CA加拿大
    - 4：US美国
    - 5：CN中国
    - 6：HK中国香港
    - 7：TW中国台湾
    - 8：MO中国澳门
    - 9：IL以色列
    - 10：SG新加坡
    - 11：KR韩国
    - 12：TR土耳其
    - 13：AU澳大利亚
    - 14：ZA南非
    - 15：BR巴西

示例
^^^^

::

   AT+WCOUNTRY=5

   OK

查询命令
^^^^^^^^

**命令：**

::

    AT+WCOUNTRY?

**响应：**

::

    +WCOUNTRY:<country_code>
    OK

参数
^^^^

-  **<country_code>**：Wi-Fi国家码
    - 0：不指定国家码，使用SDK默认配置
    - 1：JP日本
    - 2：AS美属萨摩亚
    - 3：CA加拿大
    - 4：US美国
    - 5：CN中国
    - 6：HK中国香港
    - 7：TW中国台湾
    - 8：MO中国澳门
    - 9：IL以色列
    - 10：SG新加坡
    - 11：KR韩国
    - 12：TR土耳其
    - 13：AU澳大利亚
    - 14：ZA南非
    - 15：BR巴西


示例
^^^^

::

    AT+WCOUNTRY?
    +WCOUNTRY:5
    OK

.. _cmd-WCONFIG:

AT+WCONFIG  手机配网
------------------------------------------

设置命令
^^^^^^^^

**命令：**

::

    AT+WCONFIG=<status>[,<name>]

**响应：**

::
   
   OK

参数
^^^^

-  **<status>**：
 - 0：关闭手机配网任务
 - 1：开启一次 Wi-Fi 配网(配网成功/配网超时会自动返回关闭状态)
 - 2：开启一次蓝牙配网(配网成功/配网超时会自动返回关闭状态)
 - 3：开启一次 AirKiss 配网

  - **BW16模组**
   - 1：瑞昱 Simple Config
   - 2：瑞昱 Wi-Fi Config
  - **Ai-WB2系列模组**
   - 1：Wi-Fi 配网(touch)
   - 2：蓝牙配网(BluFi)
   - 3：微信 AirKiss 配网   

-  **<name>**：这个是用来自定义配网广播名称的，当前仅BluFi协议支持该参数配网协议

示例
^^^^

::

    AT+WCONFIG=1

    OK
    
查询命令
^^^^^^^^

**命令：**

::

    AT+WCONFIG?

**响应：**

::

    +WCONFIG:<status>
    OK

参数
^^^^

-  **<status>**：
  -  0：关闭手机配网任务
  -  1：开启一次Wi-Fi配网(配网成功/配网超时会自动返回关闭状态)
  -  2：开启一次蓝牙配网(配网成功/配网超时会自动返回关闭状态)
    
示例
^^^^

::

    AT+WCONFIG?
    +WCONFIG:1
    OK

.. _cmd-WSCANOPT:

AT+WSCANOPT  筛选Wi-Fi扫描显示信息
------------------------------------------

设置命令
^^^^^^^^

**命令：**

::
    
    AT+WSCANOPT=<option>

**响应：**

::
   
   OK

参数
^^^^

 - **<option>**：Wi-Fi 扫描结果是否显示以下参数，默认值：0xFF，设置某位 bit 为 1，则显示对应参数，设为 0，则不显示对应参数。option 有两种输入方式（ 16 进制 0xXY 的形式和 10 进制的形式）。
 - bit 0: 是否显示 <ssid>
 - bit 1: 是否显示 <channel>
 - bit 2: 是否显示 <security>
 - bit 3: 是否显示 <rssi>
 - bit 4: 是否显示 <MAC>

示例
^^^^

::

    AT+WSCANOPT=15

    +WSCANOPT:0x0f

    OK

    AT+WSCANOPT=0x0f

    +WSCANOPT:0x0f

    OK

查询命令
^^^^^^^^

**命令：**

::
    
    AT+WSCANOPT?

**响应：**

::

    +WSCANOPT:<option>
    OK

参数
^^^^

 -  **<option>**：Wi-Fi 扫描结果是否显示以下参数，默认值：0xFF，设置某位 bit 为 1，则显示对应参数，设为 0，则不显示对应参数。option 有两种输入方式（ 16 进制 0xXY 的形式和 10 进制的形式）。
 - bit 0: 是否显示 <ssid>
 - bit 1: 是否显示 <channel>
 - bit 2: 是否显示 <security>
 - bit 3: 是否显示 <rssi>
 - bit 4: 是否显示 <MAC>
    
示例
^^^^
::

    AT+WSCANOPT?
    +WSCANOPT:0xff
    OK

.. _cmd-WRSSI:

AT+WRSSI  查询 Wi-Fi 连接信号强度
------------------------------------------
查询命令
^^^^^^^^

**命令：**

::

    AT+WRSSI or AT+WRSSI?
    
**响应：**

::
   
    +WRSSI :<rssi>
    OK

参数
^^^^

 - **<rssi>**：Wi-Fi 连接信号强度

示例
^^^^

::

    AT+WRSSI
    +WSCANOPT:-50
    OK
