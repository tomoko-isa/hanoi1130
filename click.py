"""ハノイの塔 クリック処理のプログラム"""
def canvas_on_click(event):
    """キャンバスがクリックされた時の処理"""  #--- (*1)
    # クリックされた位置を取得
    rect = canvas.getBoundingClientRect()
    x = int(event.clientX - rect.left)
    # クリックされた塔を特定
    panel_w = canvas.width // TOWER_COUNT
    clicked_tower = x // panel_w
    # 塔の範囲内か確認して処理
    if 0 <= clicked_tower < TOWER_COUNT:
        handle_tower(clicked_tower)

# クリックイベントの設定 --- (*2)
canvas.addEventListener("click", canvas_on_click)

def handle_tower(index):
    """塔がクリックされた時の処理"""  # --- (*3)
    q_text("#info", "")  # 情報表示をクリア
    # 塔の選択状態を確認
    if game["selected_tower"] == -1:
        # 塔が選択されていない場合 --- (*4)
        if game["towers"][index]:  # 円盤がある塔のみ選択可能
            game["selected_tower"] = index
            q_text("#info", f"塔{index + 1}の円盤の移動先を選んでください")
    else:
        # 既に塔が選択されている場合、移動できるか確認 --- (*5)
        if move_disk(game["selected_tower"], index):
            q_text("#info", f"円盤を塔{index + 1}に移動しました")
        else:
            q_text("#info", f"塔{index + 1}に移動できません")
        game["selected_tower"] = -1
    draw_game()  # 画面を再描画