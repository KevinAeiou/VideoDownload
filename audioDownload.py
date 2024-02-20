from pytube import YouTube

def baixaAudio(listaURL):
    for URL in listaURL:
        print(f'Download iniciado!')
        yt = YouTube(URL)
        audio = yt.streams.filter(only_audio=True)[0]
        audio.download('C:/Users/Kevin/Downloads')
        print(f'Download concluído!')
        print(f'_____________________________')

if __name__=='__main__':
    listaURL = ['https://youtu.be/_w1w9mcSdl4?si=IGod6Tr5AvaR23rV',
    'https://youtu.be/JIA7sVhJiPA?si=Sv15kjWijy3t1G9x',
    'https://youtu.be/saW3pCxk7Tc?si=2pMFbh9WDYJ1RLwW',
    'https://youtu.be/12zm6wThD20?si=UZp-eF5aHCrnsPvN',
    'https://youtu.be/ScaoLZncg10?si=ib_Fc06BbWKbnmQa',
    'https://youtube.com/watch?v=XCzDPMT_QME&feature=shared',
    'https://youtu.be/R9zZTlr0wSM?si=8hxvzjeGz1cWeUsl',
    'https://youtu.be/uqQj73EPCxo?si=dB_KR4OKsFL3Lxbn']
    baixaAudio(listaURL)