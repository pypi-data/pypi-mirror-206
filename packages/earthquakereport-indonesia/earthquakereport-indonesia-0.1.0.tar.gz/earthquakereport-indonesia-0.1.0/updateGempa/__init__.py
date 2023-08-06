import bs4
import requests

def ekstraksi_data():
    """
    Tanggal     : 01 Mei 2023
    Waktu       : 10:20:12 WIB
    Magnitude   : 3.8
    Kedalaman   : 10 km
    Lokasi      : LS = 4.01 BT = 136.07
    Episentrum  : Pusat gempa berada di darat 12 km Timur Laut Dogiyai
    Testimoni   : Dirasakan (Skala MMI): II Dogiyai
    :return:
    """

    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None
    if content.status_code == 200:
        soup = bs4.BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')

        i = 0
        magnitude = None
        kedalaman = None
        koordinat = None
        lokasi = None
        dirasakan = None
        ls = None
        bt= None
        for res in result:
            if i == 1:
                magnitude = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1


        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitude'] = magnitude
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        return hasil

    else:
        return None

def tampilkan_data(result):

    if result is None:
        print('Tidak bisa menemukan data gempa terkini')
        return

    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitude {result['magnitude']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Koordinat: LS =  {result['koordinat']['ls']}, BT =  {result['koordinat']['bt']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"{result['dirasakan']}")

if __name__ == '__main__':
    result = ekstraksi_data()
    tampilkan_data(result)