# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

p1 = str(input())
p2 = str(input())
if p1 == 'scissors' and p2 == 'paper':
    print('Player 1 won!')
if p1 == 'scissors' and p2 == 'rock':
    print('Player 2 won')
if p1 == 'scissors' and p2 == 'scissors':
    print('Draw')
if p1 == 'rock' and p2 == 'scissors':
    print('Player 1 won!')
if p1 == 'rock' and p2 == 'paper':
    print('Player 2 won!')
if p1 == 'rock' and p2 == 'rock':
    print('Draw')
if p1 == 'paper' and p2 == 'scissors':
    print('Player 2 won!')
if p1 == 'paper' and p2 == 'rock':
    print('Player 1 won!')
if p1 == 'paper' and p2 == 'paper':
        print('Draw')