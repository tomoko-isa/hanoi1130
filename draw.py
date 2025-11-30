"""ハノイの塔描画プログラム"""
# キャンバスの取得 --- (*1)
canvas = q("#canvas")
context = canvas.getContext("2d")
# 描画用の定数 --- (*2)
TOWER_WIDTH = 8  # 塔の幅
TOWER_HEIGHT = 200  # 塔の高さ
TOWER_BASE_WIDTH = 100  # 塔の台座の幅
TOWER_BASE_HEIGHT = 20  # 塔の台座の高さ
DISK_HEIGHT = 20  # 円盤の高さ
MAX_DISK_WIDTH = 80  # 円盤の最大幅
MIN_DISK_WIDTH = 30  # 円盤の最小幅
PANEL_W = canvas.width // TOWER_COUNT  # 塔のパネル幅

def draw_game():
    """ゲーム全体を描画"""  # --- (*3)
    # 背景をクリア
    context.clearRect(0, 0, canvas.width, canvas.height)
    draw_move_count()  # 移動回数を表示
    # 選択中の塔をハイライト
    draw_selection()
    # 3本の塔を描画
    for i in range(TOWER_COUNT):
        draw_tower(i)  # 塔を描画
        draw_disks(i)  # 円盤を描画

def draw_tower(index):
    """3つの塔を描画"""  # --- (*4)
    x = PANEL_W * index + PANEL_W // 2 # 塔の中心X座標
    # 塔の柱
    context.fillStyle = "#8B4513"  # 茶色
    tower_x = x - TOWER_WIDTH // 2
    tower_y = 150
    context.fillRect(tower_x, tower_y, TOWER_WIDTH, TOWER_HEIGHT)
    # 塔の台座
    base_x = x - TOWER_BASE_WIDTH // 2
    base_y = 150 + TOWER_HEIGHT
    context.fillRect(base_x, base_y, TOWER_BASE_WIDTH, TOWER_BASE_HEIGHT)

def draw_disks(index):
    """円盤を描画"""  # --- (*5)
    tower_x = PANEL_W * index + PANEL_W // 2 # 塔の中心X座標
    disks = game["towers"][index]
    for disk_idx, disk_size in enumerate(disks):
        # 円盤の幅（大きさに応じて）
        # disk_size: 0=最小, 1, 2, 3=最大
        # 大きい円盤ほど幅を大きくする
        disk_width = MIN_DISK_WIDTH + (MAX_DISK_WIDTH - MIN_DISK_WIDTH) * disk_size // (DISK_COUNT - 1)
        
        # 円盤の位置
        disk_x = tower_x - disk_width // 2
        disk_y = 150 + TOWER_HEIGHT - (disk_idx + 1) * DISK_HEIGHT
        
        # 円盤を描画
        context.fillStyle = DISK_COLORS[disk_size]
        context.fillRect(disk_x, disk_y, disk_width, DISK_HEIGHT)
        
        # 円盤の枠線
        context.strokeStyle = "#333333"
        context.lineWidth = 2
        context.strokeRect(disk_x, disk_y, disk_width, DISK_HEIGHT)

def draw_selection():
    """選択中の塔をハイライト"""  # --- (*6)
    if game["selected_tower"] < 0:
        return  # 選択されていない場合は何もしない
    x = PANEL_W * game["selected_tower"]
    h = TOWER_HEIGHT + TOWER_BASE_HEIGHT + 15
    # ハイライト枠を描画
    context.strokeStyle = "#FF6600"
    context.fillStyle = "rgba(200, 200, 255, 0.3)"
    context.lineWidth = 3
    context.fillRect(x + 10, 140, PANEL_W - 20, h)
    context.strokeRect(x + 10, 140, PANEL_W - 20, h)

def draw_move_count():
    """移動回数を表示"""  #-- (*7)
    context.fillStyle = "#333333"
    context.font = "16px Arial"
    context.textAlign = "center"
    context.fillText(f"移動回数: {game['move_count']}",
                     canvas.width // 2, 30)