import os, time, datetime, win32clipboard

img_directory = 'clip'
try:
    os.mkdir(img_directory)
    print(f'{img_directory} is created...')
except FileExistsError as e:
    print(e)

is_created_clipboard_record = False
latest_clipboard_data = ''
old_clipboard_data = latest_clipboard_data
while True:
    win32clipboard.OpenClipboard()
    try:
        latest_clipboard_data = win32clipboard.GetClipboardData()
        if old_clipboard_data != latest_clipboard_data:
            date_copied = datetime.datetime.today()
            with open(f'{img_directory}\clip_record.txt', 'a') as f:
                f.write(f'[(+)][{date_copied}]:(+):{latest_clipboard_data}\n')
            print(f'[{date_copied}]: {latest_clipboard_data}')
            old_clipboard_data = latest_clipboard_data
    
    except TypeError as clip_exception:
        print('Clip Board Data Access Error: ', clip_exception)
    win32clipboard.CloseClipboard()
    time.sleep(0.1)

