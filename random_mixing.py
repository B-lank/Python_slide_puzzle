
def random(difficulty):
     import random

     difficulty = input("difficulty  [high(5*5), mid(4*4), easy(3*3)] choose one : ")

     matrix = [[0 for col in range(difficulty)] for row in range(difficulty)]

     for i in range (100):
          for column in range (difficulty):
               for row in range (difficulty):

                    matrix[column][row] = Photoimage_n[column][row]

                    list1 = ['matrix[column][row]=matrix[column][row+1]', 'matrix[column][row]=matrix[column+1][row]']
                    list2 = ['matrix[column][row]=matrix[column-1][row]', 'matrix[column][row]=matrix[column][row+1]']
                    list3 = ['matrix[column][row]=matrix[column][row-1]', 'matrix[column][row]=matrix[column+1][row]']
                    list4 = ['matrix[column][row]=matrix[column-1][row]', 'matrix[column][row]=matrix[column][row-1]']
                    list5 = ['matrix[column][row]=matrix[column+1][row]', 'matrix[column][row]=matrix[column-1][row]']

                    if column==0 and row==0:
                         random.choice(list1)
                    elif column==0 and row==difficulty-1:
                         random.choice(list2)
                    elif column == difficulty-1 and row == 0:
                         random.choice(list3)
                    elif column == difficulty-1 and row ==difficulty-1 :
                         random.choice(list4)
                    else:
                         random.choice(list5)
          i = i+1
     return matrix[column][row]

                         # list 안의 내용들이 문자열로 입력되는지 아니면 실행되는지 질문
                         # 반복문 넣어야 하는 자리를 질문