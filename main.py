import cv2
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)
color  = (255, 255, 0)

cx, cy, w, h = 100,100,200,200

#Puzzle Pieces Images
piece1 = cv2.imread("./Assets/PuzzlePieces/p1.png")
piece2 = cv2.imread('./Assets/PuzzlePieces/p2.png')
piece3 = cv2.imread('./Assets/PuzzlePieces/p3.png')
piece4 = cv2.imread('./Assets/PuzzlePieces/p4.png')

#Resizing The Pieces
piece1 = cv2.resize(piece1, (w, h))
piece2 = cv2.resize(piece2, (w, h))
piece3 = cv2.resize(piece3, (w, h))
piece4 = cv2.resize(piece4, (w, h))

#List of pieces
pieces = [piece1, piece2, piece3, piece4]

class DragRectangle():
    def __init__(self, posCenter, size=[200,200]):
        self.posCenter = posCenter
        self.size = size


    def update(self, cursor):
        cx, cy = self.posCenter
        w, h = self.size

        # If the index finger is inside the puzzle piece
        if cx - w // 2 < cursor[0] < cx + w // 2 and cy - h // 2 < cursor[1] < cy + h // 2:
            self.posCenter = cursor[0], cursor[1]


rectList = []
for x in range(4):
    rectList.append(DragRectangle([x*250+150,150]))


while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        lmList = hands[0]['lmList']
    else:
        lmList = []

    if lmList:

        l, _, _ = detector.findDistance(lmList[8][0:2],lmList[12][0:2],img)

        if l < 30:
            cursor = lmList[8] # Index finger tip landmark
            for rect in rectList:
                rect.update(cursor)

    #Drawing the image/shape
    for i, rect in enumerate(rectList):
        cx, cy = rect.posCenter
        w, h = rect.size

        img[cy - h // 2:cy + h // 2, cx - w // 2:cx + w // 2] = pieces[i]


    cv2.imshow('ASN', img)
    cv2.waitKey(1)