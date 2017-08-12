/**
 * Created by main on 2015/06/14.
 */
create_headline("h1", "summery", "Stock Data Summery");
create_headline("h2", "cat_data", "Category Data");
create_div("cat_data_view");
create_svg();

function create_headline(ap, id, te) {
    d3.select("body")
        .append(ap)
        .attr("id", id)
        .text(te);
}

function create_div(id) {
    d3.select("body")
        .append("div")
        .attr("id", id);
}

function create_svg() {
    var w = 900;
    var h = 1000;
    var dx = 10;
    var dy = 10;
    var x_margin = 1;
    var y_margin = 1;
    var svg = d3.select("#cat_data_view").append("svg")
        .attr("width", w)
        .attr("height", h);

    var i_x = 0;
    d3.json("/data/date.json", function (error, json) {
        for (var i_data = 0; i_data < json.length; i_data++) {
            console.log(json[i_data]);
            d3.json("/data/" + json[i_data] + "_category.json", function (error, data) {
                var data_mean = Object.create(null);
                for (var i = 0; i < d3.keys(data).length; i++) {
                    data_mean[d3.keys(data)[i]] = data[d3.keys(data)[i]].mean;
                }

                var color = d3.scale.linear()
                    .domain([90, 110, 130, 150, 170, 190])
                    .range(["#0a0", "#6c0", "#ee0", "#eb4", "#eb9", "#fff"]);

                for (var i = 0; i < d3.keys(data_mean).length; i++) {
                    var margin = 2;
                    var len = Math.ceil(w / (json.length + margin));
                    svg.append("rect")
                        .attr("x", len * i_x + Math.floor(len / 2) - margin)
                        .attr("y", len * i + Math.floor(len / 2) - margin)
                        .attr("width", len - margin)
                        .attr("height", len - margin)
                        .attr("fill", function () {
                            return color((data_mean[d3.keys(data_mean)[i]] - 1) * 10000 + 100);
                        });
                }
                i_x = i_x + 1;
            });
        }
    });

}
