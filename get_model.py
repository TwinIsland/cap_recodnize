
import os
import beautiful_output

def status(word):
    word = str(word)
    if word.upper() != 'OK':
        beautiful_output.red_normal('--> Status: ' + '[' + "Error because " + str(word) + ']')

        input('Enter to quit...')
        os._exit(0)

    beautiful_output.green_normal('--> Status: ' + '[' + str(word) + ']')


# check the file loss

fileLib = ['beautiful_output.py', 'clean.py', 'data_generator.py', 'DB.py', 'font.ttf', 'generator.py', 'get_model.py', 'train.py']
file = os.listdir('./')

print('INITIALIZE...')

try:
    import train
except Exception as e:
    status(e)


if 'model.m' in file:
    if input('Detect you already have model.m file, Train the model again?(Y/N): ').upper() != 'Y':
        input('Enter to quit...')
        os._exit(0)

# check teh file satisfied

print('Processing...')
for f in fileLib:
    if f in file:
        continue
    else:
        status('Loss file called: ' + f + ', please re-clone the program!')


print('\n')
train.execute_program()


# clean the resource dictionary
os.system('rd /s/q train_data')
os.system('md train_data')


# stay
input()

