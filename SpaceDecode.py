import re

def extract_hidden_bits(text):
    """
    Trích xuất chuỗi bit từ khoảng trắng trong văn bản.
    Khoảng trắng đơn (" ") biểu diễn '0'
    Khoảng trắng kép ("  ") biểu diễn '1'
    """
    words = text.split(" ")
    hidden_bits = []

    for i in range(len(words) - 1):  # Duyệt qua từng khoảng trắng giữa các từ
        if words[i] == "":  # Nếu phát hiện khoảng trắng kép
            hidden_bits.append("1")
        else:
            hidden_bits.append("0")
    
    return "".join(hidden_bits)

def binary_to_text(binary_str):
    """
    Chuyển chuỗi nhị phân thành văn bản ASCII.
    """
    chars = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]  # Chia thành các byte (8 bit)
    message = "".join([chr(int(c, 2)) for c in chars if len(c) == 8])  # Chuyển thành ký tự
    return message

def decode_stego_text(stego_text):
    """
    Giải mã tin ẩn từ văn bản chứa tin.
    """
    hidden_bits = extract_hidden_bits(stego_text)
    decoded_message = binary_to_text(hidden_bits)
    return decoded_message

# ==== 🔹 Ví dụ Văn bản chứa tin ẩn 🔹 ====
stego_text = "abcddeabcdde"

# ==== 🔹 Giải mã tin ẩn 🔹 ====
decoded_message = decode_stego_text(stego_text)
print("🔍 Thông điệp giấu trong văn bản:", decoded_message)
