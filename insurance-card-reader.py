import cv2
import webbrowser

cap = cv2.VideoCapture(0)

detector = cv2.QRCodeDetector()

while True:
    _, img = cap.read()

    data, bbox, _ = detector.detectAndDecode(img)

    if data:
        if data.count(",") == 10:
            a = data
            with open("qrcode_output.txt", "w") as file:
                file.write(a)  
                print(a)
            break

    cv2.imshow("Saftinet Insurance Card Scanner", img)

    key = cv2.waitKey(1)
    if cv2.waitKey(1) == ord("q") or key == 27:
        break

cap.release()
cv2.destroyAllWindows()
