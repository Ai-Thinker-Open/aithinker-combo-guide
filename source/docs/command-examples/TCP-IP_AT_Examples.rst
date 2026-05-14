TCP-IP AT 示例
====================================

本文档主要介绍在设备上运行 :doc:`../command-set/TCP-IP_AT_Commands` 命令的详细示例。

.. contents::
   :local:
   :depth: 1

设备作为 TCP 客户端建立单连接
--------------------------------------------

#. 设置 Wi-Fi 模式为 station。

   命令：

   .. code-block:: none

     AT+WMODE=1,1

   响应：

   .. code-block:: none

     OK

#. 连接到路由器。

   命令：

   .. code-block:: none

     AT+WJAP="aithinker","1234567890"

   响应：

   .. code-block:: none

     +EVENT:WIFI_CONNECT
     
     OK

     +EVENT:WIFI_GOT_IP

   说明：

   - 您输入的 SSID 和密码可能跟上述命令中的不同。请使用您的路由器的 SSID 和密码。

#. 查询设备 IP 地址。

   命令：

   .. code-block:: none

     AT+WJAP?

   响应：

   .. code-block:: none

     +WJAP:3,aithinker,1234567890,14:de:39:06:86:e4,WPA2 TKIP,
     7c:b9:4c:1d:c6:39,6,192.168.3.142,192.168.3.1

     OK

   说明：

   - 您的查询结果可能与上述响应中的不同。

#. PC 与设备连接同一个路由。

   在 PC 上使用网络调试工具，创建一个 TCP 服务器。例如 TCP 服务器的 IP 地址为 ``192.168.3.162``，端口为 ``6666``。

#. 设备作为客户端通过 TCP 连接到 TCP 服务器，服务器 IP 地址为 ``192.168.3.162``，端口为 ``6666``。

   命令：

   .. code-block:: none

     AT+SOCKET=4,192.168.3.162,6666

   响应：

   .. code-block:: none

     connect success ConID=1

     OK

#. 发送 9 字节数据。

   命令：

   .. code-block:: none

     AT+SOCKETSEND=1,9

   响应：

   .. code-block:: none

     >

   输入 9 字节数据，例如输入数据是 ``aithinker``，之后 AT 将会输出以下信息。

   .. code-block:: none

     OK

#. 接收 9 字节数据。

   假设 TCP 服务器发送 9 字节的数据（数据为 ``aithinker``），则系统会提示：

   .. code-block:: none

     +EVENT:SocketDown,1,9


   这时候发送AT+SOCKETREAD=<ConID>命令从指定连接读取数据

   命令：

   .. code-block:: none

     AT+SOCKETREAD=1

   响应：

   .. code-block:: none

     +SOCKETREAD,1,9,aithinker

设备作为 TCP 服务器建立多连接
--------------------------------------------

以下是设备作为 softAP 建立 TCP 服务器的示例；如果是设备作为 station，可在连接路由器后按照同样方法建立服务器。

#. 设置 Wi-Fi 模式为 softAP。

   命令：

   .. code-block:: none

     AT+WMODE=2,1

   响应：

   .. code-block:: none

     OK

#. 设置 softAP。

   命令：

   .. code-block:: none

     AT+WAP="aithinker778","12345678",6,3,0

   响应：

   .. code-block:: none

     OK

#. 查询 softAP 信息。

   命令：

   .. code-block:: none

     AT+WAP?

   响应：

   .. code-block:: none

     +WAP:aithinker778,12345678,WPA/WPA2 AES,6,3,0,7c:b9:4c:1d:c6:39,1.168.43.1,192.168.43.1
     Client Num: 0

     OK

   说明：

   - 您查询到的地址可能与上述响应中的不同。

#. PC需连接设备创建的Wi-Fi热点保证在同一个网段。

   在 PC 上使用网络调试工具创建一个 TCP 客户端，连接到设备创建的 TCP 服务器。

#. 建立 TCP 服务器。

   命令：

   .. code-block:: none

     AT+SOCKET=3,6666

   响应：

   .. code-block:: none

     OK

#. 1.发送 9 字节数据到网络连接 ID 为 2 的链路上。

   命令：

   .. code-block:: none

     AT+SOCKETSENDLINE=2,9,aithinker

   响应：

   .. code-block:: none

     OK

   说明：

   - 若输入的字节数目超过 ``AT+SOCKETSENDLINE`` 命令设定的长度 (n)，则只发送数据的前 n 个字节，发送完成后响应 ``OK``。

#. 从网络连接 ID 为 2 的链路上接收 9 字节数据。

   假设 TCP 服务器发送 9 字节的数据（数据为 ``aithinker``），则系统会提示：

   .. code-block:: none

     +EVENT:SocketSeed,2,1

   这时候发送AT+SOCKETREAD=<ConID>命令从指定连接读取数据

   命令：

   .. code-block:: none

      AT+SOCKETREAD=2

   响应：

   .. code-block:: none

     +SOCKETREAD,1,9,aithinker

#. 关闭 TCP 连接。

   命令：

   .. code-block:: none

     AT+SOCKETDEL=2

   响应：

   .. code-block:: none

     OK

#. 2.发送 9 字节数据到网络连接 ID 为 3 的链路上。

   命令：

   .. code-block:: none

     AT+SOCKETSENDLINE=3,9,aithinker

   响应：

   .. code-block:: none

     OK

   说明：

   - 若输入的字节数目超过 ``AT+SOCKETSENDLINE`` 命令设定的长度 (n)，则只发送数据的前 n 个字节，发送完成后响应 ``OK``。

#. 从网络连接 ID 为 3 的链路上接收 9 字节数据。

   假设 TCP 服务器发送 9 字节的数据（数据为 ``aithinker``），则系统会提示：

   .. code-block:: none

     +EVENT:SocketSeed,3,1

   这时候发送AT+SOCKETREAD=<ConID>命令从指定连接读取数据

   命令：

   .. code-block:: none

      AT+SOCKETREAD=3

   响应：

   .. code-block:: none

     +SOCKETREAD,1,9,aithinker

#. 关闭 TCP 连接。

   命令：

   .. code-block:: none

     AT+SOCKETDEL=3

   响应：

   .. code-block:: none

     OK

设备作为 UDP 服务器建立单连接,实现 UART Wi-Fi 透传
-----------------------------------------------------

#. 设置 Wi-Fi 模式为 station。

   命令：

   .. code-block:: none

     AT+WMODE=1,1

   响应：

   .. code-block:: none

     OK

#. 连接到路由器。

   命令：

   .. code-block:: none

     AT+WJAP="aithinker","1234567890"

   响应：

   .. code-block:: none

     +EVENT:WIFI_CONNECT
     
     OK

     +EVENT:WIFI_GOT_IP

   说明：

   - 您输入的 SSID 和密码可能跟上述命令中的不同。请使用您的路由器的 SSID 和密码。

#. 查询设备 IP 地址。

   命令：

   .. code-block:: none

     AT+WJAP?

   响应：

   .. code-block:: none

     +WJAP:3,aithinker,1234567890,14:de:39:06:86:e4,WPA2 TKIP,
     7c:b9:4c:1d:c6:39,6,192.168.3.142,192.168.3.1

     OK

   说明：

   - 您的查询结果可能与上述响应中的不同。

#. PC 与设备连接到同一个路由。

   在 PC 上使用网络调试工具创建一个 UDP 客户端，连接到设备创建的 UDP 服务器。

#. PC 上使用网络调试工具作为 UDP 客户端通过 UDP 连接到 设备的 UDP 服务器，服务器 IP 地址为 ``192.168.3.142``，端口为 ``6666``。

   命令：

   .. code-block:: none

     AT+SOCKET=1,6666

   响应：

   .. code-block:: none

     connect success ConID=1

     OK


#. 接收 9 字节数据。

   假设 UDP 客户端 发送 9 字节的数据（数据为 ``aithinker``），则系统会提示：

   .. code-block:: none

     +EVENT:SocketDown,1,9


   这时候发送AT+SOCKETREAD=<ConID>命令从指定连接读取数据

   命令：

   .. code-block:: none

     AT+SOCKETREAD=1

   响应：

   .. code-block:: none

     +SOCKETREAD,1,9,aithinker

#. 发送 9 字节数据。

   命令：

   .. code-block:: none

     AT+SOCKETTT

   响应：

   .. code-block:: none

     >

   输入 9 字节数据，例如输入数据是 ``aithinker``，之后 AT 将会输出以下信息。

   .. code-block:: none

      OK

#. 关闭 UDP 连接。

   命令：

   .. code-block:: none

     AT+SOCKETDEL=1

   响应：

   .. code-block:: none

     OK

设备作为 UDP 客户端建立单连接
---------------------------------------------------

#. 设置 Wi-Fi 模式为 station。

   命令：

   .. code-block:: none

     AT+WMODE=1,1

   响应：

   .. code-block:: none

     OK

#. 连接到路由器。

   命令：

   .. code-block:: none

     AT+WJAP="aithinker","1234567890"

   响应：

   .. code-block:: none

     +EVENT:WIFI_CONNECT
     
     OK

     +EVENT:WIFI_GOT_IP

   说明：

   - 您输入的 SSID 和密码可能跟上述命令中的不同。请使用您的路由器的 SSID 和密码。

#. 查询设备 IP 地址。

   命令：

   .. code-block:: none

     AT+WJAP?

   响应：

   .. code-block:: none

     +WJAP:3,aithinker,1234567890,14:de:39:06:86:e4,WPA2 TKIP,
     7c:b9:4c:1d:c6:39,6,192.168.3.142,192.168.3.1

     OK

   说明：

   - 您的查询结果可能与上述响应中的不同。

#. PC 与设备连接同一个路由。

   在 PC 上使用网络调试工具，创建一个 UDP 服务器。例如 UDP 服务器的 IP 地址为 ``192.168.3.162``，端口为 ``6666``。

#. 设备作为客户端通过 UDP 连接到 UDP 服务器。

   命令：

   .. code-block:: none

     AT+SOCKET=2,192.168.3.162,6666

   响应：

   .. code-block:: none

     connect success ConID=1

     OK

#. 发送 9 字节数据。

   命令：

   .. code-block:: none

     AT+SOCKETSEND=1,9

   响应：

   .. code-block:: none

     >

   输入 9 字节数据，例如输入数据是 ``aithinker``，之后 AT 将会输出以下信息。

   .. code-block:: none

     OK

#. 接收 9 字节数据。

   假设 UDP 服务器发送 9 字节的数据（数据为 ``aithinker``），则系统会提示：

   .. code-block:: none

     +EVENT:SocketDown,1,9


   这时候发送AT+SOCKETREAD=<ConID>命令从指定连接读取数据

   命令：

   .. code-block:: none

     AT+SOCKETREAD=1

   响应：

   .. code-block:: none

     +SOCKETREAD,1,9,aithinker

#. 关闭 UDP 连接。

   命令：

   .. code-block:: none

     AT+SOCKETDEL=1

   响应：

   .. code-block:: none

     OK

设备作为 TCP 客户端，建立单连接，实现 UART Wi-Fi 透传
-----------------------------------------------------------------------------------------

#. 设置 Wi-Fi 模式为 station。

   命令：

   .. code-block:: none

     AT+WMODE=1,1

   响应：

   .. code-block:: none

     OK

#. 连接到路由器。

   命令：

   .. code-block:: none

     AT+WJAP="aithinker","1234567890"

   响应：

   .. code-block:: none

     +EVENT:WIFI_CONNECT

     OK

     +EVENT:WIFI_GOT_IP

   说明：

   - 您输入的 SSID 和密码可能跟上述命令中的不同。请使用您的路由器的 SSID 和密码。

#. 查询设备 IP 地址。

   命令：

   .. code-block:: none

     AT+WJAP?

   响应：

   .. code-block:: none

     +WJAP:3,aithinker,1234567890,14:de:39:06:86:e4,WPA2 TKIP,
     7c:b9:4c:1d:c6:39,6,192.168.3.142,192.168.3.1

     OK

   说明：

   - 您的查询结果可能与上述响应中的不同。

#. PC 与 设备连接到同一个路由。

   在 PC 上使用网络调试工具，创建一个 TCP 服务器。例如 IP 地址为 ``192.168.3.162``，端口为 ``6666``。

#. 设备作为客户端通过 TCP 连接到 TCP 服务器，服务器 IP 地址为 ``192.168.3.162``，端口为 ``6666``。

   命令：

   .. code-block:: none

     AT+SOCKET=4,192.168.3.162,6666

   响应：

   .. code-block:: none

     OK

#. 进入 UART Wi-Fi :term:`透传模式` 并发送数据。

   命令：

   .. code-block:: none

     AT+SOCKETTT

   响应：

   .. code-block:: none

     >

#. 停止发送数据

   在透传发送数据过程中，若识别到单独的一包数据 ``+++``，则系统会退出透传发送。此时请至少等待 1 秒，再发下一条 AT 命令。请注意，如果直接用键盘打字输入 ``+++``，有可能因时间太慢而不能被识别为连续的三个 ``+``。

   .. Important::

     使用 ``+++`` 可退出 :term:`透传模式`，回到 :term:`接收模式`，此时 TCP 连接仍然有效。您也可以使用 ``AT+SOCKETTT`` 命令恢复透传。

#. 关闭 TCP 连接。

   命令：

   .. code-block:: none

     AT+SOCKETDEL=1

   响应：

   .. code-block:: none

     OK

设备作为 TCP 服务器，建立单连接，实现 UART Wi-Fi 透传
-----------------------------------------------------------------------------------------

#. 设置 Wi-Fi 模式为 station。

   命令：

   .. code-block:: none

     AT+WMODE=1,1

   响应：

   .. code-block:: none

     OK

#. 连接到路由器。

   命令：

   .. code-block:: none

     AT+WJAP="aithinker","1234567890"

   响应：

   .. code-block:: none

     +EVENT:WIFI_CONNECT

     OK

     +EVENT:WIFI_GOT_IP

   说明：

   - 您输入的 SSID 和密码可能跟上述命令中的不同。请使用您的路由器的 SSID 和密码。

#. 查询设备 IP 地址。

   命令：

   .. code-block:: none

     AT+WJAP?

   响应：

   .. code-block:: none

     +WJAP:3,aithinker,1234567890,14:de:39:06:86:e4,WPA2 TKIP,
     7c:b9:4c:1d:c6:39,6,192.168.3.142,192.168.3.1

     OK

   说明：

   - 您的查询结果可能与上述响应中的不同。

#. PC 与 设备连接到同一个路由。

   在 PC 上使用网络调试工具，创建一个 TCP 客户端。例如 IP 地址为 ``192.168.3.142``，端口为 ``6666``。通过AT+WJAP?指令进行查询

#. 网络调试工具作为客户端通过 TCP 连接到设备，设备 IP 地址为 ``192.168.3.142``，端口为 ``6666``。

   命令：

   .. code-block:: none

     AT+SOCKET=3,6666

   响应：

   .. code-block:: none

    connect success ConID=1

    OK

#. 进入 UART Wi-Fi :term:`透传模式` 并发送数据。

   命令：

   .. code-block:: none

     AT+SOCKETTT

   响应：

   .. code-block:: none

     >

#. 停止发送数据

   在透传发送数据过程中，若识别到单独的一包数据 ``+++``，则系统会退出透传发送。此时请至少等待 1 秒，再发下一条 AT 命令。请注意，如果直接用键盘打字输入 ``+++``，有可能因时间太慢而不能被识别为连续的三个 ``+``。

   .. Important::

     使用 ``+++`` 可退出 :term:`透传模式`，回到 :term:`接收模式`，此时 TCP 连接仍然有效。您也可以使用 ``AT+SOCKETTT`` 命令恢复透传。

#. 关闭 TCP 连接,这里填写的参数填写客户端加进来的链接，需要加上1

   命令：

   .. code-block:: none

     AT+SOCKETDEL=2

   响应：

   .. code-block:: none

     OK


通过TCP SSL(HTTPS)实现大文本请求方法(此例子需要把串口工具回车换行功能去掉)
-------------------------------------------------------------------------------------

#. 设置 Wi-Fi 模式为 station。

   命令：

   .. code-block:: none

     AT+WMODE=1,1\r\n

   响应：

   .. code-block:: none

     OK

#. 连接到路由器。

   命令：

   .. code-block:: none

     AT+WJAP="aithinker","1234567890"\r\n

   响应：

   .. code-block:: none

     +EVENT:WIFI_CONNECT

     OK

     +EVENT:WIFI_GOT_IP

   说明：

   - 您输入的 SSID 和密码可能跟上述命令中的不同。请使用您的路由器的SSID和密码。

#. 设置为socket接收模式。

   命令：

   .. code-block:: none

     AT+SOCKETRECVCFG=1\r\n

   响应：

   .. code-block:: none

     OK

#. 设置创建socket(以SSL方式)连接。

   命令：

   .. code-block:: none

     AT+SOCKET=7,httpbin.org,443\r\n

   响应：

   .. code-block:: none

     OK

   说明：

   - 您要连接的服务器域名或者IP不同。请输入您要连接的服务器域名或者IP。


#. 设置通过socket发送指定长度数据。

   命令：

   .. code-block:: none

      AT+SOCKETSEND=1,237\r\n

   响应：

   .. code-block:: none

     OK

   说明：

   - 您的ID与要发送的字节长度不同。请以您实际的连接ID与长度为准。
   - 长度字节个数需要以CRLF格式为准
     
    .. figure:: ../../_static/tcp_ssl_https.png
      :scale: 80 %
      :alt: OTA


#. 出现">"后发送指定长度数据。

   命令：

   .. code-block:: none

    POST  /post  HTTP/1.1\r\nHost: httpbin.org\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 123\r\n\r\n{"key1": 123,"key2": 123,"key3": 123,"key4": 123,"key5": 123,"key6": 123","key7": 123,"key8": 123,"key9": 123,"key10": 123}   
   
   响应：

   .. code-block:: none

    {
    "args": {}, 
    "data": "", 
    "files": {}, 
    "form": {
    "{\"key1\": 123,\"key2\": 123,\"key3\": 123,\"key4\": 123,\"key5\": 123,\"key6\": 123\",\"key7\": 123,\"key8\": 123,\"key9\": 123,\"key10\": 123}": ""
    }, 
    "headers": {
    "Content-Length": "123", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "X-Amzn-Trace-Id": "Root=1-64e576bf-30fc9a971f2aace64ef99f95"
    }, 
    "json": null, 
    "origin": "120.234.24.230", 
    "url": "https://httpbin.org/post"
    }

    OK
    
  说明：

   - 您的请求字段不同。请以您实际请求字段为准。
   - MCU发送需要添加转义符
   