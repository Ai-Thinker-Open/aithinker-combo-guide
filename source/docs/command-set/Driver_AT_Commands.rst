驱动外设 AT 命令集
==================================================

本章节介绍驱动外设AT指令集，此指令集针对不同的模组会有所不同的适配，具体差异请移步：:doc:`../instruction/other/firmware_differences`。

 - :ref:`AT+SYSIOMAP <cmd-SYSIOMAP>`： 查询或设置 IO 映射表
 - :ref:`AT+SYSGPIOWRITE <cmd-SYSGPIOWRITE>`：设置 GPIO 输出电平
 - :ref:`AT+SYSGPIOREAD <cmd-SYSGPIOREAD>`：读取 GPIO 电平
 - :ref:`AT+PWMCFG <cmd-PWMCFG>`：配置 PWM 功能
 - :ref:`AT+PWMCFG <cmd-PWMCFGS>`：配置 PWM 功能
 - :ref:`AT+PWMSTOP <cmd-PWMSTOP>`：关闭 PWM 功能
 - :ref:`AT+PWMDUTYSET <cmd-PWMDUTYSET>`：更新 PWM 占空比
 - :ref:`AT+PWMDUTYSETS <cmd-PWMDUTYSETS>`：更新 PWM 占空比

.. _cmd-SYSIOMAP:

AT+SYSIOMAP 查询或设置 IO 映射表
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+SYSIOMAP=<PinNumber>,<pin1>,<pin2>,...,<pinN>

**响应：**

::

    OK

参数
^^^^

-  **<pinNumber>**：要设置的 IO 总数。
-  **<pinxx>**：模组 IO 引脚
    - （从模组左上角逆时针排序，引脚序号从 1 开始）对应的芯片引脚编号(1~254，这个根据芯片手册上的引脚编号来就可以)如果模组没有对应芯片引脚则设置为 NC


说明
^^^^

- 设置 IO 管脚映射关系。


示例
^^^^

::

    AT+SYSIOMAP=4,3,5,NC,1
    OK

    //这个指令含义一共设置 4 个 IO 的映射关系
    //模组的 1 号引脚对应芯片的 3 号引脚；
    //模组的 2 号引脚对应芯片的 5 号引脚；
    //模组的 3 号引脚没有连接到芯片或者该引脚禁止使用 AT 指令控制
    //模组的 4 号引脚对应芯片的 1 号引脚

查询命令
^^^^^^^^

**命令：**

::

    AT+SYSIOMAP? 

**响应：**

::

    +SYSIOMAP:PinNumber:<PinNumber>,PinMap:<pin1>,<pin2>,...,<pinN>

参数
^^^^

-  **<PinNumber>**：表示当前映射表一共有几组数。
-  **<pinxx>**：模组 IO 引脚
    - （从模组左上角逆时针排序，引脚序号从 1 开始）对应的芯片引脚编号(1~254，这个根据芯片手册上的引脚编号来就可以)如果模组没有对应芯片引脚则设置为 NC


说明
^^^^

- 查询 IO 管脚映射关系表

示例
^^^^

::

    AT+SYSIOMAP?
    +SYSIOMAP:PinNumber:6,PinMap:NC,5,20,NC,15,NC
    OK


.. _cmd-SYSGPIOWRITE:

AT+SYSGPIOWRITE 设置 GPIO 输出电平
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+SYSGPIOWRITE=<pin>,<level>

**响应：**

::

    OK

参数
^^^^

-  **<pin>**：模组 IO 引脚号。
    - 从模组左上角逆时针排序，引脚序号从 1 开始
-  **<level>**： 引脚电平。
    -  0：低电平
    -  1：高电平


说明
^^^^

- 设置 GPIO 输出电平


示例
^^^^

::

    AT+SYSGPIOWRITE=4,1


.. _cmd-SYSGPIOREAD:

AT+SYSGPIOREAD 读取 GPIO 电平
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+SYSGPIOREAD=<pin>

**响应：**

::

    +SYSGPIOREAD:<pin>,<level>

参数
^^^^

-  **<pin>**：模组 IO 引脚号
    - 从模组左上角逆时针排序，引脚序号从 1 开始
-  **<level>**： 引脚电平。
    -  0：低电平
    -  1：高电平


说明
^^^^

- 读取 GPIO 电平


示例
^^^^

::

    AT+SYSGPIOREAD=4

    +SYSGPIOREAD:4,1


.. _cmd-PWMCFG:

AT+PWMCFG 配置 PWM 功能
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+PWMCFG=<pin>,<cycle>,<duty>

**响应：**

::

    OK

参数
^^^^

-  **<pin>**：模组 IO 引脚号
    - 从模组左上角逆时针排序，引脚序号从 1 开始
-  **<cycle>**：PWM 周期
    - 单位 us
-  **<duty>**：占空比
    - 整数 0~100 

说明
^^^^

- Ai-WB2 系列模组一共有 5 路 PWM，同时开启时必须注意芯片引脚的 IO 序号对 5 取余不能重复，否则只会有一个生效，例如设置了 IO1/2/6 实际只有 IO2/6生效，IO1 被 IO6 覆盖了

- 注意：该指令设置的单位是芯片的周期寄存器，相同参数在不同的模组上的效果可能不同，如果在精度可以满足要求的情况下推荐使用 AT+PWMCFGS 设置，这个指令相同参数在不同模组上的效果会基本保持一致(不同芯片可能会存在几 us 的差异)



示例
^^^^

::

    AT+SYSIOMAP=38,NC,NC,NC,NC,11,NC,NC,14,17,3,NC,NC,NC,NC,NC,NC,NC,NC,NC,NC,NC,NC,NC,NC,NC,NC,4,NC,NC,NC,5,NC,NC,NC,NC,12,NC,NC

    AT+PWMCFG=27,3000,80



.. _cmd-PWMCFGS:

AT+PWMCFG 配置 PWM 功能
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+PWMCFGS=<pin>,<cycle>,<duty>

**响应：**

::

    OK

参数
^^^^

-  **<pin>**：模组 IO 引脚号
    - 从模组左上角逆时针排序，引脚序号从 1 开始
-  **<cycle>**：PWM 周期
    - 单位 us
-  **<duty>**：占空比
    - 整数 0~100 

说明
^^^^

- Ai-WB2 系列模组一共有 5 路 PWM，同时开启时必须注意芯片引脚的 IO 序号对 5 取余不能重复，否则只会有一个生效，例如设置了 IO1/2/6 实际只有 IO2/6生效，IO1 被 IO6 覆盖了

- 注意：该指令设置的单位是芯片的周期寄存器，相同参数在不同的模组上的效果可能不同，如果在精度可以满足要求的情况下推荐使用 AT+PWMCFGS 设置，这个指令相同参数在不同模组上的效果会基本保持一致(不同芯片可能会存在几 us 的差异)


示例
^^^^

::

    AT+SYSIOMAP=38,NC,NC,NC,NC,11,NC,NC,14,17,3,NC,NC,NC,NC,NC,NC,NC,NC,NC,NC,NC,NC,NC,NC,NC,NC,4,NC,NC,NC,5,NC,NC,NC,NC,12,NC,NC

    AT+PWMCFGS=27,3000,80



.. _cmd-PWMSTOP:

AT+PWMSTOP 关闭 PWM 功能
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+PWMSTOP=<pin>

**响应：**

::

    OK

参数
^^^^

-  **<pin>**：模组 IO 引脚号
    - 从模组左上角逆时针排序，引脚序号从 1 开始

说明
^^^^

- 关闭 PWM 功能

示例
^^^^

::
    
    AT+PWMSTOP=27


.. _cmd-PWMDUTYSET:

AT+PWMDUTYSET 更新 PWM 占空比
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+PWMDUTYSET=<pin>,<duty>

**响应：**

::

    OK

参数
^^^^

-  **<pin>**：模组 IO 引脚号
    - 从模组左上角逆时针排序，引脚序号从 1 开始
-  **<duty>**：占空比
    - 整数 0~100 


说明
^^^^

- 更新 PWM 占空比

示例
^^^^

::

    AT+PWMDUTYSET=27,60

    OK


.. _cmd-PWMDUTYSETS:

AT+PWMDUTYSETS 更新 PWM 占空比
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+PWMDUTYSETS=<pin>,<duty>

**响应：**

::

    OK

参数
^^^^

-  **<pin>**：模组 IO 引脚号
    - 从模组左上角逆时针排序，引脚序号从 1 开始
-  **<duty>**：占空比
    - 整数 0~100 

说明
^^^^

- 更新 PWM 占空比

示例
^^^^

::

    AT+PWMDUTYSETS=27,60

    OK


