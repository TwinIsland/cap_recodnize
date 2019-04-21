
import os
from crack_cap import beautiful_output, train

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

print('INITIALIZE...',end='      ')
try:
    from crack_cap import beautiful_output, train
    status('OK')
except Exception as e:
    status(e)


if 'model.m' in file:
    if input('Detect you already have model.m file, Train the model again?(Y/N): ').upper() != 'Y':
        input('Enter to quit...')
        os._exit(0)

# check teh file satisfied

print('Processing...',end='      ')
for f in fileLib:
    if f in file:
        continue
    else:
        status('Loss file called: ' + f + ', please re-clone the program!')

status('OK')
print('\n')
train.execute_program()

