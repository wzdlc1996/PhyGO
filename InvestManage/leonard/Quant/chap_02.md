# 量化投资中的常用数据

## 行情数据

指金融市场中交易金融资产的价格信息. 通常包括: 时间, 成交量, 开盘价, 收盘价, 最高价, 最低价.

1.  指数行情

    能够反映市场整体的行情 (国内常关注宽基指数). 价格信息被展示在K线图上

1.  股票行情

    国内分主题的版面, 存在涨跌停板机制

1.  期货行情

    额外属性
    1.  `contract_multipler` 期货乘数: 每个点位的实际价格
    2.  `margin_rate` 保证金率: 购买一定价格的期货只需要 `margin_rate * price` 的保证金. 从而杠杆率事实上就是保证金率的倒数. 

    同股票行情的差异
    1.  期货合约是不连续的, 有到期日和交割日
    2.  同种产品的不同合约时间对应不同期货
    3.  主力合约: 交易最活跃的合约

1.  期权行情

    国内期权仍相对较少(2022), 主要包括上证50ETF期权, 沪深300ETF期权, 沪深300指数期权和一些其他商品期权. 

## 财务数据

《财务报表分析与股票估值》(郭永清)

1.  资产负债表: 公司资产结构
2.  利润表: 公司的盈利能力 (可能存在人为因素调整, 失真)
3.  现金流量表: 反应公司现金获取能力和资金流动情况 (比利润表更精确反映)

注意问题

1.  上市公司的季报, 年报发布不集中在报告日, 注意公布日期, 不要使用 “未来数据”
2.  正是财报发布之前, 可能会有业绩预告和业绩快报
3.  相对静态或单一的财务指标, 三张表之间的勾稽关系更能反映一个公司的真实财务状况和经营状况.