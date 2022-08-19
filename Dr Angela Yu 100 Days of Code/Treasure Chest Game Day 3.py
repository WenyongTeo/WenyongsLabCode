print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
while True:
    print('Wanna play?')
    play = (input("Enter Choice (Y or N): "))
    print(f'Option {play} selected\n')
    if play.lower() in 'y':
        wheretoGO= input("You wanna go left or right? choose one (Left or Right): ").lower()
        if wheretoGO in 'left':
            print("\nYou have reached a river... but you have no boat... uwu. So you wanna swim across or wait?\n")
            swimOrWait = input('(Swim or Wait): ').lower()
            if swimOrWait in 'wait':
                print('\nYour boat has arrived WOOHOOO!!!! WE SAIL WITH ODIN TONIGHT!!!!\n')
                print('You have reach a room with "Treasure" sign, There is Three doors. Red, Yellow and Blue. Choose wisely Viking.. There is only 1 correct door.\n')
                door = input('Red Yellow or Blue:').lower()
                if door in 'red':
                    print('\nYour bitch ass got burnt... Game Over\n')
                elif door in 'blue':
                    print('\nYou got raped by troll... Such sadness. Game over\n')
                elif door in 'yellow':
                    print("\nYou won!!!! Here's your reward, The Krato's Axe\n")
                    print('''
                                               ..
                                   ;:
                                  .::.
                                 . ::`.                      `;.
                                :  ::  :                      ; :.
                               :   ::   :                    .;  :.
                              :    ::    :                   ::   :.
                             :     ::     :                .::    ::
                             :     ::     :               .::      ::
                             `.    ::    .               .::       ::
                              `.   ::   .               .::         ::
                                `. :: .               .::           ::
                                 :    :            .:::             :;
                          _--.   :....:       ...::::               :::
                      __-`    `-.:....:.---:::::::                  ::;
            ___----           ..............                        ::;
        --==___===============..............                        ::;
               ----___          .........:::::..                    ::;
                      ``-_    .  :\\//: ```:::::::..                :;
                          `--    ://\\:        ``:::::.             :;
                                 :\\//:            ``:::.           :;
                                 ://\\:               `::.         :;
                                 :\\//:                :::.        :;
                                 ://\\:                :::;       :;
                                 :\\//:                ::::      :;
                                 ://\\:                :::      :;
                                 :\\//:                :::      :
                                 ://\\:               :::      :
                                 :\\//:               :::     :
                                 ://\\:               ;;     :
                                 :\\//:               ;     :
                                 :THOR:              ;     :
                                 [____]              ;    :
                                 [____]             ;    :
                                 [____]            .    :
                                 [____]           .    :
                                 [____]          .   .:`
                                 [____]         .    :
                                 :\\//:         :    :
                                 ://\\:         `.   `.
                                 :\\//:          `.   `.
                                 ://\\:            `.   ;
                                 [____]              `..
                                 [____]
                                 [____]
                                 [____] 
                                 [____]
                                 [____]
                                 :....:
                               .-  :: `-.
                             .     ::  ..`.
                            /      ::  `   \
                           :       ::       ;
                           ::::::::::::::::::
                           :       ::       ;
                            \      ::      /
                             `.    ::    .
                               `-..::..-
                    ''')
                else:
                    print("\nGame over\n")
            else:
                print('\nYour dumb ass got attacked by a serpent haha bitch\n')
        else:
            print("\nFall into a hole. Game Over\n")
    else:
        break
        print('Not much of an Adventurer eh?')