import torch.nn.functional as F


def cross_entropy_loss2d(input, target, weight=None):
    log_p = F.log_softmax(input)    
    return F.nll_loss(log_p, target, weight=weight)

def explore_architecture(model):
    child_counter = 0
    for child in model.children():
       print(" child", child_counter, "is:")
       print(child)
       child_counter += 1

def freeze_children(model, children_list):
    child_counter = 0
    for child in model.children():
        if child_counter in children_list:
            for param in child.parameters():
                param.requires_grad = False
        child_counter += 1
    return model

def unfreeze_children(model, children_list):
    child_counter = 0
    for child in model.children():
        if child_counter in children_list:
            for param in child.parameters():
                param.requires_grad = True
        child_counter += 1
    return model