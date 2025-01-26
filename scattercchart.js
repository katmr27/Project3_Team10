function loadCSV(family_friendly_df){
  Papa.parse(family_friendly_df, {
    complete: function(result) {
      console.log(result.data);
      createBubbleChart(result.data);
    },
    header: true
  })
}

document.getElementById('csvInput').addEventListener('change', function(e){
  const file = e.target.family_friendly_dfs[0];
  if (family_friendly_df){

  }
});
