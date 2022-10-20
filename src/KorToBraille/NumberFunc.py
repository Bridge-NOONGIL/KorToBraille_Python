number_braille = "⠼"
number_braille_dict = {"0":"⠚", "1":"⠁", "2":"⠃", "3":"⠉", "4":"⠙","5":"⠑", "6":"⠋", "7":"⠛", "8":"⠓", "9":"⠊"}

hangul = ["ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ","ㅅ","ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"]
number_punctuation_invalid_dict = {"~":"⠤⠤"} # 수표 효력 무효
number_punctuation_valid_dict = {":":"⠐⠂", "-":"⠤", ".":"⠲", ",":"⠐", "·":"⠐⠆"} # 수표 효력 유효

number_punctuation_valid = [":", "-", ".", ",", "·"]
isdigit_flag = False

CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def getJamoFromOneSyllable(korean_word):
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

def chosungCheck(word: str):
  return getJamoFromOneSyllable(word)[0]

def translateNumber(text: str):
  result = ""
  global isdigit_flag
  for i in range(len(text)):
    if text[i].isdigit():
      if isdigit_flag == False:
        isdigit_flag = True
        result += number_braille
        result += number_braille_dict[text[i]]
      else:
        result += number_braille_dict[text[i]]

      if i < len(text) - 1: # 제38항: 숫자와 혼용되는 '운'의 약자가 숫자 다음에 이어 나올 때에는 숫자와 한글을 띄어 쓴다.
        if text[i+1] == "운":
          result += " "

    elif (text[i] in number_punctuation_valid and isdigit_flag == True):
      result += number_punctuation_valid_dict[text[i]]
    
    else: #제38항: 숫자와 혼용되는 'ㄴ,ㄷ,ㅁ,ㅋ,ㅌ,ㅍ,ㅎ'의 첫소리 글자와 숫자 다음에 이어 나올 때에는 숫자와 한글을 띄어 쓴다.
      cho =  chosungCheck(text[i])
      if (cho == "ㄴ" or cho == "ㄷ" or cho == "ㅁ" or cho == "ㅋ" or cho == "ㅌ" or cho == "ㅍ" or cho == "ㅎ") and isdigit_flag == True:
        result += "⠀"

      result += text[i]
      isdigit_flag = False
  return result
