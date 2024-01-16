import speedtest

teste = speedtest.Speedtest()

#download
print("testando download...")
velocidade_download = teste.download()
print(f'Velocidade de download: {velocidade_download / 10**6:.2f}')

#upload
print("testando upload...")
velocidade_upload = teste.upload()
print(f'Velocidade de upload: {velocidade_upload / 10**6:.2f}')


#ping
ping = teste.results.ping
print(f'Ping: {ping / 10**6:.2f}')