# World Wide Web 技术

1989年由CERN的 Tim Berners-Lee 提出概念.

## 概述

### 超文本与超媒体

技术上讲, WWW是一个支持交互式访问的分布式超媒体系统. 

Web 文档使用 HTML 表示. HTML允许文档包含用于显示的通用向导行, 并允许浏览器选择细节. 
HTML文档包含head和body, 构成上, 它由标签和文本信息组成.

### 客户/服务器交互

浏览器通过 **url (uniform resource locator)** 获得网页资源. url包含三部分: 协议, 计算机名, 和文档名.

浏览器作为客户和服务器构建起双向交互. 通过逐级网关实现信息交互. 

## Web 页面和浏览

### HTTP协议

HTTP是浏览器用于和web服务器交互的主要传输协议. 默认使用端口80,  
-  使用文本控制报文
-  传送二进制数据文件
-  可以下载和上传文件

存在四种主要请求类型
1.  GET: 请求一个文档, 服务器响应: 发送状态信息, 发送所请求文档的一个副本
2.  HEAD: 请求状态信息, 服务器响应: 仅发送状态信息
3.  POST: 发送数据给服务器, 服务器响应: 将该数据添加到指定的项上
4.  PUT: 发送数据给服务器, 服务器响应: 使用该数据覆盖指定项

使用高速缓存: 浏览器通过用户硬盘保存网站图像的副本, 利用缓存以减少网络文件传输. 通过HEAD请求以对比本地时间和服务器更新时间用于更新本地缓存.

## HTML的扩展

HTML无法区分格式和内容. 

1.  XML. 已得到广泛支持, 能够描述网页内容结构
2.  XHMTML. 对HTMLv4去除格式化标记, 然后用XML重新格式化. XHTML5作为HTML5的一部分.

## 动态Web文档

根据确定文档内容的时间分类:
1.  静态: 存放于web server上的静态文件, 每次访问都返回相同结果
2.  动态: 在访问时创建, server通过一个app来产生web文档
3.  活动: 活动文档由一个能理解如何去计算和显示数值的程序构成. server分发程序的副本, 本地执行并产生web文档.

**CGI(common gateway interface)** 是创建动态文档的基本技术. 提供一般性指导, 大多数细节交给程序员.

几种服务器脚本技术: ASP, JSP, PHP, ColdFusion(嵌入sql)


