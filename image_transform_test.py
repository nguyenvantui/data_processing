from torchvision import transforms
from PIL import Image
from ipdb import set_trace as bp
import numpy as np

# bp()

# im.show()
# train_transforms = transforms.Compose([transforms.RandomCrop(50),
#                                        transforms.Resize((64, 64)),
#                                        ])
train_transforms = transforms.Compose([
                                        # transforms.RandomCrop(50),
                                    #    transforms.Pad(10, padding_mode='reflect'),
                                        transforms.Resize((76, 76)),
                                        transforms.RandomRotation(15, expand=True),
                                        transforms.CenterCrop(64)
                                       ])
for i in range(20):
    im = Image.open("f24.png")
    im = train_transforms(im)
    # im = np.array(im)
    # bp()
    im.save(str(i)+".png")

print(">>> done <<<")