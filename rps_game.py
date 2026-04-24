import cv2
import mediapipe as mp
import random
import time
from playsound import playsound
import threading

print("🎮 Rock Paper Scissors Game Started")

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# Game variables
player_move = ""
computer_move = ""
result = ""

player_score = 0
computer_score = 0

WIN_SCORE = 3  # 🏆 first to 3 wins

start_time = 0
countdown = 3

state = "WAITING"
result_time = 0


def play_sound():
    try:
        playsound("beep.mp3")
    except:
        pass


def get_gesture(hand_landmarks):
    fingers = []
    tips = [8, 12, 16, 20]

    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    for tip in tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    total = sum(fingers)

    if total <= 1:
        return "Rock"
    elif total >= 4:
        return "Paper"
    elif fingers[1] == 1 and fingers[2] == 1:
        return "Scissors"
    else:
        return "Unknown"


while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    gesture = "Unknown"

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
            gesture = get_gesture(handLms)

    h, w, _ = frame.shape

    # 🟡 WAITING
    if state == "WAITING":
        cv2.putText(frame, "Show your move",
                    (150, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (255,255,255), 2)

        if gesture != "Unknown":
            start_time = time.time()
            state = "COUNTDOWN"

    # 🟠 COUNTDOWN
    elif state == "COUNTDOWN":
        elapsed = time.time() - start_time
        remaining = countdown - elapsed

        num = str(max(1, int(remaining) + 1))
        text_size = cv2.getTextSize(num, cv2.FONT_HERSHEY_SIMPLEX, 4, 8)[0]
        x = (w - text_size[0]) // 2
        y = (h + text_size[1]) // 2

        cv2.putText(frame, num, (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 4,
                    (0,255,255), 8)

        if remaining <= 0:
            player_move = gesture
            computer_move = random.choice(["Rock", "Paper", "Scissors"])

            threading.Thread(target=play_sound).start()

            if player_move == computer_move:
                result = "Draw"
            elif (player_move == "Rock" and computer_move == "Scissors") or \
                 (player_move == "Paper" and computer_move == "Rock") or \
                 (player_move == "Scissors" and computer_move == "Paper"):
                result = "You Win!"
                player_score += 1
            else:
                result = "You Lose!"
                computer_score += 1

            result_time = time.time()

            # 🏆 CHECK WINNER
            if player_score == WIN_SCORE or computer_score == WIN_SCORE:
                state = "GAME_OVER"
            else:
                state = "RESULT"

    # 🟢 RESULT
    elif state == "RESULT":
        cv2.putText(frame, f"You: {player_move}", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

        cv2.putText(frame, f"CPU: {computer_move}", (300, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

        cv2.putText(frame, result, (200, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,255), 3)

        if time.time() - result_time > 2:
            state = "WAITING"

    # 🔴 GAME OVER
    elif state == "GAME_OVER":
        winner = "YOU WIN THE GAME!" if player_score == WIN_SCORE else "CPU WINS!"

        cv2.putText(frame, winner,
                    (80, 200),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5,
                    (0,255,255), 3)

        cv2.putText(frame, "Press R to Restart",
                    (100, 300),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (255,255,255), 2)

    # 🧮 SCORE
    cv2.putText(frame, f"Score You: {player_score}", (10, 400),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.putText(frame, f"Score CPU: {computer_score}", (10, 450),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow("RPS Game", frame)

    key = cv2.waitKey(1) & 0xFF

    # Quit
    if key == ord('q'):
        break

    # 🔄 Restart
    if key == ord('r'):
        player_score = 0
        computer_score = 0
        state = "WAITING"

cap.release()
cv2.destroyAllWindows()