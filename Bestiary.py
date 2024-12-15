class Bestiary:
    #  This is to easily code in a for loop for a QComboBox later
    enemy_list = []

    def __init__(self, enemyname: str, health: int | str, strength: int | str, defense: int | str, magic: int | str,
                 magicdefense: int | str, gil: int | str, experience: int | str, treasure: str | tuple | None,
                 enemy_type: str | tuple | None, weakness: str | tuple | None, resistance: str | tuple | None,
                 absorb: tuple | str | None):
        self.enemyname = enemyname
        self.health = health
        self.strength = strength
        self.defense = defense
        self.magic = magic
        self.magicdefense = magicdefense
        self.gil = gil
        self.experience = experience
        self.treasure = treasure
        self.enemy_type = enemy_type
        self.weakness = weakness
        self.resistance = resistance
        self.absorb = absorb

        self.enemy_list.append(self)


Goblin: Bestiary = Bestiary("Goblin", 6, 19, 0, 0, 0, 5,
                            28, ("Potion", "Tent", "Hourglass", "Goblin"), None,
                            None, None, None)

Helldiver: Bestiary = Bestiary("Helldiver", 18, 21, 0, 0, 0,
                               5, 40, ("Phoenix Down", "Gold Needle", "Cockatrice"),
                               None, ("Pig", "Mini", "Toad"), None, None)

FloatingEyeball: Bestiary = Bestiary("Floating Eyeball", 20, 20, 0, 0,
                                     0, 9, 42,
                                     ("Eye Drops", "Phoenix Down", "Alarm Clock", "Gold Needle"),
                                     None, "Throw",
                                     ("Pig", "Mini", "Toad", "Berserk", "Sleep", "Paralyze"),
                                     None)

SwordRat: Bestiary = Bestiary("Sword Rat", 30, 21, 0, 0, 11,
                              13, 66, "Gold Needle", None, None,
                              ("Mini", "Toad"), None)

Insectus: Bestiary = Bestiary("Insectus", 28, 20, 1, 0, 4, 8,
                              49,
                              ("Potion", "Hi-Potion"), None, None,
                              ("Pig", "Mini", "Toad"), None)

DesertSahagin: Bestiary = Bestiary("Desert Sahagin", 20, 20, 0, 0, 4,
                                   17, 70,
                                   ("Antidote", "Echo Herbs", "Cross", "Tent"),
                                   "Insect", "Ice", None, None)

FlyingEyes: Bestiary = Bestiary("Flying Eyes", 40, 21, 3, 0, 5,
                                18, 74,
                                ("Eye Drops", "Phoenix Down", "Alarm Clock", "Gold Needle"),
                                None, "Throw", ("Blind", "Pig", "Mini", "Toad"),
                                None)

Hundlegs: Bestiary = Bestiary("Hundlegs", 60, 11, 3, 0, 4,
                              20, 79, ("Potion", "Hi-Potion"), None, None,
                              ("Blind", "Pig", "Mini", "Toad"), None)

SandWorm: Bestiary = Bestiary("Sand Worm", 75, 16, 2, 10, 7,
                              22, 82,
                              ("Potion", "Hi-Potion", "Remedy", "Silver Apple"), None,
                              None, ("Blind", "Pig", "Mini", "Sleep"), None)

RedMousse: Bestiary = Bestiary("Red Mousse", 35, 15, 254, 0, 7,
                               36, 134, ("Potion", "Hi-Potion"),
                               "Pudding", "Fire", "Confuse", None)

Gigantoad: Bestiary = Bestiary("Gigantoad", 47, 11, 2, 0, 6,
                               24, 89, "Maiden's Kiss", "Insect", "Ice",
                               "Toad", None)

Zombie: Bestiary = Bestiary("Zombie", 52, 13, 2, 0, 9, 31,
                            112, None, "Undead", ("Fire", "Holy"),
                            ("Poison", "Pig", "Mini", "Toad", "Death", "Sleep", "Paralyze", "Darkness"),
                            None)

VileShell: Bestiary = Bestiary("Vile Shell", 58, 11, 1, 0, 8,
                               28, 101, ("Diet Food", "Mallet", "Maiden's Kiss", "Remedy"),
                               None, "Lightning", ("Pig", "Mini"), None)

Toadgre: Bestiary = Bestiary("Toadgre", 59, 11, 1, 0, 7, 34,
                             127, "Maiden's Kiss", "Insect", "Ice",
                             "Toad", None)

Sahagin: Bestiary = Bestiary("Sahagin", 64, 18, 2, 0, 7, 38,
                             136, None, "Insect", "Lightning", None,
                             None)

KillerFish: Bestiary = Bestiary("Killer Fish", 65, 11, 1, 0, 7,
                                30, 119, ("Potion", "Hi-Potion"), None,
                                "Lightning", ("Pig", "Mini"), None)

TinyMage: Bestiary = Bestiary("Tiny Mage", 69, 19, 2, 3, 38, 63,
                              132, ("Rod", "Silver Armlet", "Ether", "Dry Ether"),
                              "Mage", None, ("Pig", "Toad"), None)

WaterBug: Bestiary = Bestiary("Water Bug", 125, 16, 3, 0, 11,
                              79, 225, ("Antidote", "Echo Herbs", "Cross", "Tent"),
                              None, "Lightning", None, None)

Alligator: Bestiary = Bestiary("Alligator", 175, 22, 2, 0, 10,
                               95, 236, ("Leather Cap", "Leather Garb", "Hi-Potion",
                                         "Silver Apple"),
                               None, "Ice", ("Pig", "Mini"), None)

BaronSolider: Bestiary = Bestiary("Baron Soldier", 27, 20, 0, 0, 4,
                                  54, 157, None, None, None,
                                  "Confuse", None)

General: Bestiary = Bestiary("General", 221, 26, 2, 0, 12, 80,
                             398, None, None, None, None, None)

Domovoi: Bestiary = Bestiary("Domovoi", 37, 15, 0, 0, 7, 48,
                             184, None, None, None, None, None)

YellowJelly: Bestiary = Bestiary("Yellow Jelly", 55, 16, 254, 0, 12,
                                 33, 144, ("Potion", "Hi-Potion"), "Pudding",
                                 "Lightning", "Confuse", None)

Basilisk: Bestiary = Bestiary("Basilisk", 90, 15, 2, 0, 9, 30,
                              110, "Gold Needle", "Insect", None,
                              ("Pig", "Mini"), None)

Leshy: Bestiary = Bestiary("Leshy", 130, 18, 2, 144, 10, 42,
                           157, None, "Ghoul", None, None, None)

Adamantoise: Bestiary = Bestiary("Adamantoise", 190, 20, 1, 0, 10,
                                 46, 234, ("Antidote", "Echo Herbs", "Cross", "Tent"),
                                 "Insect", "Ice", ("Pig", "Mini"), None)

Bomb: Bestiary = Bestiary("Bomb", 55, 19, 2, 0, 15, 76,
                          361, None, None, None,
                          ("Poison", "Pig", "Mini", "Toad"), None)

Spirit: Bestiary = Bestiary("Spirit", 86, 24, 1, 6, 9, 122,
                            278, ("Potion", "Cursed Ring"), "Ghoul",
                            "Holy",
                            ("Poison", "Blind", "Petrify", "Death", "Paralyze", "Slowing Petrify"),
                            "Fire")

GrayBomb: Bestiary = Bestiary("Gray Bomb", 111, 36, 4, 0, 25,
                              105, 445, None, None, None,
                              ("Poison", "Pig", "Mini", "Toad"), None)

Skeleton: Bestiary = Bestiary("Skeleton", 135, 26, 2, 0, 8, 126,
                              238, None, "Undead", ("Fire", "Holy"),
                              ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Berserk", "Confuse",
                               "Sleep", "Paralyze", "Curse", "Darkness"),
                              None)

Cockatrice: Bestiary = Bestiary("Cockatrice", 149, 24, 1, 0, 11,
                                82, 275, ("Phoenix Down", "Gold Needle", "Cockatrice"),
                                None, "Throw", ("Pig", "Mini", "Toad"), None)

Gargoyle: Bestiary = Bestiary("Gargoyle", 160, 28, 2, 0, 12,
                              90, 315, None, "Insect",
                              ("Holy", "Throw"), ("Pig", "Mini", "Death"), None)

Bloodbones: Bestiary = Bestiary("Bloodbones", 210, 34, 3, 0, 12,
                                169, 315, None, "Undead", ("Fire", "Holy"),
                                ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Berserk", "Confuse",
                                 "Sleep", "Paralyze", "Curse", "Darkness"),
                                None)

Gatlinger: Bestiary = Bestiary("Gatlinger", 115, 28, 2, 0, 8,
                               53, 335, "Gold Needle", None,
                               None, ("Mini", "Toad"), None)

BaronWarrior: Bestiary = Bestiary("Baron Warrior", 65, 28, 2, 0, 4,
                                  100, 400, None, None, None,
                                  ("Confuse", "Darkness", "Holy"), None)

Captain: Bestiary = Bestiary("Captain", 320, 36, 2, 0, 11,
                             152, 600, None, None, None, None,
                             None)

Zu: Bestiary = Bestiary("Zu", 941, 32, 0, 0, 0, 489,
                        432,
                        ("Feathered Cap", "Hi-Potion", "Cottage", "Silver Apple"), None,
                        "Throw", ("Pig", "Mini", "Toad"), None)

Soul: Bestiary = Bestiary("Soul", 200, 28, 3, 0, 10, 165,
                          460, ("Potion", "Cursed Ring"), "Ghoul",
                          "Holy",
                          ("Poison", "Blind", "Petrify", "Death", "Sleep", "Paralyze", "Slowing Petrify"),
                          "Fire")

Ghoul: Bestiary = Bestiary("Ghoul", 222, 32, 3, 0, 11, 179,
                           505, None, "Undead", ("Fire", "Holy"),
                           ("Poison", "Pig", "Mini", "Toad", "Death", "Sleep", "Paralyze", "Darkness"),
                           None)

Revenant: Bestiary = Bestiary("Revenant", 250, 36, 1, 0, 12,
                              186, 575, None, "Undead", ("Fire", "Holy"),
                              ("Poison", "Pig", "Mini", "Toad", "Death", "Sleep", "Paralyze", "Darkness"),
                              None)

Lilith: Bestiary = Bestiary("Lilith", 466, 46, 3, 0, 13,
                            262, 2703, ("Kiss of Lilith", "Silver Apple", "Rod of Lilith"),
                            ("Insect", "Undead"), "Fire",
                            ("Death", "Sleep", "Paralyze"), None)

Skullnant: Bestiary = Bestiary("Skullnant", 200, 42, 1, 0, 5,
                               100, 50, None, "Undead", ("Fire", "Holy"),
                               ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Death", "Berserk",
                                "Confuse", "Sleep", "Paralyze", "Curse", "Darkness", "Slowing Petrify"),
                               None)

Splasher: Bestiary = Bestiary("Splasher", 180, 30, 3, 0, 10,
                              145, 430, ("Potion", "Hi-Potion"), None,
                              "Lightning", ("Pig", "Mini", "Toad"), None)

Hydra: Bestiary = Bestiary("Hydra", 257, 44, 2, 0, 14, 209,
                           670, ("Antidote", "Unicorn Horn", "Poison Arrow"), "Insect",
                           "Lightning", ("Pig", "Mini"), None)

BaronGuard: Bestiary = Bestiary("Baron Guard", 280, 40, 3, 26, 14,
                                230, 710, None, "Mage", None, None,
                                None)

Electrofish: Bestiary = Bestiary("Electrofish", 284, 40, 2, 0, 13,
                                 214, 640, ("Diet Food", "Mallet", "Maiden's Kiss", "Remedy"),
                                 None, "Throw", ("Pig", "Mini"), "Lightning")

GigasGator: Bestiary = Bestiary("Gigas Gator", 292, 38, 2, 0, 15,
                                218, 660,
                                ("Leather Cap", "Leather Garb", "Hi-Potion", "Silver Apple"), None,
                                "Ice", ("Pig", "Mini"), None)

DeathShell: Bestiary = Bestiary("Death Shell", 380, 42, 2, 0, 19,
                                262, 1030, ("Diet Food", "Mallet", "Maiden's Kiss", "Remedy"),
                                None, "Lightning", ("Pig", "Mini"), None)

FloodWorm: Bestiary = Bestiary("Flood Worm", 638, 42, 0, 0, 22,
                               219, 690, ("Potion", "Hi-Potion", "Remedy", "Silver Apple"),
                               None, "Lightning",
                               ("Blind", "Pig", "Mini", "Sleep"), None)

TwinSnake: Bestiary = Bestiary("Twin Snake", 108, 46, 0, 0, 22,
                               222, 720, ("Antidote", "Unicorn Horn", "Poison Arrow"),
                               None, ("Ice", "Holy"), ("Pig", "Mini"), None)

Treant: Bestiary = Bestiary("Treant", 335, 52, 1, 2, 15, 148,
                            687, ("Diet Food", "Mallet", "Maiden's Kiss", "Remedy"), None,
                            "Fire", ("Pig", "Mini", "Toad"), None)

CaitSith: Bestiary = Bestiary("Cait Sith", 342, 50, 2, 0, 16,
                              252, 820, ("Unicorn Horn", "Couerl's Whisker", "Cat Claw"),
                              None, "Holy", ("Mini", "Toad"), None)

HellNeedle: Bestiary = Bestiary("Hell Needle", 398, 40, 3, 0, 12,
                                220, 700, "Gold Needle", None, None,
                                ("Mini", "Toad"), None)

DeathFlower: Bestiary = Bestiary("Death Flower", 440, 24, 2, 0, 17,
                                 210, 650, ("Diet Food", "Mallet", "Maiden's Kiss", "Remedy"),
                                 None, "Fire", ("Blind", "Pig", "Mini", "Toad"),
                                 None)

Draculady: Bestiary = Bestiary("Draculady", 270, 38, 2, 21, 15,
                               195, 810, ("Vampire Fang", "Kiss of Lilith"), "Undead",
                               ("Fire", "Holy"), "Death", "Lightning")

CaveNaga: Bestiary = Bestiary("Cave Naga", 285, 40, 3, 5, 12,
                              201, 740, ("Antidote", "Unicorn Horn", "Poison Arrow"),
                              "Insect", "Holy", None, None)

MindFlayer: Bestiary = Bestiary("Mind Flayer", 300, 44, 3, 0, 22,
                                232, 1000,
                                ("Hi-Potion", "Unicorn Horn", "Gold Hourglass", "Mind Flayer"), None,
                                None, ("Poison", "Death", "Paralyze"), None)

CaveBat: Bestiary = Bestiary("Cave Bat", 334, 42, 3, 0, 12, 151,
                             598, ("Potion", "Hi-Potion"), None, ("Holy", "Throw"),
                             ("Pig", "Mini", "Toad"), "Lightning")

Ogre: Bestiary = Bestiary("Ogre", 865, 60, 2, 0, 12, 240,
                          800, ("Bacchus's Cider", "Twist Headband", "Power Armlet", "Giant's Gloves"),
                          "Giant", "Holy", ("Pig", "Toad"), None)

PurpleBavarois: Bestiary = Bestiary("Purple Bavarois", 105, 52, 254, 0,
                                    9, 50, 750, ("Potion", "Hi-Potion"),
                                    "Pudding", "Fire", "Confuse", None)

Puppet: Bestiary = Bestiary("Puppet", 256, 56, 3, 15, 16,
                            180, 800, "Decoy", None, "Fire", None,
                            None)

Sorceress: Bestiary = Bestiary("Sorceress", 350, 50, 2, 47, 12,
                               329, 1551, ("Rod", "Silver Armlet", "Ether", "Dry Ether"),
                               "Mage", None, "Toad", None)

BlackKnight: Bestiary = Bestiary("Black Knight", 360, 64, 2, 0, 19,
                                 175, 840, ("Tent", "Cottage"), "Undead",
                                 ("Fire", "Holy"), ("Death", "Darkness"), None)

CentaurKnight: Bestiary = Bestiary("Centaur Knight", 380, 58, 2, 0,
                                   18, 172, 860, ("Tent", "Cottage"), None,
                                   None, ("Pig", "Toad"), None)

Gremlin: Bestiary = Bestiary("Gremlin", 410, 56, 3, 31, 15, 275,
                             1221, ("Bell of Silence", "Unicorn Horn", "Hourglass", "Ether"),
                             "Mage", "Fire", None, None)

Soldieress: Bestiary = Bestiary("Soldieress", 425, 60, 3, 0, 15,
                                200, 1050, ("Tent", "Cottage"), None, None,
                                ("Pig", "Toad"), None)

Puppeteer: Bestiary = Bestiary("Puppeteer", 473, 56, 3, 35, 17,
                               195, 1000,
                               ("Healing Staff", "Rune Armlet", "Rune Staff", "Grimoire"), "Mage",
                               None, ("Pig", "Toad"), None)

IceLizard: Bestiary = Bestiary("Ice Lizard", 480, 62, 2, 2, 14,
                               289, 1331, ("Ice Arrow", "Antarctic Wind", "Arctic Wind",
                                           "White Fang"), "Insect", "Fire",
                               ("Pig", "Mini"), "Ice")

ColdBeast: Bestiary = Bestiary("Cold Beast", 520, 64, 3, 3, 13,
                               276, 1441, ("Ice Arrow", "Antarctic Wind", "Arctic Wind",
                                           "White Fang"), None, "Fire", ("Mini", "Toad"),
                               "Ice")

HellTurtle: Bestiary = Bestiary("Hell Turtle", 700, 72, 4, 0, 14,
                                224, 920,
                                ("Mythril Shield", "Mythril Hammer", "Hi-Potion", "X-Potion"),
                                "Insect", "Ice", ("Pig", "Mini"), "Fire")

RocBaby: Bestiary = Bestiary("Roc Baby", 50, 60, 2, 0, 9, 81,
                             1004, ("Phoenix Down", "Gold Needle", "Cockatrice"), None,
                             "Throw", ("Pig", "Mini", "Toad"), None)

BloodFlower: Bestiary = Bestiary("Blood Flower", 370, 62, 2, 0, 6,
                                 32, 1204, ("Diet Food", "Mallet", "Maiden's Kiss", "Remedy"),
                                 None, "Fire", ("Blind", "Pig", "Mini", "Toad"),
                                 None)

Roc: Bestiary = Bestiary("Roc", 500, 66, 3, 0, 18, 150,
                         1404, ("Feathered Cap", "Hi-Potion", "Cottage", "Silver Apple"),
                         None, "Throw", ("Pig", "Mini", "Toad"), None)

Mors: Bestiary = Bestiary("Mors", 695, 60, 4, 0, 22,
                          253, 1504, ("Potion", "Hi-Potion"), None,
                          None, None, None)

SteelGolem: Bestiary = Bestiary("Steel Golem", 1950, 86, 4, 0, 21,
                                445, 703, ("Gaia Hammer", "Giant's Gloves"), "Giant",
                                "Ice", ("Poison", "Blind", "Silence", "Mini", "Toad", "Death"),
                                None)

GoblinCaptain: Bestiary = Bestiary("Goblin Captain", 199, 56, 0, 0,
                                   0, 45, 1930, None, None,
                                   None, None, None)

Armadillo: Bestiary = Bestiary("Armadillo", 325, 58, 4, 0, 12,
                               194, 1555,
                               ("Mythril Shield", "Mythril Hammer", "Hi-Potion", "X-Potion"),
                               None, None, ("Mini", "Toad"), None)

MagmaTortoise: Bestiary = Bestiary("Magma Tortoise", 435, 70, 3, 0,
                                   17, 234, 1666,
                                   ("Mythril Shield", "Mythril Hammer", "Hi-Potion", "X-Potion"),
                                   "Insect", "Ice", ("Pig", "Mini"), None)

Undergrounder: Bestiary = Bestiary("Undergrounder", 655, 76, 5, 3,
                                   29, 342, 2714,
                                   ("Spider's Silk", "Gaia Drum", "Siren"), None, None,
                                   ("Blind", "Pig", "Mini", "Toad"), None)

HellFlapper: Bestiary = Bestiary("Hell Flapper", 900, 74, 4, 0, 18,
                                 312, 3114,
                                 ("Eye Drops", "Phoenix Down", "Alarm Clock", "Gold Needle"), None,
                                 "Throw", ("Blind", "Pig", "Mini", "Toad"), None)

Chrysalis: Bestiary = Bestiary("Chrysalis", 986, 72, 3, 0, 17,
                               39, 2822, ("Potion", "Hi-Potion"), None, None,
                               ("Pig", "Mini", "Toad"), None)

Gloomwing: Bestiary = Bestiary("Gloomwing", 1580, 100, 4, 0, 254,
                               510, 2837,
                               ("Ether", "Stardust", "Lunar Curtain", "Artemis Arrow"),
                               None, "Throw", None, None)

Gorgon: Bestiary = Bestiary("Gorgon", 2550, 134, 4, 0, 40,
                            248, 3003, ("Medusa Arrow", "Gorgon Blade"), None,
                            None, None, None)

# Mystery Egg is labeled as a question mark across the board because
# it spawns a random enemy and uses their stats.

MysteryEgg: Bestiary = Bestiary("Mystery Egg", "?", "?", "?", "?",
                                "?", "?", "?", "?", "?", "?",
                                "?", "?")

Ironback: Bestiary = Bestiary("Ironback", 100, 74, 4, 0, 15,
                              233, 1077,
                              ("Mythril Shield", "Mythril Hammer", "Hi-Potion", "X-Potion"), None,
                              None, ("Mini", "Toad"), None)

WhiteMousse: Bestiary = Bestiary("White Mousse", 298, 66, 254, 0,
                                 12, 384, 1808, ("Potion", "Hi-Potion"),
                                 "Pudding", "Ice", "Confuse", None)

Naga: Bestiary = Bestiary("Naga", 320, 66, 4, 5, 14, 150,
                          1118, ("Antidote", "Unicorn Horn", "Poison Arrow"), "Insect",
                          None, None, None)

EvilDoll: Bestiary = Bestiary("Evil Doll", 388, 64, 3, 0, 13,
                              269, 1408, "Decoy", None, None, None,
                              None)

Medusa: Bestiary = Bestiary("Medusa", 490, 64, 4, 0, 14, 225,
                            1208, ("Medusa Arrow", "Gorgon Blade"), None,
                            None, None, None)

FieryKnight: Bestiary = Bestiary("Fiery Knight", 579, 76, 4, 0, 19,
                                 300, 1708,
                                 ("Fire Lance", "Flame Sword", "Fire Shield", "Flame Mail"), None,
                                 "Ice", None, "Fire")

Coeurl: Bestiary = Bestiary("Coeurl", 593, 72, 3, 0, 17,
                            345, 2759,
                            ("Unicorn Horn", "Coeurl's Whisker", "Cat Claw"), None,
                            None, ("Mini", "Toad"), None)

Balloon: Bestiary = Bestiary("Balloon", 697, 72, 4, 0, 19,
                             315, 2459,
                             ("Bomb Fragment", "Antarctic Wind", "Bomb Core", "Bomb"),
                             None, "Throw", ("Poison", "Pig", "Mini", "Toad"),
                             None)

Chimera: Bestiary = Bestiary("Chimera", 700, 80, 3, 0, 18,
                             228, 1708,
                             ("Fire Arrow", "Bomb Fragment", "Bomb Arm", "Red Fang"), None,
                             None, ("Pig", "Mini", "Toad", "Death", "Sleep", "Paralyze"),
                             ("Fire", "Ice", "Lightning"))

BlackLizard: Bestiary = Bestiary("Black Lizard", 792, 64, 4, 16, 15,
                                 43, 1298, ("Medusa Arrow", "Gorgon Blade"), "Insect",
                                 "Ice", ("Pig", "Mini"), None)

Sorcerer: Bestiary = Bestiary("Sorcerer", 1000, 82, 4, 50, 22,
                              272, 2359,
                              ("Healing Staff", "Rune Armlet", "Rune Staff", "Grimoire"),
                              "Mage", None, ("Pig", "Toad"), None)

GhostKnight: Bestiary = Bestiary("Ghost Knight", 1050, 76, 4, 0, 19,
                                 211, 2559, ("Tent", "Cottage"), "Ghoul",
                                 "Holy", None, None)

LamiaMatriarch: Bestiary = Bestiary("Lamia Matriarch", 1100, 74, 4, 0,
                                    31, 247, 2859,
                                    ("Lamia Harp", "Ruby Ring", "Light Curtain", "Angel Arrow"),
                                    "Insect", None, ("Sleep", "Paralyze"), None)

Lamia: Bestiary = Bestiary("Lamia", 1200, 72, 4, 0, 16, 143,
                           2059, ("Lamia Harp", "Ruby Ring", "Light Curtain", "Angel Arrow"),
                           "Insect", None, ("Sleep", "Paralyze"), None)

Grudger: Bestiary = Bestiary("Grudger", 1400, 76, 4, 0, 22,
                             149, 2459,
                             ("Thunder Arrow", "Rage of Zeus", "Rage of the Gods", "Blue Fang"),
                             None, "Holy", None, "Lightning")

FieryHound: Bestiary = Bestiary("Fiery Hound", 1221, 68, 3, 0, 22,
                                244, 1708,
                                ("Fire Arrow", "Bomb Fragment", "Bomb Arm", "Red Fang"),
                                None, "Ice", ("Mini", "Toad"), "Fire")

SecurityEye: Bestiary = Bestiary("Security Eye", 1425, 112, 0, 0,
                                 254, 380, 2008, "Siren", "Mech",
                                 None,
                                 ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify", "Death",
                                  "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                 None)
MadOgre: Bestiary = Bestiary("Mad Ogre", 2000, 86, 4, 53, 254,
                             270, 2359,
                             ("Bacchus's Cider", "Twist Headband", "Power Armlet", "Giant's Gloves"),
                             ("Giant", "Mage"), None, ("Pig", "Toad"), None)

GreenDragon: Bestiary = Bestiary("Green Dragon", 2200, 88, 3, 3, 18,
                                 368, 4759, ("Blue Fang", "Siren", "Silver Apple"),
                                 "Dragon", None, ("Pig", "Mini", "Toad", "Sleep"),
                                 None)

StoneGolem: Bestiary = Bestiary("Stone Golem", 2560, 84, 4, 0, 254,
                                238, 2908, ("Hi-Potion", "X-Potion", "Medusa Arrow"),
                                "Giant", "Ice",
                                ("Poison", "Blind", "Silence", "Mini", "Toad", "Petrify", "Death"),
                                None)

MythrilGolem: Bestiary = Bestiary("Mythril Golem", 2900, 92, 3, 0,
                                  20, 383, 3659,
                                  ("Mythril Knife", "Mythril Shield", "Mythril Armor", "Mythril Sword"),
                                  "Giant", None,
                                  ("Poison", "Blind", "Silence", "Mini", "Toad", "Death"),
                                  None)

BloodyBat: Bestiary = Bestiary("Bloody Bat", 439, 56, 3, 0, 16,
                               262, 1977, ("Potion", "Hi-Potion"), None,
                               ("Fire", "Throw"), ("Pig", "Mini", "Toad"), "Lightning")

Skuldier: Bestiary = Bestiary("Skuldier", 740, 74, 3, 0, 18,
                              116, 1577, None, "Undead",
                              ("Fire", "Holy"),
                              ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Death",
                               "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Darkness"), None)

TinyToad: Bestiary = Bestiary("Tiny Toad", 600, 19, 5, 47, 37,
                              335, 1841, "Maiden's Kiss", ("Insect", "Mage"),
                              "Ice", ("Pig", "Mini", "Toad"), None)

BogWitch: Bestiary = Bestiary("Bog Witch", 2960, 98, 4, 223, 0,
                              598, 3441, ("Maiden's Kiss", "Dry Ether", "Soma Drop", "Ribbon"),
                              "Mage", None, ("Pig", "Mini", "Sleep", "Paralyze"),
                              None)

EvilDreamer: Bestiary = Bestiary("Evil Dreamer", 2800, 100, 3, 11,
                                 23, 362, 3141, ("Potion", "Cursed Ring"),
                                 None, None,
                                 ("Poison", "Blind", "Petrify", "Death", "Sleep", "Paralyze",
                                  "Slowing Petrify"), "Fire")

Mammon: Bestiary = Bestiary("Mammon", 3900, 104, 3, 74, 38,
                            525, 5041, ("Diet Food", "Mallet", "Maiden's Kiss", "Remedy"),
                            "Mage", "Fire", ("Pig", "Mini", "Toad"), None)

Malboro: Bestiary = Bestiary("Malboro", 4200, 112, 3, 0, 23,
                             458, 5641,
                             ("Remedy", "Bacchus's Cider", "Yoichi Arrow", "Soma Drop"), None,
                             None, ("Pig", "Mini", "Death"), None)

Belphegor: Bestiary = Bestiary("Belphegor", 2200, 108, 5, 0, 12,
                               484, 4088, ("Potion", "Cursed Ring"), "Ghoul",
                               ("Holy", "Throw"), ("Pig", "Mini", "Death"), None)

BloodyEye: Bestiary = Bestiary("Bloody Eye", 2400, 100, 4, 0, 38,
                               465, 3444,
                               ("Eye Drops", "Phoenix Down", "Alarm Clock", "Gold Needle"),
                               None, "Throw",
                               ("Pig", "Mini", "Toad", "Berserk", "Sleep", "Paralyze"), None)

Warrior: Bestiary = Bestiary("Warrior", 2900, 104, 4, 0, 26,
                             575, 4288, ("Tent", "Cottage"), None,
                             None, None, None)

MiniSatana: Bestiary = Bestiary("Mini Satana", 3480, 102, 5, 79, 43,
                                650, 6388,
                                ("Bell of Silence", "Unicorn Horn", "Hourglass", "Ether"),
                                "Mage", None, None, None)

Summoner: Bestiary = Bestiary("Summoner", 3600, 104, 5, 60, 39,
                              475, 3688,
                              ("Healing Staff", "Rune Armlet", "Rune Staff", "Grimoire"),
                              "Mage", None, ("Pig", "Toad"), None)

Arachne: Bestiary = Bestiary("Arachne", 3650, 102, 3, 10, 18,
                             585, 4388, ("Spider's Silk", "Gaia Drum", "Siren"),
                             None, ("Ice", "Throw"), None, None)

ThunderDragon: Bestiary = Bestiary("Thunder Dragon", 7600, 124, 4, 0,
                                   254, 900, 7777,
                                   ("Rage of the Gods", "Gold Hourglass", "Gold Hairpin", "Golden Apple"),
                                   "Dragon", "Throw",
                                   ("Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                    "Death", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                   "Lightning")

EvilBat: Bestiary = Bestiary("Evil Bat", 1014, 94, 3, 0, 25,
                             355, 2306, ("Potion", "Hi-Potion"), None,
                             ("Fire", "Throw"), ("Pig", "Mini", "Toad"), "Lightning")

Screamer: Bestiary = Bestiary("Screamer", 1400, 90, 4, 0, 22,
                              205, 3082,
                              ("Thunder Arrow", "Rage of Zeus", "Rage of the Gods", "Blue Fang"),
                              ("Mech", "Giant"), None, None, None)

KingNaga: Bestiary = Bestiary("King Naga", 1480, 88, 3, 0, 26,
                              238, 3582, ("Antidote", "Unicorn Horn", "Poison Arrow"),
                              "Insect", None, None, None)

MissVamp: Bestiary = Bestiary("Miss Vamp", 2375, 88, 4, 31, 24,
                              188, 3582, ("Vampire Fang", "Kiss of Lilith"),
                              ("Mage", "Undead"), ("Fire", "Holy"), None, None)

YellowDragon: Bestiary = Bestiary("Yellow Dragon", 3100, 108, 4, 0,
                                  37, 1500, 28000,
                                  ("Blue Fang", "Siren", "Silver Apple"), "Dragon",
                                  None, ("Pig", "Mini", "Toad", "Sleep"), "Lightning")

ChimeraBrain: Bestiary = Bestiary("Chimera Brain", 3400, 114, 3, 0,
                                  38, 1200, 28000,
                                  ("Fire Arrow", "Bomb Fragment", "Bomb Arm", "Red Fang"),
                                  None, None,
                                  ("Pig", "Mini", "Toad", "Death", "Sleep", "Paralyze"),
                                  ("Fire", "Ice", "Lightning"))

TrapDoor: Bestiary = Bestiary("Trap Door", 5000, 88, 3, 0, 38,
                              4500, 30000, None, None, None,
                              ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                               "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                              None)

LunarVirus: Bestiary = Bestiary("Lunar Virus", 980, 102, 5, 0, 43,
                                1100, 3237,
                                ("Ether", "Stardust", "Lunar Curtain", "Artemis Arrow"), None,
                                None, ("Pig", "Mini", "Toad"), None)

Eukaryote: Bestiary = Bestiary("Eukaryote", 1700, 116, 5, 0, 44,
                               1560, 6999, ("Stardust", "Lunar Curtain"), None,
                               None,
                               ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                               None)

Crawler: Bestiary = Bestiary("Crawler", 1855, 100, 4, 0, 24,
                             538, 3437, ("Potion", "Hi-Potion"), None,
                             None, ("Pig", "Mini", "Toad"), None)

Prokaryote: Bestiary = Bestiary("Prokaryote", 2600, 120, 5, 0, 54,
                                1850, 7999, ("Stardust", "Lunar Curtain"), None,
                                None,
                                ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                 "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                None)

AbyssWorm: Bestiary = Bestiary("Abyss Worm", 7000, 128, 4, 15, 54,
                               310, 6303, ("Arctic Wind", "Ether"), None,
                               "Fire", ("Blind", "Pig", "Mini", "Sleep"), None)

BlackFlan: Bestiary = Bestiary("Black Flan", 1357, 116, 254, 0, 0,
                               1300, 3044, ("Ether", "Stardust", "Lunar Curtain", "Artemis Arrow"),
                               "Pudding", None, "Confuse", None)

DarkGrenade: Bestiary = Bestiary("Dark Grenade", 1820, 108, 4, 0, 37,
                                 630, 2644,
                                 ("Bomb Fragment", "Antarctic Wind", "Bomb Core", "Bomb"), None,
                                 "Throw", ("Poison", "Pig", "Mini", "Toad"), None)

Tarantula: Bestiary = Bestiary("Tarantula", 2315, 110, 5, 5, 37,
                               598, 2744, ("Spider's Silk", "Gaia Drum", "Siren"),
                               None, "Throw", None, None)

Beamer: Bestiary = Bestiary("Beamer", 3000, 88, 4, 0, 41,
                            890, 3199, ("Tent", "Rage of the Gods"), "Mech",
                            None,
                            ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                             "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                            None)

Centaurion: Bestiary = Bestiary("Centaurion", 3500, 126, 5, 0, 43,
                                1220, 9699, ("Tent", "Cottage"), "Mech",
                                None, ("Pig", "Mini", "Toad"), None)

MechSoldier: Bestiary = Bestiary("Mech Soldier", 4900, 118, 3, 0,
                                 40, 985, 7999,
                                 ("Thunder Arrow", "Rage of Zeus", "Rage of the Gods", "Blue Fang"),
                                 "Mech", None,
                                 ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                  "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                 None)

Searcher: Bestiary = Bestiary("Searcher", 5500, 138, 4, 0, 52,
                              900, 15004, "Siren", "Mech", None,
                              ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                               "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                              None)

LastArm: Bestiary = Bestiary("Last Arm", 9500, 128, 5, 0, 47,
                             338, 8703, "Siren", "Mech", None,
                             ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                              "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                             None)

GiantSoldier: Bestiary = Bestiary("Giant Soldier", 10000, 128, 4, 0,
                                  38, 1500, 31000,
                                  ("Cottage", "Ogrekiller", "Poison Axe", "Rune Axe"),
                                  ("Mech", "Giant"), None,
                                  ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                   "Death", "Confuse", "Sleep", "Paralyze"), None)

MechDragon: Bestiary = Bestiary("Mech Dragon", 18000, 138, 4, 56,
                                38, 2550, 41400,
                                ("Rage of the Gods", "Gold Hourglass", "Gold Hairpin", "Golden Apple"),
                                "Dragon", None,
                                ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                 "Death", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"), None)

GreatMalboro: Bestiary = Bestiary("Great Malboro", 12180, 132, 3, 20,
                                  254, 20000, 22000,
                                  ("Remedy", "Bacchus's Cider", "Soma Drop", "Megalixir"), None,
                                  None, ("Pig", "Mini", "Death"), None)

GoldenToad: Bestiary = Bestiary("Golden Toad", 7777, 136, 254, 112,
                                254, 65000, 65000,
                                ("Gold Hourglass", "Golden Apple", "Megalixir"), "Insect",
                                None,
                                ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                 "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                ("Fire", "Ice", "Lightning", "Darkness", "Holy", "Throw"))

SeleneGuardian: Bestiary = Bestiary("Selene Guardian", 4000, 122, 3, 0,
                                    254, 3500, 13000,
                                    ("Artemis Arrow", "Lunar Curtain", "Minerva's Plate", "Artemis's Bow"),
                                    None, None, ("Pig", "Toad"), None)

DarkSage: Bestiary = Bestiary("Dark Sage", 5100, 80, 5, 47, 41,
                              2400, 17003, ("Maiden's Kiss", "Dry Ether", "Soma Drop", "Ribbon"),
                              "Mage", None, "Toad", None)

SilverDragon: Bestiary = Bestiary("Silver Dragon", 7500, 124, 4, 95,
                                  44, 19000, 25000,
                                  ("Stardust", "Light Curtain", "Lunar Curtain", "Silver Apple"),
                                  "Dragon", None,
                                  ("Blind", "Silence", "Pig", "Toad", "Petrify", "Death", "Paralyze",
                                   "Curse", "Slowing Petrify"),
                                  None)

GoldDragon: Bestiary = Bestiary("Gold Dragon", 8200, 128, 54, 30,
                                39, 23000, 30000,
                                ("Rage of Zeus", "Rage of the Gods", "Blue Fang", "Silver Apple"),
                                "Dragon", None,
                                ("Blind", "Silence", "Pig", "Mini", "Toad", "Petrify", "Death",
                                 "Confuse", "Paralyze", "Curse", "Slowing Petrify"),
                                None)

BoneDragon: Bestiary = Bestiary("Bone Dragon", 12000, 142, 3, 0,
                                254, 6750, 14000, ("Red Fang", "Cursed Ring"),
                                ("Dragon", "Undead"), "Fire",
                                ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Death", "Berserk",
                                 "Sleep", "Paralyze", "Curse", "Darkness"),
                                None)

Dinozombie: Bestiary = Bestiary("Dinozombie", 12000, 132, 4, 0, 254,
                                8100, 15000, ("Red Fang", "Cursed Ring"),
                                ("Dragon", "Undead"), ("Fire", "Holy"),
                                ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Death", "Berserk",
                                 "Sleep", "Paralyze", "Curse", "Darkness"), None)

LilMurderer: Bestiary = Bestiary("Li'l Murderer", 12000, 174, 3, 143,
                                 0, 10700, 20000,
                                 ("Potion", "Tent", "Hourglass", "Goblin"), None,
                                 "Lightning", None, None)

GiantWarrior: Bestiary = Bestiary("Giant Warrior", 14000, 122, 4, 57,
                                  39, 7000, 18500,
                                  ("Cottage", "Ogrekiller", "Poison Axe", "Rune Axe"), "Giant",
                                  None,
                                  ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                   "Death", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                  None)

BlueDragon: Bestiary = Bestiary("Blue Dragon", 15000, 144, 4, 0, 47,
                                40200, 36000,
                                ("White Fang", "Shuriken", "Dragon's Whisker", "Wyvern Lance"),
                                "Dragon", None,
                                ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                 "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                ("Fire", "Ice", "Lightning", "Darkness", "Holy", "Throw"))

RedDragon: Bestiary = Bestiary("Red Dragon", 15000, 162, 4, 79, 39,
                               65000, 41500,
                               ("Red Fang", "Dragon Gloves", "Wyvern Lance", "Crystal Ring"),
                               "Dragon", "Ice",
                               ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                               "Fire")

Ahriman: Bestiary = Bestiary("Ahriman", 25000, 144, 5, 0, 38,
                             65200, 33333,
                             ("Eye Drops", "Elixir", "Gold Hourglass", "Protect Ring"), None,
                             "Throw",
                             ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                              "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                             None)

Behemoth: Bestiary = Bestiary("Behemoth", 23000, 154, 4, 63, 254,
                              65000, 57000,
                              ("Twist Headband", "Power Armlet", "Power Sash", "Avenger"), None,
                              None,
                              ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                               "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                              None)

WickedMask: Bestiary = Bestiary("Wicked Mask", 37000, 128, 4, 18,
                                19, 65000, 50000,
                                ("Light Curtain", "X-Potion", "Elixir", "Glass Mask"), "Mech",
                                None,
                                ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                 "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                None)

ZemusMind: Bestiary = Bestiary("Zemus's Mind", 20000, 130, 254, 99,
                               0, 50000, 65000, None, None, None,
                               ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                               None)

ZemusBreath: Bestiary = Bestiary("Zemus's Breath", 40000, 154, 0, 99,
                                 254, 50000, 60000, None, None,
                                 None,
                                 ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                  "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                 None)

FlanPrincess: Bestiary = Bestiary("Flan Princess", 20000, 154, 5, 127,
                                  22, 55555, 10000,
                                  ("Dry Ether", "Elixir", "Fuma Shuriken", "Pink Tail"), "Pudding",
                                  None,
                                  ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                   "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                  None)

GoblinPrince: Bestiary = Bestiary("Goblin Prince", 8929, 132, 3, 0,
                                  1, 12000, 22000,
                                  ("X-Potion", "Gold Hourglass", "Goblin"), None,
                                  "Lightning", ("Pig", "Mini", "Toad"), None)

Echidna: Bestiary = Bestiary("Echidna", 9130, 142, 4, 28, 33,
                             24000, 34000,
                             ("X-Potion", "Vampire Fang", "Kiss of Lilith", "Assassin Vest"),
                             ("Insect", "Undead"), None, ("Pig", "Mini", "Toad"),
                             None)

LamiaQueen: Bestiary = Bestiary("Lamia Queen", 10330, 144, 3, 35,
                                32, 25000, 35000,
                                ("Dry Ether", "Kiss of Lilith", "Rod of Lilith", "Perseus Arrow"),
                                "Insect", None,
                                ("Pig", "Mini", "Toad", "Sleep", "Paralyze"), None)

SahaginPrince: Bestiary = Bestiary("Sahagin Prince", 12902, 160, 4, 20,
                                   26, 28000, 40000,
                                   ("X-Potion", "Cottage", "Bestiary", "Battle Gear"), "Insect",
                                   "Lightning", "Ice", None)

KingBomb: Bestiary = Bestiary("King Bomb", 11100, 154, 2, 27,
                              34, 32000, 40000,
                              ("Bomb Fragment", "Bomb Arm", "Bomb Core", "Bomb"), None,
                              None, ("Poison", "Pig", "Mini", "Toad"), "Fire")

PalaceGuard: Bestiary = Bestiary("Palace Guard", 10633, 151, 4, 38,
                                 44, 28000, 38000,
                                 ("X-Potion", "Fuma Shuriken", "Minerva's Plate", "Golden Apple"),
                                 None, None, ("Pig", "Toad"), None)

CoeurlRegina: Bestiary = Bestiary("Coeurl Regina", 15935, 154, 4, 36,
                                  51, 33000, 42000,
                                  ("Unicorn Horn", "Coeurl's Whisker", "Cat Claw", "Tabby Suit"),
                                  None, None, ("Silence", "Pig", "Mini", "Toad"),
                                  None)

CrystalDragon: Bestiary = Bestiary("Crystal Dragon", 18120, 162, 4, 42,
                                   45, 34000, 46000,
                                   ("White Fang", "Dragon Shield", "Wyvern Lance", "Crystal Ring"),
                                   "Dragon", "Throw",
                                   ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                    "Death", "Sleep", "Paralyze"),
                                   None)

MagicDragon: Bestiary = Bestiary("Magic Dragon", 20830, 160, 4, 41,
                                 48, 35000, 47000,
                                 ("Blue Fang", "Dragon's Whisker", "Protect Ring", "Rising Sun"),
                                 "Dragon", None,
                                 ("Blind", "Silence", "Pig", "Mini", "Toad", "Petrify", "Death", "Confuse",
                                  "Paralyze", "Curse", "Slowing Petrify"),
                                 None)

ChaoticKnight: Bestiary = Bestiary("Chaotic Knight", 21019, 152, 2, 68,
                                   45, 42000, 50000,
                                   ("Remedy", "Cottage", "Assassin Dagger"), None,
                                   None, ("Pig", "Mini", "Toad"), None)

Stratoavis: Bestiary = Bestiary("Stratoavis", 24458, 184, 2, 13, 55,
                                50000, 55000,
                                ("Phoenix Down", "Cottage", "Silver Apple", "Chocobo Suit"), None,
                                "Throw", ("Pig", "Mini", "Toad"), None)

GoldenFlan: Bestiary = Bestiary("Golden Flan", 12384, 155, 254, 0,
                                245, 40000, 42000,
                                ("Dry Ether", "Stardust", "Lunar Curtain", "Golden Apple"),
                                "Pudding", None, ("Toad", "Confuse"), None)

DustMousse: Bestiary = Bestiary("Dust Mousse", 10882, 155, 254, 0,
                                254, 40000, 42000,
                                ("Dry Ether", "Elixir", "Fuma Shuriken", "Soma Drop"),
                                ("Pudding", "Undead"), "Holy", ("Toad", "Confuse"),
                                "Darkness")

WorstMalboro: Bestiary = Bestiary("Worst Malboro", 18428, 155, 2, 22,
                                  23, 54000, 50000,
                                  ("Remedy", "Soma Drop", "Ribbon"), None,
                                  "Fire", ("Poison", "Blind", "Silence", "Pig", "Mini", "Death"),
                                  None)

Chimerageist: Bestiary = Bestiary("Chimerageist", 24415, 164, 4, 24,
                                  55, 57000, 58000,
                                  ("Red Fang", "White Fang", "Blue Fang", "Cursed Ring"), None,
                                  None, ("Pig", "Mini", "Toad", "Death", "Sleep", "Paralyze"),
                                  ("Fire", "Ice", "Lightning"))

Catoblepas: Bestiary = Bestiary("Catoblepas", 30556, 168, 4, 30,
                                54, 62000, 62000,
                                ("Gold Needle", "Medusa Arrow", "Aegis Shield", "Gorgon Blade"),
                                "Insect", None, ("Pig", "Mini"), None)

IronGiant: Bestiary = Bestiary("Iron Giant", 29818, 171, 3, 22,
                               60, 63000, 64000,
                               ("Ogrekiller", "Poison Axe", "Rune Axe", "Gigant Axe"), "Giant",
                               None,
                               ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Throw",
                                "Slowing Petrify"),
                               None)

KingBehemoth: Bestiary = Bestiary("King Behemoth", 29834, 190, 5, 10,
                                  254, 63500, 64000,
                                  ("Power Armlet", "Power Sash", "Avenger", "Tiger Fang"), None,
                                  None,
                                  ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                   "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Holy",
                                   "Slowing Petrify"),
                                  None)

Gilgamesh: Bestiary = Bestiary("Gilgamesh", 30710, 175, 6, 101,
                               254, 62500, 63000,
                               ("X-Potion", "Bestiary", "Lunar Curtain", "Maximilian"), "Insect",
                               "Ice",
                               ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                               None)

ProtoPhase: Bestiary = Bestiary("Proto Phase", 31415, 169, 3, 23,
                                24, 62000, 62000,
                                ("Light Curtain", "X-Potion", "Lunar Curtain", "Glass Mask"),
                                "Mech", None,
                                ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                 "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                None)

MistEagle: Bestiary = Bestiary("Mist Eagle", 10290, 152, 3, 22,
                               22, 12000, 12000,
                               ("Phoenix Down", "Gold Needle", "Cockatrice"), None,
                               "Throw", ("Pig", "Mini", "Toad"), None)

MistKraken: Bestiary = Bestiary("Mist Kraken", 12512, 157, 3, 31,
                                30, 18000, 18000,
                                ("Unicorn Horn", "Gold Hourglass", "Mind Flayer"), None,
                                None, ("Poison", "Mini", "Toad", "Death", "Paralyze"), None)

MistSummoner: Bestiary = Bestiary("Mist Summoner", 15920, 155, 4, 54,
                                  36, 25000, 25000,
                                  ("Healing Staff", "Rune Armlet", "Rune Staff", "Grimoire"), "Mage",
                                  None, ("Pig", "Mini", "Toad"), None)

Metamorpha: Bestiary = Bestiary("Metamorpha", 21231, 161, 4, 30,
                                38, 30000, 30000, "Perseus Arrow", "Mage",
                                None, ("Pig", "Mini", "Toad"), None)

Specter: Bestiary = Bestiary("Specter", 23511, 158, 4, 33, 44,
                             0, 0, "Phoenix Down", "Ghoul", None,
                             ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                              "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                             None)

PlatinumToad: Bestiary = Bestiary("Platinum Toad", 11111, 150, 60, 123,
                                  254, 65000, 65000, "Megalixir", "Insect",
                                  None,
                                  ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                   "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                  None)

GrudgePuppet: Bestiary = Bestiary("Grudge Puppet", 18929, 160, 5, 32,
                                  45, 20000, 32000, "Decoy", None,
                                  None,
                                  ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Berserk", "Confuse"),
                                  None)

DeathPuppet: Bestiary = Bestiary("Death Puppet", 60702, 185, 6, 57,
                                 62, 63000, 64000, "Potion", None,
                                 None,
                                 ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Death", "Berserk",
                                  "Confuse", "Sleep", "Curse"),
                                 None)

Brachioraidos: Bestiary = Bestiary("Brachioraidos", 180000, 225, 5, 212,
                                   125, 65000, 65000, "Hero's Shield",
                                   "Dragon", None,
                                   ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                    "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                   None)

SoldierMonk: Bestiary = Bestiary("Soldier Monk", 6000, 140, 3, 0,
                                 254, 5000, 15000, None, None,
                                 "Fire",
                                 ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                  "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                 None)

SuperMonk: Bestiary = Bestiary("Super Monk", 8000, 145, 3, 0,
                               254, 8000, 18000, None, None,
                               "Fire",
                               ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                               None)

Drillmaster: Bestiary = Bestiary("Drillmaster", 10000, 150, 3, 0,
                                 254, 10000, 20000, None, None,
                                 "Fire",
                                 ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                  "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                 None)

Bandit: Bestiary = Bestiary("Bandit", 14651, 144, 4, 22, 33,
                            0, 0, None, None, None,
                            ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                             "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                            None)

Octomammoth: Bestiary = Bestiary("Octomammoth", 2350, 22, 0, 0, 25,
                                 500, 1200, None, None,
                                 ("Lightning", "Darkness"),
                                 ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                  "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                 "Holy")

Antlion: Bestiary = Bestiary("Antlion", 1100, 11, 3, 0, 11,
                             800, 1500, None, None, None,
                             ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                              "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                             None)

MomBomb: Bestiary = Bestiary("Mom Bomb", 11000, 30, 1, 5, 9,
                             1200, 1900, None, None, "Darkness",
                             ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                              "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                             None)

Baigan: Bestiary = Bestiary("Baigan", 4444, 58, 1, 9, 11,
                            3000, 4800, None, None, None,
                            ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                             "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                            None)

RightArm: Bestiary = Bestiary("Right Arn", 444, 58, 2, 9, 0,
                              0, 10, None, None, None,
                              ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                               "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                              None)

LeftArm: Bestiary = Bestiary("Left Arm", 444, 58, 2, 9, 0,
                             0, 10, None, None, None,
                             ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                              "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                             None)

DarkElf: Bestiary = Bestiary("Dark Elf", 23890, 18, 0, 1,
                             254, 4000, 1000, None, None,
                             "Holy",
                             ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                              "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                             None)

DarkDragon: Bestiary = Bestiary("Dark Dragon", 3927, 80, 1, 15,
                                254, 5000, 6000, None, "Dragon",
                                "Holy",
                                ("Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                 "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                "Holy")

Sandy: Bestiary = Bestiary("Sandy", 2591, 30, 1, 11, 11,
                           3000, 2500, None, "Mage", None,
                           ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                            "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                           None)

Cindy: Bestiary = Bestiary("Cindy", 4599, 36, 2, 11, 11,
                           3000, 2500, None, "Mage", None,
                           ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                            "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                           None)

Mindy: Bestiary = Bestiary("Mindy", 2590, 30, 1, 10, 0,
                           3000, 2500, None, "Mage", None,
                           ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                            "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                           None)

Calco: Bestiary = Bestiary("Calco", 1369, 54, 0, 31, 11,
                           500, 1000, None, None, None,
                           None, None)

Brina: Bestiary = Bestiary("Brina", 369, 54, 1, 31, 11,
                           500, 1000, None, None, None,
                           ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                            "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                           None)

Calcobrena: Bestiary = Bestiary("Calcobrena", 5315, 106, 2, 41,
                                25, 5000, 12000, None, None, None,
                                ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                 "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                None)

Golbez: Bestiary = Bestiary("Golbez", "?", "?", "?", "?", "?",
                            "?", "?", "?", "?", "?", "?", "?")

ShadowDragon: Bestiary = Bestiary("Shadow Dragon", "?", "?", "?", "?",
                                  "?", "?", "?", "?", "?", "?",
                                  "?", "?")

Doctor: Bestiary = Bestiary("Doctor", 4936, 18, 0, 0, 11,
                            2000, 5500, None, None, None,
                            ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                             "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                            None)

Barnabas: Bestiary = Bestiary("Barnabas", 4832, 85, 0, 31, 11,
                              2500, 5500, None, "Mech", None,
                              ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                               "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                              None)

DrLugae: Bestiary = Bestiary("Dr. Lugae", 9321, 86, 1, 7, 11,
                             4000, 10101, "Dr. Lugae's Key", "Mech",
                             None,
                             ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                              "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                             None)

BarnabasZ: Bestiary = Bestiary("Barnabas-Z", 4518, 114, 1, 0, 5,
                               2500, 20, None, None, None,
                               ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                               None)

ScarmiglioneMutationForm: Bestiary = Bestiary("Scarmiglione (Form 1)", 3500, 19, 2,
                                              15, 0, 2000, 3200, None,
                                              None, None,
                                              ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                               "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse",
                                               "Slowing Petrify"),
                                              None)

Scarmiglione: Bestiary = Bestiary("Scarmiglione", 3523, 46, 1, 31,
                                  22, 2500, 3600, None, "Undead",
                                  ("Fire", "Holy", "Throw"),
                                  ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                   "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                  "Ice")

Cagnazzo: Bestiary = Bestiary("Cagnazzo", 5312, 44, 2, 29, 48,
                              4000, 5500, None, None, "Ice",
                              ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                               "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                              None)

Barbariccia: Bestiary = Bestiary("Barbariccia", 8636, 82, 0, 63,
                                 12, 5500, 9000, None, None,
                                 None,
                                 ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                  "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                 None)

Rubicante: Bestiary = Bestiary("Rubicante", 34000, 80, 3, 16,
                               37, 7000, 18000, None, None,
                               None,
                               ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                               "Fire")

DemonWall: Bestiary = Bestiary("Demon Wall", 28000, 84, 3, 79,
                               29, 8000, 23000, None, None,
                               None,
                               ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                               None)

DefenseNode: Bestiary = Bestiary("Defense Node", 3000, 116, 5, 47,
                                 11, 0, 0, None, None, None,
                                 ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                  "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                 None)

AttackNode: Bestiary = Bestiary("Attack Node", 3000, 116, 5, 47,
                                11, 0, 0, None, None, None,
                                ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                 "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                None)

CPU: Bestiary = Bestiary("CPU", 30000, 174, 4, 127,
                         38, 10333, 50000, None, None, None,
                         ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                          "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                         None)

StormDragon: Bestiary = Bestiary("Storm Dragon", 40000, 139, 4, 22,
                                 33, 0, 32000, None, "Dragon",
                                 "Ice",
                                 ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                  "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                 "Fire")

GigasWorm: Bestiary = Bestiary("Gigas Worm", 55000, 155, 4, 34,
                               44, 0, 32000, None, None, None,
                               ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                               None)

MasterFlan: Bestiary = Bestiary("Master Flan", 35000, 130, 4, 34,
                                38, 0, 32000, None, "Mage", None,
                                ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                 "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                None)

T_Rex: Bestiary = Bestiary("T-Rex", 60000, 148, 3, 34, 54,
                           0, 32000, None, "Insect", None,
                           ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                            "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                           None)

DeathMech: Bestiary = Bestiary("Death Mech", 50000, 135, 4, 34,
                               54, 0, 32000, None, "Mech", None,
                               ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                               None)

Lunasaur: Bestiary = Bestiary("Lunasaur", 23000, 144, 4, 54,
                              254, 0, 29500, None, ("Dragon", "Undead"),
                              "Fire",
                              ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                               "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                              None)

Plague: Bestiary = Bestiary("Plague", 33333, 146, 5, 0,
                            38, 550, 31108, None, None, "Throw",
                            ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                             "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                            None)

WhiteDragon: Bestiary = Bestiary("White Dragon", 32700, 156, 5, 31,
                                 48, 0, 55000, None, "Dragon",
                                 None,
                                 ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                  "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                 ("Fire", "Ice", "Lightning"))

Ogopogo: Bestiary = Bestiary("Ogopogo", 50000, 150, 4, 127,
                             40, 0, 61000, None, None, None,
                             ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                              "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                             None)

DarkBahambut: Bestiary = Bestiary("Dark Bahamut", 60000, 160, 5, 8,
                                  52, 0, 64000, None, "Dragon",
                                  None,
                                  ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                   "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                  None)

Zemus: Bestiary = Bestiary("Zemus", "?", "?", "?", "?", "?",
                           "?", "?", "?", "?", "?", "?", "?")

ZeromusCrystalForm: Bestiary = Bestiary("Zeromus (Crystal Form)", "?", "?", "?",
                                        "?", "?", "?", "?", "?", "?",
                                        "?", "?", "?")

Zeromus: Bestiary = Bestiary("Zeromus", "?", "?", "?", "?", "?",
                             "?", "?", "?", "?", "?", "?",
                             "?")

MistDragon: Bestiary = Bestiary("Mist Dragon", 465, 16, 5, 10, 31,
                                200, 700, None, None, None,
                                ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                 "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                "Holy")

Ifrit: Bestiary = Bestiary("Ifrit", 70000, 177, 5, 36, 44,
                           45000, 50000, None, None, "Ice",
                           ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                            "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                           None)

Shiva: Bestiary = Bestiary("Shiva", 64000, 172, 5, 50,
                           52, 45000, 50000, None, None, "Fire",
                           ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                            "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                           None)

Titan: Bestiary = Bestiary("Titan", 75000, 180, 5, 28,
                           48, 45000, 50000, None, None,
                           None,
                           ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                            "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                           None)

Ramuh: Bestiary = Bestiary("Ramuh", 60000, 170, 5, 41,
                           54, 45000, 50000, None, None,
                           None,
                           ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                            "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Lightning",
                            "Slowing Petrify"),
                           None)

Odin: Bestiary = Bestiary("Odin", 20001, 116, 5, 95,
                          38, 0, 18000, None, None, "Lightning",
                          ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                           "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                          None)

Leviathan: Bestiary = Bestiary("Leviathan", 50001, 174, 5, 34,
                               54, 0, 28000, None, None,
                               "Lightning",
                               ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                               None)

Bahamut: Bestiary = Bestiary("Bahamut", 45001, 1784, 1, 17,
                             4, 0, 35000, None, None, None,
                             ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                              "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                             None)

Asura: Bestiary = Bestiary("Asura", 31005, 134, 3, 69,
                           37, 0, 20000, None, "Mage",
                           None,
                           ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                            "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                           None)

LunarBahamut: Bestiary = Bestiary("Lunar Bahamut", 50000, 213, 2, 18,
                                  24, 65000, 65000, "Grimoire LB", None,
                                  None,
                                  ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                   "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                  None)

LunarLeviathan: Bestiary = Bestiary("Lunar Leviathan", 135000, 205, 3, 38,
                                    51, 65000, 65000, "Grimoire LL", None,
                                    "Lighting",
                                    ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                     "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                    None)

LunarOdin: Bestiary = Bestiary("Lunar Odin", 95000, 191, 2, 95,
                               48, 65000, 65000, "Grimoire LO", None,
                               "Lightning",
                               ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                               None)

LunarAsura: Bestiary = Bestiary("Lunar Asura", 130000, 183, 3, 55,
                                40, 65000, 65000, "Grimoire LA", None,
                                None,
                                ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                 "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                None)

LunarTitan: Bestiary = Bestiary("Lunar Titan", 120000, 196, 2, 35,
                                37, 65000, 65000, "Grimoire LT", None,
                                None,
                                ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                 "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                None)

LunarDragon: Bestiary = Bestiary("Lunar Dragon", 105000, 180, 2, 254,
                                 44, 65000, 65000, "Grimoire LD", None,
                                 None,
                                 ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                  "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                 "Holy")

LunarIfrit: Bestiary = Bestiary("Lunar Ifrit", 110000, 198, 2, 40,
                                35, 65000, 65000, "Grimoire LI", None,
                                "Ice",
                                ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                 "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                "Fire")

LunarRamuh: Bestiary = Bestiary("Lunar Ramuh", 90000, 178, 2, 44,
                                48, 65000, 65000, "Grimoire LR",
                                None, None,
                                ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                 "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                "Lightning")

LunarShiva: Bestiary = Bestiary("Lunar Shiva", 100000, 173, 2, 36,
                                55, 65000, 65000, "Grimoire LS", "None",
                                "Fire",
                                ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                 "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                                "Ice")

ZeromusEG: Bestiary = Bestiary("Zeromus EG", 200000, 225, 3, 45,
                               202, 0, 0, None, None, None,
                               ("Poison", "Blind", "Silence", "Pig", "Mini", "Toad", "Petrify",
                                "Death", "Berserk", "Confuse", "Sleep", "Paralyze", "Curse", "Slowing Petrify"),
                               None)
