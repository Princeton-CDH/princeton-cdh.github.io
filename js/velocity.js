function drawVelocityChart(options) {
    /*
    options:
        id:  canvas object id
        labels: array of labels
        points: array of point values
        issues: array of issue totals
        velocity: array of velocity

    */

    var design_ctx = document.getElementById(options.id).getContext('2d');
    var designChart = new Chart(design_ctx,
    {
        type: 'bar',
        data: {
            labels: options.labels,
            datasets: [{
                label: 'Story points (tested & accepted)',
                data: options.points,
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            },
            {
                label: 'Issues closed',
                data: options.issues,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            },
            {
                label: 'Rolling velocity',
                data: options.velocity,
                // no fill under the line
                backgroundColor: 'rgba(0, 0, 0, 0.0)',
                borderColor: 'rgba(54, 162, 235, 1)',
                 data: options.velocity,
                // Changes this dataset to become a line
                type: 'line',
                // no curves
                lineTension: 0
            },
            ]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });

}
