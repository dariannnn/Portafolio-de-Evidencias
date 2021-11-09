import argparse
import sys
import configparser
import detectEsp

parser = argparse.ArgumentParser()
parser._action_groups.pop()
required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')
required.add_argument('-modo',dest='modo',help=' Indica la acción a realizar: Encriptar [e] Desencriptar [d] Crackear   [c] ')
required.add_argument('-msj',dest='msj',help=' Mensaje para crackear, cifrar o desencriptar ')
optional.add_argument('-clave',dest='clave',help=' Palabra clave para el proceso de cifrar o descifrar  ')
args = parser.parse_args()

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
translated = ''

if args.modo == "c":
    print('Hacking...')
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')
    for key in range(1,len(args.msj)):
        print('Trying key #%s...' % (key))
        translated = ''
        for symbol in args.msj:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)
    
                translated = translated + SYMBOLS[translatedIndex]
            else:
                translated = translated + symbol
        
        if detectEsp.isEsp(translated):
            print()
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, translated[:100]))
            print()
            print('Enter D if done, anything else to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                print(translated)
                break

else:
    espacios = 1
    while espacios > 0:
        clave = args.clave
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)

    for symbol in args.msj:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            if args.modo == "e":
                translatedIndex = symbolIndex + key
            elif args.modo == "d":
                translatedIndex = symbolIndex - key
        
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol

    print(translated)
