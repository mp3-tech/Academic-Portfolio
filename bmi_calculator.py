# ==========================================
# 課程名稱：AI 與程式語言 (113-1)
# 期末評分：100 / 100
# 功能描述：基礎邏輯實作 - 身體質量指數 (BMI) 計算器
# ==========================================

def calculate_bmi():
    # 獲取使用者輸入
    name = input("請輸入姓名: ")
    height = float(input("請輸入身高(cm): "))
    weight = float(input("請輸入體重(kg): "))
    
    # 計算 BMI (身高需轉換為公尺)
    bmi = weight / ((height / 100) ** 2)
    
    # 邏輯判斷流程
    if bmi < 18.5:
        result = "體重過輕，注意健康"
    elif 18.5 <= bmi < 24:
        result = "體重正常，繼續保持"
    else:
        result = "體重過重，注意健康"
    
    # 格式化輸出結果
    print(f"\n您的姓名: {name}")
    print(f"您的 BMI 值: {bmi:.2f}")
    print(f"診斷結果: {result}")

if __name__ == "__main__":
    calculate_bmi()
