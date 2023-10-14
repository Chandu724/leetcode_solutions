class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        
#         kk = sentence
#         sentence = [len(i) for i in sentence]
#         n = len(sentence)
#         res = 0
#         t = 0
#         lens = rows*cols
        
#         sr = []
        
#         if max(sentence) > cols:
#             return 0
        
#         print("hi")
        
#         while lens > 0:
#             if sentence[t] <= lens%cols or lens%cols == 0:
#                 sr.append(kk[t])
#                 if sentence[t] == lens%cols or sentence[t] == cols:
#                     lens = lens - sentence[t]
#                 else:
#                     lens = lens - sentence[t] - 1
#                     sr.append("-")
#                 if t == n-1:
#                     print(lens%cols)
#                     t=0
#                     res+=1
#                     if lens%cols == 0 or (lens%cols < sentence[0] != 1):
#                         #print(rows*cols - lens + lens%cols)
#                         x = (rows*cols)//(rows*cols - lens + lens%cols)
#                         lens = lens - (x-1)*(rows*cols - lens + lens%cols)
#                         res = res*x
#                         print(x)
#                         print("yo")
#                 else:
#                     t+=1
#             else:
#                 lens = lens - lens%cols
                
#         print(sr)
#         return res





        s = ' '.join(sentence)+' '
    
        x = 0
        
        for i in range(rows):
            x = x + cols
            
            while s[x % len(s)]!=' ':
                x = x - 1
                
            x = x + 1
            
        return x//len(s)
            