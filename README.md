# STL-10 Image Classifier & API Deployment

An end-to-end deep learning pipeline for image classification built with PyTorch Lightning and deployed as a REST API using BentoML. The project focuses on optimizing the training process and efficiently serving the model for production environments, leveraging cloud infrastructure for scalability.

## 🚀 Key Features

*   **Custom CNN Architecture:** A lightweight Convolutional Neural Network built with PyTorch Lightning for the STL-10 dataset.
*   **Hyperparameter Tuning:** Automated search for optimal learning rates and network dimensions using Optuna.
*   **Cloud Execution:** Scaled the training and hyperparameter optimization workloads by executing them on a Google Cloud Platform (GCP) cluster.
*   **VRAM Optimization:** Custom `LightningDataModule` that loads the entire dataset directly into GPU VRAM, drastically reducing I/O bottlenecks during training.
*   **Model Optimization:** Includes experiments with Post-Training Quantization (FP16, INT8) and Model Pruning (Structured & Unstructured) to evaluate inference speed vs. accuracy trade-offs.
*   **Production-Ready Serving:** The final model is packaged and served via BentoML, exposing a robust endpoint for image predictions.

## 🛠️ Tech Stack

*   **Deep Learning:** PyTorch, PyTorch Lightning, Torchvision
*   **Hyperparameter Optimization:** Optuna
*   **Model Serving & API:** BentoML, Requests
*   **Cloud & Infrastructure:** Google Cloud Platform (GCP)
*   **Data Handling:** Pandas, PIL, NumPy

## 🧠 Model Pipeline Overview

1.  **Training:** The `SimpleCNN` is trained on the STL-10 dataset. Optuna runs multiple trials to maximize the validation accuracy.
2.  **Saving:** The best-performing model is saved to the local BentoML model store (`stl10_simple_cnn`).
3.  **Serving:** The `STL10Classifier` BentoML service loads the weights, applies necessary transformations (resizing to 96x96, normalization), and runs a custom forward pass for inference.

## 💻 Usage

### Testing the API
You can send a POST request to the BentoML server to get predictions. A sample test script is provided:

```python
import requests

resp = requests.post(
    "http://<SERVER_IP>:3000/predict",
    files={"image": ("test.jpg", open("your_image.jpg", "rb"), "image/jpeg")}
)
print(f"Predicted class: {resp.text}")
