import cv2

#Indirizzo IP della webcam ip_address = "192.168.0.100"

# URL di connessione alla webcam

url = "http://" + ip_address + ":8080/video"

# Crea l'oggetto VideoCapture per accedere alla webcam

cap = cv2.VideoCapture(url)

# ciclo di acquisizione e visualizzazione del video while True: ret, frame cap.read() # Legge un frame dalla webcam

if ret:

cv2.imshow("Webcam", frame) # Visualizza il frame if cv2.waitKey(1) -- ord("q"): # Esce se premuto il tasto "q" break

# Rilascia la risorsa della webcam e chiude le finestre

cap.release()

cv2.destroyAllWindows
