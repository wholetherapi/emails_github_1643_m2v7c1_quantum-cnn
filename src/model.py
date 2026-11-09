import torch.nn as nn


class NoiseRobustCNN(nn.Module):
    """Convolutional calibrator for noisy quantum sensor traces."""

    def __init__(self, channels=3, width=64):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv1d(channels, width, kernel_size=7, padding=3),
            nn.ReLU(),
            nn.Conv1d(width, width, kernel_size=5, padding=2),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(1),
            nn.Linear(width, 1),
        )

    def forward(self, traces):
        return self.net(traces).squeeze(-1)
