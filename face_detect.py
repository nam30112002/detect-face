import cv2
import os
import pandas as pd


def faceDetect(video_path, face_id, name):
    k = 30

    excel_path = "dataset/users.xlsx"
    if not os.path.exists(excel_path):
        df = pd.DataFrame(columns=['id', 'name', 'path'])

        # Save the DataFrame to an Excel file
        df.to_excel(excel_path, index=False)
        print(f"Created Excel file at {excel_path} with columns: id, name, path")
    else:
        print(f"Excel file already exists at {excel_path}")

    df = pd.read_excel(excel_path)

    cam = cv2.VideoCapture(video_path)
    fps = cam.get(cv2.CAP_PROP_FPS)  # Lấy tốc độ khung hình của video
    sample_interval = int(fps / k)
    #make sure 'haarcascade_frontalface_default.xml' is in the same folder as this code
    face_detector = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

    # For each person, enter one numeric face id (must enter number start from 1, this is the lable of person 1)


    # Initialize individual sampling face count
    count = 0
    folder_name = "User" + str(face_id)
    path = "dataset/" + folder_name
    #start detect your face and take 30 pictures
    while (True):
        ret, img = cam.read()
        if not ret:
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1
            # Save the captured image into the datasets folder
            if not os.path.exists(path):
                os.makedirs(path)
            cv2.imwrite(path + "/" + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])

        k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 30:  # Take 30 face sample and stop video
            break

    newRow = [{'id': str(face_id), 'name': str(name), 'path': path}]
    df = pd.concat([df, pd.DataFrame(newRow)], ignore_index=True)
    df.to_excel(excel_path, index=False)

    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
