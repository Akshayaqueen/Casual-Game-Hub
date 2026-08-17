import cv2


def main():
    print("Starting webcam test...")

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        input("Press Enter to exit...")
        return

    print("Webcam opened successfully.")
    cv2.namedWindow("Casual Game Hub - Webcam Test")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        cv2.imshow("Casual Game Hub - Webcam Test", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            print("Closing webcam window...")
            break

    cap.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)


if __name__ == "__main__":
    main()