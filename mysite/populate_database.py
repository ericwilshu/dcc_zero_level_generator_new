import sqlite3
import dcc_root_path

ROOT_PATH = dcc_root_path.get_root_path()

connection = sqlite3.connect('data_files/dcc.db')
curs = connection.cursor()

def create_tables(curs, conn):

    curs.execute("DROP TABLE dwarf_occupations")
    curs.execute("DROP TABLE elf_occupations")
    curs.execute("DROP TABLE halfling_occupations")
    curs.execute("DROP TABLE human_occupations")
    curs.execute("DROP TABLE all_occupations")

    curs.execute("""CREATE TABLE IF NOT EXISTS appendix_l(
        id INTEGER PRIMARY KEY,
        language TEXT,
        zero_level INTEGER,
        warrior INTEGER,
        cleric INTEGER,
        thief INTEGER,
        wizard INTEGER,
        halfing INTEGER,
        elf INTEGER,
        dwarf INTEGER
    )""")

    curs.execute("""CREATE TABLE IF NOT EXISTS dwarf_occupations(
        id INTEGER PRIMARY KEY,
        race INTEGER,
        occupation TEXT,
        weapon TEXT,
        armor TEXT,
        trade_good TEXT,
        has_ammo INTEGER,
        has_animal INTEGER,
        has_crop INTEGER,
        has_cart INTEGER,
        extra_gp INTEGER,
        extra_sp INTEGER,
        extra_cp INTEGER
    )""")

    curs.execute("""CREATE TABLE IF NOT EXISTS elf_occupations(
        id INTEGER PRIMARY KEY,
        race INTEGER,
        occupation TEXT,
        weapon TEXT,
        armor TEXT,
        trade_good TEXT,
        has_ammo INTEGER,
        has_animal INTEGER,
        has_crop INTEGER,
        has_cart INTEGER,
        extra_gp INTEGER,
        extra_sp INTEGER,
        extra_cp INTEGER
    )""")

    curs.execute("""CREATE TABLE IF NOT EXISTS halfling_occupations(
        id INTEGER PRIMARY KEY,
        race INTEGER,
        occupation TEXT,
        weapon TEXT,
        armor TEXT,
        trade_good TEXT,
        has_ammo INTEGER,
        has_animal INTEGER,
        has_crop INTEGER,
        has_cart INTEGER,
        extra_gp INTEGER,
        extra_sp INTEGER,
        extra_cp INTEGER
    )""")

    curs.execute("""CREATE TABLE IF NOT EXISTS all_occupations(
        id INTEGER PRIMARY KEY,
        race INTEGER,
        occupation TEXT,
        weapon TEXT,
        armor TEXT,
        trade_good TEXT,
        has_ammo INTEGER,
        has_animal INTEGER,
        has_crop INTEGER,
        has_cart INTEGER,
        extra_gp INTEGER,
        extra_sp INTEGER,
        extra_cp INTEGER
    )""")

    curs.execute("""CREATE TABLE IF NOT EXISTS human_occupations(
        id INTEGER PRIMARY KEY,
        race INTEGER,
        occupation TEXT,
        weapon TEXT,
        armor TEXT,
        trade_good TEXT,
        has_ammo INTEGER,
        has_animal INTEGER,
        has_crop INTEGER,
        has_cart INTEGER,
        extra_gp INTEGER,
        extra_sp INTEGER,
        extra_cp INTEGER
    )""")

    curs.execute("""CREATE TABLE IF NOT EXISTS ability_score_modifiers(
        id INTEGER PRIMARY KEY,
        ability_score INTEGER,
        modifier INTEGER,
        wizard_spells_known INTEGER,
        max_spell_level INTEGER
    )""")

    curs.execute("""CREATE TABLE IF NOT EXISTS luck_scores(
        id INTEGER PRIMARY KEY,
        luck_sign TEXT,
        description TEXT
    )""")

    curs.execute("""CREATE TABLE IF NOT EXISTS farmer_type(
        id INTEGER PRIMARY KEY,
        crop TEXT
    )""")

    curs.execute("""CREATE TABLE IF NOT EXISTS animal_type(
        id INTEGER PRIMARY KEY,
        animal TEXT
    )""")

    curs.execute("""CREATE TABLE IF NOT EXISTS whats_in_the_cart(
        id INTEGER PRIMARY KEY,
        contents TEXT
    )""")

    curs.execute("""CREATE TABLE IF NOT EXISTS equipment(
        id INTEGER PRIMARY KEY,
        item TEXT
    )""")

    curs.execute("""CREATE TABLE IF NOT EXISTS race(
        id INTEGER PRIMARY KEY,
        race INTEGER,
        race_name TEXT
        traits TEXT
    )""")

    curs.execute("""CREATE TABLE IF NOT EXISTS weapon_damage_range(
        id INTEGER PRIMARY KEY,
        weapon_class INTEGER,
        damage TEXT,
        range TEXT
    )""")

    curs.execute("""CREATE TABLE IF NOT EXISTS armor_class(
        id INTEGER PRIMARY KEY,
        armor_type INTEGER,
        armor_class_bonus INTEGER
    )""")


    already_run = '''
    # inserts for ability_score_modifiers table
    curs.execute("""INSERT INTO ability_score_modifiers VALUES(1, NULL, NULL, NULL, NULL)""")
    curs.execute("""INSERT INTO ability_score_modifiers VALUES(2, NULL, NULL, NULL, NULL)""")
    curs.execute("""INSERT INTO ability_score_modifiers VALUES(3, 3, -3, NULL, NULL)""")
    curs.execute("""INSERT INTO ability_score_modifiers VALUES(4, 4, -3, -2, 1)""")
    curs.execute("""INSERT INTO ability_score_modifiers VALUES(5, 5, -2, -2, 1)""")
    curs.execute("""INSERT INTO ability_score_modifiers VALUES(6, 6, -1, -1, 1)""")
    curs.execute("""INSERT INTO ability_score_modifiers VALUES(7, 7, -1, -1, 1)""")
    curs.execute("""INSERT INTO ability_score_modifiers VALUES(8, 8, -1, 0, 2)""")
    curs.execute("""INSERT INTO ability_score_modifiers VALUES(10, 10, 0, 0, 3)""")
    curs.execute("""INSERT INTO ability_score_modifiers VALUES(11, 11, 0, 0, 3)""")
    curs.execute("""INSERT INTO ability_score_modifiers VALUES(12, 12, 0, 0, 4)""")
    curs.execute("""INSERT INTO ability_score_modifiers VALUES(13, 13, 1, 0, 4)""")
    curs.execute("""INSERT INTO ability_score_modifiers VALUES(14, 14, 1, 1, 4)""")
    curs.execute("""INSERT INTO ability_score_modifiers VALUES(15, 15, 1, 1, 5)""")
    curs.execute("""INSERT INTO ability_score_modifiers VALUES(16, 16, 2, 1, 5)""")
    curs.execute("""INSERT INTO ability_score_modifiers VALUES(17, 17, 2, 2, 5)""")
    curs.execute("""INSERT INTO ability_score_modifiers VALUES(18, 18, 3, 2, 5)""")


    # insert into luck_scores table
    ls = """Harsh winter: All attack rolls
The bull: Melee attack rolls
Fortunate date: Missile fire attack rolls
Raised by wolves: Unarmed attack rolls
Conceived on horseback: Mounted attack rolls
Born on the battlefield: Damage rolls
Path of the bear: Melee damage rolls
Hawkeye: Missile fire damage rolls
Pack hunter: Attack and damage rolls for 0-level starting weapon
Born under the loom: Skill checks (including thief skills)
Fox`s cunning: Find/disable traps
Four leafed clover: Find secret doors
Seventh son: spell checks
The raging storm: Spell damage
Righteous heart: Turn unholy checks
Survived the plague: Magical healing
Lucky sign: Saving throws
Guardian angel: Saving throws to escape traps
Survived a spider bite: Saving throws against poison
Struck by lightning: Reflex saving throws
Lived through famine: Fortitude saving throws
Resisted temptation: Willpower saving throws
Charmed house: Armor class
Speed of the cobra: Initiative
Bountiful harvest: Hit points (applies at each level)
Warrior`s arm: Critical hit tables
Unholy house: Corruption rolls
The broken star: Fumbles
Birdsong: Number of languages
Wild child: Speed (each +1/-1 = +5`/-5` speed)"""

    lines = ls.split('\n')
    id = 1
    for line in lines:
        line = line.split(': ')
        print("{}. {} ---- {}".format(id, line[0], line[1]))
        curs.execute("INSERT INTO luck_scores VALUES({}, '{}', '{}')".format(id, line[0], line[1]))
        id += 1

    curs.execute("DROP TABLE racial_traits")


    curs.execute("INSERT INTO race VALUES(1, 'Dwarf', 'Infravision, Underground skills')")
    curs.execute("INSERT INTO race VALUES(2, 'Elf', 'Infravision, Immune to magic sleep/paralysis, heightened senses, iron vulnerability')")
    curs.execute("INSERT INTO race VALUES(3, 'Halfling', 'Infravision, Small size')")
    curs.execute("INSERT INTO race VALUES(4, 'Human', 'None')")


    curs.execute("INSERT INTO armor_class VALUES(1, 'Leather armor', 2)")
    curs.execute("INSERT INTO armor_class VALUES(2, 'Hide armor', 3)")
    curs.execute("INSERT INTO armor_class VALUES(3, 'Shield', 1)")


    curs.execute("INSERT INTO weapon_damage_range VALUES(1, 'dagger', '1d4', '0/0/0')")
    curs.execute("INSERT INTO weapon_damage_range VALUES(2, 'spear', '1d8', '0/0/0')")
    curs.execute("INSERT INTO weapon_damage_range VALUES(3, 'staff', '1d4', '0/0/0')")
    curs.execute("INSERT INTO weapon_damage_range VALUES(4, 'club', '1d4', '0/0/0')")
    curs.execute("INSERT INTO weapon_damage_range VALUES(5, 'axe', '1d6', '10/20/30*')")
    curs.execute("INSERT INTO weapon_damage_range VALUES(6, 'short sword', '1d6', '0/0/0')")
    curs.execute("INSERT INTO weapon_damage_range VALUES(7, 'dart', '1d4', '20/40/60*')")
    curs.execute("INSERT INTO weapon_damage_range VALUES(8, 'shortbow', '1d6', '50/100/150')")
    curs.execute("INSERT INTO weapon_damage_range VALUES(9, 'sling', '1d4', '40/80/160*')")
    curs.execute("INSERT INTO weapon_damage_range VALUES(10, 'longsword', '1d8', '0/0/0')")
    curs.execute("INSERT INTO weapon_damage_range VALUES(11, 'mace', '1d6', '0/0/0')")
    curs.execute("INSERT INTO weapon_damage_range VALUES(12, 'subual', '1d3', '0/0/0')")


    farmers = "Potato, Wheat, Turnip, Corn, Rice, Parsnip, Radish, Rutabaga"
    farmers = farmers.split(', ')
    id = 1
    for type in farmers:
        curs.execute("INSERT INTO farmer_type VALUES({}, '{}')".format(id, type))
        id += 1

    animals = "Hen Sheep Goat Cow Duck Goose Mule"
    animals = animals.split(' ')
    id = 1
    for type in animals:
        curs.execute("INSERT INTO animal_type VALUES({}, '{}')".format(id, type))
        id += 1


    contents = "tomatoes, nothing, straw, your dead, dirt, rocks"
    contents = contents.split(', ')
    id = 1
    for type in contents:
        #print("{}, '{}'".format(id, type))
        curs.execute("INSERT INTO whats_in_the_cart VALUES({}, '{}')".format(id, type))
        id += 1


    things = "Backpack: Candle: Chain 10ft: Chalk 1pc.: Chest, empty: Crowbar: Flask, empty: Flint & steel: Grappling hook: Hammer, small: Holy symbol: Holy water, 1 vial: Iron spike: Lantern: Mirror, hand-sized: Oil, 1 flask: Pole, 10ft: Rations, 1 day: Rope, 50ft: Sack, large: Sack, small: Thieves` tools: Torch 1: Waterskin"
    things = things.split(": ")
    id = 1
    for thing in things:
        #print("{}, '{}'".format(id, thing))
        curs.execute("INSERT INTO equipment VALUES({}, '{}')".format(id, thing))
        id += 1
'''


    conn.commit()



if __name__ == "__main__":
    connection = sqlite3.connect('data_files/dcc.db')
    curs = connection.cursor()
    create_tables(curs, connection)
    curs.close()
    connection.close()
