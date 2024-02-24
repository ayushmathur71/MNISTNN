class Net(nn.Module):
    #This defines the structure of the NN.
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3)
        self.conv4 = nn.Conv2d(128, 256, kernel_size=3)
        self.fc1 = nn.Linear(4096, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x)) #rfout=1+2=3
        x = F.relu(F.max_pool2d(self.conv2(x), 2)) #rfout1=3+(2)1=5 ; rfoutmax=5+(1)1=6   Jin=1  Jout=2
        x = F.relu(self.conv3(x)) #Jin=2  Jout=2        rfout=6+(2)2=10
        x = F.relu(F.max_pool2d(self.conv4(x), 2)) #rfout1=10+(2)2=15 ; rfoutmax=15+(1)
        x = x.view(-1, 4096)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)