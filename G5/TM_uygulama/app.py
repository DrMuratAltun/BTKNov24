import gradio as gr
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# Bilimsel notasyonu devre dışı bırak
np.set_printoptions(suppress=True)

# Modeli yükle
model = load_model("keras_Model.h5", compile=False)

# Etiketleri yükle
class_names = [line.strip() for line in open("labels.txt", "r").readlines()]

# Tahmin fonksiyonu tanımla
def classify_image(image):
    # Görüntüyü RGB formatına çevir
    image = image.convert("RGB")
    # Görüntüyü 224x224 boyutuna yeniden boyutlandır
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    # Görüntüyü numpy array'e çevir
    image_array = np.asarray(image)
    # Görüntüyü normalleştir
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    # Veri dizisini oluştur
    data = np.expand_dims(normalized_image_array, axis=0)
    # Modeli tahmin et
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    # Tahmin sonucunu ve güven skorunu döndür
    return f"Sınıf: {class_name}\nGüven Skoru: {confidence_score:.2f}"

# Gradio arayüzünü oluştur
interface = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil", label="Resim Yükle"),
    outputs="text",
    title="Görüntü Sınıflandırma",
    description="Bir resim yükleyin ve sınıflandırma tahminini görün."
)

# Arayüzü başlat
interface.launch()
