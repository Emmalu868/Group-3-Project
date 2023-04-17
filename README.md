# This is the title of our project


# 📝 About the project

Analysis of trend in oil price across geographical regions and examining the relationship between oil price and stock market. 

## Research Questions
How does change in oil price affect stock market? <br>
Can oil prices impact certain industries?

## Datasets



## Conclusion




# ⚒️ Dependencies

-   [Python](https://www.python.org/)
-   [Conda](https://conda.io/)  

The workflow includes the following Python packages:
- [numpy](https://pypi.org/project/numpy/)
- [pandas](https://pypi.org/project/pandas/)

# Getting started 

**1. Clone this repo.**

    git clone https://github.com/Emmalu868/Group-3-Project.git
    cd Group-3-Project


**2. 🚀 Install dependencies.** <br><br>
***2.1 If you do not have Conda installed, then use the following method to install it. If you already have Conda installed, then refer directly to the next step (2.2).***

    # download Miniconda3 installer
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    
    # install Conda (respond by 'yes')
    bash miniconda.sh
    
    # update Conda
    conda update -y conda
    
  
 ***2.2 Create a conda environment named Gasoline_Dashboard and install all the dependencies in that environment.***<br>
 
 
    # create a new environment with dependencies 
    conda env create -n Gasoline_Dashboard -f environment.yaml
    
    
 ***2.3 Activate the environment***   <br>
 
    conda activate Gasoline_Dashboard
    
**3. Execute the Gasoline Dashboard**

    # In a conda environment where all dependencies are already installed
    
    python index.py
    


