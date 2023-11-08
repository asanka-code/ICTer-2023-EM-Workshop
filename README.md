# ICTer International Conference 2023 - Post-Conference Workshop: 
## Forensic Insights from Electromagnetic Radiation

### Introduction
Our digital electronics generate electromagnetic radiation. These radiation patterns are shown to be correlating with the internal operations of electronics circuitry. Electromagnetic side-channel analysis (EM-SCA) is the field that exploits electromagnetic radiation emitted from computing devices to exfiltrate sensitive information. EM-SCA can take us to places where the classical digital forensics approaches cannot go. This workshop is aimed at providing the foundation into the exciting field of EM-SCA for digital forensics, arming the participants with the required skills and directions to go deep into this field. During this full-day workshop, the participants will be exposed to the Software Defined Radio (SDR) equipment that can be used to acquire electromagnetic radiation, i.e., HackRF SDRs, and the procedure to capture, process, and analyse electromagnetic radiation from various smart and embedded devices to extract forensically-useful insights.

### Workshop Agenda

#### Part 1:
1. Introduction and background
2. SDR hardware.
3. SDR software.
4. Capturing EM side-channel radiation.

#### Part 2:
5. Analysing EM dataset using Python.

### Preparing Your Computer for the Workshop

1. You need to have a computer with a GNU/Linux operating system running natively or as a virtual machine. *Ubuntu 22.04 LTS* is recommended.
2. Install several tools and libraries by running the following commands:
   - sudo apt install gqrx-sdr
   - sudo apt install jupyter
   - sudo apt install python3-pandas
   - sudo apt install python3-matplotlib
   - sudo apt install python3-numpy
   - sudo apt install python3-scipy
   - sudo apt install python3-sklearn
   - sudo apt install python3-h5py
   - *stay prepared to install any additional libraries on the go if needed*
3. Clone/download this Git repository to your computer so that you get the latest Jupyter Notebook files (.ipynb) that contains the code examples to try in the workshop. *The code examples will be added to this repository soon.*

### Getting the Dataset

In this workshop, we will be using an EM dataset. In compressed form, it has a size of arund 12 GB. After uncompressing, it will be around 53 GB. There are two ways to get the EM dataset.

#### Option 1:
If you are physically attending the workshop in Singapore, we will provide plenty of USB sticks that have the dataset. So, you can simply copy the dataset to your computer during the workshop.

#### Option 2:
If you are joining the workshop remotely (online), or prefer to have the dataset in advance, you can download it from the following URL: https://aseados.ucd.ie/datasets/EMSCA/em-dataset.h5.gz

MD5 Hash value of the downloaded file (em-dataset.h5.gz): 876564812f06c6689563339f2b784650

MD5 Hash value of the uncompressed dataset file (em-dataset.h5): b998495b45e7aea27e1912ea060d404d

See you at the workshop! 
