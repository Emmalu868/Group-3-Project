# Analysis of Gasoline Prices and Airline Stocks in the Global Market
**Team Members:** <br>
Karthika Ramachandran <br>
Wanlin Li <br>
Shan Lu <br>
Harshitha Katta <br>

## About the project
Analysis of trend in gasoline prices across geographical regions and examining the relationship between gasoline price and stock market.<br>


## Hypothesis
How does change in gasoline price affect stock market? <br>


## Datasets
* **[internationalpumppricesall.csv](https://github.com/Emmalu868/Group-3-Project/blob/main/Resources/internationalpumppricesall.csv):** Obtained from [data.ontario.ca](https://data.ontario.ca/dataset/gasoline-report-international-gasoline-prices) and contains monthly average gasoline price from 2012 to 2022 for 6 major countries- UK, Germany, France, Japan, Canada and USA, all converted to Canadian cents per litre.  <br>
* **[coordinates.csv](https://github.com/Emmalu868/Group-3-Project/blob/main/Resources/coordinates.csv):** Contains geographic coordinates.

## Data Cleanup & Exploration
### Part 1: Analysis of Historical Gasoline Price
#### Files used for analysis 
[internationalpumppricesall.csv](https://github.com/Emmalu868/Group-3-Project/blob/main/Resources/internationalpumppricesall.csv)<br>
[coordinates.csv](https://github.com/Emmalu868/Group-3-Project/blob/main/Resources/coordinates.csv)<br>

* Used Pandas `read_csv` function to read the internationalpumppricesall csv file as a DataFrame and converted the dates to a DateTimeIndex. The internationalpumppricesall.csv file contains monthly oil price data from 2012 to 2022 for 6 major countries- UK, Germany, France, Japan, Canada and USA. 
* Detected and removed null values using `dropna` function.
* Removed a duplicate column "Situation fiscale" using `drop` function.
* Renamed columns to reflect the countries in English.
* Created a dataframe that slices the Tax Status for Total price.
* Used the hvplot function to plot the total_pump_price_all dataFrame as a line chart. 
![](https://github.com/Emmalu868/Group-3-Project/blob/main/Images/monthly_pump_price.png)

* Created a new dataframe and aggregated the values to include only the average price for each country.
* 
![](https://github.com/Emmalu868/Group-3-Project/blob/main/Images/pump_price_geoview.png)
 

### Part 2: Trend Analysis of Gasoline Prices before and after Pandemic

### Part 3: Examining the Relationship Between Oil Price and Stocks

## Conclusion




## Dependencies

-   [Python](https://www.python.org/)
-   [Conda](https://conda.io/)  

The workflow includes the following Python packages:
- [numpy](https://pypi.org/project/numpy/)
- [pandas](https://pypi.org/project/pandas/)

## Getting started 

**1. Clone this repo**

    git clone https://github.com/Emmalu868/Group-3-Project.git
    cd Group-3-Project


**2. 🚀 Install dependencies** <br><br>
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
    


