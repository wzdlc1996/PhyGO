# 量化对冲

## 风险因子和风险分割

> 桥水麦乐鸡块对冲方案
> 客户为麦当劳, 进货鸡肉输出麦乐鸡获得利润. 
> 任务: 平衡掉鸡价的波动
> 方案: 注意到鸡肉来源于鸡苗, 饲料(玉米, 大豆). 通过购买期货来实现对冲.

系统性量化投资:
1.  风险分割: 资产回报分割为不同的风险因子
2.  风险估值: 对每个风险因子进行分析和估值
3.  资产组合: 组合资产事实上是风险因子的组合
4.  风险对冲: 对冲风险获得稳定收益

### beta 对冲

通过CAPM模型, 可以得到

$$
r_i = r_f  +\alpha + \beta (R_M - r_f) +\epsilon
$$

从而, 构造一个资产组合即线性组合 $r_i$ , 选择合适的系数矩阵来尽可能消除掉风险项 $\beta$ 

### 定价对冲

可转债套利

可转债: 债券持有人可以按照发行时约定的价格将债券转换为公司普通股票.

可拽债套利: 通过转债和相关联的基础股票之间定价的 **无效率性(定价偏差)** 进行的无风险获利行为. 可转债的套利交易不一定要在可转换期内进行(卖空机制和存在机会)

可转债定价: 债券价 + 期权价

套利技术: 一般公司债, 股票期权, 动态做空股票
风险分割: 利率, 信用利差, 股票, 波动率, 外汇. 定价偏差

## Beta 对冲: 量化对冲策略
