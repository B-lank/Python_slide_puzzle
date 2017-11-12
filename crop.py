import sys
def cuting(folder, Image, rowncol):
    from folder import Image
    #임의 폴더로부터 이미지 삽입

    oldfilename = "Beforecut"
    row = rowncol
    col = rowncol
    #사용자가 입력한 곱하기값

    with Image(filename=oldfilename) as image:
        print("old : {0} , {1}".format(image.format, image.size))

        cropHeight = int(image.height / row)
        cropWidth = int(image.width / col)
        #이미지를 잘라낸 조각의 가로세로 지정

        for i in range(0, row):
            for j in range(0, col):
                left = j * cropWidth
                right = (j + 1) * cropWidth
                top = i * cropHeight
                bottom = (i + 1) * cropHeight

                #이미지 조각 크기맞추기
