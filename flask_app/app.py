from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os

# Initialize Flask app
app = Flask(__name__)

# Load the apartment data from CSV
@app.route('/')
def index():
    # Load the CSV file (update the path if needed)
    df = pd.read_csv('/mnt/data/your_csv_file.csv')  # Update with the correct path to your CSV file

    # Calculate KPIs
    mean_price = df['price'].mean()
    mean_area = df['area'].mean()

    # Plot histogram of prices
    plt.figure(figsize=(10,6))
    plt.hist(df['price'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Price Distribution of Apartments')
    plt.xlabel('Price (CHF)')
    plt.ylabel('Number of Apartments')

    # Save histogram to the static folder
    histogram_path = os.path.join('static', 'price_histogram.png')
    plt.savefig(histogram_path)
    plt.close()

    # Convert dataframe to a list of dictionaries
    apartments = df.to_dict(orient='records')

    # Render the index.html template and pass KPI data and histogram
    return render_template('index.html', apartments=apartments, mean_price=mean_price, mean_area=mean_area, histogram_path=histogram_path)

if __name__ == '__main__':
    # Ensure the 'static' directory exists for storing the histogram image
    if not os.path.exists('static'):
        os.makedirs('static')

    # Run the Flask app
    app.run(debug=True, host='0.0.0.0')
