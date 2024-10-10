import string


class cracking():


    def __init__(self, file_path):
        with open(file_path, encoding='utf-8') as file:
            self.text = file.read()
            self.count_letter_frequencies()
            self.count_bigram_frequencies()
            self.count_trigram_frequencies()
            self.start_end_with()
            self.key = {}



    """Calculate MR"""
    def cal_MR(self, letter_frequencies):
        MR = 0
        for f in letter_frequencies.values():
            MR += f * f
        MR -= 0.0385

        print(MR)  # MR = 0.02730493312419833 ,单表密码


    def count_letter_frequencies(self):
        letter_frequencies = {letter: 0 for letter in string.ascii_uppercase}
        total_letters = 0
        for ch in self.text:
            if 'A' <= ch <= 'Z':
                letter_frequencies[ch] += 1
        for frequency in letter_frequencies.values():
            total_letters += frequency

        for letter in letter_frequencies:
                letter_frequencies[letter] =  letter_frequencies[letter]/total_letters

        self.cal_MR(letter_frequencies)

        letter_frequencies = dict(sorted(letter_frequencies.items(), key=lambda item: item[1],
                                            reverse=True))
        for letter, frequency in letter_frequencies.items():
            print(f"{letter} : {frequency:.4f}")

    def count_bigram_frequencies(self):
        bigram_frequencies = {}
        for i in range(len(self.text) - 1):
            if self.text[i] != " " and self.text[i + 1] != " ":
                bigram = self.text[i:i + 2]
                if bigram not in bigram_frequencies:
                    bigram_frequencies[bigram] = 1
                else:
                    bigram_frequencies[bigram] += 1

        bigram_top = sorted(bigram_frequencies, key=bigram_frequencies.get, reverse=True)

        for i in range(31):
            print(bigram_top[i], end=' ')

        print("\n")



    def count_trigram_frequencies(self):
        trigram_frequencies = {}
        for i in range(len(self.text) - 2):
            if self.text[i] != " " and self.text[i + 1] != " " and self.text[i + 2] != " ":
                trigram = self.text[i:i + 3]
                if trigram not in trigram_frequencies:
                    trigram_frequencies[trigram] = 1
                else:
                    trigram_frequencies[trigram] += 1

        trigram_top = sorted(trigram_frequencies, key=trigram_frequencies.get, reverse=True)

        for i in range(11):
            print(trigram_top[i], end=' ')

        print("\n")

    def start_end_with(self):
        words = self.text.split()
        end_with_letter = {letter: 0 for letter in string.ascii_uppercase}
        start_with_letter = {letter: 0 for letter in string.ascii_uppercase}
        for word in words:
            end_with_letter[word[-1]] += 1
            start_with_letter[word[0]] += 1

        start_with_letter = sorted(start_with_letter, key = start_with_letter.get, reverse = True)
        end_with_letter = sorted(end_with_letter, key=end_with_letter.get, reverse=True)

        print(start_with_letter[0:4])
        print((end_with_letter[0:4]))


    def modify(self, new):
        self.key.update(new)
        decrypted_text = ''
        for ch in self.text:
            if ch in self.key.keys():
                    decrypted_text += self.key[ch]
            else:
                decrypted_text += ch
        print("This is the decrypted text:\n")
        print(decrypted_text)

        print("\n")

        for ch in decrypted_text:
            if ch.isupper():
                print(ch)



c1 = cracking('ciphertext1.txt')
text = c1.text
"""c1.modify({'A': 'e',  'J': 't',  'H': 'h',  'N': 'r', 'L': 'f',  'Y' : 's',
           'I': 'a',  'Q': 'w',  'G': 'o',  'M': 'y', 'E':'c' ,  'S': 'i',
           'V': 'n',  'P': 'd',  'F': 'v',  'K': 'm', 'Z' :'l',  'R': 'p',
           'W': 'g',  'U': 'u',  'T': 'b',  'O': 'k', 'C':'q',  'B': 'x',
           'X': 'z',  'D': 'j'
           })"""


