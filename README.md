# BCEWithLogitsLoss

torch.set_printoptions(16),tensor默认打印精度小数点后4位，涉及到log运算很容易越界

对于BCEWithLogitsLoss容易出现nan和inf的问题
1、nan，计算log时pred值为0导致，log(0)=nan
2、inf，计算loss.mean()时，loss.sum()导致
