# Analysis of Gasoline Prices and Airline Stocks in the Global Market
**Team Members:** <br>
Karthika Ramachandran <br>
Wanlin Li <br>
Shan Lu <br>
Harshitha Katta <br>

## About the project
As per studies and research, gasoline prices and airline stock prices share an inverse relationship, with the value of airline stocks rising as the gasoline's price falls. Our project is to test this by analysing historic gasoline prices and airline stocks for some of the major economies and examining their relationship. Our project also analyses how the demand and price for gasoline is impacted by a global crisis such as the COVID-19 pandemic.  <br>


## Datasets
* **[internationalpumppricesall.csv](https://github.com/Emmalu868/Group-3-Project/blob/main/Resources/internationalpumppricesall.csv):** Obtained from [data.ontario.ca](https://data.ontario.ca/dataset/gasoline-report-international-gasoline-prices) and contains monthly average gasoline price from 2012 to 2022 for 6 major countries- UK, Germany, France, Japan, Canada and USA, all converted to Canadian cents per litre.  <br>
* **[coordinates.csv](https://github.com/Emmalu868/Group-3-Project/blob/main/Resources/coordinates.csv):** Contains geographic coordinates.
* **[air_canada.csv](https://github.com/Emmalu868/Group-3-Project/blob/main/Airline%20Data/Airline/air_canada.csv):** Yahoo Finance Airline Stock <br>
* **[air_france.csv](https://github.com/Emmalu868/Group-3-Project/blob/main/Airline%20Data/Airline/air_france.csv):** Yahoo Finance Airline Stock (EUR) <br>
* **[american_airlines.csv](https://github.com/Emmalu868/Group-3-Project/blob/main/Airline%20Data/Airline/american_airlines.csv):** Yahoo Finance Airline Stock (USD) <br>
* **[germany_lha.csv](https://github.com/Emmalu868/Group-3-Project/blob/main/Airline%20Data/Airline/germany_lha.csv):** Yahoo Finance Airline Stock (EUR) <br>
* **[japan_all_nippon_airways.csv](https://github.com/Emmalu868/Group-3-Project/blob/main/Airline%20Data/Airline/japan_all_nippon_airways.csv):** Yahoo Finance Airline Stock (USD) <br>
* **[uk_tui_airways.csv](https://github.com/Emmalu868/Group-3-Project/blob/main/Airline%20Data/Airline/uk_tui_airways.csv):** Yahoo Finance Airline Stock (GBP) <br>


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
* Used Pandas `read_csv` function and Path module to read all 6 airline stocks, created 6 DataFrame and converted the dates to a DateTimeIndex for all dataframes.
* Renamed close column to the airline names and dropped other columns in the 6 airline dataframes.
* Detected and removed null values using `dropna` function.
* Used `try` and `except` inside a function and `get_rate` function to get rate for historical data, created a new column named Rate.
* Converted EUR/GBP/USD to CAD, e.g. multiply Air_France by Rate and created a new column named Air_France in CAD. Applied to 5 airlines dataframes.
* Combined 6 airlines into a single dataframe(df_monthly) by using `concat` function.
* Used the `plot` function to plot the df_monthly dataframe as a line chart. 
![](https://github.com/Emmalu868/Group-3-Project/blob/main/Airline%20Data/Airline%20Stocks%20Price%20from%202012%20to%202023.png)
### Analysis: 
UK TUI Airways has the highest stock price at all time, peak is over $175 CAD in 2018.
All 6 ariline stocks show a highest price in 2018.
In 2020 there is a sharpe decrease for all stocks.

* Calculated monthly returns by using `pct_change` function and drop null values by using `dropna`.
* Combined 6 airlines returns into a single dataframe(df_monthly_return) by using `concat` function.
* Used the `plot` function to plot the df_monthly_return dataFrame as a line chart.
![](https://github.com/Emmalu868/Group-3-Project/blob/main/Airline%20Data/Airline%20Monthly%20Returns%20from%202012%20to%202023.png)
### Analysis: 
Air Canada has the highest cumulative return for over 40 at the end of 2019, in early 2020 there is a sharp decrease to <20, which is the biggest price drop over the last 10 years.

### Risk Analysis
* Created a box plot for each portfolio
![](https://github.com/Emmalu868/Group-3-Project/blob/main/Airline%20Data/all%20monthly%20return%20box%20plot.png)
### Analysis:
- Air France has the highest return at nearly 0.8 and the lowest return at -0.6, therefore Air France is the most risky airline stocks.
- Japan Airways has the smallest fluctuation among all airline stocks, the return range is from -0.2 to 0.3.

### Import Gasoline and Correlation
* Combined total_pump_price_all and df_monthly by using `concat` function, named the dataframe all_df.
* Used `heatmap` to plot the correlation.
![](https://github.com/Emmalu868/Group-3-Project/blob/main/Airline%20Data/Correlation%20Matrix%20Gasoline%20and%20Airline'.png)
### Analysis on correlation between gasoline price and airline stocks:
- UK and UK Airways has a weak to medium negative linear correlation at -0.3.
- Germany and Germany LHA has a weak to medium negative correlation at -0.26.
- France and Air France has a weak negative correlation at -0.2.
- Japan and Japan airline has a weak to medium negative correlation at -0.17
- Canada and Air Canada has a weak positive correlation at 0.09.
- USA and American Airlines has a medium negative linear correlation at -0.42.



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
    


