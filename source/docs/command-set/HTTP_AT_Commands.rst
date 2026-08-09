HTTP AT 命令集
==================================================

本章节介绍HTTP指令集，此指令集针对不同的模组会有所不同的适配，具体差异请移步：:doc:`../instruction/other/firmware_differences`。

 - :ref:`AT+HTTPCLIENTLIN <cmd-HTTPCLIENTLIN>`：发送 HTTP/HTTPS 请求(单行模式)
 - :ref:`AT+HTTPRAW <cmd-HTTPRAW>`：发送 HTTP/HTTPS 长文本POST请求

.. _cmd-HTTPCLIENTLIN:

AT+HTTPCLIENTLIN：发送 HTTP 客户端请求
------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+HTTPCLIENTLINE=<transport_type>,<opt>,<content-type>,<host>,<port>,<path>[,<data>]

**响应：**

::

    Response length:<len> //response body 数据长度
    <response> //获取的响应数据
    OK

参数
^^^^

-  **<transport_type>**：请求协议。
     -  1：HTTP
     -  2：HTTPS
-  **<opt>**：请求类型。
     -  2：GET
     -  3：POST
-  **<content-type>**：请求数据类型。(仅 POST 生效，GET 时不生效，可以填写任意字符串，参考类型如下)
     -  application/x-www-form-urlencoded
     -  application/json
     -  multipart/form-data
     -  text/xml
     -  text/html
-  **<host>**：服务器域名或 IP。
     - eg:www.baidu.com 或者 192.168.1.100。
-  **<port>**：端口号。
     - HTTP 缺省值 80，HTTPS 缺省值 443。
-  **<path>**: HTTP(S)路径。
    -  缺省值"/"
-  **<data>**: 请求携带的数据。
    -  1：当opt为GET时这个是 携 带 在 patch 中 的 ， 格 式 符 合 http 格 式 要 求(?key1=value1&key2=value2 ...)
    -  2：当opt为POST时这个是 POST 携带的主体。

说明
^^^^

- 发起一次 HTTP 请求。


示例
^^^^

::

    //GET请求
    AT+HTTTPCLIENTLINE=1,2,"application/x-www-form-urlencoded","httpbin.org",80,"/get?key1=123&key2=456"

    //POST请求
    AT+HTTTPCLIENTLINE=1,3,"application/json","httpbin.org",80,"/post",{"key1": 123}


.. _cmd-HTTPRAW:

AT+HTTPRAW：发送 HTTP 客户端POST（带长文本）请求
--------------------------------------------------------------------------------

执行命令
^^^^^^^^

**命令：**

::

    AT+HTTPRAW=<transport_type>,<opt>,<content-type>,<host>,<port>,<path>,len

**响应：**

::
    >  //收到这个字符之后开始输入要发送的数据

    OK //当收到对应字节数据后就会发送数据(可以是任意数据)，发送完成会显示 OK


参数
^^^^

-  **<transport_type>**：请求协议。
     -  1：HTTP
     -  2：HTTPS
-  **<opt>**：请求类型。
     -  3：POST
-  **<content-type>**：请求数据类型。(仅 POST 生效，GET 时不生效，可以填写任意字符串，参考类型如下)
     -  application/x-www-form-urlencoded
     -  application/json
     -  multipart/form-data
     -  text/xml
     -  text/html
-  **<host>**：服务器域名或 IP。
     - eg:www.baidu.com 或者 192.168.1.100。
-  **<port>**：端口号。
     - HTTP 缺省值 80，HTTPS 缺省值 443。
-  **<path>**: HTTP(S)路径。
    -  缺省值"/"
-  **<len>**: 请求携带的数据。
    -  请求数据长度


说明
^^^^

- 发起一次 HTTP 请求。


示例
^^^^

::

    AT+HTTPRAW=1,3,"application/json","httpbin.org",80,"/post",13

    >{"key1": 123}
