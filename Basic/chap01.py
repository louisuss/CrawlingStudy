import urllib.request as req
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

img_url = 'http://blogfiles.naver.net/MjAyMDA2MTdfMjQ2/MDAxNTkyMzg1Nzg0ODM3.dl8fSJaSDa77W8Fj8ZkNT2B2nI15erLfzRGjsQvSqQsg.d_tuKjhMeu4G4DeI0873FGc-dvX1yEwFxyskF_UTDHkg.JPEG.noisy002/200617_%C0%CC%C1%F6%C0%BA_4.jpg'

save_path = '/Users/louis/image.jpg'
try:
    # 리턴 값 2개: 지정한 파일 이름, 수신 헤더 값
    file, header = req.urlretrieve(img_url, save_path)
except Exception as e:
    print("Failed")
    print(e)
else:
    # Header 정보 출력
    print(header)
    # 다운로드 파일 정보
    print('Filename {}'.format(file))
