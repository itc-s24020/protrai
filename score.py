def evaluate_score(score):
    if score >= 80:
        return "優"
    elif score >= 70:
        return "良"
    elif score >= 60:
        return "可"
    else:
        return "不可"

# スコアをユーザーから入力してもらう
try:
    score = float(input("スコアを入力してください: "))
    if score < 0:
        print("スコアは負の数であってはなりません。")
    else:
        result = evaluate_score(score)
        print(f"評価: {result}")
except ValueError:
    print("無効な入力です。数値を入力してください。")
