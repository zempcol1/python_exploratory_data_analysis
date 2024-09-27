
# Exploratory Data Analysis (EDA)

In this GitHub repository, methods of exploratory data analysis (EDA) are explained using a data set with data on rental apartments. The aim is to gain insights into the structure of the data, its distribution and the relationships between the variables. The various EDA techniques used in this notebook are listed below.
---

## Table of Contents

1. [Libraries and Settings](#libraries-and-settings)
2. [Univariate Non-Graphical EDA](#univariate-non-graphical-eda)
   - [Quantiles](#quantiles)
   - [Shape of Data](#shape-of-data)
   - [Data Types](#data-types)
   - [Summary Statistics](#summary-statistics)
3. [Multivariate Graphical EDA](#multivariate-graphical-eda)
   - [Scatterplot](#scatterplot)
   - [Scatterplot with Regression Line](#scatterplot-with-regression-line)
   - [Scatterplot Matrix](#scatterplot-matrix)
   - [Hexagonal Binning Plot](#hexagonal-binning-plot)
   - [Correlation Heatmap](#correlation-heatmap)
   - [Bubble Plot](#bubble-plot)

---

## Libraries and Settings

The following libraries were used in the analysis:

- `pandas` for data manipulation
- `numpy` for numerical operations
- `seaborn` and `matplotlib` for data visualization
- `statsmodels` for statistical models
- `datetime` for handling date and time information

The seaborn theme is customized for improved visualizations.

---

## Univariate Non-Graphical EDA

### Quantiles

Quantiles are used to understand the distribution of the numeric variables in the dataset. For example, you can calculate the 25th, 50th, and 75th percentiles of apartment prices to observe how prices are spread across different quartiles.

### Shape of Data

The shape of the data refers to the number of rows and columns in the dataset, which helps in understanding the dataset's size. For example, if the data has 1000 rows and 12 columns, it indicates that the dataset contains 1000 apartments and 12 attributes related to each apartment.

### Data Types

Knowing the data types (e.g., integer, float, object) of each variable is important as it dictates the type of analysis that can be performed. For example, apartment prices might be stored as float, while location details could be object (string).

### Summary Statistics

Summary statistics provide a quick overview of numeric variables in the dataset, including measures such as mean, standard deviation, minimum, and maximum values. For instance, summary statistics for apartment sizes can reveal average apartment size or the variation in sizes across different apartments.

---

## Multivariate Graphical EDA

### Scatterplot

Scatterplots are used to visualize relationships between two variables. For example, a scatterplot of apartment price vs. size can show whether larger apartments tend to have higher prices.

### Scatterplot with Regression Line

Adding a regression line to a scatterplot can help in understanding the linear relationship between two variables. For example, plotting a regression line on the price vs. size scatterplot might reveal a positive correlation between size and price.

### Scatterplot Matrix

A scatterplot matrix allows for the pairwise comparison of multiple variables in the dataset. This is useful for identifying relationships between several variables at once, such as price, size, and number of rooms.

### Hexagonal Binning Plot

A hexbin plot is useful for visualizing the relationship between two variables when there are many data points. It is similar to a scatterplot but with hexagonal bins to reduce overplotting. For example, it can show the density of apartments in certain price and size ranges.

### Correlation Heatmap

A correlation heatmap is used to visualize the pairwise correlation between variables. Strong correlations are highlighted, which can help in identifying potential relationships. For example, if apartment size and price have a high correlation, the heatmap will reflect this with a strong color.

### Bubble Plot

A bubble plot adds a third variable to a scatterplot by changing the size of the data points. For example, you could visualize apartment price vs. size and use the bubble size to represent the number of rooms.

---

## Conclusion

This notebook provides a comprehensive exploratory data analysis of apartment data, covering both univariate and multivariate techniques. The visualizations and statistical methods help uncover relationships and insights from the dataset.
