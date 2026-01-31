
from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
import mediapipe as mp

class GestureApp(App):
    def build(self):
        self.img = Image()
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=False, max_num_hands=1)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0/30.0)
        return self.img

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(rgb_frame)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    h, w, _ = frame.shape
                    cx, cy = int(hand_landmarks.landmark[8].x * w), int(hand_landmarks.landmark[8].y * h)
                    cv2.circle(frame, (cx, cy), 15, (0, 255, 0), -1)
            buf = cv2.flip(frame, 0).tobytes()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.img.texture = texture

if __name__ == '__main__':
    GestureApp().run()
