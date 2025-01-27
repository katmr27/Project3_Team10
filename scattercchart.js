function loadCSV(all_trails_data_clean_df){
  Papa.parse(all_trails_data_clean_df, {
    complete: function(result) {
      console.log(result.data);
      createBubbleChart(result.data);
    },
    header: true
  })
}

document.getElementById('csvInput').addEventListener('change', function(e){
  const file = e.target.all_trails_data_clean_df[0];
  if (all_trails_data_clean_df){

  }
});
