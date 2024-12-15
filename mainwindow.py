# ==============================
# FINAL FANTASY IV ADVANCE (GBA)
#         BESTIARY APP
#    Developed by: Phantasm
# ==============================
import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QLabel

import Bestiary as Bestiary


#
# for enemy in Bestiary.Bestiary.enemy_list:
#     print(enemy.enemyname)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Final Fantasy IV Advance Bestiary")
        self.setFixedSize(640, 480)

        # UI SETTINGS
        mainfont: QFont = QFont("System", 8)

        # WIDGETS

        self.setStyleSheet("background-color: navy; color: white;")

        self.enemyhealth_label: QLabel = QLabel("HP", self)
        self.enemyhealth_label.setFont(mainfont)
        self.enemyhealth_label.adjustSize()
        self.enemyhealth_label.move(50, 80)

        self.hpvalue_label: QLabel = QLabel(self)
        self.hpvalue_label.setFont(mainfont)
        self.hpvalue_label.setStyleSheet("color: gold")
        self.hpvalue_label.adjustSize()
        self.hpvalue_label.move(200, 80)

        self.enemystrength_label: QLabel = QLabel("Strength", self)
        self.enemystrength_label.setFont(mainfont)
        self.enemystrength_label.adjustSize()
        self.enemystrength_label.move(50, 100)

        self.strengthvalue_label: QLabel = QLabel(self)
        self.strengthvalue_label.setFont(mainfont)
        self.strengthvalue_label.setStyleSheet("color: gold")
        self.strengthvalue_label.adjustSize()
        self.strengthvalue_label.move(200, 100)

        self.enemydefense_label: QLabel = QLabel("Defense", self)
        self.enemydefense_label.setFont(mainfont)
        self.enemydefense_label.adjustSize()
        self.enemydefense_label.move(50, 120)

        self.defensevalue_label: QLabel = QLabel(self)
        self.defensevalue_label.setFont(mainfont)
        self.defensevalue_label.adjustSize()
        self.defensevalue_label.setStyleSheet("color: gold")
        self.defensevalue_label.move(200, 120)

        self.magic_label: QLabel = QLabel("Magic", self)
        self.magic_label.setFont(mainfont)
        self.magic_label.adjustSize()
        self.magic_label.move(50, 140)

        self.magicvalue_label: QLabel = QLabel(self)
        self.magicvalue_label.setFont(mainfont)
        self.magicvalue_label.adjustSize()
        self.magicvalue_label.setStyleSheet("color: gold")
        self.magicvalue_label.move(200, 140)

        self.magicdefense_label: QLabel = QLabel("Magic Def.", self)
        self.magicdefense_label.setFont(mainfont)
        self.magicdefense_label.adjustSize()
        self.magicdefense_label.move(50, 160)

        self.magicdefensevalue_label: QLabel = QLabel(self)
        self.magicdefensevalue_label.setFont(mainfont)
        self.magicdefensevalue_label.adjustSize()
        self.magicdefensevalue_label.setStyleSheet("color: gold")
        self.magicdefensevalue_label.move(200, 160)

        self.gil_label: QLabel = QLabel("Gil", self)
        self.gil_label.setFont(mainfont)
        self.gil_label.adjustSize()
        self.gil_label.move(50, 200)

        self.gilvalue_label: QLabel = QLabel(self)
        self.gilvalue_label.setFont(mainfont)
        self.gilvalue_label.adjustSize()
        self.gilvalue_label.setStyleSheet("color: gold")
        self.gilvalue_label.move(200, 200)

        self.exp_Label: QLabel = QLabel("EXP", self)
        self.exp_Label.setFont(mainfont)
        self.exp_Label.adjustSize()
        self.exp_Label.move(50, 220)

        self.expvalue_label: QLabel = QLabel(self)
        self.expvalue_label.setFont(mainfont)
        self.expvalue_label.adjustSize()
        self.expvalue_label.setStyleSheet("color: gold")
        self.expvalue_label.move(200, 220)

        self.treasurelist: QLabel = QLabel(self)
        self.treasurelist.setFont(mainfont)
        self.treasurelist.adjustSize()
        self.treasurelist.move(80, 250)

        self.treasurelabel: QLabel = QLabel("Treasure", self)
        self.treasurelabel.setFont(mainfont)
        self.treasurelabel.adjustSize()
        self.treasurelabel.move(50, 250)

        self.enemytype_label: QLabel = QLabel("Type", self)
        self.enemytype_label.setFont(mainfont)
        self.enemytype_label.adjustSize()
        self.enemytype_label.move(50, 370)

        self.enemytype_value_label: QLabel = QLabel(self)
        self.enemytype_value_label.setFont(mainfont)
        self.enemytype_value_label.adjustSize()
        self.enemytype_value_label.move(50, 390)

        self.weakness_label: QLabel = QLabel("Weakness", self)
        self.weakness_label.setFont(mainfont)
        self.weakness_label.adjustSize()
        self.weakness_label.move(300, 50)

        self.weakness_list_label: QLabel = QLabel(self)
        self.weakness_list_label.setFont(mainfont)
        self.weakness_list_label.adjustSize()
        self.weakness_list_label.move(300, 70)

        self.resistance_label: QLabel = QLabel("Resistance", self)
        self.resistance_label.setFont(mainfont)
        self.resistance_label.adjustSize()
        self.resistance_label.move(300, 110)

        self.resistance_list_label: QLabel = QLabel(self)
        self.resistance_list_label.setFont(mainfont)
        self.resistance_list_label.adjustSize()
        self.resistance_list_label.move(300, 130)

        self.absorb_label: QLabel = QLabel("Absorb", self)
        self.absorb_label.setFont(mainfont)
        self.absorb_label.adjustSize()
        self.absorb_label.move(300, 310)

        self.absorb_list_label: QLabel = QLabel(self)
        self.absorb_list_label.setFont(mainfont)
        self.absorb_list_label.adjustSize()
        self.absorb_list_label.move(300, 330)

        self.enemy_selector: QComboBox = QComboBox(self)

        enemy_counter: int = 0
        for enemy in Bestiary.Bestiary.enemy_list:
            enemy_counter += 1
            if enemy_counter <= 9:
                self.enemy_selector.addItem(f"00{enemy_counter} - {enemy.enemyname}")
            elif enemy_counter >= 10 and enemy_counter <= 99:
                self.enemy_selector.addItem(f"0{enemy_counter} - {enemy.enemyname}")
            else:
                self.enemy_selector.addItem(f"{enemy_counter} - {enemy.enemyname}")

        self.enemy_selector.move(405, 10)
        self.enemy_selector.setFont(mainfont)
        self.enemy_selector.adjustSize()
        self.enemy_selector.activated.connect(self.enemydatachange)

        self.enemydatachange()

    def enemydatachange(self):
        for enemyinfo in Bestiary.Bestiary.enemy_list:

            # This fixes an issue where the in statement takes the index string referencing
            # a bit too literal, causing a backlog of data searching that doesn't call
            # the proper information.

            # This error specifically happens at entry 102 - Mad Ogre, where it references
            # the Ogre from earlier in the bestiary list when the condition to explicitly match
            # the string is not applied.

            search_fix_stringsplitter: str = self.enemy_selector.currentText()[6:]

            if (enemyinfo.enemyname in self.enemy_selector.currentText() and
                    enemyinfo.enemyname == search_fix_stringsplitter):
                self.hpvalue_label.setText(f'{enemyinfo.health}')
                self.hpvalue_label.adjustSize()

                self.strengthvalue_label.setText(f'{enemyinfo.strength}')
                self.strengthvalue_label.adjustSize()

                self.defensevalue_label.setText(f"{enemyinfo.defense}")
                self.defensevalue_label.adjustSize()

                self.magicvalue_label.setText(f"{enemyinfo.magic}")
                self.magicvalue_label.adjustSize()

                self.magicdefensevalue_label.setText(f"{enemyinfo.magicdefense}")
                self.magicdefensevalue_label.adjustSize()

                self.gilvalue_label.setText(f"{enemyinfo.gil}")
                self.gilvalue_label.adjustSize()

                self.expvalue_label.setText(f"{enemyinfo.experience}")
                self.expvalue_label.adjustSize()

                if enemyinfo.treasure is None:
                    self.treasurelist.clear()
                    self.treasurelist.setText("\nNone")
                    self.treasurelist.adjustSize()

                if isinstance(enemyinfo.treasure, str):
                    self.treasurelist.clear()
                    self.treasurelist.setText(f"\n{enemyinfo.treasure}")
                    self.treasurelist.adjustSize()

                if isinstance(enemyinfo.treasure, tuple):
                    self.treasurelist.clear()
                    for reward in enemyinfo.treasure:
                        self.treasurelist.setText(f"{self.treasurelist.text()}\n{reward}")

                    self.treasurelist.adjustSize()

                if isinstance(enemyinfo.enemy_type, str):
                    self.enemytype_value_label.setText(f"{enemyinfo.enemy_type}")

                if isinstance(enemyinfo.enemy_type, tuple):
                    self.enemytype_value_label.setText(f"{enemyinfo.enemy_type[0]}\t\t{enemyinfo.enemy_type[1]}")

                if enemyinfo.enemy_type is None:
                    self.enemytype_value_label.setText(f"{enemyinfo.enemy_type}")

                self.enemytype_value_label.adjustSize()

                if enemyinfo.weakness is None:
                    self.weakness_list_label.setText("None")

                if isinstance(enemyinfo.weakness, str):
                    self.weakness_list_label.setText(f"{enemyinfo.weakness}")

                if isinstance(enemyinfo.weakness, tuple) and len(enemyinfo.weakness) == 2:
                    self.weakness_list_label.setText(f"{enemyinfo.weakness[0]}\t\t{enemyinfo.weakness[1]}")

                if isinstance(enemyinfo.weakness, tuple) and len(enemyinfo.weakness) == 3:
                    self.weakness_list_label.setText(f"{enemyinfo.weakness[0]}\t\t{enemyinfo.weakness[1]}\n"
                                                     f"{enemyinfo.weakness[2]}")

                self.weakness_list_label.adjustSize()

                if enemyinfo.resistance is None:
                    self.resistance_list_label.setText("None")

                if isinstance(enemyinfo.resistance, str):
                    self.resistance_list_label.setText(f"{enemyinfo.resistance}")

                # FIXME
                #  This generally works the way it needs to, but there are some nuances
                #  that don't match up the way it does in game that need to be fixed and debugged.

                # Handling Enemy Resistances if there's more than one.

                if isinstance(enemyinfo.resistance, tuple):

                    full_resistance_string: str = ""
                    proper_resistance_list: list = list(enemyinfo.resistance)

                    # if list amount is even:
                    #  print the two resistances and print new line
                    #  delete the first two indexes
                    # if list amount is odd:
                    #  print the last resistance

                    while len(proper_resistance_list) > 0:
                        if len(proper_resistance_list) % 2 == 0:
                            if proper_resistance_list[0] == "Poison" and proper_resistance_list[1] == "Blind":
                                full_resistance_string += f"{proper_resistance_list[0]}\t{proper_resistance_list[1]}\n"
                                proper_resistance_list.pop(0)
                                proper_resistance_list.pop(0)
                            elif proper_resistance_list[0] == "Silence" and proper_resistance_list[1] == "Pig":
                                full_resistance_string += f"{proper_resistance_list[0]}\t{proper_resistance_list[1]}\n"
                                proper_resistance_list.pop(0)
                                proper_resistance_list.pop(0)
                            elif proper_resistance_list[0] == "Petrify" and proper_resistance_list[1] == "Death":
                                full_resistance_string += f"{proper_resistance_list[0]}\t{proper_resistance_list[1]}\n"
                                proper_resistance_list.pop(0)
                                proper_resistance_list.pop(0)
                            elif proper_resistance_list[0] == "Berserk":
                                full_resistance_string += f"{proper_resistance_list[0]}\t{proper_resistance_list[1]}\n"
                                proper_resistance_list.pop(0)
                                proper_resistance_list.pop(0)
                            else:
                                full_resistance_string += f"{proper_resistance_list[0]}\t\t{proper_resistance_list[1]}\n"
                                proper_resistance_list.pop(0)
                                proper_resistance_list.pop(0)
                        elif len(proper_resistance_list) == 1:
                            if "Slowing Petrify" in proper_resistance_list:
                                full_resistance_string += f"{proper_resistance_list[0]}"
                            else:
                                full_resistance_string += f"{proper_resistance_list[0]}"
                            proper_resistance_list.pop(0)
                        else:
                            full_resistance_string += f"{proper_resistance_list[0]}\t\t{proper_resistance_list[1]}\n"
                            proper_resistance_list.pop(0)
                            proper_resistance_list.pop(0)

                    self.resistance_list_label.setText(full_resistance_string)
                    self.resistance_list_label.adjustSize()

                if enemyinfo.absorb is None:
                    self.absorb_list_label.setText("None")

                if isinstance(enemyinfo.absorb, str):
                    self.absorb_list_label.setText(f"{enemyinfo.absorb}")

                if isinstance(enemyinfo.absorb, tuple):
                    absorb_list: list = list(enemyinfo.absorb)
                    full_absorb_string: str = ""
                    while len(absorb_list) > 0:
                        if absorb_list[0] == "Lightning" and absorb_list[1] == "Darkness":
                            full_absorb_string += f"{absorb_list[0]}\t{absorb_list[1]}\n"
                            absorb_list.pop(0)
                            absorb_list.pop(0)
                        if len(absorb_list) % 2 == 0:
                            full_absorb_string += f"{absorb_list[0]}\t\t{absorb_list[1]}\n"
                            absorb_list.pop(0)
                            absorb_list.pop(0)
                        elif len(absorb_list) == 1:
                            full_absorb_string += f"{absorb_list[0]}"
                            absorb_list.pop(0)
                        elif len(absorb_list) % 2 == 1:
                            full_absorb_string += f"{absorb_list[0]}\t\t{absorb_list[1]}\n"
                            absorb_list.pop(0)
                            absorb_list.pop(0)
                        else:
                            pass

                    self.absorb_list_label.setText(full_absorb_string)
                self.absorb_list_label.adjustSize()

                break


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
