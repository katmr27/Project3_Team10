function loadCSV(file){
  Papa.parse(file, {
    complete: function(result) {
      console.log(result.data);
      createBubbleChart(result.data); 
    },
    header: true
  })
}

document.getElementById('csvInput').addEventListener('change', function(e){
  const file = e.target.files[0];
  if (!file) {
    alert("No file chosen!");  // Show a message if no file was selected
  } else {
    console.log(file);  // Log the file object to check if it's correctly selected
    loadCSV(file);  // If a file is selected, parse and load it
  }
});

function createBubbleChart(data){
  // Prepare data for Plotly (scatter chart)
  var trace1 = {
    x: data.map(row => parseFloat(row.elevation)),  
    y: data.map(row => parseFloat(row.distance)),  
    mode: 'markers',  
    type: 'scatter',
    text: data.map(row => row.trail_name),  
    hoverinfo: 'text', 
    marker: {
      color: data.map(row => parseFloat(row.elevation)),  
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

  // Use Plotly to create the chart inside the div with id "scatter-plot"
  Plotly.newPlot('scatter-plot', [trace1], layout);
}