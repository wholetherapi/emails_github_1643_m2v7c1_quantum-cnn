# Noise-Robust Convolutional Networks for Quantum Sensor Calibration

This repository is the official implementation of "Noise-Robust Convolutional
Networks for Quantum Sensor Calibration", accepted at AAAI 2026.

## Repository Status

**Released.**  Model code, calibration pipeline, training script and
evaluation utilities are all included.

## Repository Structure

```
├── src/
│   ├── model.py         # Noise-robust convolutional calibrator
│   ├── calibration.py   # Drift and shot-noise modelling
│   ├── train.py         # Training entry point
│   └── utils.py         # Signal processing helpers
├── data/
│   └── README.md        # Sensor trace format
├── experiments/
│   └── aaai_config.yaml
├── results/
│   └── README.md
├── tests/
│   └── test_calibration.py
├── requirements.txt
└── .gitignore
```

## Quick Start

```bash
git clone https://github.com/wholetherapi/emails_github_1643_m2v7c1_quantum-cnn.git
cd quantum-cnn
pip install -r requirements.txt
python src/train.py --config experiments/aaai_config.yaml
```

## Citation

```bibtex
@inproceedings{carter2026noise,
  title={Noise-Robust Convolutional Networks for Quantum Sensor Calibration},
  author={Carter, Patrick and others},
  booktitle={Proceedings of AAAI 2026},
  year={2026}
}
```
