from .NumberFunc import translateNumber
from .PunctuationFunc import translatePunc
from .data import kor_abb, kor_cho, kor_jung, kor_jong

# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ',
                'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ',
                 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ',
                 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

CHO = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ",
       "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]

JUNG = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ",
        "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]

JONG = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ",
        "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]

JONG_DOUBLE = {"ㄲ": "ㄱㄱ", "ㄳ": "ㄱㅅ", "ㄵ": "ㄴㅈ", "ㄶ": "ㄴㅎ", "ㄺ": "ㄹㄱ",
               "ㄻ": "ㄹㅁ", "ㄼ": "ㄹㅂ", "ㄽ": "ㄹㅅ", "ㄾ": "ㄹㅌ", "ㄿ": "ㄹㅍ", "ㅀ": "ㄹㅎ", "ㅄ": "ㅂㅅ"}


class KorToBraille:

    flag_10 = False  # 제 10항 관련 Flag - 앞글자가 모음으로 끝남 = 종성이 없음
    flag_11 = False  # 제 11항 관련 flag
    flag_17 = False  # 제 12항 관련 flag

    def __init__(self) -> None:
        pass

    #  [약어 번역]
    # 제18항: 다음이 단어들은 약어로 적어 나타낸다.
    #  [붙임] 위에 제시된 말들의 뒤에 다른 음절이 붙어 쓰일 때에도 약어를 사용하여 적는다. ex. 그래서인지, 그러면서
    #  [다만] 위에 제시된 말들의 앞에 다른 음절이 붙어 쓰일 때에는 약어를 사용하여 적지 않는다. ex. 쭈그리고, 찡그리고, 오그리고

    def korabbToBraille(self, input: str):
        result = input

        for (key, value) in kor_abb.items():
            if key in input:
                # [다만] 맨 앞에 오는 경우인지 확인
                for i in input:
                    if i == key[0]:
                        result.replace(key, value)
                    else:
                        break
        return result

    # [한글 분해] 자모음으로 분해해서 리턴하는 함수 (한글로 규칙을 파악해야할 때 사용)

    def getJamoFromOneSyllable(self, korean_word):
        r = ""
        for w in list(korean_word.strip()):
            # 영어인 경우 구분해서 작성함.
            if '가' <= w <= '힣':
                # 588개 마다 초성이 바뀜.
                ch1 = (ord(w) - ord('가'))//588
                # 중성은 총 28가지 종류
                ch2 = ((ord(w) - ord('가')) - (588*ch1)) // 28
                ch3 = (ord(w) - ord('가')) - (588*ch1) - 28*ch2
                # r_lst.append([CHOSUNG_LIST[ch1], JUNGSUNG_LIST[ch2], JONGSUNG_LIST[ch3]])
                r += (CHOSUNG_LIST[ch1] +
                      JUNGSUNG_LIST[ch2] + JONGSUNG_LIST[ch3])
            else:
                r += w
        return r

    # [점자 번역] 자모음으로 분해한 음절을 "점자"로 번역하여 리턴하는 함수 (한 음절씩 번역 처리(초성+중성+종성))
    def getBrailleFromJamo(self, n):
        if "가" <= n <= "힣":
            try:
                cho, jung, jong = self.getJamoFromOneSyllable(n)
            except:
                cho, jung = self.getJamoFromOneSyllable(n)
                jong = ""

            # 제2항: ‘ᄋ’이 첫소리 자리에 쓰일 때에는 이를 표기하지 않는다.
            if cho == "ㅇ":
                cho = ""

            braille_cho = kor_cho[cho]  # 초성 점자
            # 중성
            braille_jung = kor_jung[jung]  # 중성 점자

            # 제10항: 모음자에 '예'가 이어 나올 때에는 그 사이에 붙임표(⠤)를 적어 나타낸다.
            if cho == "" and jung == "ㅖ" and self.flag_10:
                braille_jung = "⠤" + braille_jung
                self.flag_10 = False
            # 제11항: 'ㅑ,ㅘ,ㅜ,ㅝ'에 '애'가 이어 나올 때에는 그 사이에 붙임표(⠤)를 적어 나타낸다.
            elif cho == "" and jung == "ㅐ" and self.flag_11:
                braille_jung = "⠤" + braille_jung
                self.flag_11 = False
            # 제17항: 한 어절 안에서 'ㅏ'를 생략한 약자에 받침 글자가 없고 다음 음절이 모음으로 시작될 때에는 'ㅏ'를 생략하지 않는다.
            elif cho == "" and self.flag_17:
                braille_cho = "⠣" + braille_cho
                self.flag_17 = False

            # 제12항: 다음 글자가 포함된 글자들은 아래 표에 제시한 약자 표기를 이용하여 적는 것을 표준으로 삼는다.
            if jung == "ㅏ":
                if cho == "ㄱ":
                    braille_cho = ""
                    braille_jung = "⠫"
                elif cho == "ㅅ":
                    braille_cho = ""
                    braille_jung = "⠇"
                elif cho == "ㄴ" or cho == "ㄷ" or cho == "ㅁ" or cho == "ㅂ" or cho == "ㅈ" or cho == "ㅋ" or cho == "ㅌ" or cho == "ㅍ" or cho == "ㅎ":
                    # '나,다,마,바,자,카,타,파,하'는 모음 'ㅏ'를 생략하고 첫소리 글자로 약자 표기한다.
                    braille_cho = ""
                    braille_jung = kor_cho[cho]
                    self.flag_17 = True
                elif cho == "ㄸ":
                    braille_cho = ""
                    braille_jung = "⠠⠊"
                    self.flag_17 = True
                elif cho == "ㅃ":
                    braille_cho = ""
                    braille_jung = "⠠⠘"
                    self.flag_17 = True
                elif cho == "ㅉ":
                    braille_cho = ""
                    braille_jung = "⠠⠨"
                    self.flag_17 = True
                elif cho == "ㄲ":  # 제14항 '까,싸,껏'은 각각 '가,사,것'의 약자 표기에 된소리 표를 덧붙여 적는다.
                    braille_cho = ""
                    braille_jung = "⠠⠫"
                elif cho == "ㅆ":
                    braille_cho = ""
                    braille_jung = "⠠⠇"

            # print(f'cho: {cho}')
            # print(f'jung: {jung}')
            # print(f'braille_jung: {braille_jung}')

            if jong == " ":  # 종성 없음(모음자)
                self.flag_10 = True
                if jung == "ㅑ" or jung == "ㅘ" or jung == "ㅜ" or jung == "ㅝ":
                    self.flag_11 = True
                braille_jong = ""

            else:  # 종성 있음
                # 겹받침 처리를 위해 first와 second로 나누었음
                firstjong = " "
                secondjong = " "

                if jong in kor_jong.keys():
                    braille_jong = kor_jong[jong]

                # 종성이 double(ex. ㄲ, ㄹㄱ...)일 때
                if jong in JONG_DOUBLE.keys():
                    jong = JONG_DOUBLE[jong]
                    firstjong = jong[0]
                    secondjong = jong[1]

                # 제12항: 다음 글자가 포함된 글자들은 아래 표에 제시한 약자 표기를 이용하여 적는 것을 표준으로 삼는다.
                # 제15항: 다음과 같이 글자 속에 모음으로 시작하는 약자가 포함되어 있을 때에는 해당 약자를 이용하여 적는다.
                if jung == "ㅓ":
                    # 글자 속에 "ㅓㄱ"이 포함된 경우
                    if jong == "ㄱ":
                        braille_jung = ""
                        braille_jong = "⠹"
                    elif firstjong == "ㄱ":
                        braille_jung = ""
                        braille_jong = "⠹" + kor_jong[secondjong]
                    elif jong == "ㄴ":  # 글자 속에 "ㅓㄴ"이 포함된 경우
                        braille_jung = ""
                        braille_jong = "⠾"
                    elif firstjong == "ㄴ":
                        braille_jung = ""
                        braille_jong = "⠾" + kor_jong[secondjong]
                    elif jong == "ㄹ":  # 글자 속에 "ㅓㄹ"이 포함된 경우
                        braille_jung = ""
                        braille_jong = "⠞"
                    elif firstjong == "ㄹ":
                        braille_jung = ""
                        braille_jong = "⠞" + kor_jong[secondjong]
                    # 한글점자규정 제16항: '성,썽,정,쩡,청'은 'ㅅ,ㅆ,ㅈ,ㅉ,ㅊ' 다음에 'ㅕㅇ'의 약자('⠻')를 적어 나타낸다.
                    elif jong == "ㅇ" and (cho == "ㅅ" or cho == "ㅆ" or cho == "ㅈ" or cho == "ㅉ" or cho == "ㅊ"):
                        braille_jung = ""
                        braille_jong = "⠻"

                elif jung == "ㅕ":
                    if jong == "ㄴ":  # 글자 속에 "ㅕㄴ"이 포함된 경우
                        braille_jung = ""
                        braille_jong = "⠡"
                    elif firstjong == "ㄴ":
                        braille_jung = ""
                        braille_jong = "⠡" + kor_jong[secondjong]
                    elif jong == "ㄹ":  # 글자 속에 "ㅕㄹ"이 포함된 경우
                        braille_jung = ""
                        braille_jong = "⠳"
                    elif firstjong == "ㄹ":
                        braille_jung = ""
                        braille_jong = "⠳" + kor_jong[secondjong]
                    elif jong == "ㅇ":  # 글자 속에 "ㅕㅇ"이 포함된 경우
                        braille_jung = ""
                        braille_jong = "⠻"

                elif jung == "ㅗ":
                    if jong == "ㄱ":  # 글자 속에 "ㅗㄱ"이 포함된 경우
                        braille_jung = ""
                        braille_jong = "⠭"
                    elif firstjong == "ㄱ":
                        braille_jung = ""
                        braille_jong = "⠭" + kor_jong[secondjong]
                    elif jong == "ㄴ":  # 글자 속에 "ㅗㄴ"이 포함된 경우
                        braille_jung = ""
                        braille_jong = "⠷"
                    elif firstjong == "ㄴ":
                        braille_jung = ""
                        braille_jong = "⠷" + kor_jong[secondjong]
                    elif jong == "ㅇ":  # 글자 속에 "ㅗㅇ"이 포함된 경우
                        braille_jung = ""
                        braille_jong = "⠿"
                elif jung == "ㅜ":
                    if jong == "ㄴ":  # 글자 속에 "ㅜㄴ"이 포함된 경우
                        braille_jung = ""
                        braille_jong = "⠛"
                    elif firstjong == "ㄴ":
                        braille_jung = ""
                        braille_jong = "⠛" + kor_jong[secondjong]
                    elif jong == "ㄹ":  # 글자 속에 "ㅜㄹ"이 포함된 경우
                        braille_jung = ""
                        braille_jong = "⠯"
                    elif firstjong == "ㄹ":
                        braille_jung = ""
                        braille_jong = "⠯" + kor_jong[secondjong]
                elif jung == "ㅡ":
                    if jong == "ㄴ":  # 글자 속에 "ㅡㄴ"이 포함된 경우
                        braille_jung = ""
                        braille_jong = "⠵"
                    elif firstjong == "ㄴ":
                        braille_jung = ""
                        braille_jong = "⠵" + kor_jong[secondjong]
                    elif jong == "ㄹ":  # 글자 속에 "ㅡㄹ"이 포함된 경우
                        braille_jung = ""
                        braille_jong = "⠮"
                    elif firstjong == "ㄹ":
                        braille_jung = ""
                        braille_jong = "⠮" + kor_jong[secondjong]
                elif jung == "ㅣ":
                    if jong == "ㄴ":  # 글자 속에 "ㅣㄴ"이 포함된 경우
                        braille_jung = ""
                        braille_jong = "⠟"
                    elif firstjong == "ㄴ":
                        braille_jung = ""
                        braille_jong = "⠟" + kor_jong[secondjong]

                # 한글점자규정 제12항: 것은 약자("⠸⠎")를 사용한다.
                if n == "것":
                    braille_cho = ""
                    braille_jong = ""
                    braille_jung = "⠸⠎"
                elif n == "껏":  # 한글점자규정 제14항: '까,싸,껏'은 각각 '가,사,것'의 약자 표기에 된소리표를 덧붙여 적는다.
                    braille_cho = ""
                    braille_jong = ""
                    braille_jung = "⠠⠸⠎"
                # 한글점자규정 제17항 [붙임]: '팠'을 적을 때에는 'ㅏ'를 생략하지 않고 적는다.
                elif n == "팠":
                    braille_cho = ""
                    braille_jong = ""
                    braille_jung = "⠙⠣⠌"

                self.flag_17 = False

                # print(f'braille_jong: {braille_jong}')

            return braille_cho + braille_jung + braille_jong

        return n

    # [단어 번역] 주어진 "단어"를 자모음으로 분해해서 번역된 점자로 리턴하는 함수

    def korWordToBraille(self, input: str):

        wordToTranslate = ""  # 번역할 단어

        jamo = ""  # 분해된 문장
        braillejamo = ""  # 분해된 점자 문장

        wordToTranslate = self.korabbToBraille(input)  # 약어 처리

        for scalar in wordToTranslate:
            # 자모음 분해
            try:
                jamo += self.getJamoFromOneSyllable(scalar)
            except:
                jamo += " "

            # 점자 번역
            try:
                braillejamo += self.getBrailleFromJamo(scalar)
            except:
                braillejamo += "⠀"

        return braillejamo

    # [최종 번역] 주어진 문장을 단어로 decompose -> korWordToBraille로 각각 점자 단어로 변경 -> 점자 단어 compose (result)

    def korTranslate(self, input: str):
        result = ""
        components = input.split()

        for word in components:
            if word == "":
                continue

            word_translatedNumber = translateNumber(word)  # (1) 숫자번역
            word_translatedNumber = translatePunc(
                word_translatedNumber)  # (2) 문장부호 번역
            result += self.korWordToBraille(word_translatedNumber)  # (3) 한글번역

            result += "⠀"

            # 모든 flag 초기화
            self.flag_10 = False
            self.flag_11 = False
            self.flag_17 = False

        return result

# if __name__ == '__main__':
#     b = KorToBraille().korTranslate("2019년 11월 4일 제93회 점자의 날을 기념하여 점자 번역기 '점자로'를 공개합니다. 별도의 프로그램 설치 없이 웹 페이지에서 바로 사용할 수 있습니다.")
#     print(b)
