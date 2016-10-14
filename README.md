# fast-neural-style.tf

An implementation of [1][2].

Time: 0.05 seconds on NVIDIA TITAN X GPU for at resolution of 1200x630.

ModelName | Style | Samples
---       | ---   | ---
composition_v | ![](examples/inputs/cropped_composition_vii.jpg) | ![](examples/outputs/composition_vii.jpg)
feathers | ![](examples/inputs/cropped_feathers.jpg) | ![](examples/outputs/feathers.jpg)
la_muse | ![](examples/inputs/cropped_la_muse.jpg) | ![](examples/outputs/la_muse.jpg)
mosaic | ![](examples/inputs/cropped_mosaic.jpg) | ![](examples/outputs/mosaic.jpg)
the scream | ![](examples/inputs/cropped_the_scream.jpg) | ![](examples/outputs/the_scream.jpg)
udnie | ![](examples/inputs/cropped_udnie.jpg) | ![](examples/outputs/udnie.jpg)
wave | ![](examples/inputs/cropped_wave.jpg) | ![](examples/outputs/wave.jpg)
cubist | ![](examples/inputs/cropped_cubist.jpg) | ![](examples/outputs/cubist_style.jpg)

## Requirement
Tensorflow(>= r0.11), Numpy, Scipy, Pillow

## Usage

```{bash}
python render.py --input $INPUT_IMAGE --output $OUTPUT_FILE_NAME --model $MODEL_NAME --arch $GENERATOR_ARCH
```

## Training
Coming soon.

## License
MIT



## Reference
[1] Johnson, Justin, Alexandre Alahi, and Li Fei-Fei. "Perceptual losses for real-time style transfer and super-resolution." arXiv preprint arXiv:1603.08155.

[2] Ulyanov, Dmitry, Andrea Vedaldi, and Victor Lempitsky. "Instance Normalization: The Missing Ingredient for Fast Stylization." arXiv preprint arXiv:1607.08022.

[3] Gatys, Leon A., Alexander S. Ecker, and Matthias Bethge. "A neural algorithm of artistic style." arXiv preprint arXiv:1508.06576.

