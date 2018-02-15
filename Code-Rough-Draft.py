import random
import os
import cmd
import sys



def ArmorPen(decay, armor, ):
    armorpre = round(armor * 5)
    y = round(decay * round(armorpre - 5) + 5)
    return y


def StatInc(PercentInc, MonsterStat):
    Inc = round(MonsterStat / (100 - PercentInc))
    LevelInc = Inc * level
    return LevelInc


# This section asks the player whether they want lore enabled or disabled
LoreReader = input("Do you want to have the lore enabled of disabled?(Enabled or Disabled)")
if LoreReader == "Enabled" or LoreReader == "ENABLED" or LoreReader == "enabled":
    LoreReader = "Enabled"
elif LoreReader == "Disabled" or LoreReader == "DISABLED" or LoreReader == "disabled":
    LoreReader = "Disabled"
else:
    LoreReader = "Disabled"
print("Lore has been", LoreReader)
levelEq3 = False

# This section is where the player chooses their class and establishes their name
MainName = input("What is your name adventurer?")
MainClass = input("Choose your starting class adventurer: (Warrior, Mage, or Thief)")
if MainClass == "Warrior" or MainClass == "warrior" or MainClass == "WARRIOR":
    MainATK = 10
    MainHp = 400
    MainDef = 7
    MainMaxHp = 400
    MainSkillList = ["HeavyAttack", "BloodLust"]
elif MainClass == MainClass == "Mage" or MainClass == "mage" or MainClass == "MAGE":
    MainATK = 30
    MainHp = 300
    MainDef = 3
    MainMaxHp = 300
    MainSkillList = ["MagicMissile", "CureLightWounds", "MeteorRain"]
elif MainClass == MainClass == "Thief" or MainClass == "thief" or MainClass == "THIEF":
    MainATK = 20
    MainDef = 5
    MainHp = 400
    MainMaxHp = 400
    MainSkillList = ["BackStab", "Invisibility"]
else:
    MainATK = 10
    MainHp = 400
    MainDef = 7
    MainMaxHp = 400
    MainClass = "Warrior"
    MainSkillList = ["HeavyAttack", "BloodLust"]
MainRegen = 10
MainInventory = []
MainStatus = []
MainEquipped = []
BackStabBool = False
MainEvasion = 0
LevelEq3 = False
print("Welcome", MainName, "! Good choice choosing the", MainClass, "class.")

# this runs the loop of the actual level
level = 0
while MainHp > 0:
    if MainMaxHp > MainHp:
        MainRegenHealed = MainMaxHp - MainHp
        MainRegenHealedSub = round(MainRegenHealed / 10 + MainHp)
        MainHp = (MainRegenHealed / 10 + MainHp)
        print("You regenerated", MainRegenHealedSub, "Hp!")
    # RealWorld = 0
    level += 1
    print("You are on level", level)
    if level % 3 == 0:
        LevelEq3 = True

    def TavernScreen():
        print("Type the command of what you would like to do")
        print("Command   | Description")
        print("=======================")
        print("EquipItem | Shows your inventory and allows you to equip items")
        print("")
        print("")
        print("")
        TavernPrompt = input(">")
        if TavernPrompt == "EquipItem":
            for item in MainInventory:
                print(item)
        else:
            print("You failed to type a command, re-input your command.")
            TavernScreen()

    TavernScreen()
    # this section is where we find out what monster the player is attacking and setting a few basic stats
    MonsterRand = random.randint(1, 101)
    MonsterName = ""
    MonsterATK = round(0)
    MonsterDef = round(0)
    MonsterHp = round(100)
    LastMonsterHp = round(1000000000)
    MainDmgD = 0
    # This section identifies what monster the player will fight based on luck and level
    if 0 <= level <= 10 and levelEq3:
        if 1 <= MonsterRand <= 100:
            MonsterName = "Slime"
        elif 101 <= MonsterRand <= 95:
            MonsterName = "Goblin"
        elif 101 <= MonsterRand <= 100:
            MonsterName = "GoldenSlime"
    elif levelEq3 == 0:
        if level == 3:
            MonsterName = "King Slime"
            MonsterATK = 75
            MonsterDef = 0
            MonsterHp = 750
            MonsterPass = "Absorb"
        if level == 6:
            MonsterName = "Goblin Chieftain"
            MonsterATK = 90
            MonsterDef = 20
            MonsterHp = 500
            MonsterPass = "Evade"
        if level == 9:
            MonsterName = "Regal Kobold"
            MonsterATK = 120
            MonsterDef = 50
            MonsterHp = 1000
    if MonsterName == "Slime":
        MonsterATK = round(15 + StatInc(3, MonsterATK))
        MonsterDef = round(0 + StatInc(0, MonsterDef))
        MonsterHp = round(50 + StatInc(5, MonsterHp))
    elif MonsterName == "Goblin":
        MonsterATK = 20
        MonsterDef = 3
        MonsterHp = 25
    elif MonsterName == "GoldenSlime":
        MonsterATK = 10
        MonsterDef = 5
        MonsterHp = 60

    # This tells the player what monster they're attacking
    print("You have encountered a monster!")
    print("===============================")
    print("You started battle with a", MonsterName)
    print("===============================")

    # This section is where the player is attacking
    BreakBatt = 0
    while MonsterHp >= 0:
        if "Invisible" in MainStatus:
            InvisibleTurnCounter += 1
            InvisibleTurnCounter = 0
            if InvisibleTurnCounter == 3:
                MainStatus.remove("Invisible")
                print("You slowly started to reappear until you were completely visible.")
        TurnCounter = 1
        MonsterPassPrompt = random.randint(1, 101)
        MonsterATKPrompt = random.randint(1, 101)

        if MonsterName == "Goblin" and 1 <= MonsterPassPrompt <= 50:
            print("PLACEHOLDER")

        print(""
              "")
        print("The", MonsterName, "has", MonsterHp, "Life left.")
        print("You have", MainHp, "life left.")
        ATKPrompt = input("Do you want to attack, use a skill, or guard?(Attack, Skill, Guard)")
        print(""
              "")
        if ATKPrompt == "Attack" or ATKPrompt == "attack" or ATKPrompt == "ATTACK":
            MainPen = ArmorPen(.42, MonsterDef)
            MonsterHp = round(MonsterHp - (MainATK - (MainATK * (MainPen / 100))))
            MainDmgD = round(MainATK - (MainATK * (MainPen / 100)))
            print("You attacked the", MonsterName, "for", MainDmgD, "points of damage!")
            LastMonsterHp = round(MonsterHp - MainDmgD)
        elif ATKPrompt == "Skill" or ATKPrompt == "skill" or ATKPrompt == "SKILL":
            print("Which skill would you like to use?:")
            for Skill in MainSkillList:
                print(Skill)
            SkillPrompt = input("")

            if MainClass == "Thief":
                if SkillPrompt == "BackStab":
                    BackStabPrompt = 1 # random.randint(1, 2)
                    if BackStabPrompt == 1:
                        if "Invisible" in MainStatus or TurnCounter == 1:
                            MainPen = ArmorPen(.42, MonsterDef)
                            MonsterHp = round(MonsterHp - (MainATK - (MainATK * (MainPen / 100))))
                            MainDmgD = round((MainATK - (MainATK * (MainPen / 100))) * 2)
                            print("BackStab did", MainDmgD, "points of damage!")
                if SkillPrompt == "Invisibility":
                    InvisibilityPrompt = random.randint(1, 101)
                    if 1 <= InvisibilityPrompt <= 70:
                        if "Invisible" not in MainStatus:
                            MainStatus.append("Invisibility")
                            print("You murmured a chant and are suddenly no longer visible.")
                        else:
                            print("You murmured a chant but nothing seemed to happen.")
            elif MainClass == "Mage":
                if SkillPrompt == "MagicMissile":
                        print("in development")

            LastMonsterHp = round(MonsterHp - MainDmgD)
        elif ATKPrompt == "Guard" or ATKPrompt == "GUARD" or ATKPrompt == "guard":
            print("You guarded")
        else:
            print("You must type one of the Commands, 'Attack' has automatically been selected.")
            MainPen = ArmorPen(.42, MonsterDef)
            MonsterHp = round(MonsterHp - (MainATK - (MainATK * (MainPen / 100))))
            MainDmgD = round(MainATK - (MainATK * (MainPen / 100)))
            print("You attacked the", MonsterName, "for", MainDmgD, "points of damage!")
            LastMonsterHp = round(MonsterHp - MainDmgD)
        # This section is where the Monster passives go, Most of them anyway
        if MonsterName == "Slime":
            if 1 <= MonsterPassPrompt <= 50:
                if LastMonsterHp < MonsterHp:
                    MonsterHealed = round(MonsterHp / 10)
                    MonsterHp += MonsterHealed
                    print("The Slime's passive ability activated! The Slime healed for", MonsterHealed, "Hp!")
        if MonsterName == "Goblin":
            if 1 <= MonsterPassPrompt:
                print("PLACEHOLDER")

                # This Section is where the monster is attacking
        if 1 <= MonsterATKPrompt <= 100 and "Invisibility" not in MainStatus:
            MonsterPen = ArmorPen(.42, MainDef)
            MainHp = round(MainHp - (MonsterATK - (MonsterATK * (MonsterPen / 100))))
            MonsterDmgD = round(MonsterATK - (MonsterATK * (MonsterPen / 100)))
            print(MonsterName, "attacked you for", MonsterDmgD, "points of damage!")
            print(""
                  "")
        elif "Invisibility" in MainStatus:
            print(MonsterName, "tried to attack but couldn't see you.")
        LastMonsterHp = MonsterHp
        if "Invisible" in MainStatus:
            BackStabBool = True
        # elif 86 <= MonsterATKPrompt <= 100:
        #
        if MonsterHp <= 0:
            break

    print("You killed a", MonsterName)

