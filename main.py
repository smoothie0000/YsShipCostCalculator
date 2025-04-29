import math
import customtkinter as ctk
import constants

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("light")
        ctk.set_window_scaling(1.2)

        self.title("杨神快递费计算器")
        self.geometry("1000x800")

        # 标题
        title_label = ctk.CTkLabel(self, text="杨神快递费计算器", font=ctk.CTkFont(size=22, weight="bold"))
        title_label.grid(row=0, column=0, columnspan=4, pady=(20, 10))

        # 主frame
        self.frame = ctk.CTkFrame(self)
        self.frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        # 快递省份
        province_label = ctk.CTkLabel(self.frame, text="快递省份", font=ctk.CTkFont(size=16))
        province_label.grid(row=0, column=0, padx=10, pady=0, sticky="w")

        self.province_combobox = ctk.CTkComboBox(self.frame, values=constants.china_provinces, width=200)
        self.province_combobox.set("上海市")
        self.province_combobox.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="w")

        # 小标题
        labels = ["选择产品", "数量", "单个产品尺寸(cm*cm*cm)", "单个产品重量(kg)", "单个产品体积(cm³)"]
        for idx, text in enumerate(labels):
            label = ctk.CTkLabel(self.frame, text=text, font=ctk.CTkFont(size=16))
            label.grid(row=2, column=idx, padx=10, pady=(10, 0), sticky="w")

        self.product_rows = []
        self.next_row = 3

        self.add_product_row()

        # 按钮
        self.add_product_button = ctk.CTkButton(self.frame, text="添加新产品", font=ctk.CTkFont(size=16), command=self.add_product_row)
        self.add_product_button.grid(row=998, column=0, padx=10, pady=(10, 10), sticky="w")

        self.shipping_cost_label = ctk.CTkLabel(self.frame, text="快递费用:\n极兔:\n韵达:\n", font=ctk.CTkFont(size=16))
        self.shipping_cost_label.grid(row=999, column=0, padx=10, pady=(35, 0), sticky="w")

        self.calculate_shipping_button = ctk.CTkButton(self.frame, text="运费计算", font=ctk.CTkFont(size=16), command=self.calculate_shipping_cost)
        self.calculate_shipping_button.grid(row=1000, column=0, padx=10, pady=(0, 10), sticky="w")

    def add_product_row(self):
        row_widgets = {}

        product_combobox = ctk.CTkComboBox(self.frame, values=constants.product_types, width=150)
        product_combobox.set("网格川字")
        product_combobox.grid(row=self.next_row, column=0, padx=10, pady=(0, 10), sticky="w")
        row_widgets['product'] = product_combobox

        count_entry = ctk.CTkEntry(self.frame, placeholder_text="个", width=100)
        count_entry.grid(row=self.next_row, column=1, padx=10, pady=(0, 10), sticky="w")
        row_widgets['count'] = count_entry

        length_entry = ctk.CTkEntry(self.frame, placeholder_text="长", width=80)
        length_entry.grid(row=self.next_row, column=2, padx=(10, 2), pady=(0, 10), sticky="w")
        row_widgets['length'] = length_entry

        width_entry = ctk.CTkEntry(self.frame, placeholder_text="宽", width=80)
        width_entry.grid(row=self.next_row, column=2, padx=(90, 2), pady=(0, 10), sticky="w")
        row_widgets['width'] = width_entry

        height_entry = ctk.CTkEntry(self.frame, placeholder_text="高", width=80)
        height_entry.grid(row=self.next_row, column=2, padx=(170, 2), pady=(0, 10), sticky="w")
        row_widgets['height'] = height_entry

        weight_entry = ctk.CTkEntry(self.frame, placeholder_text="kg", width=100)
        weight_entry.grid(row=self.next_row, column=3, padx=10, pady=(0, 10), sticky="w")
        row_widgets['weight'] = weight_entry

        size_label = ctk.CTkLabel(self.frame, text="0 cm³", font=ctk.CTkFont(size=16))
        size_label.grid(row=self.next_row, column=4, padx=10, pady=(0, 10), sticky="w")
        row_widgets['size'] = size_label

        calculate_button = ctk.CTkButton(self.frame, text="计算体积", font=ctk.CTkFont(size=16),
                                         command=lambda rw=row_widgets: self.calculate_volume(rw))
        calculate_button.grid(row=self.next_row, column=5, padx=(30, 10), pady=(0, 10))
        row_widgets['button'] = calculate_button

        delete_button = ctk.CTkButton(self.frame, text="删除", font=ctk.CTkFont(size=16),
                                      command=lambda rw=row_widgets: self.delete_row(rw))
        delete_button.grid(row=self.next_row, column=6, padx=10, pady=(0, 10))
        row_widgets['delete'] = delete_button

        self.product_rows.append(row_widgets)
        self.next_row += 1

    def delete_row(self, row_widgets):
        # 删除界面上的组件
        for widget in row_widgets.values():
            if isinstance(widget, ctk.CTkBaseClass):
                widget.destroy()
        # 从列表中删除
        self.product_rows.remove(row_widgets)

    def calculate_volume(self, widgets):
        try:
            count = float(widgets['count'].get())
            length = float(widgets['length'].get())
            width = float(widgets['width'].get())
            height = float(widgets['height'].get())

            reminder = count % 2
            divide = math.floor(count / 2)
            single_volume = reminder * (length * width * height)

            product_type = widgets['product'].get()

            if product_type == "网格川字":
                bi_volume = length * (width + 18) * (height + 4)
                total_volume = int(single_volume + bi_volume)
            elif product_type == "网格九脚":
                total_volume = int((5 * (count - 1) + 14) * length * width * height)
            elif product_type == "平板四脚":
                bi_volume = length * (width + 13) * (height + 3)
                total_volume = int(single_volume + bi_volume)
            elif product_type == "平板六脚":
                bi_volume = length * (width + 13) * (height + 3)
                total_volume = int(single_volume + bi_volume)
            elif product_type == "平板九脚":
                bi_volume = length * (width + 18) * (height + 3)
                total_volume = int(single_volume + bi_volume)
            else:
                widgets['size'].configure(text="产品类型错误")
                return 0

            widgets['size'].configure(text=f"{total_volume} cm³")
            return total_volume

        except ValueError:
            widgets['size'].configure(text="输入有误")
            return 0

    def calculate_debang_cost(self, total_volume, real_weight):
        first_kg_cost = 0
        over_per_kg_cost = 0
        if self.province_combobox.get() in ["江苏省", "浙江省", "上海市"]:
            first_kg_cost = 7
            over_per_kg_cost = 1
        elif self.province_combobox.get() in ["广东省", "安徽省", "山东省",  "北京市", "天津市", "河北省", "河南省", "湖北省", "湖南省", "江西省", "山西省", "福建省"]:
            first_kg_cost = 8
            over_per_kg_cost = 2
        elif self.province_combobox.get() in ["广西壮族自治区", "海南省", "云南省", "贵州省", "四川省", "重庆市", "黑龙江省", "吉林省", "辽宁省"]:
            first_kg_cost = 9
            over_per_kg_cost = 2.5
        elif self.province_combobox.get() in ["陕西省", "甘肃省", "宁夏回族自治区", "青海省", "内蒙古自治区"]:
            first_kg_cost = 13
            over_per_kg_cost = 3
        elif self.province_combobox.get() in ["新疆维吾尔自治区", "西藏自治区"]:
            first_kg_cost = 28
            over_per_kg_cost = 8
        
        ship_cost = 0
        volume_weight = total_volume / 12000
        ship_weight = max(volume_weight, real_weight)
        if ship_weight < 1:
            ship_cost = first_kg_cost
        else:
            ship_cost = first_kg_cost + over_per_kg_cost * (ship_weight - 1)

        return ship_cost


    def calculate_shipping_cost(self):
        error_flag = False
        total_volume = 0
        real_weight = 0
        for widgets in self.product_rows:
            total_volume += self.calculate_volume(widgets)
            try:
                weight = float(widgets['weight'].get())
                count = float(widgets['count'].get())
                real_weight += weight * count
            except ValueError:
                error_flag = True

        debang_cost = self.calculate_debang_cost(total_volume, real_weight)
        jitu_cost = 0
        yunda_cost = 0

        if error_flag:
            self.shipping_cost_label.configure(text="输入有误，无法计算， 请重新检查输入")
        else:
            self.shipping_cost_label.configure(
                text=f"快递费用:\n德邦: {debang_cost} 元\n极兔: {jitu_cost} 元\n韵达: {yunda_cost} 元\n"
            )

if __name__ == "__main__":
    app = App()
    app.mainloop()
