<<<<<<< HEAD
import bentoml
from PIL import Image
import torch
import torch.nn.functional as F
import torchvision.transforms as transforms

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

@bentoml.service(
    resources={"cpu": "2"},
    traffic={"timeout": 10},
)
class STL10Classifier:
    bento_model = bentoml.models.get("stl10_simple_cnn:latest")

    def __init__(self):
        self.model = self.bento_model.load_model(weights_only=False)
        self.model.to(device)
        self.model.eval()
        
        self.transform = transforms.Compose([
            transforms.Resize((96, 96)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        ])

    @bentoml.api
    def predict(self, image: Image.Image) -> str:
        input_tensor = self.transform(image).unsqueeze(0).to(device)

        with torch.no_grad():
            # RĘCZNY FORWARD PASS OMIJAJĄCY SYSTEM ERROR Z PYTHONA 3.13!
            x = self.model.pool(F.relu(self.model.conv1(input_tensor)))
            x = self.model.pool(F.relu(self.model.conv2(x)))
            x = x.view(x.size(0), -1)
            x = F.relu(self.model.fc1(x))
            output = self.model.fc2(x)
            
            _, predicted = torch.max(output, 1)

=======
import bentoml
from PIL import Image
import torch
import torch.nn.functional as F
import torchvision.transforms as transforms

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

@bentoml.service(
    resources={"cpu": "2"},
    traffic={"timeout": 10},
)
class STL10Classifier:
    bento_model = bentoml.models.get("stl10_simple_cnn:latest")

    def __init__(self):
        self.model = self.bento_model.load_model(weights_only=False)
        self.model.to(device)
        self.model.eval()
        
        self.transform = transforms.Compose([
            transforms.Resize((96, 96)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        ])

    @bentoml.api
    def predict(self, image: Image.Image) -> str:
        input_tensor = self.transform(image).unsqueeze(0).to(device)

        with torch.no_grad():
            # RĘCZNY FORWARD PASS OMIJAJĄCY SYSTEM ERROR Z PYTHONA 3.13!
            x = self.model.pool(F.relu(self.model.conv1(input_tensor)))
            x = self.model.pool(F.relu(self.model.conv2(x)))
            x = x.view(x.size(0), -1)
            x = F.relu(self.model.fc1(x))
            output = self.model.fc2(x)
            
            _, predicted = torch.max(output, 1)

>>>>>>> 67c31a867bc2eaf808bf2b9070126c5c0b99d120
        return str(predicted.item())