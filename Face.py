import dlib
import face_recognition
import cv2
import numpy as np
import csv
import os
import glob
from datetime import datetime

video_capture = cv2.VideoCapture(0)
"""while True:
    ret , video_data =video_capture.read()
    cv2.imshow("video_live",video_data)
    if cv2.waitKey(10)=ord("a"):
        break
video_capture.release()"""




riba_image = face_recognition.load_image_file("photos/riba.jpg")
riba_encoding = face_recognition.face_encodings(riba_image)[0]



rupesh_image = face_recognition.load_image_file("photos/riba.jpg")
rupesh_encoding = face_recognition.face_encodings(rupesh_image)[0]


prasana_image = face_recognition.load_image_file("photos/prasana.jpg")
prasana_encoding = face_recognition.face_encodings(prasana_image)[0]

know_face_encoding = [
    riba_encoding,
    prasana_encoding
]

known_faces_names = [
    "riba maharjan",
    "prasana maharjan"
]

employees = known_faces_names.copy()

face_locations = []
face_encodings = []
face_names = []
s=True

now =datetime.now()
current_date = now.strftime("%d-%m-%Y")
current_time = now.strftime("%H:%M")

# f = open(current_date+'.csv','a+',newline='')
# lnwriter= csv.writer(f)

# while True:
#     _, frame = video_capture.read()
#     small_frame =cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
#     rgb_small_frame = small_frame[:,:,::-1]
#     if s:
#         face_locations =face_recognition.face_locations(rgb_small_frame)
#         face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
#         face_names =[]
#         for face_encoding in face_encodings:
#             matches = face_recognition.compare_faces(know_face_encoding, face_encoding)
#             name= " "
#             face_distance =face_recognition.face_distance(know_face_encoding,face_encoding)
#             best_match_index =np.argmin(face_distance)
#             if matches[best_match_index]:
#                 name= known_faces_names[best_match_index]
            
#             face_names.append(name)
#             # if name in known_faces_names:
#             #     if name in employees:
#             #        # employees.remove(name)
#             #         print (employees)
#             current_time =now.strftime("%H-%M-%S")
#             lnwriter.writerow([face_names,current_time])
#     cv2.imshow("attendence system",frame)
#     if cv2.waitKey(100) & 0xFF == ord('q'):
#         break
# video_capture.release()
# cv2.destroyAllWindows()
# f.close()

# Open the CSV file in append mode ('a+')
f = open(current_date + '.csv', 'a+', newline='')
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    if s:
        # Detect face locations
        face_locations = face_recognition.face_locations(rgb_small_frame)
        print("Face Locations:", face_locations)

        if face_locations:
            # Only process if at least one face is detected
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            print("Face Locations:", face_locations)
            face_names = []
            lnwriter.writerow([', '.join(known_faces_names), current_time])

            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(know_face_encoding, face_encoding)
                name = " "
                face_distance = face_recognition.face_distance(know_face_encoding, face_encoding)
                best_match_index = np.argmin(face_distance)
                if matches[best_match_index]:
                    name = known_faces_names[best_match_index]

                face_names.append(name)
                current_time = now.strftime("%H-%M-%S")
                lnwriter.writerow([', '.join(face_names), current_time])

    cv2.imshow("attendance system", frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

# Close the CSV file
f.close()

video_capture.release()
cv2.destroyAllWindows()

