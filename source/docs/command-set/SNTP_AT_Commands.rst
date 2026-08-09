SNTP AT 命令集
==================================================

本章节介绍驱动 SNTP 指令集，此指令集针对不同的模组会有所不同的适配，具体差异请移步：:doc:`../instruction/other/firmware_differences`。

 - :ref:`AT+SNTPTIME <cmd-SNTPTIME>`：查询 SNTP 时间
 - :ref:`AT+SNTPTIMECFG <cmd-SNTPTIMECFG>`：查询和设置 SNTP 时区和服务器
 - :ref:`AT+SNTPINTV <cmd-SNTPINTV>`：查询和设置 SNTP 刷新时间间隔


.. _cmd-SNTPTIME:

AT+SNTPTIME:查询 SNTP 时间
------------------------------------------

说明
^^^^

- SNTP 默认没有开启，需要联网后使用 AT+SNTPTIMECFG 启动，没有启用的时候查询的是本地 RTC 时间


查询命令
^^^^^^^^

**命令：**

::

    AT+SNTPTIME?

**响应：**

::

    +SNTPTIME:<week> <month> <day> <HH>:<mm>:<ss> <yyyy>
    OK

参数
^^^^

- **<week>**：星期[Mon,Tue,Wed,Thu,Fri,Sat,Sun]
- **<month>**：月份[Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec]
- **<day>**：日
- **<HH>**：小时
- **<mm>**：分钟
- **<ss>** ：秒
- **<yyyy>** ：年

示例
^^^^

::

    AT+SNTPTIMECFG=1,8//开启 SNTP

    OK

    AT+SNTPTIME?//同步成功后查询时间

    +SNTPTIME:Wed May 03 10:49:41 2023

    OK


.. _cmd-SNTPTIMECFG:

AT+SNTPTIMECFG 查询和设置 SNTP 时区和服务器
--------------------------------------------------------------------------------



设置命令
^^^^^^^^

**命令：**

::

    AT+SNTPTIMECFG=<enable>,<timezone>[,<SNTP server1>,<SNTP server2>,<SNTP server3>]

**响应：**

::

    OK

参数
^^^^

-  **<enable>**：SNTP 刷新服务状态设置；0 关闭；1 启动
-  **<timezone>**：时区，取值-12~+14
-  **<SNTP server1/2/3>**：SNTP服务器域名，如果缺省默认设置为"cn.ntp.org.cn"，"ntp.sjtu.edu.cn"，"us.pool.ntp.org"

示例
^^^^

::

   AT+SNTPTIMECFG=1,8,cn.ntp.org.cn

   OK


查询命令
^^^^^^^^

**命令：**

::

    AT+SNTPTIMECFG?

**响应：**

::

    +SNTPTIMECFG:<enable>,<timezone>[,<SNTP server1>,<SNTP server2>,<SNTP server3>]

    OK

参数
^^^^

- **<SNTPTIME>**：响应时间
- **<enable>**：SNTP 刷新服务是否启动；0 未运行；1 运行中
- **<timezone>**：时区，取值-12~+14
- **<SNTP server1/2/3>**：SNTP 服务器域名


示例
^^^^

::

    AT+SNTPTIMECFG?

    +SNTPTIMECFG:1,8,"cn.ntp.org.cn","ntp.sjtu.edu.cn","us.pool.ntp.org"

    OK


.. _cmd-SNTPINTV:

AT+SNTPINTV 查询和设置 SNTP 刷新时间间隔
------------------------------------------

设置命令
^^^^^^^^

**命令：**

::

   AT+SNTPINTV=<interval second>

**响应：**

::

    OK

参数
^^^^

-  **<interval second>**：刷新间隔，单位 S，取值 15~4294967


示例
^^^^

::

    AT+SNTPINTV=15

    OK

查询命令
^^^^^^^^

**命令：**

::

   AT+SNTPINTV?

**响应：**

::

   +SNTPINTV:<interval second>
   OK

 interval second：刷新间隔，单位 S

参数
^^^^

-  **<interval second>**： second：刷新间隔，单位 S


示例
^^^^

::

   AT+SNTPINTV?

   +SNTPINTV:3600
   OK
