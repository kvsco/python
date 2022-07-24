def sing():
    return 'sing'

def cry():
    return 'cry'

print(f'song.py: {__name__}')

if __name__ == "__main__":
    print(sing())
    print(f'main_song : {__name__}')