# ICTer International Conference 2023
## Workshop: Forensic Insights from Electromagnetic Radiation

### 1. Introduction
Our digital electronics generate electromagnetic radiation. These radiation patterns are shown to be correlating with the internal operations of electronics circuitry. Electromagnetic side-channel analysis (EM-SCA) is the field that exploits electromagnetic radiation emitted from computing devices to exfiltrate sensitive information. EM-SCA can take us to places where the classical digital forensics approaches cannot go. This workshop is aimed at providing the foundation into the exciting field of EM-SCA for digital forensics, arming the participants with the required skills and directions to go deep into this field. During this full-day workshop, the participants will be exposed to the Software Defined Radio (SDR) equipment that can be used to acquire electromagnetic radiation, i.e., HackRF SDRs, and the procedure to capture, process, and analyse electromagnetic radiation from various smart and embedded devices to extract forensically-useful insights.

### 2. Workshop Agenda

#### Part 1:
1. Introduction.
2. Hardware security.
3. Challenges in digital forensics.

#### Part 2:
4. Software-defined radio hardware.
5. Software-defined radio software.
   
#### Part 3:
6. Electromagnetic trace data acquisition.
7. Electromagnetic trace data processing.

#### Part 4:
8. Exploring a large electromagnetic dataset.
9. Training machine learning models on electromagnetic data.
10. Conclusion.

### 3. Preparing Your Computer for the Workshop

1. You need to have a computer with a GNU/Linux operating system running natively or as a virtual machine. We recommend **Ubuntu 22.04 LTS** distribution. If you are going to go with a virtual machine, provide adequate disk space for it to hold the dataset.
2. Install the following packages on the computer (using **apt** package manager on Ubuntu):
   - sudo apt install gqrx-sdr jupyter python3-pandas python3-matplotlib python3-numpy python3-scipy python3-sklearn python3-h5py
   - *stay prepared to install any additional libraries on the go if needed*

### 4. Getting the Dataset

In this workshop, we will be using an EM dataset. In compressed form, it has a size of arund **12 GB**. After uncompressing, it will be around **53 GB**. There are two ways to get the EM dataset.

#### Option 1:
At the workshop venue, we will provide plenty of USB sticks that contain the dataset. You can simply copy the dataset from such a USB stick to your computer during the workshop.

#### Option 2:
If you prefer to have the dataset in advance, you can download it from the following URL: https://aseados.ucd.ie/datasets/EMSCA/em-dataset.h5.gz

MD5 Hash value of the downloaded file (em-dataset.h5.gz): 876564812f06c6689563339f2b784650

MD5 Hash value of the uncompressed dataset file (em-dataset.h5): b998495b45e7aea27e1912ea060d404d

See you at the workshop! 
