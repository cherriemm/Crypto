# 补全引用库
import serial
import numpy as np
from Crypto.Cipher import AES


# 补全函数参数
mega = serial.Serial('COM3', 115200, timeout=1)

def get_meta():
    # 产生随机明文，补全函数参数
    p = np.random.randint(0, 256, 16, dtype=np.uint8)
    send = p.tobytes()
    # 发送数据到开发板，补全函数
    mega.write(send)
    # 读取加密结果，补全函数
    recv = mega.read(16)
    c = np.frombuffer(recv, dtype=np.uint8)
    return p, c



# 与开发板设置相同的密钥，验证开发板结果
key = bytes([0x00, 0x13, 0x3A, 0x5f, 
            0x04, 0x36, 0x1b, 0x45, 
            0x08, 0x96, 0x67, 0x26, 
            0x0c, 0x35, 0x2e, 0x53])

aes = AES.new(key, AES.MODE_ECB)

# 验证函数，使用Crypto库的AES类验证开发板结果是否正确
def verify(p, c):
    # 补全函数
    c_correct = aes.encrypt(p.tobytes())
    if c.tobytes() == c_correct:
        return True
    else:
        return False

# 得到随机明文和开发板的加密结果
p, c = get_meta()

# 使用验证函数验证开发板结果是否正确
result = verify(p, c)
print("验证结果:", result)