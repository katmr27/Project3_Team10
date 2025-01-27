fetch('resources/cleaned_data/all_trails_data_clean_df.csv')
  .then(response => response.text())
  .then(csv => Papa.parse(csv, {
    header: true,
    complete: function(result) {
      createBubbleChart(result.data);
    }
  }));
// Changed the code above this line to get the relative path of the csv file 

function createBubbleChart(data) {
  var trace1 = {
      x: data.map(row => parseFloat(row['elevation_gain(feet)'])),  
      y: data.map(row => parseFloat(row['distance(miles)'])),  
      mode: 'markers',  
      type: 'scatter',
      text: data.map(row => row.trail_name),  
      hoverinfo: 'text', 
      marker: {
          color: data.map(row => parseFloat(row['elevation_gain(feet)'])),  
          colorscale: 'Viridis',  
          size: 6,  
          colorbar: {  
              title: 'Elevation',
          },
          cmin: 10, 
          cmax: 2000   
      }
  };

  var layout = {
      title: 'Hikes Elevations vs Distance',
      xaxis: {
          title: "Elevation",
          range: [0,2000]  
      },
      yaxis: {
          title: 'Distance',
          range: [0, 17] 
      }
  };

  Plotly.newPlot('scatter-plot', [trace1], layout);
}