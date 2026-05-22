import arcade
import math
import subprocess
import combat_ui
import random

class EnemySprite(arcade.Sprite):
    def __init__(self, img, scale, enemy_type, detect_radius=300, encounter_radius=60, patrol_speed=0.3, chase_speed=2.0):
        super().__init__(img, scale)
        self.enemy_type = enemy_type
        self.detect_radius = detect_radius
        self.encounter_radius = encounter_radius
        self.patrol_speed = patrol_speed
        self.chase_speed = chase_speed
        self.awake = False
        # small random wander vector for patrol behavior
        self._wander_angle = random.random() * 2 * math.pi
    def update(self):
        # default sprite update (position change by change_x/change_y)
        super().update()

def update_enemies(player_sprite: arcade.Sprite, enemy_list: arcade.SpriteList, light_layer, player_light):

    if player_sprite is None:
        return

    light_on = (player_light is not None) and (player_light in light_layer)

    for enemy in enemy_list:
        dist = math.dist(player_sprite.position, enemy.position)

        # check if enemy is inside the player's light radius
        lit = False
        if light_on and player_light is not None:
            try:
                light_radius = getattr(player_light, "radius", None)
                if light_radius is None:
                    # fallback if Light implementation doesn't expose radius
                    light_radius = 300
                lit = math.dist(enemy.position, player_light.position) <= light_radius
            except Exception:
                lit = False

        # Activate chase when within detect radius or lit
        if dist <= enemy.detect_radius or lit:
            enemy.awake = True
            dx = player_sprite.center_x - enemy.center_x
            dy = player_sprite.center_y - enemy.center_y
            mag = math.hypot(dx, dy) or 1.0
            enemy.change_x = (dx / mag) * enemy.chase_speed
            enemy.change_y = (dy / mag) * enemy.chase_speed
        else:
            # Idle / patrol behavior: slow drift and occasional random wander
            enemy.awake = False
            # gradual slow down
            enemy.change_x *= 0.85
            enemy.change_y *= 0.85
            # occasional wander impulse
            if random.random() < 0.01:
                angle = random.random() * 2 * math.pi
                enemy.change_x += math.cos(angle) * enemy.patrol_speed
                enemy.change_y += math.sin(angle) * enemy.patrol_speed

        # trigger encounter if very close
        if dist <= enemy.encounter_radius:
            try:
                # Call your combat UI – adapt if your implementation requires different calls
                combat_ui.create_combat_ui()
                combat_ui.determine_enemy(enemy.enemy_type)
            except Exception as e:
                # don't crash the game on combat UI problems; log for debug
                print("Failed to start combat:", e)
            # stop movement after encounter trigger
            enemy.change_x = 0
            enemy.change_y = 0
   
class Enemy(arcade.Sprite):
    def __init__(self, img, size, enemy_type):
        super().__init__(img, size)
        self.enemy_type = enemy_type

        self.enemy_list = arcade.SpriteList()

        enemy1 = Enemy(":resources:images/enemies/slimeBlock.png", 0.5, "slime")
        enemy1.center_x = 500
        enemy1.center_y = 300
        self.enemy_list.append(enemy1)



        for enemy in self.enemy_list:
            distance = math.dist(
                (self.player_sprite.center_x, self.player_sprite.center_y),
                (enemy.center_x, enemy.center_y)
            )

            if distance <= 100:
                print(f"enemy '{enemy.enemy_type}' is near, distance: {math.ceil(distance)}")

                if enemy.enemy_type == "slime":
                    subprocess.run([combat_ui.create_combat_ui(), combat_ui.determine_enemy("slime")])
                    return
                if enemy.enemy_type == "skeleton":
                    subprocess.run([combat_ui.create_combat_ui(), combat_ui.determine_enemy("skeleton")])
                    return
                if enemy.enemy_type == "witch":
                    subprocess.run([combat_ui.create_combat_ui(), combat_ui.determine_enemy("witch")])
                    return
                if enemy.enemy_type == "goblin":
                    subprocess.run([combat_ui.create_combat_ui(), combat_ui.determine_enemy("goblin")])
                    return