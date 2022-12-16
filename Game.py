from Card import Card
import copy


class Play(Card):

    def happy_end(self, lst):
        '''
              Проверяет остались ли в карточке незакрашенные значения!!!
              :param lst: принимает карточку
              :return: bool
              '''
        for s in lst:
            for n in s:
                if type(n) != str:
                    return False
        return True

    def recognition(self, check, lst):
        status = False
        for s in range(len(lst)):
            if check in lst[s]:
                indx = lst[s].index(check)
                lst[s][indx] = 'X'
                status = True
        return lst, status

    def fight_manually(self):
        check = self.barrel(1)[0]

        print(f'Выпало: {check}\n')

        user1 = copy.deepcopy(self.user)

        computer, status_pc = self.recognition(check, self.computer)
        user, status_user = self.recognition(check, self.user)

        if status_pc:
            print('PC зачеркнул')
            self.show_card(computer)
            print()
        else:
            print('У PC ничего нет')
            self.show_card(computer)
            print()

        if status_user:
            self.show_card(user1)
            us = input('У вас есть? Д/Н\n')
            if us.upper() != 'Д':
                print('Проиграл!!!')


        else:
            self.show_card(user1)
            us = input('У вас есть? Д/Н\n')
            if us.upper() != 'Н':
                print('Проиграл!!!')

        return computer, status_pc, user, status_user

    def fight_auto(self):
        check = self.barrel(1)[0]

        print(f'Выпало: {check}\n')

        computer, status_pc = self.recognition(check, self.computer)
        user, status_user = self.recognition(check, self.user)

        self.show_card(computer)
        self.show_card(user)

        return computer, status_pc, user, status_user

    def go(self):

        text = '''
        ===== Выбирите игру =====

        1. Автоматически
        2. Вручную    
        '''.strip()

        select = input(f'{text}\n')
        if select == '1':
            auto = True

        else:
            auto = False

        self.computer = self.get_card()
        self.user = self.get_card()

        if auto:
            while True:
                comp, st_PC, user, st_user = self.fight_auto()
                PC = self.happy_end(comp)
                USER = self.happy_end(user)
                if PC:
                    print('Выиграл Computer...')
                    self.show_card(comp)
                    self.show_card(user)
                    break
                if USER:
                    print('Вы выиграли !!!')
                    self.show_card(comp)
                    self.show_card(user)
                    break
        else:
            while True:
                comp, st_PC, user, st_user = self.fight_manually()
                PC = self.happy_end(comp)
                USER = self.happy_end(user)
                if PC:
                    print('Выиграл Computer...')
                    self.show_card(comp)
                    self.show_card(user)
                    break
                if USER:
                    print('Вы выиграли !!!')
                    self.show_card(comp)
                    self.show_card(user)
                    break


if __name__ == '__main__':
    play = Play()
    play.go()





