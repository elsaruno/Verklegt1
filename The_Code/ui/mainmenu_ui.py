class MainMenu_UI:
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()

    def main_menu(self):
        print('Main menu')
        print('1) Player menu')
        print('2) Team menu')
        print('3) Club menu')
        print('4) Match menu')
        print('5) Tournament menu')
        print('q) to quit')

    def input_prompt(self):
        while True:
            self.main_menu()
            command = input('Choose menu: ')
            command = command.lower()
            if command == 'q':
                break
            elif command == '1':
                pass
            elif command == '2':
                pass
            elif command == '3':
                pass
            elif command == '4':
                pass
            elif command == '5':
                pass

