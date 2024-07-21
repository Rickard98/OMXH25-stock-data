

###########################################################
##########Function for loading all data from a chosen map##
###########################################################

read_non_empty_excel_files <- function(directory_path) {
  # Get all file names in the specified directory
  file_names <- list.files(directory_path, full.names = TRUE)
  
  # Create an empty list to store the data
  data_list <- list()
  
  # Loop through each file, read data, and store it in the list
  for (file in file_names) {
    # Attempt to read the file and handle errors if it fails
    tryCatch({
      # Assuming Excel files (xlsx), adjust read function accordingly if it's different
      data <- readxl::read_excel(file)
      
      # Extracting the file name without extension to use as a list element name
      file_name <- tools::file_path_sans_ext(basename(file))
      
      # Store data in the list with a name derived from the file name
      data_list[[file_name]] <- data
    }, error = function(e) {
      # Print the error message if a file couldn't be read
      cat("Error reading file:", file, "\n")
      cat("Error message:", conditionMessage(e), "\n")
    })
  }
  
  # Remove data frames with zero observations (zero rows)
  data_list <- data_list[sapply(data_list, function(x) nrow(x) > 0)]
  
  return(data_list)
}


###########################################################
##########Ploting function#################################
###########################################################

plot_time_series <- function(data, x_var, y_var) {
  ggplot(data, aes_string(x = x_var, y = y_var)) +
    geom_line() +
    labs(x = "Date", y = "Close Values", title = "Time Series Plot of Values.Close")
}

