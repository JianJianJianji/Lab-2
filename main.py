def main():
    print("ET0735( Lab 2)")
    n1,n2=get_user_input()
    display_main_menu()

    calc_average(n1,n2)

def display_main_menu():
    print("display_main_menu")

def get_user_input():
     n1 = float(input('Enter a Number:'))
     n2= float(input ('Enter a Number:'))
     return n1,n2


def calc_average(n1,n2):
    average = (n1+n2)/2.0
    print(average)
if __name__=="__main__":
    main()