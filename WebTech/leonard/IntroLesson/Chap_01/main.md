# 概述

**计算机网络**: 多台自主计算机所组成的互联系统. 其目的是资源共享和信息交换.
-  用户必须制定系统中的哪个计算机来做什么样的操作. 
**自主**: 不从属于其他任何计算机的计算机, 被称为自主计算机
**互联**: 两台计算机能够交换信息称为两台计算机互联. 

资源共享解决了单机能力弱, 提高了利用率(联机挖矿). 
信息交换提供高等复杂的服务, 如邮件, 文件服务器, 网上即时交谈/课堂/会议等. 

## 相关概念

**主机系统**: 由主机和终端组成的系统. 主机负责计算, 多种外设终端进行交互. 
**分布式系统**: 基于自主计算机的互联, 由一个操作系统进行统一管理. 用户视角来看是一个多台计算机组成的一台虚拟计算机. 

## 网络的分类

1.  按介质分:
    -  有线网络: 双绞线, 同轴电缆, 光纤等
    -  无线网络: 无线电波, 微波(地面-卫星), 红外线, 激光
2.  按技术分:
    -  广播式网络: 采用一条公共信道
    -  点到点网络: 采用分组存储/转发和路由选择. 
3.  按使用范围分:
    -  专用网: 为本系统的特殊业务服务需要而建造的网络
       > 公安网. 最初是基于internet的, 但后来改建为与其平行
       > 军网. 设计之初就和internet平行, 近几年技术建设更好. 
    -  公共网: 一般是国家电信部门建造的网络
4.  按拓扑结构分:
    -  总线: 若干计算机连到同一条总线上, 同一时刻总线只供应两台计算机通信. 
       优点: 结构简单. 组网灵活方便, 成本低
       缺点: 传输距离有限, 故障检测困难, 站点必须有 *介质访问控制功能*.
    -  环型: 若干计算机结成环形 (线性环形链表). 
       优点: 成本低, 增减工作站只需要简单链接, 很早就可用光纤
       缺点: 信息流向固定, 节点故障会让全网故障.
    -  星型: 存在一个中心网络设备(hub, 交换机)
       优点: 结构简单 便于管理, 入网计算机出问题不影响网络(隔离). 
    -  树状: 网络设备作为内节点, 计算机作为叶节点组成树
       很少见到, 增减方便, 计算机和网络结构隔离, 可能军事单位可以看到
    -  网状: 计算机尽可能和其他链接, 成网状, 冗余性高.
       优点: 信息通道宽, 稳定
       缺点: 成本高, 复杂, 难维护

5.  按规模分:
    1.  个域网: personal area network(PAN)
        指个人范围内(数米范围)的计算设备组成的通信网络. 
        > 穿戴设备发展停滞导致个域网研究也相对停滞. 

        实例: 蓝牙, 红外, ISM无限 (工业, 科学, 医疗预留频段通信. 环境可能会有电磁干扰)
    2.  局域网: local area net(LAN)
        覆盖地域小, 传输速率高(目前典型速率 1000Mb/s~10Gb/s), 技术成熟, 应用广泛. 是计算机网络最流行的形式. (经济原因, 访问局部性原理)
        > 访问局部性（Locality of reference）指的是在计算机科学领域中应用程序在访问内存的时候，倾向于访问内存中较为靠近的值。 
        > 被分为时间/空间局部性. 空间-内存相邻地址更容易被访问到(所以适应该规律总访问临近内存可能性能更好), 时间-最近访问/调用过的地址更容易被再次访问/调用. (统计规律)

        技术: 总线型 IEEE802.3(以太网) CSMA/CD, IEEE802.11(wifi, 无线局域网) CSMA/CA
    3.  城域网: metropolitan area network
        介于广域/局域. 设计目标是满足几十公里范围的大量企业, 公司的多个局域网互联的需求. 比如几十个网店的大型连锁超市的内部网. 
        > 目前已经没有代表技术了. 过去曾有 FDDI, WiMAX. 现在可以使用局域网的扩展技术. 

        所用的典型设备: 网桥, 交换机, 光纤调制解调器.
    4.  广域网: wide area network
        跨越地域较大, 链接多个城市, 国家, 大洲. 
        基本构件: 分组交换机(packet switch), 使用存储/转发的方法. 通常可以使用公用网络系统(卫星网络, 公用电话网)等搭建. 
        技术实例: (国际电信联盟 ITU的 X.25. 帧中继(frame relay), 交换式多兆位数据服务(SMDS), ATM(asynchronous transfer mode))(这些已经没了). DWDM(dense wavelenth division multiplexing)

# 网络互联和互联网

1960年代, 大家开始研究 “分组交换” 技术. 
-  随着研究诞生了各种这样的技术与它们构成的网络
-  为了更好的实现(因为不同的分组交换网络是不能互联的), 人们又研究把这些网络统一起来的最优分组交换技术, 来试图让它们天生一致能够互联. 

1973年, Vinton Cerf 和 Robert Kahn观察到目前没有分组交换技术来满足所有需求. 他们建议停止寻找最优的, 取而代之探索能够把多个分组交换技术互联为一个整体的技术, 即 “网络互联”. 

他们提出了一组标准, 这个标准最终形成了 TCP/IP 协议族.

> 事实上就是为了给出网络地址的统一格式, 和网络数据包的统一格式. 

网络互联目前已经是现代组网技术的最重要思想之一. 把多个网络互联在一起, 就形成了 “互联网”. 
-  在逻辑上, 互联网可以被看成一个单一的, 无缝的通信系统
-  在物理上, 它是由多个路由器互连起来的多个网络的集合, 每个网络可以有自己的连接技术. 

**TCP/IP 的重要性**: 除了私有互联网外, 它还使得全球性的Internet成为可能. 根本上是对异构性(heterogeneity)的容忍. 具体的, 它使用了一种虚拟化方法, 定义了一种与底层网络无关的分组格式, 以及一种和底层网络无关的识别方案. 

## Internet 的起源和发展

1968年: 美国国防部高级研究计划局建立 ARPANET. 研究分组交换技术, 解决互通性/互操作性两大难题(目前互通性解决了, 互操作性反而会带来大量安全问题), 最初的 ARPANET 由四个节点组成.

70年代中期: 联网主机的范围跨越美国大陆, 扩展到夏威夷 日本和西欧

70年代后期: 放宽入网限制, 国模扩大

1983年: ARPANET分为两个独立部分, ARPANET(研究) 和 MILNET(军用)

80年代初: 美国NSF建立了 NSFNET, 使用 TCP/IP 协议, 并以 ARPANET 为主干建立了 Internet

80年代末90年代初: NSF 围绕六个超级计算机中心重新建立了 NSFNET, 具备三级结构: 主干网, 地区网, 校园网. 和ARPANET相连成了新的Internet, 并随之成为事实上的美国国家计算机网.

1993年: 美国政府资助的 NSFNET 逐渐被若干个商用的 ISP 网络代替

1994年: 建立了4个网络接入点 (Network access point, NAP), 分别由4个电信公司经营

1995年底: 已经联通154个国家和地区

> 一点题外话
> 不要只有论点, 没有论据
> 观点要有数据支持. 宏观, 微观, 不要以偏概全 (多数时候采样本身的bias就很强)
> 数据也会骗人: 即使使用完整的数据, 也能通过刻意的处理引导人得到想要的结论.

# 计算机网络参考模型

## 协议与分层

为了实现计算机网络不同主机, 不同操作系统之间的通信而规定的, 网络全体成员都必须共同遵守的一系列规则和约定, 被称为 **计算机网络协议(protocol)**

为了减少设计的复杂性, 用高度结构化的方法分层制定协议: “分而治之”. 每个功能层次负责简单的功能, 并向下一层提出服务请求, 完成上一层的服务请求.

## ISO/OSI 七层模型

1981年, 国际标准化组织(ISO)为计算机网络通信制定了一个七层协议的框架. 称为 (OSI/RM(open system interconnection/reference model)) 模型

从底层向上: 1-物理层, 2-数据链路层, 3-网络层, 4-传输层, 5-会话层, 6-表示层, 7-应用层.

> 1981年 TCP/IP 和计算机网络已经有所发展, ISO此举是为了摘桃子

1.  物理层: 是最底层的支持信息传输
2.  数据链路层: 给出帧的概念. 
3.  网络层: 为不同网络的两个节点之间的通信建立一条逻辑通道. 实现网络互联. 
4.  传输层: 提供可靠的端到端通信, 并向会话层屏蔽了下层数据通信的细节. 
5.  会话层: 提供会话服务, 并同步
6.  表示层: 关心语法和语义. 屏蔽不同系统在信息表示层面的差异. 包括语法转换, 加密, 压缩, 恢复等
7.  应用层: 支持用户各类联网应用的需求. 

每层中活动的元素称为实体. 对等实体是指发送方和接收方同层的实体. 每层都是为了上一层的需求服务的.

## TCP/IP 的分层

通常来说从下往上分为 1-物理层, 2-网络接口层(对应链路层), 3-互联层(对应网络层), 4-传输层(包含了传输和部分会话层功能), 5-应用层(对应会话, 表示, 应用层)

## Internet 体系结构

对于包含在体系结构中的新协议, 必须产生一个协议规范和至少一个(最好两个)典型实现, 并且这种实现能够工作

# World Wide Web

是基于 Internet 的目前最大的互联应用, 是一种超媒体网络. 

**自由和共享的矛盾**: **HTML**: 90年代左右诞生的旨在给网络应用传输信息提供一个统一的接口(标准). 它的低扩展性带来了 **XML**. 但它也没能很好地解决这个矛盾. 

> (来自授课老师18年前的论断) 大众平台上自由为主, Web上会出现越来越多的专业应用站点, 他们将遵守某种规范实现特定的功能. 

# 未来的展望

中国的互联网建设: 21世纪开端的初衷很好, 基础研究拖了后腿(造不如买?)

今后计算机网络会更多的影响我们的实际生活, 其覆盖的用户量也会越来越多. 

缺乏杀手级应用: ipv6, 5g
技术的发展必然伴随泡沫: 区块链(谨慎乐观), 大数据/AI(目前可开发的红利需要谨慎)

# 参考书

主参考书: 计算机网络与因特网(Douglas E Comer) www.netbook.cs.purdue.edu