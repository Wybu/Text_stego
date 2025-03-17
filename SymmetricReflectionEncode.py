class SymmetricReflectionCipher:
    def __init__(self):
        # Nhóm chữ cái theo tính đối xứng
        self.groups = {
            "00": "FGJLNPRSZ",
            "01": "BCDEK",
            "10": "AMTUVWY",
            "11": "HIOX"
        }
        
        # Tạo bảng mã hóa từ nhóm chữ cái
        self.encode_map = {}
        for bits, letters in self.groups.items():
            for letter in letters:
                self.encode_map[letter] = bits
                self.encode_map[letter.lower()] = bits
        
        # Tạo bảng giải mã
        self.decode_map = {v: k for k, v in self.encode_map.items()}
    
    def encode(self, text):
        binary_string = "".join(self.encode_map.get(c, "") for c in text if c in self.encode_map)
        return binary_string
    
    def decode(self, binary_string):
        decoded_text = "".join(self.decode_map.get(binary_string[i:i+2], "?") for i in range(0, len(binary_string), 2))
        return decoded_text

# Ví dụ sử dụng
cipher = SymmetricReflectionCipher()
text = "Hello World"
cipher_text = cipher.encode(text)
print("Mã hóa:", cipher_text)

decoded_text = cipher.decode(cipher_text)
print("Giải mã:", decoded_text)
