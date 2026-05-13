import arcade
import math
import subprocess



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

            if distance <= 5:
                print(f"enemy '{enemy.enemy_type}' is near, distance: {math.ceil(distance)}")

                if enemy.enemy_type == "slime":
                    subprocess.run([ combat_ui.determine_enemy("slime"), combat_ui.create_combat_ui(),])
                    return
                if enemy.enemy_type == "skeleton":
                    subprocess.run([combat_ui.determine_enemy("skeleton"), combat_ui.create_combat_ui()])
                    return
                if enemy.enemy_type == "witch":
                    subprocess.run([combat_ui.determine_enemy("witch"), combat_ui.create_combat_ui()])
                    return
                if enemy.enemy_type == "goblin":
                    subprocess.run([combat_ui.determine_enemy("goblin"), combat_ui.create_combat_ui()])
                    return