import cv2
import numpy as np

# Variáveis para acessar os arquivos e algumas de suas propriedades
default_classifier = cv2.CascadeClassifier("model/haarcascade_frontalface_default.xml")
alt_classifier = cv2.CascadeClassifier("model/haarcascade_frontalface_alt.xml")
video = cv2.VideoCapture("../assets/la_cabra.mp4")
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv2.CAP_PROP_FPS)


#Coloca um retangulo em volta da imagem
def coloca_retangulo(img, faces):
  img_saida = img.copy()
  for face in faces:
    pos_x, pos_y, largura, altura = face
    cv2.rectangle(img_saida, (pos_x,pos_y), (pos_x+largura, pos_y+altura), color=(200,0,158), thickness=3)
  return img_saida

def main():
       # Check if camera opened successfully
    if not video.isOpened():
      print("Error opening video stream or file")

    frames = []
    # Read until video is completed
    while(video.isOpened()):
      # Capture frame-by-frame
      ret, frame = video.read()

      if ret:

        # Display the resulting frame
        frames.append(frame)

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
          break

      # Break the loop
      else:
        break
    video.release()


    images_with_rect = []
    for frame in frames:
 #       faces_default = default_classifier.detectMultiScale(frame, scaleFactor = 1.7, minNeighbors=5)
        faces_alt = alt_classifier.detectMultiScale(frame, scaleFactor = 1.3, minNeighbors=9)
        images_with_rect.append(coloca_retangulo(frame,faces_alt))

    new_video = cv2.VideoWriter('../assets/video.avi',cv2.VideoWriter_fourcc('M','J','P','G'),fps,(width,height))
    for image in images_with_rect:
      new_video.write(image)

    # Create a VideoCapture object and read from input file
    cap = cv2.VideoCapture('../assets/video.avi')

    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error opening video file")

    # Read until video is completed
    while(cap.isOpened()):

    # Capture frame-by-frame
        ret, frame = cap.read()
        if ret:
        # Display the resulting frame
            cv2.imshow("Frame",frame)

        # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

    # Break the loop
        else:
            break

main()