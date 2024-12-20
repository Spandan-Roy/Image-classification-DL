# Image-classification-DL on macOS

'''
## Workflows

1. Update config.yaml
2. Update secrets.yaml[optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py
'''

### STEPS:
Clone the repository:
```bash
https://github.com/Spandan-Roy/Image-classification-DL
```

### STEP 01- Create a conda environment after opening the repository
```bash
conda create -n cnncls python=3.9 -y
conda activate cnncls
```
### STEP 02- Install the requirements(Note that this is for macOS version)-for windows use tensforflow=2.12 instead of macos and metal

```bash
pip install -r requirements.txt
```

### DVC Commands
1. dvc init
2. dvc repro
3. dvc dag


# Deployment Steps
 1. Build docker image of source code
 2. Push docker image to ECR
 3. Launch EC2
 4. Pull image from ECR to EC2
 5. Launch docker image in EC2