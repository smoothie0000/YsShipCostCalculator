#---------------------------------------------------------------------------------------------------------------------#
#                                                                                                                     #
#                                                    Python Script                                                    #
#                                                                                                                     #
#---------------------------------------------------------------------------------------------------------------------#
#
# File        : volume_strategy.py
# Description : 计算不同规格产品的尺寸大小
#
# History
# 2025-07-04  : Creation
'''volume_strategy'''
__author__ = 'Weihan Zu'

from abc import ABC, abstractmethod
import math

class VolumeCalcStrategy(ABC):
    @abstractmethod
    def calculate(self, count: float, length: float, width: float, height: float) -> tuple:
        """
        Return tuple: (total_volume, total_length, total_width, total_height)
        """
        pass

# 网格川字
class WangGeChuanZiStrategy(VolumeCalcStrategy):
    def calculate(self, count, length, width, height):
        reminder = count % 2
        divide = math.floor(count / 2)

        if count == 1:
            total_length = length
            total_width = width
            total_height = height
        elif reminder == 0:
            total_length = length
            total_width = width + 18
            total_height = divide * (height + 4)
        else:
            total_length = length
            total_width = width + 18
            total_height = divide * (height + 4) + height

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

# 网格九脚
class WangGeJiuJiaoStrategy(VolumeCalcStrategy):
    def calculate(self, count, length, width, height):
        if count == 1:
            total_length = length
            total_width = width
            total_height = height
        else:
            total_length = length
            total_width = width
            total_height = 5 * (count - 1) + 14

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

# 平板四脚/平板六脚
class PingBanSiLiuJiaoStrategy(VolumeCalcStrategy):
    def calculate(self, count, length, width, height):
        reminder = count % 2
        divide = math.floor(count / 2)

        if count == 1:
            total_length = length
            total_width = width
            total_height = height
        elif reminder == 0:
            total_length = length
            total_width = width + 13
            total_height = divide * (height + 3)
        else:
            total_length = length
            total_width = width + 13
            total_height = divide * (height + 3) + height

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

# 平板九脚
class PingBanJiuJiaoStrategy(VolumeCalcStrategy):
    def calculate(self, count, length, width, height):
        reminder = count % 2
        divide = math.floor(count / 2)

        if count == 1:
            total_length = length
            total_width = width
            total_height = height
        elif reminder == 0:
            total_length = length
            total_width = width + 18
            total_height = divide * (height + 3)
        else:
            total_length = length
            total_width = width + 18
            total_height = divide * (height + 3) + height

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

# 圆孔垫板
class YuanKongDianBanStrategy(VolumeCalcStrategy):
    def calculate(self, count, length, width, height):
        total_length = length
        total_width = width
        total_height = count * height

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

# 防渗漏托盘
class FangShenLou3333Strategy(VolumeCalcStrategy):
    def calculate(self, count, length = 0, width = 0, height = 0):
        total_length = 33
        total_width = 33
        total_height = 6 + (count - 1) * 4

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

class FangShenLou4545Strategy(VolumeCalcStrategy):
    def calculate(self, count, length = 0, width = 0, height = 0):
        total_length = 45
        total_width = 45
        total_height = 10 + (count - 1) * 8

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

class FangShenLou6636Strategy(VolumeCalcStrategy):
    def calculate(self, count, length = 0, width = 0, height = 0):
        total_length = 66
        total_width = 36
        total_height = 12 + (count - 1) * 10

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

class FangShenLou5060Strategy(VolumeCalcStrategy):
    def calculate(self, count, length = 0, width = 0, height = 0):
        total_length = 60
        total_width = 60
        total_height = 15 + (count - 1) * 6

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

class FangShenLou6767Strategy(VolumeCalcStrategy):
    def calculate(self, count, length = 0, width = 0, height = 0):
        total_length = 67
        total_width = 67
        total_height = 15 + (count - 1) * 10

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

class FangShenLou8242Strategy(VolumeCalcStrategy):
    def calculate(self, count, length = 0, width = 0, height = 0):
        total_length = 82
        total_width = 42
        total_height = 15 + (count - 1) * 8

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

class FangShenLou1206_10Strategy(VolumeCalcStrategy):
    def calculate(self, count, length = 0, width = 0, height = 0):
        total_length = 120
        total_width = 60
        total_height = 10 + (count - 1) * 7

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

class FangShenLou1206_17Strategy(VolumeCalcStrategy):
    def calculate(self, count, length = 0, width = 0, height = 0):
        total_length = 120
        total_width = 60
        total_height = 17 + (count - 1) * 10

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

class FangShenLou1210_17Strategy(VolumeCalcStrategy):
    def calculate(self, count, length = 0, width = 0, height = 0):
        total_length = 120
        total_width = 100
        total_height = 17 + (count - 1) * 10

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

class FangShenLou1212_10Strategy(VolumeCalcStrategy):
    def calculate(self, count, length = 0, width = 0, height = 0):
        total_length = 120
        total_width = 120
        total_height = 10 + (count - 1) * 7

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

class FangShenLou1212_17Strategy(VolumeCalcStrategy):
    def calculate(self, count, length = 0, width = 0, height = 0):
        total_length = 120
        total_width = 120
        total_height = 17 + (count - 1) * 10

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

class FangShenLou1368_15Strategy(VolumeCalcStrategy):
    def calculate(self, count, length = 0, width = 0, height = 0):
        total_length = 130
        total_width = 68
        total_height = 15 + (count - 1) * 9

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

class FangShenLou1368_17Strategy(VolumeCalcStrategy):
    def calculate(self, count, length = 0, width = 0, height = 0):
        total_length = 130
        total_width = 68
        total_height = 17 + (count - 1) * 11

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

class FangShenLou1368_30Strategy(VolumeCalcStrategy):
    def calculate(self, count, length = 0, width = 0, height = 0):
        total_length = 130
        total_width = 68
        total_height = 30 + (count - 1) * 11

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

class FangShenLou1313_15Strategy(VolumeCalcStrategy):
    def calculate(self, count, length = 0, width = 0, height = 0):
        total_length = 130
        total_width = 130
        total_height = 15 + (count - 1) * 11

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

class FangShenLou1313_17Strategy(VolumeCalcStrategy):
    def calculate(self, count, length = 0, width = 0, height = 0):
        total_length = 130
        total_width = 130
        total_height = 17 + (count - 1) * 11

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

class FangShenLou1313_30Strategy(VolumeCalcStrategy):
    def calculate(self, count, length = 0, width = 0, height = 0):
        total_length = 130
        total_width = 130
        total_height = 30 + (count - 1) * 11

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

class FangShenLou1311_30Strategy(VolumeCalcStrategy):
    def calculate(self, count, length = 0, width = 0, height = 0):
        total_length = 130
        total_width = 130
        total_height = 30 + (count - 1) * 11

        total_volume = int(total_length * total_width * total_height)
        return total_volume, total_length, total_width, total_height

# 无效产品规格
class InvalidStrategy(VolumeCalcStrategy):
    def calculate(self, count, length, width, height):
        return 0, 0, 0, 0

#---------------------------------------------------------------------------------------------------------------------#
