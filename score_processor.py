# ==========================================
# 課程名稱：AI 與程式語言 (113-1) 
# 實作項目：學期成績計算與數據格式化輸出
# 期末成績：100 / 100
# ==========================================

def process_scores():
    # 交互式輸入
    name = input("請問您的姓名? ")
    score_a = int(input("請輸入多媒體成績? "))
    score_b = int(input("請輸入資概成績? "))
    score_c = int(input("請輸入體育成績? "))
    
    # 計算平均值
    average = (score_a + score_b + score_c) / 3
    
    # 格式化輸出報表
    print("\n" + "="*30)
    print(f"【學生成績報表】")
    print(f"姓名：{name}")
    print(f"多媒體成績：{score_a}")
    print(f"資概成績：{score_b}")
    print(f"體育成績：{score_c}")
    print("-" * 30)
    print(f"平均成績：{average:.2f}")
    print("="*30)

if __name__ == "__main__":
    process_scores()
