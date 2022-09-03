# 초성 리스트. 00 ~ 18



CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

class KorToBraille:


    def __init__(self) -> None:
        pass

    # [한글 분해] 자모음으로 분해해서 리턴하는 함수 (한글로 규칙을 파악해야할 때 사용)
    def getJamoFromOneSyllable(self, korean_word):
        r = ""
        for w in list(korean_word.strip()):
            ## 영어인 경우 구분해서 작성함. 
            if '가'<=w<='힣':
                ## 588개 마다 초성이 바뀜. 
                ch1 = (ord(w) - ord('가'))//588
                ## 중성은 총 28가지 종류
                ch2 = ((ord(w) - ord('가')) - (588*ch1)) // 28
                ch3 = (ord(w) - ord('가')) - (588*ch1) - 28*ch2
                # r_lst.append([CHOSUNG_LIST[ch1], JUNGSUNG_LIST[ch2], JONGSUNG_LIST[ch3]])
                r += (CHOSUNG_LIST[ch1] + JUNGSUNG_LIST[ch2] + JONGSUNG_LIST[ch3])
            else:
                r += w
        return r

    # [단어 번역] 주어진 "단어"를 자모음으로 분해해서 번역된 점자로 리턴하는 함수
    def korWordToBraille(self, input: str):
        
        wordToTranslate = "" # 번역할 단어
        
        jamo = "" # 분해된 문장
        braillejamo = "" # 분해된 점자 문장

        wordToTranslate = self.korabbToBraille(input) # 약어 처리

        for scalar in wordToTranslate:
            # 자모음 분해
            try:
                jamo += self.getJamoFromOneSyllable(scalar)
            except:
                jamo += ""
            
            # 점자 번역
            try:
                braillejamo += self.getBrailleFromJamo(scalar)
            except:
                jamo += ""

        return braillejamo


    # [최종 번역] 주어진 문장을 단어로 decompose -> korWordToBraille로 각각 점자 단어로 변경 -> 점자 단어 compose (result)
    def korTranslate(self, input: str):
        result = ""
        components = input.split( )

        for word in components:
            if word == "":
                continue
            
            # (1) 숫자번역
            # (2) 문장부호 번역
            result += self.korWordToBraille(word) # (3) 한글번역

            result += " "

            # 모든 flag 초기화
            flag_10 = False
            flag_11 = False
            flag_17 = False
            isdigit_flag = False
        
        return result

if __name__ == '__main__':
    b = KorToBraille().getJamoFromOneSyllable("자")
    print(b)
