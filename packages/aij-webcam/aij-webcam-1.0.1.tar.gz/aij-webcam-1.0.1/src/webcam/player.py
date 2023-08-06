import cv2
import mediapipe as mp
import pandas as pd
import threading
from gtts import gTTS
from pygame import mixer


class NewsPlayer:
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands
        self.zoomed_text_color = (0, 255, 0)
        self.standard_text_color = (255, 255, 255)
        self.color = self.standard_text_color
        self.direction = 0
        self.font_size = 12
        self.box_size = 50
        self.news_are_being_played = False
        self.df = pd.read_csv('news/news.csv', encoding='utf-8')
        self.df = self.df.dropna()
        self.df = self.df.reset_index(drop=True)
        self.titles = ' ... | '.join(self.df['title'].tolist())

    def generate_audio_from_news(self):
        """
        Convert text to speech and play it
        """
        # initialize tts, create mp3 and play
        tts = gTTS(text=self.titles, lang='en')
        # save the audio file
        tts.save('news/news.mp3')
        # print the text
        print(
            'The news is: \n' + self.titles + '\n\n' +
            'The audio file has been saved to news/news.mp3\n\n'
        )

    def play_news_from_audio(self):
        """
        Play the news
        """
        print(
            'Playing the news...\n\n'
        )
        mixer.init()
        mixer.music.load('news/news.mp3')
        mixer.music.play()

    def pause_news_from_audio(self):
        """
        Pauze the news
        """
        mixer.music.pause()

    def stop_news_from_audio(self):
        """
        Stop the news
        """
        mixer.music.stop()

    def resume_news_from_audio(self):
        """
        Resume the news
        """
        mixer.music.unpause()

    def rewind_news_from_audio(self):
        """
        Rewind the news
        """
        mixer.music.rewind()

    def forward_news_from_audio(self):
        """
        Forward the news
        """
        mixer.music.forward()

    def start_news_player(self):
        # make sure the audio file is generated before playing it
        thread_generate_audio_from_news = threading.Thread(target=self.generate_audio_from_news)
        thread_play_news_from_audio = threading.Thread(target=self.play_news_from_audio)

        thread_generate_audio_from_news.start()
        thread_generate_audio_from_news.join()
        thread_play_news_from_audio.start()

    def start_webcam(self):
        cap = cv2.VideoCapture(0)

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)
        cap.set(cv2.CAP_PROP_FPS, 60)

        with self.mp_hands.Hands(
                model_complexity=0,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5) as hands:

            while cap.isOpened():

                success, image = cap.read()

                if not success:
                    print("Ignoring empty camera frame.")
                    # If loading a video, use 'break' instead of 'continue'.
                    continue

                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

                image.flags.writeable = False
                results = hands.process(image)

                image_height, image_width, _ = image.shape

                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        self.mp_drawing.draw_landmarks(
                            image,
                            hand_landmarks,
                            self.mp_hands.HAND_CONNECTIONS,
                            self.mp_drawing_styles.get_default_hand_landmarks_style(),
                            self.mp_drawing_styles.get_default_hand_connections_style())

                        index_finger_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
                        thumb_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP]

                        index_finger_tip_x = index_finger_tip.x * image_width
                        index_finger_tip_y = index_finger_tip.y * image_height

                        thumb_tip_x = thumb_tip.x * image_width
                        thumb_tip_y = thumb_tip.y * image_height

                        if index_finger_tip_x > thumb_tip_x:
                            self.direction = 1
                        else:
                            self.direction = -1

                        if self.direction == 1:
                            self.color = self.zoomed_text_color
                            self.font_size = 24
                            self.box_size = 100
                        else:
                            self.color = self.standard_text_color
                            self.font_size = 12
                            self.box_size = 50

                        cv2.rectangle(
                            image,
                            (int(index_finger_tip_x - self.box_size), int(index_finger_tip_y - self.box_size)),
                            (int(index_finger_tip_x + self.box_size), int(index_finger_tip_y + self.box_size)),
                            self.color,
                            cv2.FILLED
                        )

                        cv2.putText(
                            image,
                            'News',
                            (int(index_finger_tip_x - self.box_size), int(index_finger_tip_y + self.box_size)),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            self.standard_text_color,
                            2
                        )

                        cv2.putText(
                            image,
                            'Zoom',
                            (int(index_finger_tip_x - self.box_size), int(index_finger_tip_y - self.box_size)),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            self.standard_text_color,
                            2
                        )

                        cv2.putText(
                            image,
                            'Pause',
                            (int(index_finger_tip_x + self.box_size), int(index_finger_tip_y - self.box_size)),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            self.standard_text_color, 2
                        )

                        cv2.putText(
                            image,
                            'Stop',
                            (int(index_finger_tip_x + self.box_size), int(index_finger_tip_y + self.box_size)),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            self.standard_text_color,
                            2
                        )

                        cv2.putText(
                            image,
                            'Resume',
                            (int(index_finger_tip_x), int(index_finger_tip_y - self.box_size)),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            self.standard_text_color,
                            2
                        )

                        cv2.putText(
                            image,
                            'Rewind',
                            (int(index_finger_tip_x), int(index_finger_tip_y + self.box_size)),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            self.standard_text_color,
                            2
                        )

                        cv2.putText(
                            image,
                            'Forward',
                            (int(index_finger_tip_x), int(index_finger_tip_y + self.box_size * 2)),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            self.standard_text_color,
                            2
                        )

                        if self.direction == 1:
                            if self.previous_direction == -1:
                                self.previous_direction = 1
                                self.start_news_player()
                            else:
                                self.previous_direction = 1
                        else:
                            if self.previous_direction == 1:
                                self.previous_direction = -1
                                self.start_news_player()
                            else:
                                self.previous_direction = -1

                cv2.imshow('MediaPipe Hands', image):
                
                if cv2.waitKey(5) & 0xFF == 27:
                    break

        cap.release()
