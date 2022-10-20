punctuation_dict = {".": "⠲", "?": "⠦", "!": "⠖", ",": "⠐", "·": "⠐⠆", ":": "⠐⠂", ";":"⠰⠆", "(": "⠦⠄", ")":"⠠⠴", "{": "⠦⠂", "}": "⠐⠴", "[": "⠦⠆", "]": "⠰⠴", "-": "⠤", "~": "⠤⠤" }

punctuation_list = [".", "?", "!", ",", "·", ":", ";", "(", ")", "{", "}", "[", "]", "-", "~"]
quotes_kor_list = ["\"", "'"]
quotes_list = ["⠦", "⠴", "⠠⠦", "⠴⠄"] # 여는 큰따옴표, 닫는 큰따옴표, 여는 작은따옴표, 닫는 작은따옴표

open_flag = False # 따옴표 열고 닫는 flag

def translatePunc(text: str):
  result = ""
  global open_flag
  for i in range(len(text)):
    if text[i] in quotes_kor_list:
      if open_flag == False:
        if text[i] == "'":
          result += quotes_list[2] # 여는 작은따옴표
        elif text[i] == "\"":
          result += quotes_list[0] # 여는 큰 따옴표
        open_flag = True
      else:
        if text[i] == "'":
          result += quotes_list[3] # 닫는 작은따옴표
        elif text[i] == "\"":
          result += quotes_list[1] # 닫는 큰 따옴표
        
        open_flag = False
    elif text[i] in punctuation_list:
      result += punctuation_dict[text[i]]
    else:
      result += text[i]
  
  return result