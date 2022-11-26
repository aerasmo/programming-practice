def head_smash(arr):
    if not arr:
        return "Gym is empty"
    try:
        # try replacing heads
        return [e.replace('O', ' ') for e in arr]
    except TypeError:
        return "This isn't the gym!!"

# print(head_smash(
# [
# '*****************************************',
# '***********   _O_   *   _O_   ***********',
# '**  _O_   *  /(.)J  *  /(.)J  *   _O_  **',
# '** /(.)J  *  _| |_  *  _( )_  *  /(.)J **',
# '** _( )_  *********************  _( )_ **',
# '******************* X ******************']))

# print(head_smash([1,2,3]))
# print(head_smash(123))
# print(head_smash(''))