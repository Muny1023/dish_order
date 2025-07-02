menu = {"爆炒油辣子": 25, "小馆羊杂面": 17, "家常蛋炒饭": 8, "炒年糕": 8}
#折扣率
discount_rate = 0.9

print(">>> 欢迎使用点菜系统 <<<")
print("以下是菜单")
for dish, price in menu.items():
    # 计算折扣价
    discount_price = price * discount_rate
    print(f"{dish}：{price}元（折扣价：{discount_price:.1f}元）")

print('<---分割线--->')
print("请问想吃什么^q^")
order = {}

# 点菜
while True:
    dishname = input("（输入 'end' 结束点菜 输入'menu'查看菜单）\n"
                     "请输入要点的菜名:\n")
    if dishname == 'menu':
        print("\n=== 菜单 ===")
        for dish, price in menu.items():
            discount_price = price * discount_rate
            print(f"{dish}：{price}元（折扣价：{discount_price:.1f}元）")
        continue
    if dishname == 'end':
        break
    if dishname in menu:
        order[dishname] = order.get(dishname, 0) + 1
        order_detail = " ".join([f"{dish} {count}份" for dish, count in order.items()])
        print(f"当前点单：{order_detail}")
    else:
        print("菜单中没有这道菜，请重新输入")

if order:
    totalprice = 0
    print("\n=== 点单详情 ===")
    for dish, count in order.items():
        # 单价
        danjia = menu[dish]
        # 单件商品总价（使用折扣价）
        jiage = danjia * count * discount_rate
        totalprice += jiage
        print(f"{dish} x {count}份 = {jiage:.1f}元")
    print(f"折扣率：{discount_rate * 10:.1f}折")
    print(f"折扣后总价：{totalprice:.1f}元")