HTTP AT 示例
==========================

本文档主要提供在模组设备上运行 :doc:`../command-set/HTTP_AT_Commands` 命令的详细示例。

.. contents::
   :local:
   :depth: 1

.. Important::
  - 文档中所描述的例子均基于设备已连接 Wi-Fi 的前提。
  - 当前仅支持部分 HTTP 客户端的功能。
  - 此示例针对不同的模组会有所不同的适配，具体差异请移步查询您手上的模组指令支持情况：:doc:`../instruction/other/firmware_differences`。


HTTP 客户端 GET 请求方法
---------------------------------------------------
本例以向 http://httpbin.org/get 发起get请求为例：
transport_type设置为1，opt设置为2，在get请求中content-type不生效可以填写任意字符，域名为httpbin.org，http默认端口为80，资源路径为/get。

   命令：

   .. code-block:: none

     AT+HTTPCLIENTLINE=1,2,application/x-www-form-urlencoded,httpbin.org,80,/get

   响应：

   .. code-block:: none

      {
        "args": {}, 
        "headers": {
          "Host": "httpbin.org", 
          "X-Amzn-Trace-Id": "Root=1-63c20ccc-0f33c8bf4bae7a8d3bb44270"
        }, 
        "origin": "120.234.24.230", 
        "url": "http://httpbin.org/get"
      }

      OK

   说明：

   - 您获取到的结果可能与上述响应中的不同。      


HTTP 客户端 POST 请求方法
-------------------------------------------------------------------------------------

本示例以 http://httpbin.org 作为 HTTP 服务器，transport_type设置为1，opt设置为3，数据类型为application/json，域名为httpbin.org，http默认端口为80，资源路径为/post。

   命令：

   .. code-block:: none

    AT+HTTPCLIENTLINE=1,3,application/json,httpbin.org,80,/post,"{\"form\":{\"purpose\":\"test\"}}"

   响应：

   .. code-block:: none

      {
        "args": {}, 
        "data": "{\"form\":{\"purpose\":\"test\"}}", 
        "files": {}, 
        "form": {}, 
        "headers": {
          "Content-Length": "27", 
          "Content-Type": "application/json", 
          "Host": "httpbin.org", 
          "X-Amzn-Trace-Id": "Root=1-63c2118c-552ac5547eedb78e37959f59"
        }, 
        "json": {
          "form": {
            "purpose": "test"
          }
        }, 
        "origin": "120.234.24.230", 
        "url": "http://httpbin.org/post"
      }

      OK

   说明：

   - 您获取到的结果可能与上述响应中的不同。  


HTTPS 客户端 POST（长文本）请求方法
-------------------------------------------------------------------------------------

本示例以 https://httpbin.org 作为 HTTP 服务器，transport_type设置为2，opt设置为3，数据类型为application/json，域名为httpbin.org，https默认端口为443，资源路径为/post。

   命令：

   .. code-block:: none

     AT+HTTPRAW=2,3,"application/x-www-form-urlencoded","httpbin.org",443,"/post",123

     >{"key1": 123,"key2": 123,"key3": 123,"key4": 123,"key5": 123,"key6": 123","key7": 123,"key8": 123,"key9": 123,"key10": 123}


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
      "Content-Length": "125", 
      "Content-Type": "application/x-www-form-urlencoded", 
      "Host": "httpbin.org", 
      "X-Amzn-Trace-Id": "Root=1-64e56a61-147868f33dfa052e237b81b6"
      }, 
      "json": null, 
      "origin": "120.234.24.230", 
      "url": "https://httpbin.org/post"
      }

     OK

   说明：

   - 您获取到的结果可能与上述响应中的不同。  
