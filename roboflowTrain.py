from roboflow import Roboflow
rf = Roboflow(api_key="ztuSjmkiccPdbrivPKxW")
project = rf.workspace("kyle-apiyh").project("components_detection")
version = project.version(2)
dataset = version.download("yolov8")