BUF_SIZE = 1024
with open('src.png', 'rb') as sf, open('dst.png', 'wb') as df: # 1
    while True:
        data = sf.read(BUF_SIZE) # 2
        if not data:
            break # 3
        df.write(data) # 4