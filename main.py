from streamlit_webrtc import (
    VideoProcessorBase,
    webrtc_streamer,
    VideoHTMLAttributes
)
import threading
from aiortc.contrib.media import MediaRecorder
from video import find_face

#Defining the variables
lock = threading.Lock()
img_container = {"frames":[]}

s_per_question=60 #maximum duration of the video input in s


#Extracting frames from the video input
class VideoProcessor(VideoProcessorBase):
    def __init__(self):
        self.style = 'color'

    def video_frame_callback(self):
        img = self.to_ndarray(format="bgr24")
        img = find_face(img)
        with lock:
            if img is not None:
                img_container["frames"].append(img)


webrtc_streamer(
            key="object-detection",
            # video_frame_callback=VideoProcessor.video_frame_callback,
            media_stream_constraints={
                "video": True,
                "audio": True
            },
            desired_playing_state=True #link to Start/Stop button
            # , in_recorder_factory= MediaRecorder("record.mp3")
            , video_html_attrs = VideoHTMLAttributes(muted=True, volume=0, autoPlay=True, controls=False, stop=False #unabling the user to control video input
                                                    #,style={"border": "5px red solid", "margin": "0 auto", "width":"50%"}
                                                    )
            ,  rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
                            }
        )