import torch
import numpy as np
import matplotlib.pyplot as plt

class Explainer:
    def __init__(self, model):
        self.model = model

    def gradcam(self, spec, target_layer=None):
        # placeholder
        return None

    def attention_weights(self, rr_feat):
        return None
