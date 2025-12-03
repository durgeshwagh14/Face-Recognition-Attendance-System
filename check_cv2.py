import cv2
import sys

print(f"Python version: {sys.version}")
print(f"OpenCV version: {cv2.__version__}")
try:
    print(f"cv2.face available: {hasattr(cv2, 'face')}")
    if hasattr(cv2, 'face'):
        print(f"LBPHFaceRecognizer_create available: {hasattr(cv2.face, 'LBPHFaceRecognizer_create')}")
except Exception as e:
    print(f"Error checking attributes: {e}")

try:
    import cv2.face
    print("Successfully imported cv2.face")
except ImportError:
    print("Failed to import cv2.face")
