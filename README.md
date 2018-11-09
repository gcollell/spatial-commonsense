# Requirements

Python 3
Keras 2.0.9 (tested with tensorflow backend)
sklearn 0.19.1 (for evaluation)
h5py (if we want to store model weights)


# Download data 

Download the following .json data files from the Visual Genome dataset. 

- image_data.json
- relationships.json

Notice that we do not require actual images for our setting but only coordinates and bounding boxes. Assume we store the two files above in ./visualgenome folder.


# Pre-process the data

In the terminal, cd to the ./code folder of this repository. Run:

python pre-process_data.py

passing the right paths and desired choices (i.e., implicit, explicit, or all relations) as arguments. See --help for details.



# Train and evaluate the model

Run on the terminal:

python learn_and_eval.py

passing the desired choices as arguments (e.g., PIX or REG model, etc.). See --help for details.

Results are automatically stored in the ./results folder.

