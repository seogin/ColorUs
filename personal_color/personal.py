import torch
from transformers import CLIPModel, CLIPProcessor
from torch.utils.data import DataLoader, Dataset, random_split, Subset
from torchvision import datasets, transforms
import os
from PIL import Image
import numpy as np

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define the transformation with data augmentation
train_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

test_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# Custom Dataset class
class PersonalColorDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.classes = sorted([d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))])
        self.filepaths = []
        self.labels = []
        for idx, class_name in enumerate(self.classes):
            class_dir = os.path.join(root_dir, class_name)
            for file in os.listdir(class_dir):
                # Skip .DS_Store and non-image files
                if file == '.DS_Store' or not file.lower().endswith(('png', 'jpg', 'jpeg')):
                    continue
                self.filepaths.append(os.path.join(class_dir, file))
                self.labels.append(idx)
    
    def __len__(self):
        return len(self.filepaths)
    
    def __getitem__(self, idx):
        image_path = self.filepaths[idx]
        image = Image.open(image_path).convert("RGB")
        label = self.labels[idx]
        if self.transform:
            image = self.transform(image)
        return image, label

# Load dataset
dataset = PersonalColorDataset(root_dir='./src', transform=train_transform)

# Split dataset into training and testing sets (80% train, 20% test)
dataset_size = len(dataset)
indices = list(range(dataset_size))
np.random.shuffle(indices)
split = int(np.floor(0.1 * dataset_size))
train_indices, test_indices = indices[split:], indices[:split]

train_dataset = Subset(dataset, train_indices)
test_dataset = Subset(PersonalColorDataset(root_dir='./src', transform=test_transform), test_indices)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

# Load pre-trained FaRL model
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Adjust the classification head
model.visual_projection = torch.nn.Linear(model.visual_projection.in_features, 8).to(device)  # 8 classes

# Training parameters
optimizer = torch.optim.Adam(model.parameters(), lr=1e-5)
criterion = torch.nn.CrossEntropyLoss()

# Training loop
num_epochs = 20  # Adjust as needed
model.train()
for epoch in range(num_epochs):
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        
        # Forward pass
        outputs = model.get_image_features(images)
        loss = criterion(outputs, labels)
        
        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

torch.save(model.state_dict(), 'personal_color_model.pth')

# Evaluation function
def evaluate(model, test_loader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model.get_image_features(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    return correct / total

accuracy = evaluate(model, test_loader)
print(f'Test Accuracy: {accuracy * 100:.2f}%')

def classify_personal_color(image_path):
    model.eval()
    
    image = Image.open(image_path).convert("RGB")
    image = processor(images=image, return_tensors="pt").pixel_values.to(device)
    with torch.no_grad():
        outputs = model.get_image_features(image)
    
    _, predicted = torch.max(outputs, 1)
    categories = ['fall', 'spring', 'summer', 'winter']
    return categories[predicted.item()]

# Example usage
# if __name__ == "__main__":
    # image_path = 'lee.png'
    # personal_color = classify_personal_color(image_path)
    # print(f'The personal color category is: {personal_color}')
