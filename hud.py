from direct.gui.OnscreenText import OnscreenText

def draw_hud(player_units, enemy_units):
    player_hp = sum(unit.hp for unit in player_units)
    enemy_hp = sum(unit.hp for unit in enemy_units)
    player_text = OnscreenText(text=f"Player HP: {player_hp}", pos=(-1.3, 0.9), scale=0.07, fg=(0, 1, 0, 1))
    enemy_text = OnscreenText(text=f"Enemy HP: {enemy_hp}", pos=(-1.3, 0.8), scale=0.07, fg=(1, 0, 0, 1))

    # Display individual unit health
    for i, unit in enumerate(player_units):
        OnscreenText(text=f"Unit {i+1} HP: {unit.hp}", pos=(-1.3, 0.7 - i * 0.1), scale=0.05, fg=(0, 1, 0, 1))
    for i, unit in enumerate(enemy_units):
        OnscreenText(text=f"Enemy {i+1} HP: {unit.hp}", pos=(-1.3, 0.7 - (i + len(player_units)) * 0.1), scale=0.05, fg=(1, 0, 0, 1))
