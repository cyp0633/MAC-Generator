import random

manufacturer = {
    'HUAWEI': ['00:18:82', '00:25:9E', '00:E0:FC', '04:C0:6F', '0C:37:DC', '10:C6:1F', '1C:1D:67', '28:3C:E4'],
    'CISCO': ['00:00:0C', '00:01:42', '00:01:43', '00:01:97'],
    'LINKSYS': ['00:04:5A', '00:06:25', '00:0C:41'],
    'NETGEAR': ['E0:91:F5', 'E0:46:9A', 'C4:3D:C7'],
    'RUIJIE': ['00:11:AD'],
    'ZTE': ['D0:15:4A', 'C8:64:C7', 'B4:B3:92', 'B0:75:D5'],
    'FOXCONN': ['00:01:6C', '00:15:58', '98:E7:9A'],
    'CLEVO': ['00:90:F5'],
    'LENOVO': ['00:06:1B', '00:12:FE', 'D8:71:57'],
    'TONGFANG': ['00:16:3D', '00:27:78', '00:26:46'],
    'DELL': ['F0:4D:A2', 'D0:67:E5', 'BC:30:5B', 'B8:AC:6F', 'A4:BA:DB'],
    'HEWLETT-PACKARD': ['F4:CE:46', 'D8:D3:85', 'D4:85:64'],
    'ACER': ['00:00:E2'],
    'ASUS': ['F4:6D:04', 'E0:CB:4E', 'BC:AE:C5'],
}


def ConvertToHex(num):
    num_str = '0123456789ABCDEF'
    if num == 0:
        return '00'
    hex = []
    while num != 0:
        num, i = divmod(num, 16)
        hex.append(num_str[i])
    if len(hex) == 1:
        hex.append('0')
    return ''.join(reversed(hex))


def main():
    with open('./MacOutput.txt', 'a') as f:  # Open file
        for i in manufacturer:
            f.write('{}:\n'.format(i.title()))  # Print manufacturer name
            MacNum = len(manufacturer[i])
            for j in range(10):
                a = ConvertToHex(random.randint(0, 255))
                b = ConvertToHex(random.randint(0, 255))
                c = ConvertToHex(random.randint(0, 255))
                # Randomly choose prefixes of a certain manufacturer
                prefix = manufacturer[i][random.randint(0, MacNum-1)]
                f.write(prefix+':'+a+':'+b+':'+c+'\n')

    return


if __name__ == '__main__':
    main()
