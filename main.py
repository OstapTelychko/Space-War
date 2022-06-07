import json
import random
import pygame
import os

from account_management import Account
from PyQt5.QtWidgets import QWidget,QMessageBox
from windows_layouts import *
from Langauge_packs import Languages

def find_file(file):
    "Return path to file"
    #Use this method, if you're using exe file
    Path = os.path.join(os.environ.get("_MEIPASS2",os.path.abspath(".")),file).replace("\\","/")
    #Use this method, if you're using the python Interpreter
    # Path = os.path.join(os.path.abspath(__file__ + "/.."),file).replace("\\","/")
    return Path
start_window = QWidget()
login_window = QWidget()
Language_window = QWidget()
menu_window = QWidget()
Tip_window = QWidget()
upgrade_ship_window = QWidget()
best_players_window = QWidget()
subtitles_window = QWidget()
def change_active_language():
    global app,start_window,login_window,Language_window,menu_window,Tip_window,upgrade_ship_window,best_players_window,main_select_language_layout
    start_window.hide()
    start_window = QWidget()
    login_window = QWidget()
    Language_window = QWidget()
    menu_window = QWidget()
    Tip_window = QWidget()
    upgrade_ship_window = QWidget()
    best_players_window = QWidget()
    Choose_language = QComboBox()
    Choose_language.addItems(["None","English","Українська"])
    Choose_language.setMinimumWidth(75)
    Select_language_text = QLabel("Select language to continue")
    Select_language_text.setFont(Font)
    main_select_language_layout = QVBoxLayout()
    main_select_language_layout.addStretch(1)
    main_select_language_layout.addWidget(Select_language_text,alignment=Qt.AlignHCenter)
    main_select_language_layout.addWidget(Choose_language,alignment=Qt.AlignHCenter)
    main_select_language_layout.addStretch(1)
    Choose_language.currentTextChanged.connect(change_language)
    show_Language_window()
def change_language(language):
    global Language,button_start,button_change_language,main_start_layout,\
        Line_user_name,Line_password,Button_check,Button_login_or_create,Login_text,main_create_and_login_account_layout,\
            Button_level_1,Button_level_2,Button_level_3,Button_level_4,players_name,players_money,Button_upgrade_ship,Button_tips,Button_best_players,main_menu_layout,level_1_layout,level_2_layout,level_3_layout,level_4_layout,\
                main_tip_layout,main_upgrade_ship_layout,Button_upgrade,rocket_level_text,rocket_hp_amount,rocket_speed_amount,rocket_damage_amount,rocket_ammo_amount,upgrade_cost_amount,\
                    Button_back,main_subtitles_window_layout
    Language = language
    with open(find_file("active_language.json"),"w",encoding="utf-8") as file:
        json.dump({"language":Language},file,indent=4,ensure_ascii=False)
    button_start,button_change_language,main_start_layout,\
        Line_user_name,Line_password,Button_check,Button_login_or_create,Login_text,main_create_and_login_account_layout,\
            Button_level_1,Button_level_2,Button_level_3,Button_level_4,players_name,players_money,Button_upgrade_ship,Button_tips,Button_best_players,main_menu_layout,level_1_layout,level_2_layout,level_3_layout,level_4_layout,\
                main_tip_layout,main_upgrade_ship_layout,Button_upgrade,rocket_level_text,rocket_hp_amount,rocket_speed_amount,rocket_damage_amount,rocket_ammo_amount,upgrade_cost_amount,\
                    Button_back,main_subtitles_window_layout=create_layouts(Language)
    show_start_window()
    activate_buttons()
    Language_window.hide()
def show_Tips_window():
    if Tip_window.width() < 500 and Tip_window.height() < 600:
        Tip_window.resize(500,600)
    Tip_window.setWindowTitle("Space War")
    Tip_window.setWindowIcon(Icon)
    Tip_window.setLayout(main_tip_layout)
    Tip_window.setStyleSheet(backgrounds)
    Tip_window.show()
def upgrade_ship():
    global money,ship_level
    if ship_level != 4:
        if money >= int(upgrade_cost_amount.text()):
            question = QMessageBox()
            question.setText(Languages[Language]["Menu_and_levels"]["Menu"][12])
            question.setWindowTitle("Space War")
            question.setWindowIcon(Icon)
            question.setIconPixmap(QPixmap(find_file("Images/Icon.ico")).scaled(50,50,Qt.KeepAspectRatio))
            question.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            return_value = question.exec()
            if return_value == QMessageBox.Ok:
                menu_window.hide()
                money -= int(upgrade_cost_amount.text())
                ship_level +=1
                accounts.update_info("money",money,user_name)
                accounts.update_info("ship_level",ship_level,user_name)
                show_menu_window()
        else:
            error = QMessageBox()
            error.setIconPixmap(QPixmap(find_file("Images/Icon.ico")).scaled(50,50,Qt.KeepAspectRatio))
            error.setWindowIcon(Icon)
            error.setText(Languages[Language]["Menu_and_levels"]["Menu"][13])
            error.setWindowTitle("Space War")
            error.setFont(Font)
            error.exec()
def show_upgrade_ship_window():
    if upgrade_ship_window.width() < 500 and upgrade_ship_window.height() < 600:
        upgrade_ship_window.resize(500,600)
    upgrade_ship_window.setWindowTitle("Space War")
    upgrade_ship_window.setWindowIcon(Icon)
    upgrade_ship_window.setLayout(main_upgrade_ship_layout)
    upgrade_ship_window.setStyleSheet(backgrounds)
    upgrade_ship_window.show()
    print(1)
def show_best_players_window():
    upgrade_ship_window.hide()
    if best_players_window.width() < 600 and best_players_window.height() < 500:
        best_players_window.resize(600,500)
    best_players_window.setWindowIcon(Icon)
    best_players_window.setWindowTitle("Space War")
    accounts_name = QLabel(Languages[Language]["Menu_and_levels"]["Menu"][14])
    accounts_name.setFont(Title_font)
    accounts_ship_level = QLabel(Languages[Language]["Menu_and_levels"]["Menu"][15])
    accounts_ship_level.setFont(Title_font)
    accounts_money = QLabel(Languages[Language]["Menu_and_levels"]["Menu"][16])
    accounts_money.setFont(Title_font)
    accounts_info = QHBoxLayout()
    accounts_info.addWidget(accounts_name,alignment=Qt.AlignLeft)
    accounts_info.addWidget(accounts_ship_level,alignment=Qt.AlignHCenter)
    accounts_info.addWidget(accounts_money,alignment=Qt.AlignRight)
    accounts_top_layout = QVBoxLayout()
    accounts_top_layout.addLayout(accounts_info)
    for account in accounts.get_best_players():
        account_name = QLabel(account[1])
        account_name.setFont(Font)
        account_ship_level = QLabel(str(account[5]))
        account_ship_level.setFont(Font)
        account_money = QLabel(str(account[4]))
        account_money.setFont(Font)
        account_layout = QHBoxLayout()
        account_layout.addWidget(account_name,alignment=Qt.AlignLeft)
        account_layout.addWidget(account_ship_level,alignment=Qt.AlignHCenter)
        account_layout.addWidget(account_money,alignment=Qt.AlignRight)
        account_layout.setContentsMargins(10,0,25,0)
        accounts_top_layout.addLayout(account_layout)
    accounts_top = QWidget()
    accounts_top.setLayout(accounts_top_layout)
    accounts_scroll_area = QScrollArea()
    accounts_scroll_area.setWidgetResizable(True)
    accounts_scroll_area.setWidget(accounts_top)
    accounts_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    accounts_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    accounts_scroll_area.setStyleSheet(levels_backgrounds)
    main_best_players_layout = QVBoxLayout()
    main_best_players_layout.addWidget(accounts_scroll_area)
    best_players_window.setLayout(main_best_players_layout)
    best_players_window.setStyleSheet(backgrounds)
    best_players_window.show()
def show_Language_window():
    Language_window.resize(500,500)
    Language_window.setWindowIcon(Icon)
    Language_window.setWindowTitle("Space War")
    Language_window.move(400,50)
    Language_window.setStyleSheet(backgrounds)
    Language_window.setLayout(main_select_language_layout)
    Language_window.show()
def activate_buttons():
    button_change_language.clicked.connect(change_active_language)
    button_start.clicked.connect(show_login_window)
    Button_login_or_create.clicked.connect(show_login_window)
    Button_check.clicked.connect(create_or_login_account)
    Button_tips.clicked.connect(show_Tips_window)
    Button_upgrade_ship.clicked.connect(show_upgrade_ship_window)
    Button_upgrade.clicked.connect(upgrade_ship)
    Button_best_players.clicked.connect(show_best_players_window)
    Button_level_1.pressed.connect(runing_level_1)
    Button_level_2.pressed.connect(runing_level_2)
    Button_level_3.pressed.connect(runing_level_3)
    Button_level_4.pressed.connect(runing_level_4)
    Button_back.clicked.connect(show_menu_window)
def show_start_window():
    start_window.setWindowIcon(Icon)
    if start_window.width() < 700 and start_window.height() < 500:
        start_window.resize(700,500)
    start_window.move(250,50)
    start_window.setWindowTitle("Space War")
    start_window.setStyleSheet(backgrounds)
    start_window.setLayout(main_start_layout)
    start_window.show()
    pygame.mixer.music.load(find_file("Music/welcome music.mp3"))
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
def show_menu_window():
    global player,subtitles_showed
    pygame.quit()
    if level_1_finished is True and level_2_finished is True and level_3_finished is True and level_4_finished is True and not (subtitles_showed is True):
        show_subtitles_window()
        subtitles_showed = True
        accounts.update_info("subtitles_showed",subtitles_showed,user_name)
    else:
        subtitles_window.hide()
        if login_window.width() > 700 and login_window.height() > 600 or menu_window.width() > 700 and menu_window.height() > 600:
            menu_window.showNormal()
            menu_window.showMaximized()
        else:
            menu_window.resize(700,600)
            menu_window.move(250,50)
        menu_window.setWindowTitle("Space War")
        menu_window.setWindowIcon(Icon)  
        menu_window.setStyleSheet(backgrounds)
        menu_window.setLayout(main_menu_layout)
        players_name.setText(user_name)
        players_money.setText(str(money))
        if ship_level == 0:
            player = Player(image="Images/rocket.png",size_width=70,size_height=100,x=315,y=400,speed=3,Hp=5,ammo_amount=1,damage=1)
            upgrade_cost_amount.setText("100")
            rocket_level_text.setText(Languages[Language]["Menu_and_levels"]["Menu"][11]+" 0")
        elif ship_level == 1:
            player = Player(image="Images/rocket.png",size_width=70,size_height=100,x=315,y=400,speed=3,Hp=8,ammo_amount=1,damage=1)
            upgrade_cost_amount.setText("1000")
            rocket_level_text.setText(Languages[Language]["Menu_and_levels"]["Menu"][11]+" 1")
        elif ship_level == 2:
            player = Player(image="Images/rocket.png",size_width=70,size_height=100,x=315,y=400,speed=5,Hp=8,ammo_amount=1,damage=1)
            rocket_level_text.setText(Languages[Language]["Menu_and_levels"]["Menu"][11]+" 2")
            upgrade_cost_amount.setText("15000")
        elif ship_level == 3:
            player = Player(image="Images/rocket.png",size_width=70,size_height=100,x=315,y=400,speed=5,Hp=8,ammo_amount=2,damage=1)
            rocket_level_text.setText(Languages[Language]["Menu_and_levels"]["Menu"][11]+" 3")
            upgrade_cost_amount.setText("300000")
        elif ship_level == 4:
            player = Player(image="Images/rocket.png",size_width=70,size_height=100,x=315,y=400,speed=5,Hp=10,ammo_amount=2,damage=3)
            rocket_level_text.setText(Languages[Language]["Menu_and_levels"]["Menu"][11]+" 4")
            upgrade_cost_amount.setText(Languages[Language]["Menu_and_levels"]["Menu"][21])
        rocket_hp_amount.setText(str(player.Hp))
        rocket_speed_amount.setText(str(player.speed))
        rocket_ammo_amount.setText(str(player.ammo_amount+1))
        rocket_damage_amount.setText(str(player.damage))
        menu_window.show()
        if pygame.mixer.get_init() is None:
            pygame.mixer.init()
        pygame.mixer.music.load(find_file("Music/menu music.mp3"))
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
def show_login_window():
    start_window.hide()
    login_window.setWindowIcon(Icon)
    if start_window.width() > 822 and start_window.height() > 663 or login_window.width() > 700 and login_window.height() > 500:
        login_window.showMaximized()
    else:
        login_window.resize(700,500)
    login_window.setWindowTitle("Space War")
    if button_start.sender() == button_start:
        login_window.setLayout(main_create_and_login_account_layout)
    elif Button_login_or_create.sender() == Button_login_or_create and Button_login_or_create.text() == Languages[Language]["Login_window"][3]:
        Button_check.setText(Languages[Language]["Showed_login_window"][0])
        Button_login_or_create.setText(Languages[Language]["Showed_login_window"][1])
        Login_text.setText(Languages[Language]["Showed_login_window"][2])
    elif Button_login_or_create.sender() == Button_login_or_create and Button_login_or_create.text() == Languages[Language]["Showed_login_window"][1]:
        Button_check.setText(Languages[Language]["Showed_login_window"][3])
        Button_login_or_create.setText(Languages[Language]["Showed_login_window"][4])
        Login_text.setText(Languages[Language]["Showed_login_window"][5])
    login_window.setStyleSheet(backgrounds)
    login_window.show()
def create_or_login_account():
    global user_name,password,money,ship_level,level_1_finished,level_2_finished,level_3_finished,level_4_finished,subtitles_showed,accounts
    accounts = Account(find_file("players.db"))
    if Line_user_name.text() != "" and len([symbol for symbol in Line_password.text()]) >=8 and len([symbol for symbol in Line_password.text()]) <=20:
        user_name = Line_user_name.text()
        password = Line_password.text()
        if Button_check.text() == Languages[Language]["Login_window"][2]:
            if not accounts.check_for_name_exists(user_name):
                accounts.add_account(user_name,password)
                Login_text.setText(Languages[Language]["Created_or_logined_account_and_errors"][0])
                login_window.hide()
                money = 0
                ship_level = 0
                level_1_finished = False
                level_2_finished = False
                level_3_finished = False
                level_4_finished = False
                subtitles_showed = False
                show_menu_window()
            else:
                Login_text.setText(Languages[Language]["Created_or_logined_account_and_errors"][1])
                user_name = ""
        elif Button_check.text() == Languages[Language]["Showed_login_window"][0]:
            if accounts.account_exists(user_name,password):
                login_window.hide()
                money = accounts.get_info("money",user_name)
                ship_level = accounts.get_info("ship_level",user_name)
                level_1_finished = bool(accounts.get_info("level_1_finished",user_name))
                level_2_finished = bool(accounts.get_info("level_2_finished",user_name))
                level_3_finished = bool(accounts.get_info("level_3_finished",user_name))
                level_4_finished = bool(accounts.get_info("level_4_finished",user_name))
                subtitles_showed = bool(accounts.get_info("subtitles_showed",user_name))
                show_menu_window()
            else:
                Login_text.setText(Languages[Language]["Created_or_logined_account_and_errors"][2])
    else:
        if len([symbol for symbol in Line_password.text()]) < 8 or len([symbol for symbol in Line_password.text()]) > 20:
            Login_text.setText(Languages[Language]["Created_or_logined_account_and_errors"][3])
        elif Line_user_name.text() =="":
            Login_text.setText(Languages[Language]["Created_or_logined_account_and_errors"][4])
def show_subtitles_window():
    subtitles_window.resize(700,600)
    subtitles_window.setWindowIcon(Icon)
    subtitles_window.setLayout(main_subtitles_window_layout)
    subtitles_window.setStyleSheet(backgrounds)
    subtitles_window.setWindowTitle("Space war")
    subtitles_window.show()
    pygame.mixer.init()
    pygame.mixer.music.load(find_file("Music/welcome music.mp3"))

def show_error_window():
    error_window = QMessageBox()
    error_window.setIconPixmap(QPixmap(find_file("Images/Icon.ico")).scaled(50,50,Qt.KeepAspectRatio))
    error_window.setWindowIcon(Icon)
    error_window.setText(Languages[Language]["Menu_and_levels"]["Menu"][20])
    error_window.setWindowTitle("Space War")
    error_window.setFont(Font)
    error_window.exec()
def runing_level_1():
    global level_1_layout,Button_level_1
    pygame.init()
    level_1_layout.removeWidget(Button_level_1)
    Button_level_1 = QPushButton(Languages[Language]["Menu_and_levels"]["Levels"][0])
    Button_level_1.setMinimumWidth(75)
    Button_level_1.setMaximumWidth(75)
    level_1_layout.addWidget(Button_level_1,alignment=Qt.AlignHCenter)
    activate_buttons()
    level_1()
def runing_level_2():
    if ship_level >= 2:
        global level_2_layout,Button_level_2
        pygame.init()
        level_2_layout.removeWidget(Button_level_2)
        Button_level_2 = QPushButton(Languages[Language]["Menu_and_levels"]["Levels"][1])
        Button_level_2.setMinimumWidth(75)
        Button_level_2.setMaximumWidth(75)
        level_2_layout.addWidget(Button_level_2,alignment=Qt.AlignHCenter)
        activate_buttons()
        level_2()
    else:
        show_error_window()
def runing_level_3():
    if ship_level >= 3:
        global level_3_layout,Button_level_3
        pygame.init()
        level_3_layout.removeWidget(Button_level_3)
        Button_level_3 = QPushButton(Languages[Language]["Menu_and_levels"]["Levels"][2])
        Button_level_3.setMinimumWidth(75)
        Button_level_3.setMaximumWidth(75)
        level_3_layout.addWidget(Button_level_3,alignment=Qt.AlignHCenter)
        activate_buttons()
        level_3()
    else:
        show_error_window()
def runing_level_4():
    if ship_level >= 4:
        global level_4_layout,Button_level_4
        pygame.init()
        level_4_layout.removeWidget(Button_level_4)
        Button_level_4 = QPushButton(Languages[Language]["Menu_and_levels"]["Levels"][3])
        Button_level_4.setMinimumWidth(75)
        Button_level_4.setMaximumWidth(75)
        level_4_layout.addWidget(Button_level_4,alignment=Qt.AlignHCenter)
        activate_buttons()
        level_4()
    else:
        show_error_window()
class GameSprite():
    def __init__(self,image,x,y,size_width,size_height,speed,Hp):
        self.size_width = size_width
        self.size_height = size_height
        self.Image = pygame.transform.scale(pygame.image.load(find_file(image)),(self.size_width,self.size_height))
        self.Rect = self.Image.get_rect()
        self.Rect.x = x
        self.Rect.y = y
        self.speed = speed
        self.Hp = Hp

    def draw(self,display):
        global boss_summoned
        if boss_summoned == False and type(self) is Boss:
            for iteration in range(1,len(bullets)):
                del bullets[0]
            pygame.mixer.music.load(find_file("Music/boss music.mp3"))
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.6)
            boss_summoned = True
        pygame.font.init()
        hp_amount = pygame.font.SysFont("Aeral",30).render(str(self.Hp),True,(255,255,255))
        display.blit(hp_amount,(self.Rect.x+20,self.Rect.y-20))
        display.blit(Hp_icon,(self.Rect.x-20,self.Rect.y-20))
        display.blit(self.Image,(self.Rect.x,self.Rect.y))
class Player(GameSprite):
    def __init__(self, image, x, y, size_width, size_height, speed,Hp,ammo_amount,damage):
        super().__init__(image, x, y, size_width, size_height, speed,Hp)
        self.ammo_amount = ammo_amount
        self.damage = damage
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.Rect.x>0:
            self.Rect.x -= self.speed
        elif keys[pygame.K_d] and self.Rect.x<625:
            self.Rect.x += self.speed
class Enemy(GameSprite):
    def __init__(self, image, x, y, size_width, size_height, speed,Hp):
        super().__init__(image, x, y, size_width, size_height,speed,Hp)
        self.Rect.x =  random.randint(self.size_width,700-self.size_width)
        self.Rect.y = random.randint(-100,-60)
        self.start_hp =Hp
        self.direction = "Right"
        self.timer = 20
    def move(self):
        global lost,score,finish,player
        self.Rect.y += self.speed
        if self.Rect.colliderect(player.Rect):
            for iteration in range(1,player.Hp+1):
                self.Hp -=1
                player.Hp -=1
                if self.Hp == 0:
                    score +=1
                    if score == second_phaze:
                        finish = True
                        index = elite_ufos.index(self)
                        del elite_ufos[index]
                    if score <first_phaze:
                        self.Rect.x =  random.randint(self.size_width,700-self.size_width)
                        self.Rect.y = random.randint(-100,-60)
                        self.Hp = self.start_hp
                    if player.Hp == 0:
                        player.Rect.x = 10000
                        finish = True
                        lost = 3
                    break
                elif player.Hp == 0:
                    player.Rect.x = 10000
                    finish = True
                    lost = 3
                    break
        else:
            if self.Rect.y > 500:
                if score < first_phaze:
                    self.Rect.x = random.randint(self.size_width,700-self.size_width)
                    self.Rect.y = random.randint(-100,-60)
                    lost +=1
                else:
                    try:
                        index = elite_ufos.index(self)
                        del elite_ufos[index]
                        lost +=1
                    except:
                        pass
    def move_and_fire(self):
        if self.Rect.y <=100:
            self.Rect.y += self.speed+1
        else:
            if self.Rect.x > 550:
                self.direction = "Left"
            elif self.Rect.x < 0:
                self.direction = "Right"
            if self.timer > 0:
                if self.direction == "Right":
                    self.Rect.x += self.speed 
                elif self.direction == "Left":
                    self.Rect.x -= self.speed 
                self.timer -= 1
            else:
                fire.play()
                bullet = Bullet(self.Rect.midbottom[0],self.Rect.midbottom[1],7,20,4,(100,205,0))
                enemy_bullets.append(bullet)
                self.timer = random.randint(45,55)
class Bullet():
    def __init__(self, x, y, size_width, size_height, speed,color):
        self.Rect = pygame.rect.Rect(x,y,size_width,size_height)
        self.speed = speed
        self.color = color
    def move(self):
        global score, bullets_amount,finish,boss,finish,lost
        if self in bullets:
            self.Rect.y -= self.speed
        else:
            self.Rect.y += self.speed
        for enemy in enemies:
            if self.Rect.colliderect(enemy.Rect):
                enemy.Hp -=player.damage
                if enemy.Hp <=0:
                    score += 1
                    enemy.Rect.x =  random.randint(enemy.size_width,700-enemy.size_width)
                    enemy.Rect.y = random.randint(-100,-60)
                    enemy.Hp = enemy.start_hp
                index = bullets.index(self)
                del bullets[index]
                bullets_amount -=1
                break
        if self.Rect.y <0:
            bullets_amount -=1
            index = bullets.index(self)
            del bullets[index]
        try:
            if self in enemy_bullets:
                if self.Rect.colliderect(player.Rect):
                    if boss_summoned is  True:
                        player.Hp -= 2
                    else:
                        player.Hp -= 1
                    if player.Hp <= 0:
                        finish = True
                        lost = 3
                    index = enemy_bullets.index(self)
                    del enemy_bullets[index]
                if self.Rect.y >500:
                    index = enemy_bullets.index(self)
                    del enemy_bullets[index]
        except:
            pass
        try:
            if self.Rect.colliderect(boss.Rect):
                boss.Hp -= player.damage
                if boss.Hp <= 0:
                    finish = True
                    score +=1
                    del boss
                index = bullets.index(self)
                del bullets[index]
                bullets_amount -=1
        except:
            pass
        try:
            for elite_ufo in elite_ufos:
                if self.Rect.colliderect(elite_ufo.Rect) and self in bullets:
                    elite_ufo.Hp -= player.damage
                    if elite_ufo.Hp <= 0:
                        score += 1
                        if score == second_phaze:
                            finish = True
                        index = elite_ufos.index(elite_ufo)
                        del elite_ufos[index]
                    index = bullets.index(self)
                    del bullets[index]
                    bullets_amount -= 1
                    break
        except:
            pass
    def draw(self,display):
        pygame.draw.ellipse(display,self.color,self.Rect)
class Boss(GameSprite):
    def __init__(self, image, x, y, size_width, size_height, speed,Hp):
        super().__init__(image, x, y, size_width, size_height, speed,Hp)
        self.Rect = pygame.rect.Rect(x,y,size_width,size_height-20)
        self.Rect.x = x
        self.Rect.y = y
        self.Left = True
        self.Right = False
    def move(self):
        global wait,finish,lost,player,boss
        self.Rect = pygame.rect.Rect(self.Rect.x,self.Rect.y,self.Rect.width,self.Rect.height)
        if self.Rect.colliderect(player.Rect):
            for iteration in range(1,player.Hp+1):
                self.Hp -=1
                player.Hp -=1
                if self.Hp == 0:
                    if player.Hp ==0:
                        finish = True
                        lost = 3
                        del boss
                    else:
                        finish=True
                        del boss
                if player.Hp == 0:
                    finish = True
                    lost = 3
                    break
        else:
            if self.Rect.x <0:
                self.Right = True
                self.Left = False
            elif self.Rect.x > 550:
                self.Right = False
                self.Left = True
            if wait >0:
                if self.Left == True:
                    self.Rect.x -= self.speed
                if self.Right == True:
                    self.Rect.x += self.speed
                wait -= 1
            else:
                self.Rect.y += self.speed-1
                wait = 15
    def move_and_fire(self):
        global wait
        self.Rect.y = 100
        if self.Rect.x > 500:
            self.Right = False
            self.Left = True
        elif self.Rect.x < 0:
            self.Right = True
            self.Left = False
        if wait > 0:
            if self.Right is True:
                self.Rect.x += self.speed
            elif self.Left is True:
                self.Rect.x -= self.speed
            wait -= 1
        else:
            wait = 45
            bullet = Bullet(self.Rect.midbottom[0],self.Rect.midbottom[1],7,20,4,(20,100,35))
            enemy_bullets.append(bullet)
            fire.play()
wait = 20
pygame.mixer.init()
fire = pygame.mixer.Sound(find_file("Music/fire.mp3"))
fire.set_volume(0.1)
Hp_icon = pygame.transform.scale(pygame.image.load(find_file("Images/Hp.png")),(30,30))
coin_icon = pygame.transform.scale(pygame.image.load(find_file("Images/money_icon.png")),(50,50))
boss_summoned = False
def level_1():
    global bullets_amount,finish,player,elite_ufos,money,score,lost,bullets,first_phaze,second_phaze,level_1_finished,enemies
    pygame.time.delay(500)
    first_phaze = 10
    second_phaze = 13
    background = pygame.transform.scale(pygame.image.load(find_file("Images/galaxy.jpg")),(700,500))
    FPS = pygame.time.Clock()
    menu_window.hide()
    best_players_window.hide()
    upgrade_ship_window.hide()
    Tip_window.hide()
    display = pygame.display.set_mode((700,500))
    pygame.display.get_window_size()[0]
    pygame.display.set_caption("Space war")
    pygame.display.set_icon(pygame.image.load(find_file("Images/Icon.ico")))
    game = True
    score = 0
    lost = 0
    bullets = []
    lost = 0       
    bullets_amount = 0
    finish = False
    enemies = [Enemy("Images/ufo.png",0,0,100,60,random.randint(1,2),1) for iteration in range(1,5)]    
    elite_ufos = [Enemy("Images/elite ufo.png",0,0,120,70,2,2) for iteration in range(1,4)]
    pygame.mixer.music.load(find_file("Music/level music.mp3"))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1.5)
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                finish = True
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if bullets_amount <=player.ammo_amount:
                        bullet = Bullet(player.Rect.x+player.Rect.width/2-5,player.Rect.y-30,7,20,4,(0,255,150))
                        bullets.append(bullet)
                        fire.play()
                        bullets_amount +=1
            if event.type == pygame.VIDEORESIZE:
                pass
        if finish == True:
            if pygame.get_init() == True:
                if lost == 3:
                    display.blit(background,(0,0))
                    display.blit(pygame.font.SysFont("Aeral",50).render(Languages[Language]["Menu_and_levels"]["Levels"][5],True,(255,255,255)),(300,250))
                    text_score = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][6]} {score}",True,(255,255,255))
                    text_lost = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][7]} {lost}",True,(255,255,255))
                    display.blit(text_score,(10,10))
                    display.blit(text_lost,(10,40))
                    player.draw(display)
                    FPS.tick(60)
                    pygame.display.flip()
                elif score == second_phaze:
                    reward = random.randint(30,50)
                    display.blit(background,(0,0))
                    display.blit(pygame.font.SysFont("Aeral",50).render(Languages[Language]["Menu_and_levels"]["Levels"][4],True,(255,255,255)),(300,250))
                    display.blit(pygame.font.SysFont("Aeral",50).render(str(reward),True,(255,255,255)),(360,290))
                    display.blit(coin_icon,(300,280))
                    text_score = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][6]} {score}",True,(255,255,255))
                    text_lost = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][7]} {lost}",True,(255,255,255))
                    display.blit(text_score,(10,10))
                    display.blit(text_lost,(10,40))
                    player.draw(display)
                    FPS.tick(60)
                    pygame.display.flip()
                    money += reward
                    level_1_finished = True
                    accounts.update_info("level_1_finished",level_1_finished,user_name)
                    accounts.update_info("money",money,user_name)
                pygame.time.delay(2000)
                pygame.quit()
            show_menu_window()
            break
        display.blit(background,(0,0))
        player.draw(display)
        player.move()
        for enemy  in enemies:
            enemy.draw(display)
            enemy.move()
        for bullet in bullets:
            bullet.draw(display)
            bullet.move()
        text_score = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][6]} {score}",True,(255,255,255))
        text_lost = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][7]} {lost}",True,(255,255,255))
        display.blit(text_score,(10,10))
        display.blit(text_lost,(10,40))
        if score >= first_phaze and finish != True:
            for enemy in enemies:
                enemy.Rect.x = 10000
                enemy.speed = 0
            for elite_ufo in elite_ufos:
                elite_ufo.draw(display)
                elite_ufo.move()
        if lost == 3:
            display.blit(background,(0,0))
            if score>=10:
                for elite_ufo in elite_ufos:
                    elite_ufo.draw(display)
                display.blit(background,(0,0))
                for elite_ufo in elite_ufos:
                    elite_ufo.draw(display)
            else:
                for enemy in enemies:
                    enemy.draw(display)
                display.blit(background,(0,0))
                for enemy in enemies:
                    enemy.draw(display)
            display.blit(pygame.font.SysFont("Aeral",50).render(Languages[Language]["Menu_and_levels"]["Levels"][5],True,(255,255,255)),(300,250))
            text_score = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][6]} {score}",True,(255,255,255))
            text_lost = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][7]} {lost}",True,(255,255,255))
            display.blit(text_score,(10,10))
            display.blit(text_lost,(10,40))
            player.draw(display)
            FPS.tick(60)
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.quit()
            show_menu_window()
            break
        FPS.tick(60)
        pygame.display.flip()
def level_2():
    global lost,score,finish,game,bullets_amount,bullets,display,boss_summoned,boss,money,first_phaze,second_phaze,level_2_finished,enemies
    first_phaze = 20
    second_phaze = 21
    background = pygame.transform.scale(pygame.image.load(find_file("Images/level_2_background.jpg")),(700,500))
    FPS = pygame.time.Clock()
    boss_summoned = False
    menu_window.hide()
    best_players_window.hide()
    upgrade_ship_window.hide()
    Tip_window.hide()
    display = pygame.display.set_mode((700,500))
    pygame.display.set_caption("Space war")
    pygame.display.set_icon(pygame.image.load(find_file("Images/Icon.ico")))
    game = True
    score = 0
    lost = 0
    bullets = []
    lost = 0       
    bullets_amount = 0
    finish = False
    enemies = [Enemy("Images/elite ufo.png",0,0,120,70,2,2) for iteration in range(1,4)]
    boss = Boss(find_file("Images/First boss.png"),250,80,160,130,2,50) 
    pygame.mixer.music.load(find_file("Music/level music.mp3"))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1.5)
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                finish = True
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if bullets_amount <=player.ammo_amount:
                        bullet = Bullet(player.Rect.x+player.Rect.width/2-5,player.Rect.y-30,7,20,4,(0,255,150))
                        bullets.append(bullet)
                        fire.play()
                        bullets_amount +=1
            if event.type == pygame.VIDEORESIZE:
                pass
        if finish is True:
            if pygame.get_init() is True:
                if lost == 3:
                    display.blit(background,(0,0))
                    display.blit(pygame.font.SysFont("Aeral",50).render(Languages[Language]["Menu_and_levels"]["Levels"][5],True,(255,255,255)),(300,250))
                    text_score = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][6]} {score}",True,(255,255,255))
                    text_lost = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][7]} {lost}",True,(255,255,255))
                    display.blit(text_score,(10,10))
                    display.blit(text_lost,(10,40))
                    player.draw(display)
                    FPS.tick(60)
                    pygame.display.flip()
                elif score >=second_phaze:
                    reward = random.randint(750,1200)
                    display.blit(background,(0,0))
                    display.blit(pygame.font.SysFont("Aeral",50).render(Languages[Language]["Menu_and_levels"]["Levels"][4],True,(255,255,255)),(300,250))
                    display.blit(pygame.font.SysFont("Aeral",50).render(str(reward),True,(255,255,255)),(360,290))
                    display.blit(coin_icon,(300,280))
                    text_score = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][6]} {score}",True,(255,255,255))
                    text_lost = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][7]} {lost}",True,(255,255,255))
                    display.blit(text_score,(10,10))
                    display.blit(text_lost,(10,40))
                    player.draw(display)
                    FPS.tick(60)
                    pygame.display.flip()
                    money += reward
                    level_2_finished = True
                    accounts.update_info("level_2_finished",level_2_finished,user_name)
                    accounts.update_info("money",money,user_name)
                pygame.time.delay(2000)
                pygame.quit()
            show_menu_window()
            break
        if finish is False:
            display.blit(background,(0,0))
            player.draw(display)
            player.move()
            for enemy in enemies:
                enemy.draw(display)
                enemy.move()
            for bullet in bullets:
                bullet.draw(display)
                bullet.move()
            text_score = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][6]} {score}",True,(255,255,255))
            text_lost = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][7]} {lost}",True,(255,255,255))
            display.blit(text_score,(10,10))
            display.blit(text_lost,(10,40))
            if score >=first_phaze and finish != True:
                if boss_summoned == False:
                    for enemy in enemies:
                        enemy.Rect.x = 10000
                        enemy.draw(display)
                boss.draw(display)
                boss.move()
            if lost == 3:
                display.blit(background,(0,0))
                if score >= first_phaze:
                    boss.draw(display)
                    display.blit(background,(0,0))
                    boss.draw(display)
                else:
                    for enemy in enemies:
                        enemy.draw(display)
                    display.blit(background,(0,0))
                    for enemy in enemies:
                        enemy.draw(display)
                display.blit(pygame.font.SysFont("Aeral",50).render(Languages[Language]["Menu_and_levels"]["Levels"][5],True,(255,255,255)),(300,250))
                text_score = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][6]} {score}",True,(255,255,255))
                text_lost = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][7]} {lost}",True,(255,255,255))
                display.blit(text_score,(10,10))
                display.blit(text_lost,(10,40))
                player.draw(display)
                FPS.tick(60)
                pygame.display.flip()
                pygame.time.delay(2000)
                pygame.quit()
                show_menu_window()
                break
        FPS.tick(60)
        pygame.display.flip()
def level_3():
    global bullets_amount,finish,player,elite_ufos,money,score,lost,bullets,enemy_bullets,first_phaze,second_phaze,level_3_finished,enemies
    first_phaze = 10
    second_phaze = 13
    background = pygame.transform.scale(pygame.image.load(find_file("Images/level_3_background.png")),(700,500))
    FPS = pygame.time.Clock()
    menu_window.hide()
    best_players_window.hide()
    upgrade_ship_window.hide()
    Tip_window.hide()
    display = pygame.display.set_mode((700,500))
    pygame.display.set_caption("Space war")
    pygame.display.set_icon(pygame.image.load(find_file("Images/Icon.ico")))
    game = True
    score = 0
    lost = 0
    bullets = []
    enemy_bullets = []
    lost = 0       
    bullets_amount = 0
    finish = False
    enemies = [Enemy("Images/First boss.png",0,0,150,110,1,10) for iteration in range(1,3)]    
    elite_ufos = [Enemy("Images/damager.png",0,0,120,70,5,1.5) for iteration in range(1,4)]
    pygame.mixer.music.load(find_file("Music/level music.mp3"))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1.5)
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                finish = True
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if bullets_amount <=player.ammo_amount:
                        bullet = Bullet(player.Rect.x+player.Rect.width/2-5,player.Rect.y-30,7,20,4,(0,255,150))
                        bullets.append(bullet)
                        fire.play()
                        bullets_amount +=1
            if event.type == pygame.VIDEORESIZE:
                pass
        if finish is True:
            if pygame.get_init() is True:
                if lost == 3:
                    display.blit(background,(0,0))
                    display.blit(pygame.font.SysFont("Aeral",50).render(Languages[Language]["Menu_and_levels"]["Levels"][5],True,(255,255,255)),(300,250))
                    text_score = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][6]} {score}",True,(255,255,255))
                    text_lost = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][7]} {lost}",True,(255,255,255))
                    display.blit(text_score,(10,10))
                    display.blit(text_lost,(10,40))
                    player.draw(display)
                    FPS.tick(60)
                    pygame.display.flip()
                elif score >= second_phaze:
                    reward = random.randint(12000,30000)
                    display.blit(background,(0,0))
                    display.blit(pygame.font.SysFont("Aeral",50).render(Languages[Language]["Menu_and_levels"]["Levels"][4],True,(255,255,255)),(300,250))
                    display.blit(pygame.font.SysFont("Aeral",50).render(str(reward),True,(255,255,255)),(360,290))
                    display.blit(coin_icon,(300,280))
                    text_score = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][6]} {score}",True,(255,255,255))
                    text_lost = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][7]} {lost}",True,(255,255,255))
                    display.blit(text_score,(10,10))
                    display.blit(text_lost,(10,40))
                    player.draw(display)
                    FPS.tick(60)
                    pygame.display.flip()
                    money += reward
                    level_3_finished = True
                    accounts.update_info("level_3_finished",level_3_finished,user_name)
                    accounts.update_info("money",money,user_name)
                pygame.time.delay(2000)
                pygame.quit()
            show_menu_window()
            break
        display.blit(background,(0,0))
        player.draw(display)
        player.move()
        for enemy  in enemies:
            enemy.draw(display)
            enemy.move()
        for bullet in bullets:
            bullet.draw(display)
            bullet.move()
        for bullet in enemy_bullets:
            bullet.draw(display)
            bullet.move()
        text_score = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][6]} {score}",True,(255,255,255))
        text_lost = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][7]} {lost}",True,(255,255,255))
        display.blit(text_score,(10,10))
        display.blit(text_lost,(10,40))
        if score >= first_phaze:
            for enemy in enemies:
                enemy.Rect.x = 10000
                enemy.speed = 0
            for elite_ufo in elite_ufos:
                elite_ufo.draw(display)
                elite_ufo.move_and_fire()
        if lost == 3:
            display.blit(background,(0,0))
            if score>=10:
                for elite_ufo in elite_ufos:
                    elite_ufo.draw(display)
                display.blit(background,(0,0))
                for elite_ufo in elite_ufos:
                    elite_ufo.draw(display)
            else:
                for enemy in enemies:
                    enemy.draw(display)
                display.blit(background,(0,0))
                for enemy in enemies:
                    enemy.draw(display)
            display.blit(pygame.font.SysFont("Aeral",50).render(Languages[Language]["Menu_and_levels"]["Levels"][5],True,(255,255,255)),(300,250))
            text_score = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][6]} {score}",True,(255,255,255))
            text_lost = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][7]} {lost}",True,(255,255,255))
            display.blit(text_score,(10,10))
            display.blit(text_lost,(10,40))
            player.draw(display)
            FPS.tick(60)
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.quit()
            show_menu_window()
            break
        FPS.tick(60)
        pygame.display.flip()
def level_4():
    global bullets_amount,finish,player,money,score,lost,bullets,enemy_bullets,first_phaze,second_phaze,level_4_finished,enemies,boss,boss_summoned
    first_phaze = 10
    second_phaze = 11
    background = pygame.transform.scale(pygame.image.load(find_file("Images/level_4_background.png")),(700,500))
    FPS = pygame.time.Clock()
    menu_window.hide()
    best_players_window.hide()
    upgrade_ship_window.hide()
    Tip_window.hide()
    display = pygame.display.set_mode((700,500))
    pygame.display.set_caption("Space war")
    pygame.display.set_icon(pygame.image.load(find_file("Images/Icon.ico")))
    game = True
    score = 0
    lost = 0
    bullets = []
    enemy_bullets = []
    lost = 0       
    bullets_amount = 0
    finish = False
    boss_summoned = False
    enemies = [Enemy("Images/damager.png",0,0,135,100,1.5,10) for iteration in range(1,3)]    
    boss = Boss("Images/Last boss.png",100,-100,240,110,1,120)
    pygame.mixer.music.load(find_file("Music/level music.mp3"))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1.5)
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                finish = True
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if bullets_amount <=player.ammo_amount:
                        bullet = Bullet(player.Rect.x+player.Rect.width/2-5,player.Rect.y-30,7,20,4,(0,255,150))
                        bullets.append(bullet)
                        fire.play()
                        bullets_amount +=1
            if event.type == pygame.VIDEORESIZE:
                pass
        if finish is True:
            if pygame.get_init() is True:
                if lost == 3:
                    display.blit(background,(0,0))
                    display.blit(pygame.font.SysFont("Aeral",50).render(Languages[Language]["Menu_and_levels"]["Levels"][5],True,(255,255,255)),(300,250))
                    text_score = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][6]} {score}",True,(255,255,255))
                    text_lost = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][7]} {lost}",True,(255,255,255))
                    display.blit(text_score,(10,10))
                    display.blit(text_lost,(10,40))
                    player.draw(display)
                    FPS.tick(60)
                    pygame.display.flip()
                elif score >= second_phaze:
                    reward = random.randint(55000,110000)
                    display.blit(background,(0,0))
                    display.blit(pygame.font.SysFont("Aeral",50).render(Languages[Language]["Menu_and_levels"]["Levels"][4],True,(255,255,255)),(300,250))
                    display.blit(pygame.font.SysFont("Aeral",50).render(str(reward),True,(255,255,255)),(360,290))
                    display.blit(coin_icon,(300,280))
                    text_score = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][6]} {score}",True,(255,255,255))
                    text_lost = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][7]} {lost}",True,(255,255,255))
                    display.blit(text_score,(10,10))
                    display.blit(text_lost,(10,40))
                    player.draw(display)
                    FPS.tick(60)
                    pygame.display.flip()
                    money += reward
                    level_4_finished = True
                    accounts.update_info("level_4_finished",level_3_finished,user_name)
                    accounts.update_info("money",money,user_name)
                pygame.time.delay(2000)
                pygame.quit()
            show_menu_window()
            break
        display.blit(background,(0,0))
        player.draw(display)
        player.move()
        for enemy  in enemies:
            enemy.draw(display)
            enemy.move_and_fire()
        for bullet in bullets:
            bullet.draw(display)
            bullet.move()
        for bullet in enemy_bullets:
            bullet.draw(display)
            bullet.move()
        text_score = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][6]} {score}",True,(255,255,255))
        text_lost = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][7]} {lost}",True,(255,255,255))
        display.blit(text_score,(10,10))
        display.blit(text_lost,(10,40))
        if score == first_phaze:
            for enemy in enemies:
                enemy.Rect.x = 10000
                enemy.speed = 0
            boss.draw(display)
            boss.move_and_fire()
        if lost == 3:
            display.blit(background,(0,0))
            for enemy in enemies:
                enemy.draw(display)
            display.blit(background,(0,0))
            for enemy in enemies:
                enemy.draw(display)
            display.blit(pygame.font.SysFont("Aeral",50).render(Languages[Language]["Menu_and_levels"]["Levels"][5],True,(255,255,255)),(300,250))
            text_score = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][6]} {score}",True,(255,255,255))
            text_lost = pygame.font.SysFont("Aeral",36).render(f"{Languages[Language]['Menu_and_levels']['Levels'][7]} {lost}",True,(255,255,255))
            display.blit(text_score,(10,10))
            display.blit(text_lost,(10,40))
            player.draw(display)
            FPS.tick(60)
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.quit()
            show_menu_window()
            break
        FPS.tick(60)
        pygame.display.flip()
if __name__ == "__main__":
    with open(find_file("active_language.json"),encoding="utf-8") as file:
        Language = json.load(file)
    if Language["language"] != None:
        Language = Language["language"]
        change_language(Language)
    else:
        show_Language_window()
    Choose_language.currentTextChanged.connect(change_language)
    app.exec_()    
  
