<p align="center">
  <a href="https://github.com/sikora-toma/melody_generation">
    <img src="https://www.primorskihrvat.hr/wp-content/uploads/2024/01/sopile.jpg" alt="Sopile" width=72 height=72>
  </a>
  <h3 align="center">Traditional melody generation</h3>
  <p align="center">
    A diffusion model for generating traditional folk-inspired melodies
  </p>
</p>

## Table of contents
- [Quick start](#quick-start)
- [Status](#status)
- [What's included](#whats-included)
- [Bugs and feature requests](#bugs-and-feature-requests)
- [Creators](#creators)
- [Copyright and license](#copyright-and-license)

## Quick start
Get started and generate your own folk-inspired melodies:

- Clone the repository: `git clone https://github.com/sikora-toma/melody_generation.git`
- Install dependencies: `pip install -r requirements.txt`
- Run the example: `python difusion_example.py`

## Status
This project is currently **in active development**. The core framework for training a 1D UNet on melody generation is functional, with ongoing work to expand the dataset and refine the melody representation.

## What's included
The repository includes utilities for working with musical data and training diffusion models for melody generation:

```text
melody_generation/
├── models/
│   ├── model-1.pt
├── utils/
│   ├── midi_utils.py
│   ├── melody_helpers.py
├── res/
│   └── sample_midis
├── saved_melodies/
│   └── output_melody0.wav
└── diffusion_example.py
└── readme.md
```

Key components:
- MIDI file parsing and processing utilities
- Melody representation tools
- Scale definition and manipulation functions
- Working example that generates melodies in major scales

## Bugs and feature requests
Have a bug or a feature request? Please first read the [issue guidelines](https://github.com/sikora-toma/melody_generation/blob/master/CONTRIBUTING.md) and search for existing and closed issues. If your problem or idea is not addressed yet, [please open a new issue](https://github.com/sikora-toma/melody_generation/issues/new).

### Current Feature Requests
We're actively looking for contributors to help with:

- **Dataset Compilation**: Help collect and organize traditional folk melodies for training
- **Melody Representation**: Contribute to defining optimal code representations for melodies


## Creators
**Marjan Sikora**
- <https://github.com/MarjanSikora>

**Toma Sikora**
- <https://github.com/TomaSikora>

## Thanks
Special thanks to the open-source music generation community and the contributors to the diffusion model research that makes this project possible.

## Copyright and license
Code and documentation copyright 2024-2025 Marjan Sikora and Toma Sikora. Code released under the [MIT License](https://github.com/MarjanSikora/MelodyDiffusion/blob/master/LICENSE).
