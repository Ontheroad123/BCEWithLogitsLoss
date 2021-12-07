from torch import optim, nn
import torch
torch.set_printoptions(16)
def BCEWithLogitsLoss(pred, y): 
    m = nn.Sigmoid()
    pred = m(pred)
    pred = torch.clamp(pred, min=1e-7, max=1-1e-7)
    loss = -((pred.log())*y+(1-pred).log()*(1-y))
    return loss.mean()
  
input = torch.tensor((15,4))
loss = BCEWithLogitsLoss(input, torch.tensor((1,1)))
print(loss)
