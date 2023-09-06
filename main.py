import os, time, datetime, win32clipboard

clip_record_directory = 'clip'
clip_record_file_names = [
    'clip_record',
    'clip-record-IT-videos-special',
    'clip-record-TCP-and-Sockets-videos-special',
    'clip-record-various-videos',
    'clip-record-web-development'
    ]

print('Choose from the folllowing text files below:')
for i in range(len(clip_record_file_names)):
    print(f'[{i}]', clip_record_file_names[i])

file_index = int(input(f'Enter the file index (0-{len(clip_record_file_names)-1}): '))
clip_record_file = clip_record_file_names[file_index]

try:
    os.mkdir(clip_record_directory)
    print(f'{clip_record_directory} is created...')
except FileExistsError as e:
    print(e)

is_created_clipboard_record = False
latest_clipboard_data = ''
old_clipboard_data = latest_clipboard_data
while True:
    try:
        win32clipboard.OpenClipboard()
    except win32clipboard.pywintypes.error as err:
        print(f'Opening Clipboard Error: {err}')
        continue
    date_copied = datetime.datetime.today()
    try:
        latest_clipboard_data = win32clipboard.GetClipboardData()
        if old_clipboard_data != latest_clipboard_data:
            
            with open(f'{clip_record_directory}\{clip_record_file}.txt', 'a') as f:
                f.write(f'[(+)][{date_copied}]:(+):{latest_clipboard_data}\n')
            print(f'Writing to ({clip_record_file}) -> [{date_copied}]: {latest_clipboard_data}')
            old_clipboard_data = latest_clipboard_data
    
    except TypeError as clip_exception:
        print('Clip Board Data Access Error: ', clip_exception)
    except Exception as general_exception:
        print('General Error: ', general_exception)
        with open('error-log-folder\error-log-file.txt', 'a') as f:
            f.write(f'[{date_copied}]: {general_exception}\n')
        break
    win32clipboard.CloseClipboard()
    time.sleep(0.1)

