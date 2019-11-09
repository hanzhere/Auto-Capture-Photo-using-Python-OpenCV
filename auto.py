import cv2

camera = cv2.VideoCapture(0)

sampleNum = 0

while (True):
    ret, img = camera.read()

    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sampleNum = sampleNum + 1
    cv2.imwrite('dataSet/' + str(sampleNum) + '.jpg', gray[50:800, 50:800])
    print('saved')
    
    cv2.imshow('frame', img)

    if cv2.waitKey(200) & 0xFF == ord('q'):
        break
    elif sampleNum>100:
        break    

camera.release()
cv2.destroyAllWindows()