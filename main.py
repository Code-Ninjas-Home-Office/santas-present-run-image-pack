def on_a_pressed():
    if playerSprite.is_hitting_tile(CollisionDirection.BOTTOM):
        playerSprite.vy = -200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    playerSprite.set_image(assets.image("""
        santaLeft
    """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile(sprite, location):
    tiles.place_on_tile(sprite, tiles.get_tile_location(0, 0))
    music.play(music.melody_playable(music.big_crash),
        music.PlaybackMode.UNTIL_DONE)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        snowPath13
    """),
    on_overlap_tile)

def on_right_pressed():
    playerSprite.set_image(assets.image("""
        santaRight
    """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap(sprite2, otherSprite):
    sprites.destroy(otherSprite, effects.smiles, 500)
    music.play(music.melody_playable(music.magic_wand),
        music.PlaybackMode.UNTIL_DONE)
    if len(sprites.all_of_kind(SpriteKind.food)) == 0:
        game.game_over(True)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def on_on_overlap2(sprite3, otherSprite2):
    sprites.destroy(otherSprite2, effects.disintegrate, 500)
    info.change_countdown_by(-5)
    music.play(music.melody_playable(music.zapped),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

cookieSprite: Sprite = None
presentSprite: Sprite = None
playerSprite: Sprite = None
scene.set_background_image(assets.image("""
    winterBackground
"""))
game.splash("Oh no!", "Santa lost his presents!")
game.splash("Collect all the presents", "before the time runs out!")
game.splash("Avoid the milk and cookies", "they take away time!")
tiles.set_current_tilemap(tilemap("""
    level
"""))
info.start_countdown(30)
playerSprite = sprites.create(assets.image("""
    santaRight
"""), SpriteKind.player)
tiles.place_on_tile(playerSprite, tiles.get_tile_location(0, 6))
controller.move_sprite(playerSprite, 100, 0)
scene.camera_follow_sprite(playerSprite)
playerSprite.ay = 500
for value in tiles.get_tiles_by_type(assets.tile("""
    foodSpawnTile
""")):
    presentSprite = sprites.create(assets.image("""
        greenGift
    """), SpriteKind.food)
    tiles.place_on_tile(presentSprite, value)
    tiles.set_tile_at(value, assets.tile("""
        transparency16
    """))
for value2 in tiles.get_tiles_by_type(assets.tile("""
    enemySpawnTile
""")):
    cookieSprite = sprites.create(assets.image("""
        milkGlassCookie
    """), SpriteKind.enemy)
    tiles.place_on_tile(cookieSprite, value2)
    tiles.set_tile_at(value2, assets.tile("""
        transparency16
    """))