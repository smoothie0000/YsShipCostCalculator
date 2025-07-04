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

# 平板四脚
class PingBanSiJiaoStrategy(VolumeCalcStrategy):
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

# 无效产品规格
class InvalidStrategy(VolumeCalcStrategy):
    def calculate(self, count, length, width, height):
        return 0, 0, 0, 0

#---------------------------------------------------------------------------------------------------------------------#
