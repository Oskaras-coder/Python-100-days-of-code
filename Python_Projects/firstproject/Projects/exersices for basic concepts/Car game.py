pasikartojimas = None
while True:
    veiksmas = str(input('>'))
    if(veiksmas == 'help'):
        print('start - to start a car\nstop - to stop the car\nquit - to exit')
    elif veiksmas == 'start' and pasikartojimas != 'start':
        print('Car started...Ready to go')
    elif veiksmas == 'stop' and pasikartojimas != 'stop':
        print('Car stopped')
    elif veiksmas == 'quit':
        break
    elif veiksmas == 'stop' and pasikartojimas == 'stop':
        print('Wtf..Car is already stopped')
    elif veiksmas == 'start' and pasikartojimas == 'start':
        print('Wtf..Car is already started')
    else:
        print('I don`t understand')
    pasikartojimas = veiksmas