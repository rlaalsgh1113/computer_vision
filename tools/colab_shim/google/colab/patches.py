"""google.colab.patches 대체: Jupyter 셀 출력에 OpenCV 이미지를 표시."""
import cv2
import numpy as np
from IPython.display import display
from PIL import Image


def cv2_imshow(a):
    """Colab의 cv2_imshow와 동일하게 BGR(A) 이미지를 RGB(A)로 바꿔 표시한다."""
    a = a.clip(0, 255).astype(np.uint8)
    if a.ndim == 3:
        if a.shape[2] == 4:
            a = cv2.cvtColor(a, cv2.COLOR_BGRA2RGBA)
        else:
            a = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    display(Image.fromarray(a))
