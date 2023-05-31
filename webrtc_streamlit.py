import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase


class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        # Process the video frame here (if needed)
        return frame


def main():
    # Set Streamlit app title
    st.title("WebRTC Streamlit Example")

    # Set the STUN server information
    rtc_configuration = {
        "iceServers": [
            {"urls": ["stun:stun.l.google.com:19302"]},
            {"urls": ["turn:numb.viagenie.ca"], "username": "webrtc@live.com", "credential": "muazkh"}
        ]
    }

    # Establish the WebRTC connection and display the video stream
    webrtc_streamer(key="example", video_transformer_factory=VideoTransformer, rtc_configuration=rtc_configuration)

if __name__ == "__main__":
    # Run the Streamlit app
    main()

