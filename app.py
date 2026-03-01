import streamlit as st
import cv2
import numpy as np

st.title("Dengue NS1 Digital Strip Reader")

uploaded_file = st.file_uploader("Upload Strip Image", type=["jpg","png","jpeg"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)

    height, width = thresh.shape
    
    C_region = thresh[int(height*0.3):int(height*0.4), :]
    T_region = thresh[int(height*0.5):int(height*0.6), :]

    C_mean = np.mean(C_region)
    T_mean = np.mean(T_region)

    threshold = 20

    if C_mean > threshold:
        if T_mean > threshold:
            result = "POSITIVE"
        else:
            result = "NEGATIVE"
    else:
        result = "INVALID"

    st.image(image, caption="Uploaded Strip")
    st.subheader("DENGUE NS1 RESULT:")
    st.success(result)
