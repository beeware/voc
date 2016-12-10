for x in range(2):
    try:
        print('success', next(iter([])))
    except Exception:
        print('whoops')
