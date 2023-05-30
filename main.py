# import streamlit as st
# import io
# from PIL import Image

# img_file_buffer = st.camera_input("Take a picture")

# if img_file_buffer is not None:
#     # To read image file buffer as bytes:
#     bytes_data = img_file_buffer.getvalue()
#     img = Image.open(io.BytesIO(bytes_data))
#     img.show()
    

#     # Check the type of bytes_data:
#     # Should output: <class 'bytes'>
#     # st.write(type(bytes_data))
    
    
    
from streamlit_webrtc import webrtc_streamer
webrtc_streamer(key="sample")