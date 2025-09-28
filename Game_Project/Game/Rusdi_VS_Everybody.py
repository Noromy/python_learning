# Time to fight
import time
import json
class Character:
    def __init__(self, name, health, strength, level):
        self.name = name 
        self.health = health
        self.max_health = health
        self.strength = strength
        self.level = level
        self.alive = True
        self.experience = 0
        self.equipped_weapon = None

    def is_alive(self):
        return self.alive
    
    def receive_loot(self, loot):
        if isinstance(loot, Weapon):
            print(f'{self.name} mendapatkan loot {loot.name} dan langsung menggunakannya')
            self.equip_weapon(loot)
        elif isinstance(loot, Item) and loot.item_type == "consumable":
            print(f'{self.name} mendapatkan potion loot {loot.name} dan langsung menggunakannya')
            self.potions +=  loot.value
            print(f'Potions sekarang: {self.potions}')
        else:
            print(f'{self.name} mendapatkan potion loot {loot.name} dan dan tidak bisa digunakan')

    def equip_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.equipped_weapon = weapon
            print(weapon.equip_message(self.name))
        else:
            print("Senjata tidak bisa digunakan")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} sudah lemes dan tidak bisa diserang lagi.")
            return

        weapon_bonus = self.equipped_weapon.damage_bonus if self.equipped_weapon else 0
        damage = self.strength + weapon_bonus
        print(f"PLAKKKK !!! \n{self.name} menabok {target.name} sebanyak {damage} damage !!!")
        target.take_damage(damage, attacker=self)
        
                  
    def take_damage(self, amount, attacker=None):

        self.health -= amount
        time.sleep(0.5)
        print(f'{self.name} menerima damage {amount}. Nyawa : {self.health}/{self.max_health}')

        if self.health <= 0 and self.alive:
            self.alive = False
            print(f'\n{self.name} sudah tumbang !! \n')
            xp_reward = 5
            print(f'{attacker.name} mendapatkan {xp_reward} kredit')
            attacker.gain_exp(xp_reward)
            if isinstance(self, Crime) and isinstance(attacker, Hero) and self.loot:
                print(f"\n{self.name} menjatuhkan loot : {self.loot}")
                attacker.receive_loot(self.loot)

    def gain_exp(self, amount):
        self.experience += amount
        print(f'{self.name} memperoleh {amount}. Total kredit : {self.experience}')
        while self.experience >= 5:
            self.level += 1
            self.experience -= 5
            print(f'Selamat {self.name} naik ke level {self.level}')

    def heal(self, amount):
        self.health = min(amount + self.health, self.max_health)
        print(f'{self.name} menyembuhkan diri sebanyak {amount}. Health : {self.health}')

class Hero(Character):
    def __init__(self, name, health, strength, level, potions):
        super().__init__(name, health, strength, level)
        self.potions = potions
    
    def use_potions(self):
        if self.potions > 0 and self.health < self.max_health:
            self.potions -= 1
            heal_amount = 30
            self.health = min(self.health + heal_amount, self.max_health)
            print(f'{self.name} menggunakan jamu! Health : + {self.health}/{self.max_health}. \nPotion left : {self.potions}')
        else :
            print("No potion Left :(")


class Crime(Character):
    def __init__(self, name, health, strength, level, loot):
        super().__init__(name, health, strength, level)
        self.loot = loot

    def shoot(self, target): 
        if not target.is_alive():
            print(f"{target.name} sudah tumbang dan tidak bisa diserang lagi.")
            return

        shoot_damage = self.strength * 2
        print(f'Duuarrr mati kau bangsat \n{target.name} terkena Tembekan oleh {self.name}')
        target.take_damage(shoot_damage, attacker=self)
        time.sleep(0.5)


class GameWorld:
    def __init__(self, name):
        self.name = name 
        self.location = {}
        self.current_location = None

    def add_location(self, location):
        self.location[location.name] = location
        print(f'Added {location.name} to the world map')

class Location:
    def __init__(self, name, description):
        self.name = name 
        self.description = description
        self.items = []
        self.monster = []
        self.connection = {}


    def add_connection(self, direction, location):
        self.connection[direction] = location
        print(f'Connected {self.name} to {location.name} ({direction})')

    def move_character(self, character, direction):
        if self.current_location and direction in self.current_location.connection:
            new_location = self.current_location.connection[direction]
            self.current_location = new_location
            print(f"{character.name} pindah ke {new_location.name}")
        else:
            print(f"Tidak bisa pindah ke arah {direction} dari {self.current_location.name}")

    def spawn_monster(self, monster):
        self.monster.append(monster)
        print(f"Monster {monster.name} muncul di {self.name}")

    def remove_monster(self, monster):
        if monster in self.monster:
            self.monster.remove(monster)

class Item:
    def __init__(self, name, item_type, value):
        self.name = name 
        self.item_type = item_type
        self.value = value

    def __str__(self):
        return f"{self.name} ({self.item_type}) {self.value}"
    
class Weapon(Item):
    def __init__(self, name, item_type, value, damage_bonus):
        super().__init__(name, item_type, value)
        self.damage_bonus = damage_bonus
    
    def equip_message(self, user_name):
        return f"{user_name} menggunakan {self.name}! Damage + {self.damage_bonus}"



import random

class BattleSystem():
    def __init__(self, state):
        self.turn_count = 0
        self.state = state

    def start_battle(self, Hero, Crime, active_quest=None):
        print(f'\n PERTARUNGAN DIMULAI: {Jahat.name} vs {Baik.name} \n')

        while Hero.is_alive() and Crime.is_alive():
            self.turn_count += 1
            print(f"--- Turn {self.turn_count} ----")

            self.Baik_turn(Hero, Crime)
            if not Jahat.is_alive():
                return self.victory(Hero, Crime, active_quest)
        
            self.Jahat_turn(Jahat, Baik)
            if not Baik.is_alive():
                return self.defeat(Hero, Crime, active_quest)
        
            print()


    def Baik_turn(self, Hero, Crime):
        action = random.choice(["attack", "potion"])

        if action == "potion" and Hero.potions > 0 and Hero.health < Hero.max_health:
            Hero.use_potions()
        else:
            Hero.attack(Crime)

    def Jahat_turn(self, Crime, Hero):

        action = random.randint(1, 3)
        if action == 1:
            Crime.shoot(Hero)
        else:
            Crime.attack(Hero)


    def victory(self, Baik, Jahat, active_quests):
        print(f'\nVICTORY!! {Baik.name} mengalahkan {Jahat.name}\n')
        xp_reward = Jahat.strength 
        Baik.gain_exp(xp_reward)

        for quest in active_quests[:]:
            for task in quest.task:
            # Update progress hanya jika task relevan dengan musuh yang dikalahkan
                task.update_progress()
            if quest.check_complete(finisher=Baik, game_state=self.state):
                print(f'{Baik.name} mendapat {quest.reward_xp} XP dari quest "{quest.name}" \n"')
                Baik.gain_exp(quest.reward_xp)
        return "victory"

    
    def defeat(self, Baik, Jahat, active_quest=None):
        print(f'\nDEFEAT! {Baik.name} di kalahkan oleh {Jahat.name}\n')
        return "defeat"
    

class GameState:
    def __init__(self):
        self.Baik = None
        self.Arena = None
        self.game_over = False
        self.active_quests = []
        self.completed_quest = []

    def activate_quests(self, quest):
        if quest not in self.active_quests:
            self.active_quests.append(quest)
            print(f"✅ Quest '{quest.name}' diaktifkan.")
        else:
            print(f"⚠️ Quest '{quest.name}' sudah aktif.")

    def save_game(self, filename='SaveGame.json'):

        if not self.Baik or not self.Arena:
            print("❌ Tidak bisa menyimpan: karakter atau lokasi belum diatur.")
            return

        save_data = {
            "Baik_name" : self.Baik.name,
            "Baik_health" : self.Baik.health,
            "Baik_level" : self.Baik.level,
            "Location" : self.Arena.name,
            "Baik_strength" : self.Baik.strength,
            "Baik_potions" : self.Baik.potions,
            "Baik_experience" : self.Baik.experience,
            "active_quests" : [q.name for q in self.active_quests],
            "completed_quest" : [q.name for q in self.completed_quest]
        }

        with open('SaveGame.json', 'w') as f:
            json.dump(save_data, f, indent=4, separators=(",", ":"))
        print(f"\n Game saved \n")
    
    def load_game(self, filename='SaveGame.json'):

        import os
        if not os.path.exists(filename):
            print("❌ Save file tidak ditemukan.")
            return
        
        with open ('SaveGame.json', 'r') as f:
            save_data = json.load(f)

        self.Baik = Hero(
        name=save_data["Baik_name"],
        health=save_data["Baik_health"],
        strength=save_data["Baik_strength"],
        level=save_data["Baik_level"],
        potions=save_data["Baik_potions"]
        )
        self.Baik.experience = save_data["Baik_experience"]

        self.Arena = Location(save_data["Location"], "Deskripsi default")

        self.active_quests = [Quest(name, description=None, reward_exp=None) for name in save_data.get("active_quests", [])]
        self.completed_quest = [Quest(name, description=None, reward_exp=None) for name in save_data.get("completed_quest", [])]
        print(f'✅ Game loaded! Welcome back, {self.Baik.name} di {self.Arena.name}')
        print(f'📜 Quest aktif: {[q.name for q in self.active_quests]}')
        print(f'✅ Quest selesai: {[q.name for q in self.completed_quest]}')

class Quest:
    def __init__(self, name, description, reward_exp):
        self.name = name 
        self.description = description
        self.reward_xp = reward_exp
        self.completed = False
        self.task = []
        self.finisher = None
        self.active_quest = []

    def add_task(self, task):
        self.task.append(task)
    

    def check_complete(self, finisher=None, game_state=None):
        if all(task.completed for task in self.task):
            self.finisher = finisher
            self.completed = True
            print(f"Quest {self.name} telah diselesaikan oleh {finisher.name}")

            if game_state:
                if self not in game_state.completed_quest:
                    game_state.completed_quest.append(self)
                if self in game_state.active_quests:
                    game_state.active_quests.remove(self)
            return True
        return False

class Task:
    def __init__(self, description, target_count=1):
        self.description = description
        self.current_count = 0
        self.target_count = target_count
        self.completed = False

    def update_progress(self, amount=1):
        if not self.completed:
            self.current_count += amount
        if self.current_count >= self.target_count and not self.completed :
            self.completed = True
            print(f'\nQuest Selesai : {self.description}')

world = GameWorld("Negri Ngawi")
state = GameState()

# Para Pahlawan

Artefak_Ngawi = Weapon("Artefak_Ngawi", "Senjata", 1, damage_bonus= 20)
health_potion = Item("Healing", "consumable", 20)

Baik = Hero("Rusdi", health=100, strength=25, level=20, potions=3)
Jahat = Crime("Azril", health=120, strength=15, level= 23, loot=Artefak_Ngawi)


BarberShop = Location("BarberShop", "Tempat para kesatria berkumpul")
Laundry = Location("Londri", "Tempat istirahat")
Arena = Location("Arena", "Tempat bara kesatria bertarung")

world.add_location(Arena)
world.add_location(BarberShop)
world.add_location(Laundry)

BarberShop.add_connection("selatan", Laundry)
Arena.add_connection("timur", BarberShop)
Arena.add_connection("timur", Laundry)


Arena.items.append(Artefak_Ngawi)
Arena.items.append(health_potion)


quest_ngawi = Quest("Ngawi", "Bunuh semua jomok", reward_exp=10)
task_bunuh_jomok = Task("Bunuh Azril", target_count=1)
quest_ngawi.add_task(task_bunuh_jomok)

quest_testin = Quest("Njeng", "Hell", reward_exp=5)
task_testin = Task("Bunuh Azril", target_count=1)
quest_testin.add_task(task_testin)

state.active_quests = [quest_ngawi, quest_testin]

Arena.spawn_monster(Jahat)


battle = BattleSystem(state)
result = battle.start_battle(Baik, Jahat, state.active_quests)



# Save game after battle
state.save_game()


state.load_game()







