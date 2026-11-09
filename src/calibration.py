import torch


def apply_drift_correction(traces, drift_estimate):
    return traces - drift_estimate.unsqueeze(-1)


def shot_noise_weight(signal):
    return 1.0 / torch.sqrt(signal.clamp_min(1e-6))
