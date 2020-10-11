from pyfiglet import Figlet

f = Figlet(font='slant')

def main():
    on = True
    while on:
        print("Choose network")
        selection = input("Please select one of the options listed above")
        if selection != 'off':
            print('Welcome to stellar wallet')

        else:
            print("goodbye")
            on = False


if __name__ == '__main__':
    f = Figlet(font='slant')
    print(f.renderText('Stellar Network Interface'))
    main()
