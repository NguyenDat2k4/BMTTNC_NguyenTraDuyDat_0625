def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5(message):
    # Khởi tạo các biến ban đầu
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476

    # Tiền xử lý chuỗi văn bản
    original_length = len(message)
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += original_length.to_bytes(8, 'little')

    # Chia chuỗi thành các block 512-bit
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]

        a0, b0, c0, d0 = a, b, c, d

        # Vòng lặp chính của thuật toán MD5
        for j in range(64):
            if j < 16:
                f = (b & c) | ((~b) & d)
                g = j
            elif j < 32:
                f = (d & b) | ((~d) & c)
                g = (5 * j + 1) % 16
# Hàm left_rotate không được định nghĩa trong ảnh,
# nhưng là một hàm cần thiết cho thuật toán MD5
def left_rotate(n, d):
    return ((n << d) | (n >> (32 - d))) & 0xFFFFFFFF

def md5(input_string):
    # Khởi tạo các giá trị ban đầu (IVs)
    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    # Tiền xử lý: đệm tin nhắn
    message = bytearray(input_string.encode('utf-8'))
    original_len_bits = (8 * len(message)) & 0xFFFFFFFFFFFFFFFF
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0x00)
    message += original_len_bits.to_bytes(8, byteorder='little')

    # Xử lý từng khối 512-bit
    for i in range(0, len(message), 64):
        chunk = message[i:i+64]
        words = [int.from_bytes(chunk[j:j+4], byteorder='little') for j in range(0, 64, 4)]

        a = a0
        b = b0
        c = c0
        d = d0

        # Vòng lặp chính (như hiển thị trong ảnh, không phải toàn bộ 64 bước MD5 tiêu chuẩn)
        for j in range(64): # Loop range assumed for MD5 steps
            # Logic tính toán f và g dựa trên các dòng 34-39 trong ảnh
            f = 0 # Khởi tạo giá trị f
            g = 0 # Khởi tạo giá trị g

            # Dòng 34: elif j < 48:
            if j < 48: # Giả định đây là phần của một chuỗi if/elif/else lớn hơn
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            # Dòng 37: else:
            else:
                f = c ^ (b | (~d))
                g = (7 * j) % 16
            
            # Cập nhật các biến a, b, c, d (dòng 41-45 trong ảnh)
            temp = d
            d = c
            c = b
            b = left_rotate((a + f + 0x5A827999 + words[g]) & 0xFFFFFFFF, 3)
            a = temp

        # Cập nhật tổng các biến a0, b0, c0, d0 (dòng 47-50 trong ảnh)
        a0 = (a0 + a) & 0xFFFFFFFF
        b0 = (b0 + b) & 0xFFFFFFFF
        c0 = (c0 + c) & 0xFFFFFFFF
        d0 = (d0 + d) & 0xFFFFFFFF

    # Trả về chuỗi băm (dòng 52 trong ảnh)
    return '{:08x}{:08x}{:08x}{:08x}'.format(a0, b0, c0, d0)

# Phần sử dụng hàm md5 (dòng 54-57 trong ảnh)
input_string = input("Nhập chuỗi cần băm: ")
md5_hash = md5(input_string)
print("Mã băm MD5 của chuỗi '{}' là: {}".format(input_string, md5_hash))