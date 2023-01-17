// adapted from https://www.d3-graph-gallery.com/graph/stackedarea_template.html

function activityGraph(options) {
    /*

    Draw a stacked area chart of project activity

    options:
        id:  container element id
        keys: labels for the groups of data in the dataset
        data: data to be graphed
        projects: object with information about projects, including colors
        label: label to display at the top left of the graph
        drawLegend: boolean to indicate if the key legend should be added
    */

    var container = d3.select(options.id);

    var margin = {top: 60, right: 230, bottom: 50, left: 50},
        width = 800 - margin.left - margin.right,
        height = 400 - margin.top - margin.bottom;

    var svg = container.append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform",
              "translate(" + margin.left + "," + margin.top + ")");

      //stack the data
      var stackedData = d3.stack()
        .keys(options.keys)
        (options.data)

      // Add X axis
      var x = d3.scaleTime()
        .domain(d3.extent(options.data, function(d) { return d.date; }))
        .range([ 0, width ]);
      var xAxis = svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x).ticks(5))

      // Add Y axis
      var y = d3.scaleLinear()
        .domain([0, 50]) // get max from data
        .range([ height, 0 ]);
      svg.append("g")
        .call(d3.axisLeft(y).ticks(5))

      // Add Y axis label using text provided:
      svg.append("text")
          .attr("text-anchor", "end")
          .attr("x", 0)
          .attr("y", -20 )
          .text(options.label)
          .attr("text-anchor", "start")


    // Create the scatter variable: where both the circles and the brush take place
      var areaChart = svg.append('g')
        .attr("clip-path", "url(#clip)")

    // Area generator
      var area = d3.area()
        .x(function(d) { return x(d.data.date); })
        .y0(function(d) { return y(d[0]); })
        .y1(function(d) { return y(d[1]); })


      function projectColor(projectName) {
        if (projectName in options.projects) {
          return options.projects[projectName].color;
        }
        // warn about missing color so it can be remedied
        console.log(`No color defined for ${projectName} in projects data file`);
        return 'gray';
      }


      // Show the areas
      areaChart
        .selectAll("mylayers")
        .data(stackedData)
        .enter()
        .append("path")
          .attr("class", function(d) { return "myArea " + d.key })
          .style("fill", function(d) { return projectColor(d.key); })
          .attr("d", area)


      var idleTimeout
      function idled() { idleTimeout = null; }

      // A function that update the chart for given boundaries
      function updateChart() {

        extent = d3.event.selection

        // If no selection, back to initial coordinate. Otherwise, update X axis domain
        if(!extent){
          if (!idleTimeout) return idleTimeout = setTimeout(idled, 350); // This allows to wait a little bit
          x.domain(d3.extent(options.data, function(d) { return d.date; }))
        }else{
          x.domain([ x.invert(extent[0]), x.invert(extent[1]) ])
          areaChart.select(".brush").call(brush.move, null) // This remove the grey brush area as soon as the selection has been done
        }

        // Update axis and area position
        xAxis.transition().duration(1000).call(d3.axisBottom(x).ticks(5))
        areaChart
          .selectAll("path")
          .transition().duration(1000)
          .attr("d", area)
        }

      //////////
      // BRUSHING AND CHART //
      //////////

      // Add a clipPath: everything out of this area won't be drawn.
      var clip = svg.append("defs").append("svg:clipPath")
          .attr("id", "clip")
          .append("svg:rect")
          .attr("width", width )
          .attr("height", height )
          .attr("x", 0)
          .attr("y", 0);

      // Add brushing
      var brush = d3.brushX()                 // Add the brush feature using the d3.brush function
          .extent( [ [0,0], [width,height] ] ) // initialise the brush area: start at 0,0 and finishes at width,height: it means I select the whole graph area
          .on("end", updateChart) // Each time the brush selection changes, trigger the 'updateChart' function


     // Add the brushing
      areaChart
        .append("g")
          .attr("class", "brush")
          .call(brush);

     //////////
    // HIGHLIGHT GROUP //
    //////////

    // What to do when one group is hovered
    var highlight = function(d){
      // reduce opacity of all groups
      d3.selectAll(".myArea").style("opacity", .1)
      // expect the one that is hovered
      d3.selectAll("."+d).style("opacity", 1)
    }

    // And when it is not hovered anymore
    var noHighlight = function(d){
      d3.selectAll(".myArea").style("opacity", 1)
    }

    //////////
    // LEGEND //
    //////////

    // Add one dot in the legend for each name.
    if (options.drawLegend) {

        var size = 20
        svg.selectAll("myrect")
          .data(options.keys)
          .enter()
          .append("rect")
            .attr("x", 600)
            .attr("y", function(d,i){ return 10 + i*(size+5)}) // 100 is where the first dot appears. 25 is the distance between dots
            .attr("width", size)
            .attr("height", size)
            .style("fill", function(d){ return projectColor(d); })
            .on("mouseover", highlight)
            .on("mouseleave", noHighlight);

        // Add one dot in the legend for each name.
        svg.selectAll("mylabels")
          .data(options.keys)
          .enter()
          .append("text")
            .attr("x", 600 + size*1.2)
            .attr("y", function(d,i){ return 10 + i*(size+5) + (size/2)}) // 100 is where the first dot appears. 25 is the distance between dots
            .style("fill", function(d){ return projectColor(d); })
            .text(function(d){ return d})
            .attr("text-anchor", "left")
            .style("alignment-baseline", "middle")
            .on("mouseover", highlight)
            .on("mouseleave", noHighlight);

    }
}
