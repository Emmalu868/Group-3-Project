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


## Data Cleanup & Exploration and Data Analysis
### Part 1: Analysis of Historical Gasoline Price
* Used the Pandas `read_csv` function to read the internationalpumppricesall csv file as a DataFrame and converted the dates to a DateTimeIndex. The internationalpumppricesall.csv file contains monthly oil price data from 2012 to 2022 for 6 major countries- UK, Germany, France, Japan, Canada and USA. 
* Detected and removed null values using `dropna` function.
* Removed a duplicate column "Situation fiscale" using `drop` function.
* Renamed columns to reflect the countries in English.
* Created a dataframe that slices the Tax Status for Total price.
* Used the `hvplot` function to plot the total_pump_price_all dataFrame as a line chart.
* Calculated correlation using `corr` function and plotted as heatmap. 
* Created a new dataframe and aggregated the values using `agg` to include only the average price for each country.
* Transposed the dataframe using `T` and renamed columns accordingly.
* Used the Pandas `read_csv` function to read the coordinates csv file as a DataFrame.
* Used the Pandas `concat` function to join the pump_price_df and the coordinates DataFrames.
* Plotted an interactive map displaying average gasoline price for each country using `hvplot.points`. 

#### Analysis:
![](https://github.com/Emmalu868/Group-3-Project/blob/main/Images/average_monthly_pump_price.png)<br>
The above plot displays the change in the monthly average gasoline price across 6 major countries from 2012 to 2022. It can be observed that all the countries follow a similar pattern except for Japan which is further analysed below. There is a sharp decrease in the average price from mid 2014 to early 2015. This due to an oversupply of petroleum on the world market which accelerated the drop in overall prices. There is also a drop in the average price in the early 2020 due to covid-19 pandemic. As the novel coronavirus continued to spread around the world, several countries imposed strict quarantine measures and travel restrictions, causing a drop in the demand for gasoline. Morevover, it can be observed that the price continues to go up from late 2020 reaching decade's highest in mid 2022 with major contributing factors being economic recovery after pandemic and Russia-Ukraine war.

![](https://github.com/Emmalu868/Group-3-Project/blob/main/Images/gasoline_price_correlation.png)<br>
From the above heatmap, it is observed that USA, Canada, UK, Germany and France have a strong positive correlation with each other, whereas Japan has a weak positive correlation. 
 
![](https://github.com/Emmalu868/Group-3-Project/blob/main/Images/pump_price_geoview.png)<br>
From the above plot, it is seen that among the countries analysed, USA has the lowest average gasoline price followed by Canada. Countries in Europe and the UK have the highest average price.

### Part 2: Examining the tax status of each country to identifying factors that impact the prices. Descriptive statistics of each country to identify trends, patterns, and anomalies. Visualization of gasoline prices
* Used Pandas `read_csv` function and Path module to read gasoline prices of all six countries, created international_gasoline_prices DataFrame and converted the dates to a DateTimeIndex for all dataframes.
* Slicing the data by Tax Status: base price of gasoline price, tax and total price of the gasoline.
* Three separate data frames are created according to tax status 'base_prices', 'tax_prices', 'total_prices'
* Measured average Gasoline prices by tax status.
![](https://github.com/Emmalu868/Group-3-Project/blob/hdkatta1-ReadMe-final/tax%20status.PNG)<br>



* Descriptive Analysis to understand the data deeper.
* Calculating Mean, Median, Maximum, Minimum, Variance and Standard Deviation. 
* ![](https://github.com/Emmalu868/Group-3-Project/blob/hdkatta1-ReadMe-final/des%20stats.PNG)<br>


* Trend Analysis of gasoline prices Before And After the Pandemic 
*  Creating two separate dataframes of the data 'before_2020_df' and 'after_2020_df'
![Trend Analysis](https://github.com/Emmalu868/Group-3-Project/blob/hdkatta1-patch-4/Trend%20Analysis.ipynb)

![Before_2020_df](https://github.com/Emmalu868/Group-3-Project/blob/hdkatta1-ReadMe-final/before%202020.PNG)<br>
![After_2020_df](https://github.com/Emmalu868/Group-3-Project/blob/hdkatta1-ReadMe-final/after%202020.PNG)<br>
Visulaize the trend of gasoline prices before and after the pandemic.
![Analysis of dataframes before and after 2020](https://github.com/Emmalu868/Group-3-Project/blob/hdkatta1-ReadMe-final/box.PNG)<br>
![Price Range](https://github.com/Emmalu868/Group-3-Project/blob/hdkatta1-ReadMe-final/pr.PNG)<br>
![Price Range Difference](https://github.com/Emmalu868/Group-3-Project/blob/hdkatta1-ReadMe-final/ga.PNG)<br>
![Correlaion](https://github.com/Emmalu868/Group-3-Project/blob/hdkatta1-ReadMe-final/correlation%20graph%20before%20and%20after%20pandemic.PNG)<br>
![Growth rate Of UK](https://github.com/Emmalu868/Group-3-Project/blob/hdkatta1-ReadMe-final/growth%20rate%20of%20UK%20through%20before%20and%20after%20pandemic.PNG)<br>
![Canada](https://github.com/Emmalu868/Group-3-Project/blob/hdkatta1-ReadMe-final/growth%20rate%20of%20canada%20before%20and%20after%20pandemic.PNG)<br>
![France](https://github.com/Emmalu868/Group-3-Project/blob/hdkatta1-ReadMe-final/growth%20rate%20of%20france%20before%20and%20after%20pandemic.PNG)<br>
![japan](https://github.com/Emmalu868/Group-3-Project/blob/hdkatta1-ReadMe-final/growth%20rate%20of%20japan%20before%20and%20after%20pandemic.PNG)<br>
![USA](https://github.com/Emmalu868/Group-3-Project/blob/hdkatta1-ReadMe-final/growth%20rate%20of%20usa%20before%20and%20after%20pandemic.PNG)<br>
![USA](https://github.com/Emmalu868/Group-3-Project/blob/hdkatta1-ReadMe-final/Growth%20rate%20germany%20before%20and%20after%20pandemic.PNG)<br>

### Part 3: Examining the Relationship Between Oil Price and Stocks
* Used Pandas `read_csv` function and Path module to read all 6 airline stocks, created 6 DataFrame and converted the dates to a DateTimeIndex for all dataframes.
* Renamed close column to the airline names and dropped other columns in the 6 airline dataframes.
* Detected and removed null values using `dropna` function.
* Used `try` and `except` inside a function and `get_rate` function to get rate for historical data, created a new column named Rate.
* Converted EUR/GBP/USD to CAD, e.g. multiply Air_France by Rate and created a new column named Air_France in CAD. Applied to 5 airlines dataframes.
* Combined 6 airlines into a single dataframe(df_monthly) by using `concat` function.
* Used the `plot` function to plot the df_monthly dataframe as a line chart. 
![](https://github.com/Emmalu868/Group-3-Project/blob/main/Airline%20Data/Airline%20Stocks%20Price%20from%202012%20to%202023.png)
#### Analysis: 
UK TUI Airways has the highest stock price at all time, peak is over $175 CAD in 2018.
All 6 ariline stocks show a highest price in 2018.
In 2020 there is a sharpe decrease for all stocks.

* Calculated monthly returns by using `pct_change` function and drop null values by using `dropna`.
* Combined 6 airlines returns into a single dataframe(df_monthly_return) by using `concat` function.
* Used the `plot` function to plot the df_monthly_return dataFrame as a line chart.
![](https://github.com/Emmalu868/Group-3-Project/blob/main/Airline%20Data/Airline%20Monthly%20Returns%20from%202012%20to%202023.png)
#### Analysis: 
Air France has the highest return in 2020 at nearly 0.8, and the lowest return in 2022 at about -0.6.

* Plotted cumulative returns by using `cumprod` function and `plot`
![](https://github.com/Emmalu868/Group-3-Project/blob/main/Airline%20Data/Cumulative%20Monthly%20Returns%20on%20Airlines%20from%202012%20to%202023.png)
#### Analysis: 
Air Canada has the highest cumulative return for over 40 at the end of 2019, in early 2020 there is a sharp decrease to <20, which is the biggest price drop over the last 10 years.

#### Risk Analysis
* Created a box plot for each portfolio
![](https://github.com/Emmalu868/Group-3-Project/blob/main/Airline%20Data/all%20monthly%20return%20box%20plot.png)
#### Analysis:
- Air France has the highest return at nearly 0.8 and the lowest return at -0.6, therefore Air France is the most risky airline stocks.
- Japan Airways has the smallest fluctuation among all airline stocks, the return range is from -0.2 to 0.3.

#### Import Gasoline and Correlation
* Combined total_pump_price_all and df_monthly by using `concat` function, named the dataframe all_df.
* Used `heatmap` to plot the correlation.
![](https://github.com/Emmalu868/Group-3-Project/blob/main/Airline%20Data/Correlation%20Matrix%20Gasoline%20and%20Airline'.png)
#### Analysis on correlation between gasoline price and airline stocks:
- UK and UK Airways has a weak to medium negative linear correlation at -0.3.
- Germany and Germany LHA has a weak to medium negative correlation at -0.26.
- France and Air France has a weak negative correlation at -0.2.
- Japan and Japan airline has a weak to medium negative correlation at -0.17
- Canada and Air Canada has a weak positive correlation at 0.09.
- USA and American Airlines has a medium negative linear correlation at -0.42.



## Conclusion
In conclusion, we see a negative correlation between gasoline prices and airline stocks. This may be because higher gasoline prices increase the cost of operating airlines, which can decrease their profits and overall value. Alternatively, when gasoline prices are low, airlines may have lower operating costs and higher profits, which can increase the value of their stocks.

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
    


