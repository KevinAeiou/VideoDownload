from pytube import YouTube

def baixaVideo(listaURL):
    for URL in listaURL:
        print(f'Download iniciado!')
        yt = YouTube(URL)
        video = yt.streams.get_highest_resolution()
        video.download('C:/Users/Kevin/Videos/VoceEmForma/PrimeiraMaratona')
        print(f'Download concluído!')
        print(f'_____________________________')

if __name__=='__main__':
    listaVideo = [
    'https://www.youtube.com/watch?v=NeXXJxd8lPc',
    'https://www.youtube.com/watch?v=NlNNUQm6yX8',
    'https://www.youtube.com/watch?v=benDHl-0UPs',
    'https://www.youtube.com/watch?v=wb7IuZ3z8vA',
    'https://www.youtube.com/watch?v=t8DVjz0LtZE',
    'https://www.youtube.com/watch?v=FGgIJGwL2oQ',
    'https://www.youtube.com/watch?v=hDtZ2OhlrhM',
    'https://www.youtube.com/watch?v=mgZcaMfiFq4',
    'https://www.youtube.com/watch?v=rFFx8XsieSg',
    'https://www.youtube.com/watch?v=1ozb67uZG14',
    'https://www.youtube.com/watch?v=pRoLLkyFHXM',
    'https://www.youtube.com/watch?v=Ma7wDIFXQ7Q',
    'https://www.youtube.com/watch?v=DDSZ723943M',
    'https://www.youtube.com/watch?v=5jV-cJAJ5pE',
    'https://www.youtube.com/watch?v=1mzBkBnLzXU',
    'https://www.youtube.com/watch?v=eWKgC3dzIF8',
    'https://www.youtube.com/watch?v=HbK0-0JJ5ro',
    'https://www.youtube.com/watch?v=bJMcXQi_KLY',
    'https://www.youtube.com/watch?v=nYKIfC5ACos',
    'https://www.youtube.com/watch?v=xBzC_sMhp-U',
    'https://www.youtube.com/watch?v=LNj3ec7-qxg',
    'https://www.youtube.com/watch?v=U_CiyjPEtVg',
    'https://www.youtube.com/watch?v=0JqzQW0NEpw',
    'https://www.youtube.com/watch?v=yIpuI2VdEOg',
    'https://www.youtube.com/watch?v=VT7CVboIq2c']

    baixaVideo(listaVideo)