try:
    print('outer try')
    try:
        print('inner try')
    except:
        print('inner except')
except:
    print('outer except')
