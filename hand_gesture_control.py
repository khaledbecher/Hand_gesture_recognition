# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 12:42:19 2023

@author: MAISON INFO
"""

import cv2
import mediapipe as mp
import math
import pyautogui


### -----------------Functions definition---------------------###

# Calculate distance between two points
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


# closed_fist detection
def closed_fist(fingertip_landmarks,palm_landmark):
    # Calculate the average distance between the fingertips and the palm
    fingertip_palm_distances = [calculate_distance(fingertip.x, fingertip.y, palm_landmark.x, palm_landmark.y) 
               for fingertip in fingertip_landmarks]
    average_distance = sum(fingertip_palm_distances) / len(fingertip_palm_distances)
    
    #Calculate the distance between the index fingertip and the middle fingertip
    index_middle_dist = calculate_distance(fingertip_landmarks[1].x,fingertip_landmarks[1].y,fingertip_landmarks[2].x,fingertip_landmarks[2].y)

    # Define a threshold for closed fist gesture
    closed_fist_threshold = 0.17
        
    # Detect closed fist gesture
    return average_distance < closed_fist_threshold and calculate_distance(fingertip_landmarks[0].x,fingertip_landmarks[0].y,fingertip_landmarks[1].x,fingertip_landmarks[1].y) < 0.08 and index_middle_dist<0.15

# Thumb_down gesture detection
def thumb_down(fingertip_landmarks,palm_landmark):
    # Calculate the average distance between the fingertips and the palm
    fingertip_palm_distances = [calculate_distance(fingertip.x, fingertip.y, palm_landmark.x, palm_landmark.y) 
               for fingertip in fingertip_landmarks]
    average_distance = sum(fingertip_palm_distances) / len(fingertip_palm_distances)
    
    #Calculate the distance between the index fingertip and the middle fingertip
    index_middle_dist = calculate_distance(fingertip_landmarks[1].x,fingertip_landmarks[1].y,fingertip_landmarks[2].x,fingertip_landmarks[2].y)
    
    #Calculate the distance between the pinky fingertip and the palm
    pinky_palm_dist = calculate_distance(fingertip_landmarks[4].x,fingertip_landmarks[4].y,palm_landmark.x,palm_landmark.y)
    
    dists = [fingertip_landmarks[0].y - fingertip.y for fingertip in fingertip_landmarks]
    return max(dists) > 0.18 and average_distance < 0.2 and pinky_palm_dist<0.13 and index_middle_dist<0.15

# Thumb_up gesture detection
def thumb_up(fingertip_landmarks,palm_landmark):
    # Calculate the average distance between the fingertips and the palm
    fingertip_palm_distances = [calculate_distance(fingertip.x, fingertip.y, palm_landmark.x, palm_landmark.y) 
               for fingertip in fingertip_landmarks]
    average_distance = sum(fingertip_palm_distances) / len(fingertip_palm_distances)
    
    #Calculate the distance between the index fingertip and the middle fingertip
    index_middle_dist = calculate_distance(fingertip_landmarks[1].x,fingertip_landmarks[1].y,fingertip_landmarks[2].x,fingertip_landmarks[2].y)
    
    #Calculate the distance between the pinky fingertip and the palm
    pinky_palm_dist = calculate_distance(fingertip_landmarks[4].x,fingertip_landmarks[4].y,palm_landmark.x,palm_landmark.y)

    dists = [fingertip_landmarks[0].y - fingertip.y for fingertip in fingertip_landmarks]
    return min(dists) < -0.18 and average_distance < 0.2 and pinky_palm_dist<0.13 and index_middle_dist<0.15

# Thumb_right gesture detection
def thumb_right(fingertip_landmarks,palm_landmark):
    # Calculate the average distance between the fingertips and the palm
    fingertip_palm_distances = [calculate_distance(fingertip.x, fingertip.y, palm_landmark.x, palm_landmark.y) 
               for fingertip in fingertip_landmarks]
    average_distance = sum(fingertip_palm_distances) / len(fingertip_palm_distances)
    
    #Calculate the distance between the index fingertip and the middle fingertip
    index_middle_dist = calculate_distance(fingertip_landmarks[1].x,fingertip_landmarks[1].y,fingertip_landmarks[2].x,fingertip_landmarks[2].y)
    
    #Calculate the distance between the pinky fingertip and the palm
    pinky_palm_dist = calculate_distance(fingertip_landmarks[4].x,fingertip_landmarks[4].y,palm_landmark.x,palm_landmark.y)
    
    dists = [fingertip_landmarks[0].x - fingertip.x for fingertip in fingertip_landmarks]
    return max(dists) > 0.15 and average_distance < 0.2 and pinky_palm_dist<0.13 and index_middle_dist<0.15

# Thumb_left gesture detection
def thumb_left(fingertip_landmarks,palm_landmark):
    # Calculate the average distance between the fingertips and the palm
    fingertip_palm_distances = [calculate_distance(fingertip.x, fingertip.y, palm_landmark.x, palm_landmark.y) 
               for fingertip in fingertip_landmarks]
    average_distance = sum(fingertip_palm_distances) / len(fingertip_palm_distances)
    
    #Calculate the distance between the index fingertip and the middle fingertip
    index_middle_dist = calculate_distance(fingertip_landmarks[1].x,fingertip_landmarks[1].y,fingertip_landmarks[2].x,fingertip_landmarks[2].y)
    
    #Calculate the distance between the pinky fingertip and the palm
    pinky_palm_dist = calculate_distance(fingertip_landmarks[4].x,fingertip_landmarks[4].y,palm_landmark.x,palm_landmark.y)
    
    dists = [fingertip_landmarks[0].x - fingertip.x for fingertip in fingertip_landmarks]
    return min(dists) < -0.15 and average_distance < 0.2 and pinky_palm_dist<0.13 and index_middle_dist<0.15

# Mouse up movement
def mouse_up(fingertip_landmarks,palm_landmark):
    # Calculate the average distance between the fingertips and the palm
    fingertip_palm_distances = [calculate_distance(fingertip.x, fingertip.y, palm_landmark.x, palm_landmark.y) 
               for fingertip in fingertip_landmarks]
    average_distance = sum(fingertip_palm_distances) / len(fingertip_palm_distances)
    #Calculate the distance between the index fingertip and the middle fingertip
    index_middle_dist = calculate_distance(fingertip_landmarks[1].x,fingertip_landmarks[1].y,fingertip_landmarks[2].x,fingertip_landmarks[2].y)
    
    #Calculate the distance between the pinky fingertip and the palm
    pinky_palm_dist = calculate_distance(fingertip_landmarks[4].x,fingertip_landmarks[4].y,palm_landmark.x,palm_landmark.y)
    
    dists = [fingertip_landmarks[0].y - fingertip.y for fingertip in fingertip_landmarks]
    return min(dists) < -0.28 and average_distance < 0.23 and pinky_palm_dist>0.23 and index_middle_dist<0.15

# Mouse right movement
def mouse_right(fingertip_landmarks,palm_landmark):
    # Calculate the average distance between the fingertips and the palm
    fingertip_palm_distances = [calculate_distance(fingertip.x, fingertip.y, palm_landmark.x, palm_landmark.y) 
               for fingertip in fingertip_landmarks]
    average_distance = sum(fingertip_palm_distances) / len(fingertip_palm_distances)
    
    #Calculate the distance between the index fingertip and the middle fingertip
    index_middle_dist = calculate_distance(fingertip_landmarks[1].x,fingertip_landmarks[1].y,fingertip_landmarks[2].x,fingertip_landmarks[2].y)
    
    #Calculate the distance between the pinky fingertip and the palm
    pinky_palm_dist = calculate_distance(fingertip_landmarks[4].x,fingertip_landmarks[4].y,palm_landmark.x,palm_landmark.y)
    
    dists = [fingertip_landmarks[0].x - fingertip.x for fingertip in fingertip_landmarks]
    return max(dists) > 0.15 and average_distance < 0.23 and pinky_palm_dist>0.23 and index_middle_dist<0.15

# Mouse left movement
def mouse_left(fingertip_landmarks,palm_landmark):
    # Calculate the average distance between the fingertips and the palm
    fingertip_palm_distances = [calculate_distance(fingertip.x, fingertip.y, palm_landmark.x, palm_landmark.y) 
               for fingertip in fingertip_landmarks]
    average_distance = sum(fingertip_palm_distances) / len(fingertip_palm_distances)

    #Calculate the distance between the index fingertip and the middle fingertip
    index_middle_dist = calculate_distance(fingertip_landmarks[1].x,fingertip_landmarks[1].y,fingertip_landmarks[2].x,fingertip_landmarks[2].y)
    
    #Calculate the distance between the pinky fingertip and the palm
    pinky_palm_dist = calculate_distance(fingertip_landmarks[4].x,fingertip_landmarks[4].y,palm_landmark.x,palm_landmark.y)
    
    dists = [fingertip_landmarks[0].x - fingertip.x for fingertip in fingertip_landmarks]
    return min(dists) < -0.25 and average_distance < 0.23 and pinky_palm_dist>0.23 and index_middle_dist<0.15

# Mouse down movement
def mouse_down(fingertip_landmarks,palm_landmark):
    # Calculate the average distance between the fingertips and the palm
    fingertip_palm_distances = [calculate_distance(fingertip.x, fingertip.y, palm_landmark.x, palm_landmark.y) 
               for fingertip in fingertip_landmarks]
    average_distance = sum(fingertip_palm_distances) / len(fingertip_palm_distances)
    
    #Calculate the distance between the index fingertip and the middle fingertip
    index_middle_dist = calculate_distance(fingertip_landmarks[1].x,fingertip_landmarks[1].y,fingertip_landmarks[2].x,fingertip_landmarks[2].y)
    
    #Calculate the distance between the pinky fingertip and the palm
    pinky_palm_dist = calculate_distance(fingertip_landmarks[4].x,fingertip_landmarks[4].y,palm_landmark.x,palm_landmark.y)
    
    dists = [fingertip_landmarks[0].y - fingertip.y for fingertip in fingertip_landmarks]
    return max(dists) > 0.18 and average_distance < 0.23 and pinky_palm_dist>0.23 and index_middle_dist<0.15

# Mouse press movement
def mouse_press(fingertip_landmarks,palm_landmark):
    # Calculate the average distance between the fingertips and the palm
    fingertip_palm_distances = [calculate_distance(fingertip.x, fingertip.y, palm_landmark.x, palm_landmark.y) 
               for fingertip in fingertip_landmarks]
    average_distance = sum(fingertip_palm_distances) / len(fingertip_palm_distances)
    
    #Calculate the distance between the index fingertip and the middle fingertip
    index_middle_dist = calculate_distance(fingertip_landmarks[1].x,fingertip_landmarks[1].y,fingertip_landmarks[2].x,fingertip_landmarks[2].y)
    
    #Calculate the distance between the pinky fingertip and the palm
    pinky_palm_dist = calculate_distance(fingertip_landmarks[4].x,fingertip_landmarks[4].y,palm_landmark.x,palm_landmark.y)
    
    dists = [fingertip_landmarks[0].y - fingertip.y for fingertip in fingertip_landmarks]
    index_thumb_dist = calculate_distance(fingertip_landmarks[1].x,fingertip_landmarks[1].y,fingertip_landmarks[0].x,fingertip_landmarks[0].y)
    return index_thumb_dist > 0.11 and average_distance < 0.1  and index_middle_dist<0.15

# volume down movement
def volume_down(fingertip_landmarks,palm_landmark):
    # Calculate the average distance between the fingertips and the palm
    fingertip_palm_distances = [calculate_distance(fingertip.x, fingertip.y, palm_landmark.x, palm_landmark.y) 
               for fingertip in fingertip_landmarks]
    average_distance = sum(fingertip_palm_distances) / len(fingertip_palm_distances)
    pinky_palm_dist = calculate_distance(fingertip_landmarks[4].x,fingertip_landmarks[4].y,palm_landmark.x,palm_landmark.y)
    dists = [fingertip_landmarks[0].y - fingertip.y for fingertip in fingertip_landmarks]
    index_thumb_dist = calculate_distance(fingertip_landmarks[1].x,fingertip_landmarks[1].y,fingertip_landmarks[0].x,fingertip_landmarks[0].y)
    index_middle_dist = calculate_distance(fingertip_landmarks[1].x,fingertip_landmarks[1].y,fingertip_landmarks[2].x,fingertip_landmarks[2].y)
    return index_thumb_dist < 0.06 and average_distance < 0.17 and index_middle_dist>0.11

# volume up movement
def volume_up(fingertip_landmarks,palm_landmark):
    # Calculate the average distance between the fingertips and the palm
    fingertip_palm_distances = [calculate_distance(fingertip.x, fingertip.y, palm_landmark.x, palm_landmark.y) 
               for fingertip in fingertip_landmarks]
    average_distance = sum(fingertip_palm_distances) / len(fingertip_palm_distances)
    pinky_palm_dist = calculate_distance(fingertip_landmarks[4].x,fingertip_landmarks[4].y,palm_landmark.x,palm_landmark.y)
    dists = [fingertip_landmarks[0].y - fingertip.y for fingertip in fingertip_landmarks]
    index_thumb_dist = calculate_distance(fingertip_landmarks[1].x,fingertip_landmarks[1].y,fingertip_landmarks[0].x,fingertip_landmarks[0].y)
    index_middle_dist = calculate_distance(fingertip_landmarks[1].x,fingertip_landmarks[1].y,fingertip_landmarks[2].x,fingertip_landmarks[2].y)
    thumb_palm_dist = calculate_distance(fingertip_landmarks[0].x,fingertip_landmarks[0].y,fingertip_landmarks[2].x,fingertip_landmarks[2].y)
    print(thumb_palm_dist)
    return index_thumb_dist > 0.12 and average_distance < 0.17 and index_middle_dist>0.15 and thumb_palm_dist>0.1
 
###--------------------end of functions definition------------###



# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Open the camera
cap = cv2.VideoCapture(0)
pyautogui.FAILSAFE =False
# Start the loop
while True:
    # Read frames from the camera
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip the frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)
    
    # Convert the frame to RGB for MediaPipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame with MediaPipe Hands
    results = mp_hands.process(frame_rgb)
    
    # Check if hands are detected
    if results.multi_hand_landmarks:
        
        # We only need one hand
        hand_landmarks = results.multi_hand_landmarks[0]
        
        
        # Render hand landmarks on the frame
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
            
            
        
        # Getting fingertip landmarks
        fingertip_landmarks= [hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP],
                              hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP],
                              hand_landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP],
                              hand_landmarks.landmark[mp.solutions.hands.HandLandmark.RING_FINGER_TIP],
                              hand_landmarks.landmark[mp.solutions.hands.HandLandmark.PINKY_TIP]]
        # Getting palm landmark
        palm_landmark  = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.WRIST]

        # Thumb tip orientation
        diff = ( fingertip_landmarks[0].x - fingertip_landmarks[2].x )
        # #Detect gestures
        if closed_fist(fingertip_landmarks,palm_landmark) : 
            print("Closed fist !")
        elif thumb_down(fingertip_landmarks,palm_landmark) :
            print("Reverse !") 
          
            pyautogui.press('down',presses=2)

        elif thumb_up(fingertip_landmarks,palm_landmark):
            if(diff <0):
                print("Forward !++++++++") 
                pyautogui.keyDown('left')
                pyautogui.press('up',presses=150)
                pyautogui.keyUp('left')

            elif (diff<0.09):
                print("Forward !") 
                pyautogui.press('up',presses=150)
               
            else :
                print("Forward !---------")
                pyautogui.keyDown('right')
                pyautogui.press('up',presses=150)
                pyautogui.keyUp('right')
                
        
        if(mouse_up(fingertip_landmarks,palm_landmark)):
            print("mouse up !")
            pyautogui.move(0,-25,0.01)    #Move the mouse cursor up
        elif(mouse_right(fingertip_landmarks,palm_landmark)):
            pyautogui.move(25,0,0.01)      #Move the mouse cursor to the right
            print("mouse right !")
        elif(mouse_left(fingertip_landmarks,palm_landmark)):
            pyautogui.move(-25,0,0.01)     #Move the mouse cursor to the left
            print("mouse left !")
        elif(mouse_down(fingertip_landmarks,palm_landmark)):
            pyautogui.move(0,25,0.01)    #Move the mouse cursor down
            print("mouse down !")
        
        if(mouse_press(fingertip_landmarks,palm_landmark)):
            print("mouse press !")
            pyautogui.click()        #Mouse click
        if(volume_down(fingertip_landmarks,palm_landmark)):
            print("volume --- !")
            pyautogui.press('volumedown')    #Press volumedown button
        elif(volume_up(fingertip_landmarks,palm_landmark)):
            print("volume +++ !")
            pyautogui.press('volumeup')       #Press volumeup button

    # Display the frame
    cv2.imshow("Hand Gesture Detection", frame)
    
    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
