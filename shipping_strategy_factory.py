#---------------------------------------------------------------------------------------------------------------------#
#                                                                                                                     #
#                                                    Python Script                                                    #
#                                                                                                                     #
#---------------------------------------------------------------------------------------------------------------------#
#
# File        : shipping_strategy_factory.py
# Description : 用于创建shipping strategies
#
# History
# 2025-07-04  : Creation
'''shipping_strategy_factory'''
__author__ = 'Weihan Zu'

from shipping_strategy import (
    DebangShippingStrategy,
    JituShippingStrategy,
    YundaShippingStrategy,
    YouzhengShippingStrategy,
    KuaiyunShippingStrategy,
    ZhongtongShippingStrategy,  # 假设你已实现
)

class ShippingStrategyFactory:
    @staticmethod
    def get_strategy(delivery_type: str):
        if delivery_type == "德邦":
            return DebangShippingStrategy()
        elif delivery_type == "极兔":
            return JituShippingStrategy()
        elif delivery_type == "韵达":
            return YundaShippingStrategy()
        elif delivery_type == "邮政":
            return YouzhengShippingStrategy()
        elif delivery_type == "快运（顺心捷达/壹米滴答）":
            return KuaiyunShippingStrategy()
        elif delivery_type == "中通":
            return ZhongtongShippingStrategy()
        else:
            raise ValueError(f"未知快递类型: {delivery_type}")

#---------------------------------------------------------------------------------------------------------------------#
