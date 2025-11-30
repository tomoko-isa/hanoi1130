"""ハノイの塔のメインプログラム"""
# 定数宣言 --- (*1)
DISK_COUNT = 4  # 円盤の数
TOWER_COUNT = 3  # 塔の数（棒の数）
# ゲーム管理 --- (*2)
game = {
    "towers": [[], [], []],  # 3本の棒（左、中央、右）
    "selected_tower": -1,  # 選択された棒のインデックス
    "move_count": 0  # 移動回数
}
# 円盤の色定義（番号順: 0=最小, 3=最大） --- (*3)
DISK_COLORS = [
    "#FFFF44",  # 黄色（0: 一番小さい円盤）
    "#4444FF",  # 青色（1: 小さい円盤）
    "#44FF44",  # 緑色（2: 大きい円盤）
    "#FF4444"   # 赤色（3: 一番大きい円盤）
]

def start_game():
    """ゲームを開始する"""  # --- (*4)
    # 最初の棒に全ての円盤を配置
    game["towers"] = [list(range(DISK_COUNT-1, -1, -1)), [], []]
    game["selected_tower"] = -1
    game["move_count"] = 0
    draw_game()  # 画面を描画

def move_disk(from_tower, to_tower):
    """円盤を移動する"""  # --- (*5)
    if not can_move(from_tower, to_tower):
        return False
    # 円盤を移動
    disk = game["towers"][from_tower].pop()
    game["towers"][to_tower].append(disk)
    game["move_count"] += 1
    # ゲームのクリア判定 --- (*6)
    if check_clear():
        def show_clear_message():  # メッセージを表示
            q_text("#title", "ハノイの塔をゲームクリア")
            q_text("#info", "おめでとう！")
        set_timeout(show_clear_message, 100)  # 少し遅延させて表示
    return True

def can_move(from_tower, to_tower):
    """円盤が移動可能かチェック"""  # --- (*7)
    if from_tower < 0 or from_tower >= TOWER_COUNT:
        return False
    if to_tower < 0 or to_tower >= TOWER_COUNT:
        return False
    if from_tower == to_tower:
        return False
    # 移動元に円盤がなければ移動できない
    if len(game["towers"][from_tower]) == 0:
        return False
    # 移動先が空なら移動可能
    if len(game["towers"][to_tower]) == 0:
        return True
    # 小さい円盤の上に大きな円盤を置けない
    from_disk = game["towers"][from_tower][-1]  # 移動する円盤
    to_disk = game["towers"][to_tower][-1] # 移動先の一番上の円盤
    return from_disk < to_disk

def check_clear():
    """クリア判定"""  #-- (*8)
    # 正しい順序: [3, 2, 1, 0] （大きいものが下、小さいものが上）
    target_order = list(range(DISK_COUNT-1, -1, -1))
    # 全ての円盤が正しい順序で積まれていればクリア
    for tower_index in [1, 2]:  # 左の棒（0）は除外
        if game["towers"][tower_index] == target_order:
            return True
    return False