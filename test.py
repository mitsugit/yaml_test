import yaml
with open('test.yaml','r') as f:
    shop_info = yaml.safe_load(f)

## 店のtypeを表示
print("店タイプ:  ",shop_info["shop_type"])

# 果物リストの2番目を表示
print("果物リストの２番目:  ",shop_info["fruits_list"][1])

# ミカンの価格を表示
print("ミカンの価格:  ",shop_info["fruits__price_dict"]["みかん"])

# 会社の名前を表示
print("会社名:  ", shop_info["shop_company_name"])

# 更新前のスタッフリストを表示
print("スタッフリスト:  ",shop_info["staff_dict"])

# 更新1回目のスタッフリストを表示
print("スタッフリスト更新1回目:  ",shop_info["staff_dict_updated"])

# 更新2回目のスタッフリストを表示
print("スタッフリスト更新2回目:  ",shop_info["staff_dict_updated2"])

# 店の説明
print("会社説明:  ",shop_info["description"])