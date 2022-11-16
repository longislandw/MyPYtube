from pytube import YouTube
from datetime import datetime

run = True
while run:
    confirm = "no"

    # Get URL
    yt_URL = input('欲下載的網址:')
    # yt_URL = ""
    # if yt_URL == '':
    #     yt_URL = 'https://www.youtube.com/watch?v=WiVCliVfiTs'

    # Build YouTube Object

    try:
        yt = YouTube(yt_URL)
        # print(yt)
        confirm = input(rf"Download {yt.title}? ")
    except Exception as e:
        a = e
        print("URL not exist")

    if confirm != "no" or confirm != 'n':
        # Get Required Stream
        req_stream = -1
        abr = 0
        for stream in yt.streams.filter(only_audio=True):
            abr_ = stream.abr[0:-4]
            abr_ = int(abr_)
            if abr < abr_:
                abr = abr_
                req_stream = stream
        print(req_stream)

        # Download File
        if req_stream == -1:
            print('Unable to find request file')
        else:
            file_type = 'mp3'
            today = datetime.now()
            today1 = today.strftime("%m月%d日%H點%M分")
            download_config = {
                'output_path': 'file/',
                'filename': rf'{yt.title}.{file_type}'
            }
            req_stream.download(**download_config)

    run = input("Continue?:")
    if run == 'n' or run == 'no':
        run = False
print("Program Exit")
