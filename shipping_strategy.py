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
from decimal import Decimal, ROUND_HALF_UP

class ShippingStrategy(ABC):
    def __init__(self):
        super().__init__()
        self.notice_text = "无注意事项"

    @abstractmethod
    def calculate(self, total_volume: float, total_length: float, province: str) -> float:
        pass

# 德邦
class DebangShippingStrategy(ShippingStrategy):
    def __init__(self):
        super().__init__()
        self.notice_text = "单票实际重量不能超过50kg，超过打子母单"

    def calculate(self, total_volume, total_length, province):
        self.notice_text = "单票实际重量不能超过50kg，超过打子母单"
        first_3kg_cost = 0
        over_per_kg_cost = 0

        if province in ["江苏省", "浙江省", "上海市"]:
            first_3kg_cost = 9
            over_per_kg_cost = 1
        elif province in ["广东省", "安徽省", "山东省",  "北京市", "天津市", "河北省", "河南省", "湖北省", "湖南省", "江西省", "山西省", "福建省"]:
            first_3kg_cost = 11
            over_per_kg_cost = 1.8
        elif province in ["广西壮族自治区", "海南省", "贵州省", "四川省", "重庆市", "黑龙江省", "吉林省", "辽宁省", "陕西省", ]:
            first_3kg_cost = 11
            over_per_kg_cost = 2.6
        elif province in ["甘肃省", "宁夏回族自治区", "青海省", "内蒙古自治区"]:
            first_3kg_cost = 13
            over_per_kg_cost = 3
        elif province in ["西藏自治区", "新疆维吾尔自治区"]:
            first_3kg_cost = 29
            over_per_kg_cost = 12
        elif province in ["云南省"]:
            first_3kg_cost = 12
            over_per_kg_cost = 3
        else:
            raise Exception(f"不支持 {province} 省份")

        ship_cost = 0
        volume_weight = round(total_volume / 12000, 1)
        if volume_weight <= 3:
            ship_cost += first_3kg_cost
        else:
            ship_cost += first_3kg_cost + over_per_kg_cost * (volume_weight - 3)
        
        if total_length > 250:
            ship_cost += 20
            self.notice_text = self.notice_text + "\n由于产品三边尺寸之和超过250cm\n额外增加20元运费"

        return round(ship_cost, 1)

# 极兔
class JituShippingStrategy(ShippingStrategy):
    def calculate(self, total_volume, total_length, province):
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
            cost += cost_table[3] + over_per_kg * (math.ceil(weight) - 3)

        return round(cost, 1)

# 韵达 (洪家)
class YundaShippingStrategy(ShippingStrategy):
    def calculate(self, total_volume, total_length, province):
        weight = total_volume / 8000

        if province in ["江苏省", "浙江省", "安徽省"]:
            cost_table = [2.3, 2.7, 3.7, 4.7]
            over_per_kg = 0.9
        elif province in ["河北省", "天津市", "河南省", "湖南省", "湖北省", "山东省", "广东省", "江西省", "福建省"]:
            cost_table = [2.3, 2.7, 3.7, 4.7]
            over_per_kg = 1.8
        elif province in ["山西省", "陕西省", "广西壮族自治区", "四川省", "重庆市", "贵州省", "云南省", "黑龙江省", "辽宁省", "吉林省"]:
            cost_table = [2.3, 2.7, 3.7, 4.7]
            over_per_kg = 2.2
        elif province in ["内蒙古自治区", "甘肃省", "青海省", "宁夏回族自治区", "海南省"]:
            cost_table = [3.7, 3.8, 5.2, 6.2]
            over_per_kg = 3.2
        elif province == "北京市":
            cost_table = [3.5, 4, 5, 6]
            over_per_kg = 3.1
        elif province == "上海市":
            cost_table = [3.5, 4, 5, 6]
            over_per_kg = 1.6
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
            first_kg_cost = 4
            cost = first_kg_cost + over_per_kg * (weight - 1)

        return round(cost, 1)

# 中通
class ZhongtongShippingStrategy(ShippingStrategy):
    def calculate(self, total_volume, total_length, province):
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

""" # 邮政-电商标快洪家
class YouzhengDianShangShippingStrategy(ShippingStrategy):
    def __init__(self):
        super().__init__()
        self.notice_text = "三边不超过100cm，按照实际重量计算，限制20kg内, 单边不超过100cm，三边不超2.5米，实际重量不超20kg"

    def calculate(self, total_volume, total_length, province):
        if province in ["上海市", "浙江省", "江苏省"]:
            first_kg_cost = 4
            over_per_kg_cost = 1
        elif province in ["安徽省"]:
            first_kg_cost = 4
            over_per_kg_cost = 1.2
        elif province in ["北京市", "天津市", "河北省", "山西省", "山东省", "福建省", "江西省", "河南省", "湖北省", "湖南省", "广东省"]:
            first_kg_cost = 5
            over_per_kg_cost = 2
        elif province in ["辽宁省", "海南省", "四川省", "陕西省", "重庆市", "广西壮族自治区"]:
            first_kg_cost = 6
            over_per_kg_cost = 3
        elif province in ["贵州省", "宁夏回族自治区", "甘肃省", "内蒙古自治区", "吉林省"]:
            first_kg_cost = 7
            over_per_kg_cost = 3
        elif province in ["黑龙江省", "云南省"]:
            first_kg_cost = 8
            over_per_kg_cost = 4
        elif province in ["青海省"]:
            first_kg_cost = 16
            over_per_kg_cost = 18
        elif province in ["西藏自治区", "新疆维吾尔自治区"]:
            first_kg_cost = 18
            over_per_kg_cost = 21
        else:
            raise Exception(f"不支持 {province} 省份")

        volume_weight = math.ceil(total_volume / 12000)
        if volume_weight <= 1:
            return first_kg_cost
        else:
            return round(first_kg_cost + over_per_kg_cost * (volume_weight - 1), 1)
"""

# 邮政-电商标快洪家
class YouzhengDianShangShippingStrategy(ShippingStrategy):
    def __init__(self):
        super().__init__()
        self.notice_text = "三边不超过100cm，按照实际重量计算\n限制20kg内, 单边不超过100cm\n三边不超2.5米，实际重量不超20kg"

    def calculate(self, total_volume, total_length, province):
        if province in ["上海市", "江苏省"]:
            first_kg_cost = 4
            over_500g_cost = 0.5
        elif province in ["安徽省"]:
            first_kg_cost = 4
            over_500g_cost = 0.6
        elif province in ["北京市"]:
            first_kg_cost = 4
            over_500g_cost = 1
        elif province in ["天津市", "河北省", "山西省", "福建省", "江西省", "山东省", "河南省", "湖北省", "湖南省", "广东省"]:
            first_kg_cost = 5
            over_500g_cost = 1
        elif province in ["陕西省"]:
            first_kg_cost = 4
            over_500g_cost = 1.5
        elif province in ["云南省"]:
            first_kg_cost = 4
            over_500g_cost = 2
        elif province in ["甘肃省", "宁夏回族自治区"]:
            first_kg_cost = 4
            over_500g_cost = 1.5
        elif province in ["辽宁省", "广西壮族自治区", "海南省", "重庆市", "四川省", "贵州省"]:
            first_kg_cost = 6
            over_500g_cost = 1.5
        elif province in ["内蒙古自治区", "吉林省"]:
            first_kg_cost = 7
            over_500g_cost = 1.5
        elif province in ["青海省"]:
            first_kg_cost = 16
            over_500g_cost = 9
        elif province in ["黑龙江省"]:
            first_kg_cost = 8
            over_500g_cost = 2
        elif province in ["新疆维吾尔自治区"]:
            first_kg_cost = 18
            over_500g_cost = 10.5
        elif province in ["西藏自治区"]:
            first_kg_cost = 18
            over_500g_cost = 10.5
        elif province in ["浙江省"]:
            first_kg_cost = 4
            over_500g_cost = 0.5
        else:
            raise Exception(f"不支持 {province} 省份")

        volume_weight = math.ceil(total_volume / 12000)
        if volume_weight <= 1:
            return first_kg_cost
        else:
            return round(first_kg_cost + over_500g_cost * math.ceil((volume_weight - 1) * 2), 1)

# 邮政-EMS洪家
class YouzhengEmsShippingStrategy(ShippingStrategy):
    def __init__(self):
        super().__init__()
        self.notice_text = "单边不超过60cm的按照实际重量, 超过的按照计抛算法\n且单边不超150CM，不超40KG"

    def calculate(self, total_volume, total_length, province):
        if province in ["上海市", "浙江省", "江苏省", "安徽省"]:
            first_kg_cost = 5
            over_per_kg_cost = 1
        elif province in ["福建省", "江西省", "山东省", "河南省", "湖北省", "湖南省", "天津市", "河北省", "山西省", "广东省"]:
            first_kg_cost = 6.5
            over_per_kg_cost = 1.7
        elif province in ["北京市", "海南省", "陕西省", "重庆市"]:
            first_kg_cost = 6.5
            over_per_kg_cost = 2
        elif province in ["四川省", "辽宁省", "广西壮族自治区", "贵州省"]:
            first_kg_cost = 7
            over_per_kg_cost = 3
        elif province in ["宁夏回族自治区", "甘肃省", "内蒙古自治区", "吉林省"]:
            first_kg_cost = 8
            over_per_kg_cost = 4
        elif province in ["黑龙江省", "云南省"]:
            first_kg_cost = 10
            over_per_kg_cost = 4
        elif province in ["西藏自治区", "新疆维吾尔自治区", "青海省"]:
            first_kg_cost = 18
            over_per_kg_cost = 21
        else:
            raise Exception(f"不支持 {province} 省份")

        volume_weight = math.ceil(total_volume / 6000)
        if volume_weight <= 1:
            return first_kg_cost
        else:
            return round(first_kg_cost + over_per_kg_cost * (volume_weight - 1), 1)

# 邮政-小包
class YouzhengXiaoBaoShippingStrategy(ShippingStrategy):
    def __init__(self):
        super().__init__()
        self.notice_text = "三边之和不超过94cm，实重"

    def calculate(self, total_volume, total_length, province):
        weight = total_volume / 12000
        if total_length > 94:
            return "三边之和超过90cm，不考虑邮政-小包"
        if weight > 3:
            return "超过3kg，不考虑邮政-小包"

        if province in ["浙江省", "江苏省", "安徽省"]:
            cost_table = [1.7, 2.2, 3.3, 4.3]
            over_per_kg = 1
        elif province == "上海市":
            cost_table = [1.7, 2.2, 3.3, 4.3]
            over_per_kg = 1
        elif province in ["湖南省", "河南省", "山东省", "湖北省", "江西省", "福建省", "广东省"]:
            cost_table = [1.7, 2.2, 3.3, 4.3]
            over_per_kg = 1
        elif province in ["天津市", "河北省", "山西省", "陕西省"]:
            cost_table = [2, 2.5, 3.8, 4.8]
            over_per_kg = 1
        elif province in ["广西壮族自治区", "海南省", "辽宁省"]:
            cost_table = [2, 2.5, 3.8, 4.8]
            over_per_kg = 1
        elif province in ["四川省", "重庆市", "贵州省"]:
            cost_table = [2.5, 2.8, 3.8, 4.8]
            over_per_kg = 1
        elif province in ["宁夏回族自治区", "甘肃省", "内蒙古自治区", "云南省", "黑龙江省", "吉林省"]:
            cost_table = [3.6, 4.2, 5.2, 6.2]
            over_per_kg = 1
        elif province == "北京市":
            cost_table = [8, 10, 13, 16]
            over_per_kg = 1
        elif province in ["青海省", "新疆维吾尔自治区", "西藏自治区"]:
            cost_table = [12, 16, 28, 40]
            over_per_kg = 1
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
            first_3kg_cost = 4
            cost = first_3kg_cost + over_per_kg * (math.ceil(weight) - 3)

        return round(cost, 1)

# 顺丰
class ShunFengShippingStrategy(ShippingStrategy):
    def __init__(self):
        super().__init__()
        self.notice_text = "高峰附加服务费：国庆节2025年10月1日-10月7日，\n双十一2025年10月21日-10月25日，11.1-11.5,11.11-11.15加1元/票，\n春节前2026年02月2号-02月15号，加1元/票，\n春节：2026年02月16号-02月24号，加3元/票"

    def round_half_up(self, value, ndigits=1):
        return float(Decimal(str(value)).quantize(Decimal('0.' + '0'* (ndigits-1) + '1'), rounding=ROUND_HALF_UP))

    def calculate(self, total_volume, total_length, province):
        if province in ["浙江省"]:
            first_kg_cost = 4.301
            over_1kg_per_kg_cost = 1.3
            first_3kg_cost = 8.001
            over_3kg_per_3kg_cost = 1.8
        elif province in ["上海市","福建省", "江苏省", "安徽省", "湖北省", "江西省"]:
            first_kg_cost = 4.301
            over_1kg_per_kg_cost = 1.3
            first_3kg_cost = 8.001
            over_3kg_per_3kg_cost = 1.8
        elif province in ["甘肃省", "广西壮族自治区", "贵州省", "海南省", "辽宁省", "宁夏回族自治区", "陕西省", "山西省", "四川省", "重庆市", "内蒙古自治区", "山东省", "天津市", "北京市", "河南省", "湖南省", "河北省", "广东省"]:
            first_kg_cost = 4.801
            over_1kg_per_kg_cost = 1.8
            first_3kg_cost = 10.001
            over_3kg_per_3kg_cost = 2.8
        elif province in ["黑龙江省", "云南省", "吉林省", "青海省"]:
            first_kg_cost = 5.001
            over_1kg_per_kg_cost = 2.5
            first_3kg_cost = 10.001
            over_3kg_per_3kg_cost = 2.8
        elif province in ["新疆维吾尔自治区"]:
            first_kg_cost = 17.001
            over_1kg_per_kg_cost = 10
            first_3kg_cost = 37.001
            over_3kg_per_3kg_cost = 10
        else:
            raise Exception(f"不支持 {province} 省份")

        print(total_volume)
        volume_weight = self.round_half_up(total_volume / 12000)
        print(volume_weight)
        if volume_weight < 3:
            cost = first_kg_cost + over_1kg_per_kg_cost * (volume_weight - 1)
        else:
            cost = first_3kg_cost + over_3kg_per_3kg_cost * (volume_weight - 3)
        
        return round(cost, 1)

# 快运-顺心捷达
class KuaiyunShunXinShippingStrategy(ShippingStrategy):
    def calculate(self, total_volume, total_length, province):
        price_list = {
            "浙江省": [90, 25], "安徽省": [100, 30], "江苏省": [90, 25], "上海市": [100, 25],
            "福建省": [150, 35], "广东省": [150, 35], "江西省": [150, 35], "山东省": [150, 35],
            "北京市": [210, 50], "天津市": [160, 40], "河北省": [150, 45], "河南省": [150, 35],
            "湖北省": [150, 40], "湖南省": [150, 40], "重庆市": [240, 35], "四川省": [240, 50],
            "贵州省": [258, 40], "山西省": [210, 35], "陕西省": [210, 35], "广西壮族自治区": [218, 40],
            "辽宁省": [228, 40], "云南省": [258, 40], "黑龙江省": [228, 40], "吉林省": [228, 35],
            "甘肃省": [330, 50], "宁夏回族自治区": [330, 50], "海南省": [320, 50], "青海省": [330, 50],
            "内蒙古自治区": [330, 50], "新疆维吾尔自治区": [550, 100], "西藏自治区": [680, 100],
        }

        if province not in price_list or price_list[province][0] == -1:
            raise Exception(f"{province} 不支持快运发货")

        per_cube_meter_cost, start_cost = price_list[province]
        volume_m3 = total_volume / 1000000
        cost = per_cube_meter_cost * volume_m3
        if cost < start_cost:
            return round(start_cost, 1)
        return round(cost, 1)

# 快运-壹米滴答
class KuaiyunYiMiShippingStrategy(ShippingStrategy):
    def calculate(self, total_volume, total_length, province):
        price_list = {
            "浙江省": [90, 25], "安徽省": [100, 30], "江苏省": [90, 25], "上海市": [100, 25],
            "福建省": [145, 35], "广东省": [145, 35], "江西省": [145, 35], "山东省": [145, 35],
            "北京市": [210, 50], "天津市": [155, 40], "河北省": [145, 40], "河南省": [145, 35],
            "湖北省": [145, 40], "湖南省": [145, 40], "重庆市": [235, 35], "四川省": [235, 40],
            "贵州省": [253, 40], "山西省": [205, 35], "陕西省": [210, 35], "广西壮族自治区": [213, 40],
            "辽宁省": [223, 40], "云南省": [253, 40], "黑龙江省": [228, 40], "吉林省": [223, 35],
            "甘肃省": [380, 50], "宁夏回族自治区": [380, 50], "海南省": [500, 50], "青海省": [480, 50],
            "内蒙古自治区": [380, 50], "新疆维吾尔自治区": [680, 100], "西藏自治区": [680, 100],
        }

        if province not in price_list or price_list[province][0] == -1:
            raise Exception(f"{province} 不支持快运发货")

        per_cube_meter_cost, start_cost = price_list[province]
        volume_m3 = total_volume / 1000000
        cost = per_cube_meter_cost * volume_m3
        if cost < start_cost:
            return round(start_cost, 1)
        return round(cost, 1)

# 快运-韵达快运
class KuaiyunYunDaShippingStrategy(ShippingStrategy):
    def calculate(self, total_volume, total_length, province):
        price_list = {
            "浙江省": [85, 25], "安徽省": [105, 30], "江苏省": [90, 25], "上海市": [100, 30],
            "福建省": [140, 35], "广东省": [140, 35], "江西省": [140, 35], "山东省": [140, 35],
            "北京市": [210, 40], "天津市": [140, 35], "河北省": [140, 35], "河南省": [140, 35],
            "湖北省": [140, 35], "湖南省": [140, 35], "重庆市": [210, 40], "四川省": [210, 40],
            "贵州省": [210, 40], "山西省": [210, 40], "陕西省": [210, 40], "广西壮族自治区": [210, 40],
            "辽宁省": [260, 55], "云南省": [260, 55], "黑龙江省": [260, 55], "吉林省": [260, 55],
            "甘肃省": [400, 100], "宁夏回族自治区": [400, 100], "海南省": [400, 100], "青海省": [400, 100],
            "内蒙古自治区": [400, 120], "新疆维吾尔自治区": [800, 150], "西藏自治区": [680, 100],
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
