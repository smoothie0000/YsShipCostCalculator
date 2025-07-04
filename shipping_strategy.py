#---------------------------------------------------------------------------------------------------------------------#
#                                                                                                                     #
#                                                    Python Script                                                    #
#                                                                                                                     #
#---------------------------------------------------------------------------------------------------------------------#
#
# File        : shipping_strategy.py
# Description : 不同快递费用计算
#
# History
# 2025-07-04  : Creation
'''shipping_strategy'''
__author__ = 'Weihan Zu'

from abc import ABC, abstractmethod
import math

class ShippingStrategy(ABC):
    @abstractmethod
    def calculate(self, total_volume: float, province: str) -> float:
        pass

# 德邦
class DebangShippingStrategy(ShippingStrategy):
    def calculate(self, total_volume, province):
        first_3kg_cost = 0
        over_per_kg_cost = 0

        if province in ["江苏省", "浙江省", "上海市"]:
            first_3kg_cost = 7
            over_per_kg_cost = 1
        elif province in ["广东省", "安徽省", "山东省",  "北京市", "天津市", "河北省", "河南省", "湖北省", "湖南省", "江西省", "山西省", "福建省"]:
            first_3kg_cost = 8
            over_per_kg_cost = 2.5
        elif province in ["广西壮族自治区", "海南省", "云南省", "贵州省", "四川省", "重庆市", "黑龙江省", "吉林省", "辽宁省"]:
            first_3kg_cost = 9
            over_per_kg_cost = 3
        elif province in ["陕西省", "甘肃省", "宁夏回族自治区", "青海省", "内蒙古自治区"]:
            first_3kg_cost = 12
            over_per_kg_cost = 3
        else:
            raise Exception(f"不支持 {province} 省份")

        ship_cost = 1  # 保单费
        volume_weight = round(total_volume / 12000)
        if volume_weight <= 3:
            ship_cost += first_3kg_cost
        else:
            ship_cost += first_3kg_cost + over_per_kg_cost * (volume_weight - 3)

        return round(ship_cost, 1)

# 极兔
class JituShippingStrategy(ShippingStrategy):
    def calculate(self, total_volume, province):
        additional_cost = 0
        weight = total_volume / 8000

        if province in ["江苏省", "浙江省", "上海市", "安徽省"]:
            cost_table = [2.3, 2.8, 3.7, 5]
            over_per_kg = 1
            if province == "上海市":
                additional_cost = 1
        elif province in ["福建省", "广东省", "江西省", "山东省", "河南省", "河北省", "天津市", "北京市", "湖南省", "湖北省"]:
            cost_table = [2.3, 2.8, 3.7, 5]
            over_per_kg = 2
            if province == "北京市":
                additional_cost = 1
        elif province in ["黑龙江省", "吉林省", "辽宁省", "云南省", "重庆市", "广西壮族自治区", "贵州省", "四川省", "山西省", "陕西省"]:
            cost_table = [2.3, 2.8, 3.7, 5]
            over_per_kg = 3
        elif province in ["内蒙古自治区", "宁夏回族自治区", "青海省", "甘肃省", "海南省"]:
            cost_table = [3.5, 4, 8, 12]
            over_per_kg = 4
        else:
            raise Exception(f"不支持 {province} 省份")

        cost = additional_cost * weight

        if weight <= 0.5:
            cost += cost_table[0]
        elif weight <= 1:
            cost += cost_table[1]
        elif weight <= 2:
            cost += cost_table[2]
        elif weight <= 3:
            cost += cost_table[3]
        else:
            weight = math.ceil(weight)
            cost += cost_table[3] + over_per_kg * (weight - 3)

        return round(cost, 1)

# 韵达
class YundaShippingStrategy(ShippingStrategy):
    def calculate(self, total_volume, province):
        weight = total_volume / 8000

        if province in ["江苏省", "浙江省", "安徽省"]:
            cost_table = [2.5, 2.8, 3.6, 4.6]
            over_per_kg = 1
        elif province in ["河北省", "天津市", "河南省", "湖南省", "湖北省", "山东省", "广东省", "江西省", "福建省"]:
            cost_table = [2.5, 2.8, 3.6, 4.6]
            over_per_kg = 2
        elif province in ["山西省", "陕西省", "广西壮族自治区", "四川省", "重庆市", "贵州省", "云南省", "黑龙江省", "辽宁省", "吉林省"]:
            cost_table = [2.5, 2.8, 3.6, 4.6]
            over_per_kg = 2.8
        elif province in ["内蒙古自治区", "甘肃省", "青海省", "宁夏回族自治区", "海南省"]:
            cost_table = [3.5, 3.8, 4.8, 5.8]
            over_per_kg = 3.8
        elif province == "北京市":
            cost_table = [3, 3.8, 4.8, 5.8]
            over_per_kg = 3
        elif province == "上海市":
            cost_table = [3, 3.8, 4.8, 5.8]
            over_per_kg = 1.5
        else:
            raise Exception(f"不支持 {province} 省份")

        if weight <= 0.5:
            cost = cost_table[0]
        elif weight <= 1:
            cost = cost_table[1]
        elif weight <= 2:
            cost = cost_table[2]
        elif weight <= 3:
            cost = cost_table[3]
        else:
            cost = cost_table[3] + over_per_kg * (math.ceil(weight) - 3)

        return round(cost, 1)

# 中通
class ZhongtongShippingStrategy(ShippingStrategy):
    def calculate(self, total_volume, province):
        # 初始化参数
        additional_cost = 0
        calculate_with_volume = False
        price_per_square_meter = 0
        price_calculate_with_volume_fixed = 0
        cost_table = [0, 0, 0, 0]
        over_per_kg_cost = 0
        first_3kg_cost = 0

        if province in ["江苏省", "浙江省", "安徽省"]:
            cost_table = [2.3, 2.8, 3.5, 5]
            over_per_kg_cost = 1.5
            first_3kg_cost = 5
        elif province in ["河北省", "天津市", "河南省", "湖南省", "湖北省", "山东省", "广东省", "江西省", "福建省"]:
            cost_table = [2.3, 2.8, 3.5, 5]
            calculate_with_volume = True
            price_per_square_meter = 150
            price_calculate_with_volume_fixed = 5
        elif province in ["山西省", "陕西省", "广西壮族自治区", "四川省", "重庆市", "贵州省", "云南省", "黑龙江省", "辽宁省", "吉林省"]:
            cost_table = [2.3, 2.8, 3.5, 5]
            calculate_with_volume = True
            price_per_square_meter = 150
            price_calculate_with_volume_fixed = 5
        elif province in ["内蒙古自治区", "甘肃省", "青海省", "宁夏回族自治区", "海南省"]:
            cost_table = [3.5, 4, 5, 6]
            calculate_with_volume = True
            price_per_square_meter = 500
            price_calculate_with_volume_fixed = 0
        elif province == "北京市":
            cost_table = [3, 4, 5, 6.5]
            additional_cost = 1.5
            calculate_with_volume = True
            price_per_square_meter = 150
            price_calculate_with_volume_fixed = 5.5
        elif province == "上海市":
            cost_table = [3, 4, 5, 5.5]
            additional_cost = 0.5
            over_per_kg_cost = 1.5
            first_3kg_cost = 5.5
        else:
            raise Exception(f"不支持 {province} 省份")

        ship_cost = additional_cost
        volume_weight = total_volume / 10000

        if volume_weight <= 0.5:
            ship_cost += cost_table[0]
        elif volume_weight <= 1:
            ship_cost += cost_table[1]
        elif volume_weight <= 2:
            ship_cost += cost_table[2]
        elif volume_weight <= 3:
            ship_cost += cost_table[3]
        elif volume_weight > 3 and calculate_with_volume:
            # 特殊体积计费
            ship_cost += price_calculate_with_volume_fixed + price_per_square_meter * math.ceil(volume_weight) / 100
        else:
            # 普通超重计费
            ship_cost += first_3kg_cost + over_per_kg_cost * (math.ceil(volume_weight) - 3)

        return round(ship_cost, 1)

# 邮政
class YouzhengShippingStrategy(ShippingStrategy):
    def calculate(self, total_volume, province):
        if province in ["上海市", "浙江省", "江苏省"]:
            first_kg_cost = 4
            over_per_kg_cost = 1
        elif province == "安徽省":
            first_kg_cost = 4
            over_per_kg_cost = 1.2
        elif province in ["北京市", "天津市", "河北省", "山西省", "山东省", "福建省", "江西省", "河南省", "湖北省", "湖南省", "广东省"]:
            first_kg_cost = 5
            over_per_kg_cost = 1.7
        elif province in ["广西壮族自治区", "陕西省", "重庆市", "贵州省"]:
            first_kg_cost = 5.5
            over_per_kg_cost = 1.7
        elif province in ["辽宁省", "海南省", "宁夏回族自治区", "四川省", "甘肃省", "内蒙古自治区", "吉林省"]:
            first_kg_cost = 6
            over_per_kg_cost = 1.7
        elif province in ["黑龙江省", "云南省"]:
            first_kg_cost = 6
            over_per_kg_cost = 2.6
        elif province == "青海省":
            first_kg_cost = 12
            over_per_kg_cost = 10
        else:
            raise Exception(f"不支持 {province} 省份")

        volume_weight = math.ceil(total_volume / 12000)
        if volume_weight <= 1:
            return first_kg_cost
        else:
            return round(first_kg_cost + over_per_kg_cost * (volume_weight - 1), 1)

# 快运
class KuaiyunShippingStrategy(ShippingStrategy):
    def calculate(self, total_volume, province):
        price_list = {
            "浙江省": [90, 25], "安徽省": [100, 30], "江苏省": [90, 25], "上海市": [100, 25],
            "福建省": [150, 35], "广东省": [150, 35], "江西省": [150, 35], "山东省": [150, 35],
            "北京市": [210, 50], "天津市": [160, 40], "河北省": [150, 45], "河南省": [150, 35],
            "湖北省": [150, 40], "湖南省": [150, 40], "重庆市": [240, 35], "四川省": [240, 50],
            "贵州省": [258, 40], "山西省": [210, 35], "陕西省": [210, 35], "广西壮族自治区": [218, 40],
            "辽宁省": [228, 40], "云南省": [258, 40], "黑龙江省": [228, 40], "吉林省": [228, 35],
            "甘肃省": [330, 50], "宁夏回族自治区": [330, 50], "海南省": [320, 50], "青海省": [330, 50],
            "内蒙古自治区": [330, 50], "西藏自治区": [-1, -1],
        }

        if province not in price_list or price_list[province][0] == -1:
            raise Exception(f"{province} 不支持快运发货")

        per_cube_meter_cost, start_cost = price_list[province]
        volume_m3 = total_volume / 1000000
        cost = per_cube_meter_cost * volume_m3
        if cost < start_cost:
            return round(start_cost, 1)
        return round(cost, 1)

#---------------------------------------------------------------------------------------------------------------------#
