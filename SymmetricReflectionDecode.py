def decode_reflective_symmetry(text):
    # Bảng ánh xạ ký tự sang bit dựa theo bảng đã cho
    bit_mapping = {
        'F': '00', 'G': '00', 'J': '00', 'L': '00', 'N': '00', 'P': '00', 'Q': '00', 'R': '00', 'S': '00', 'Z': '00',
        'B': '01', 'C': '01', 'D': '01', 'E': '01', 'K': '01',
        'A': '10', 'M': '10', 'T': '10', 'U': '10', 'V': '10', 'W': '10', 'Y': '10',
        'H': '11', 'I': '11', 'O': '11', 'X': '11'
    }

    # Tách câu và lấy chữ cái đầu tiên
    sentences = text.split('. ')  # Giả định các câu cách nhau bởi dấu chấm + khoảng trắng
    bits = ''

    for sentence in sentences:
        if sentence:  # Kiểm tra nếu câu không rỗng
            first_char = sentence[0].upper()  # Chuyển thành chữ hoa
            if first_char in bit_mapping:
                bits += bit_mapping[first_char]

    # Chuyển chuỗi bit thành ký tự ASCII
    decoded_text = ''
    for i in range(0, len(bits), 8):  # Mỗi ký tự là 8 bit
        byte = bits[i:i+8]
        if len(byte) == 8:
            decoded_text += chr(int(byte, 2))

    return decoded_text

# Văn bản mã hóa (thay thế bằng dữ liệu thực tế)
encoded_text = "Alice met Tom. Henry is kind. Oscar loves music. Xavier plays violin."
decoded_message = decode_reflective_symmetry(encoded_text)
print("Thông điệp giải mã:", decoded_message)
