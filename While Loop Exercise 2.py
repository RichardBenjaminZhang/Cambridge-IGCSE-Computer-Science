secretPassword = 'MacBookPro'

guessedPassword = ' '

while(guessedPassword != secretPassword):

    guessedPassword = input('Password?')
    if(guessedPassword != secretPassword):
        print('Password incorrect! You have three times to try.')

print('Password is correct,Welcome Sir!')
