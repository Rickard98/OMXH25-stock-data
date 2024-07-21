install.packages("pacman")

pacman::p_load(readxl, dplyr, ggplot2)

source("Functions/Functions.R")

# Load data
directory_path <- "Aktie data/"  # Replace this with your directory path
Stock_list <- read_non_empty_excel_files(directory_path)

##chose the Stock you want to analyse

stock_data <- data.frame(Values = Stock_list$NESTE.HE)

# Sorting the data frame in descending order based on 'Values' column
stock_data <- stock_data %>%
  arrange(desc(Values.Date))

# Create a time series plot using ggplot2
plot_time_series(stock_data, "Values.Date", "Values.Close")


