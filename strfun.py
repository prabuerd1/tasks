class StringValidation:
    # sample input: str1 = "AEIO bcd 123 #$@"
    # sample input:str1 = "AEIO bcd 123 #$@ zQvX"
    def __init__(self):
        self.str1 = input("Enter the word:")
        print("You entered word is:", self.str1)
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0

    def validaton(self):
        str2 = self.str1.lower()

        for S in str2:
            self.even_no_vowels(S)
            self.not_have_zqvx(S)
            self.odd_no_numbers(S)
            self.spl3_char(S)

        self.result()
        return 0

    def even_no_vowels(self, temp):
        s = temp

        if(s == "a" or s == "e" or s == "i" or s == "o" or s == "u"):
            # print("vowels=",s)
            self.a += 1

        return self.a

    def not_have_zqvx(self, temp):
        s = temp

        if(s == "z" or s == "q" or s == "v" or s == "x"):
            # print("zqvx=",s)
            self.b += 1

        return self.b

    def odd_no_numbers(self, temp):
        s = temp

        if(s.isnumeric()):
            # print("numbers=",s)
            self.c += 1

        return self.c

    def spl3_char(self, temp):
        s = temp

        if(s.isalnum() == False and s.isspace() == False):
            # print("spl_char=",s)
            self.d += 1

        return self.d

    def result(self):

        if(self.a % 2 == 0 and self.b == 0 and self.c % 2 != 0 and self.d <= 3):
            print("Wow,The word is valid!")
            # print("a=",self.a)
            # print("b=",self.b)
            # print("c=",self.c)
            # print("d=",self.d)
        else:
            print("The word is not valid!")
            # print("a=",self.a)
            # print("b=",self.b)
            # print("c=",self.c)
            # print("d=",self.d)

        return 0


sv = StringValidation()
sv.validaton()
