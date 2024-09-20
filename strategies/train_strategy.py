import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# 定义一个简单的二分类神经网络
class SimpleBinaryClassifier(nn.Module):
    def __init__(self):
        super(SimpleBinaryClassifier, self).__init__()
        self.layer1 = nn.Linear(4, 10)  # 输入层到第一层隐藏层
        self.layer2 = nn.Linear(10, 10) # 第一层隐藏层到第二层隐藏层
        self.layer3 = nn.Linear(10, 10) # 第二层隐藏层到第三层隐藏层
        self.output_layer = nn.Linear(10, 1) # 第三层隐藏层到输出层
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.relu(self.layer1(x))
        x = self.relu(self.layer2(x))
        # x = self.relu(self.layer3(x))
        x = self.sigmoid(self.output_layer(x))
        return x

# 创建模型实例
model = SimpleBinaryClassifier()

def predict(state):
    # state = [0,1,2,3]
    X_state = torch.tensor([state], dtype=torch.float32)
    probabilities = model(X_state)
    action = 0 if probabilities < 0.5 else 1
    print(X_state)
    print(probabilities)
    print(action)

predict([0,1,2,3])
    # action =

# def train():

# # 定义损失函数和优化器
# criterion = nn.BCELoss()
# optimizer = optim.SGD(model.parameters(), lr=0.01)
#
# # 生成一些示例数据
# X_train = torch.tensor([[0.0, 0.0],
#                         [0.0, 1.0],
#                         [1.0, 0.0],
#                         [1.0, 1.0]],
#                        dtype=torch.float32)
# y_train = torch.tensor([[0.0],
#                         [1.0],
#                         [1.0],
#                         [0.0]],
#                        dtype=torch.float32)
#
# # 创建DataLoader
# dataset = TensorDataset(X_train, y_train)
# dataloader = DataLoader(dataset, batch_size=1, shuffle=True)
#
# # 训练模型
# num_epochs = 100
# for epoch in range(num_epochs):
#     for batch_idx, (inputs, labels) in enumerate(dataloader):
#         # 前向传播
#         outputs = model(inputs)
#         loss = criterion(outputs, labels)
#
#         # 反向传播和优化
#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()
#
#     if (epoch + 1) % 10 == 0:
#         print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')
#
# # 测试模型
# X_test = torch.tensor([[0.5, 0.5]], dtype=torch.float32)
# with torch.no_grad():
#     y_test_pred = model(X_test)
# print(f'Predicted Label (0.5, 0.5): {y_test_pred.item():.4f}')
