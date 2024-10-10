import string
import re


class cracking():

    def __init__(self, text):
        self.text = text
        self.key = ''

    def cal_IC(self, letter_frequencies, total_letters):
        IC = 0
        for frequency in letter_frequencies.values():
            IC += frequency * (frequency - 1)
        IC = IC / (total_letters * (total_letters - 1))
        return IC

    def cal_letter_nums(self, text, start=0, interval=1):
        letter_frequencies = {letter: 0 for letter in string.ascii_uppercase}

        i = start
        while i < len(text):
            letter_frequencies[text[i]] += 1
            i += interval

        total_letters = 0
        for frequency in letter_frequencies.values():
            total_letters += frequency

        return letter_frequencies, total_letters

    def cal_std_ic(self, letter_frequencies):
        freq_std = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.02, 0.061, 0.07, 0.002, 0.008, 0.04, 0.024, 0.067,
                    0.075, 0.019, 0.001, 0.06, 0.063, 0.091, 0.028, 0.01, 0.023, 0.001, 0.02, 0.001]
        ic = 0

        for letter, letter_frequency in letter_frequencies.items():
            ic += freq_std[ord(letter) - ord('A')] * letter_frequency

        return ic

    def key_len_hacked(self):
        text = re.sub('\s', '', self.text)
        offset_each_len = {l: 0 for l in range(2, 30)}

        for key_len in range(2, 30):
            offset = 0
            for col in range(key_len):  # 将text填入一个 key_len x (len(text) / key_len) 的矩阵，col遍历某列的所有行
                letter_frequencies, total_letters = self.cal_letter_nums(text, col, key_len)
                ic = self.cal_IC(letter_frequencies, total_letters)
                offset += abs(ic - 0.065)   # 计算所有 key_len = m 时，所有列的ic偏移之和，和最小的即为最可能得 key_len

            offset_each_len[key_len] = offset

        offset_each_len = dict(sorted(offset_each_len.items(),key= lambda item: item[1], reverse=False))
        for l, offset in offset_each_len.items():
            print(f"The length of the key is {l}, the offset sum is {offset:.4f}")

        most_possible_len = next(iter(offset_each_len.keys()))
        print("----------------------------------------------------------------------------------")
        print(f"The most possible length of the key is {most_possible_len}\n")

        return most_possible_len

    def exhaustion_subkey(self):
        print("----------------------------------Now hacking the length of the key----------------------------------")
        len_key = self.key_len_hacked()
        text = re.sub('\s', '', self.text)
        print("--------------------------------Now cracking each character of the key--------------------------------")

        key = ''
        for pos in range(len_key):
            ic_each_letter = {letter : 0 for letter in string.ascii_uppercase}
            print(
                f"----------------------------Now cracking the {pos} th character of the key--------------------------")
            print("The possibility of the letter is decreasing ...")
            for subkey in range(0, 26):
                sub_text = ''
                col = pos
                while col < len(text):
                    sub_text += chr((ord(text[col]) - ord('A') - subkey + 26) % 26 + ord('A'))
                    col += len_key
                letter_frequencies, total_letters = self.cal_letter_nums(sub_text, pos, len_key)

                for letter in letter_frequencies.keys():
                    letter_frequencies[letter] /= total_letters

                ic = self.cal_std_ic(letter_frequencies)
                letter = chr(subkey + ord('A'))
                ic_each_letter[letter] = ic

            ic_each_letter = dict(sorted(ic_each_letter.items(), key=lambda item: abs(item[1] - 0.065)))

            for letter, ic in ic_each_letter.items():
                print(f"The letter is {letter}, the value of ic is {ic:.4f}")

            most_possible_subkey = next(iter(ic_each_letter.keys()))
            key += most_possible_subkey

        print(f"The key is : {key}")

        self.key = key

    def decrypt_vegenere(self, key='', ciphertext=''):
        if key == '' and ciphertext == '':
            self.exhaustion_subkey()
            decrypt_text = ''
            cnt = 0
            for ch in self.text:
                if 'A' <= ch <= 'Z':
                    k = ord(self.key[cnt % len(self.key)]) - ord('A')
                    new_ch = chr((ord(ch) - ord('A') - k  + 26) % 26 + ord('a'))
                    decrypt_text += new_ch
                    cnt += 1
                else:
                    decrypt_text += ch

            print("\n\n")

            print("---------------------------------Now output the decrypt_text---------------------------------")

            print(decrypt_text)



if __name__ == "__main__" :
    file_path = "ciphertext2.txt"
    with open(file_path, encoding='utf-8') as file:
        text = file.read().upper()
        c2 = cracking(text)
        c2.decrypt_vegenere()


