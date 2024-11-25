"use strict";

document.addEventListener("DOMContentLoaded", function () {
    var brandPrimary = "rgba(51, 179, 90, 1)";

    var BARCHART = document.getElementById("barChart");
    var barChart = new Chart(BARCHART, {
        type: "bar",
        data: {
            labels: ["Python", "Java", "C++", "PHP", "Android", "iOS", "ReactJs"],
            datasets: [
                {
                    label: "Trending Tech",
                    backgroundColor: [
                        "rgb(98 160 220)",
                        "rgb(59 67 132)",
                        "rgb(76 107 185)",
                        "rgb(96 138 179)",
                        "rgb(51 75 100)",
                        "rgb(59 73 135)",
                        "rgb(53 63 124)",
                    ],
                    borderColor: [
                        "rgb(98 160 220)",
                        "rgb(59 67 132)",
                        "rgb(76 107 185)",
                        "rgb(96 138 179)",
                        "rgb(51 75 100)",
                        "rgb(59 73 135)",
                        "rgb(53 63 124)",
                    ],
                    borderWidth: 1,
                    data: [6, 4, 3, 5, 3, 5, 2],
                    barThickness: 10,
                },
            ],
        },
        options: {
            scales: {
                xAxes: [{
                    gridLines: {
                        display: true, // Set to false to hide grid lines
                        color: 'rgba(255, 255, 255, 0.1)', // Customize grid line color
                        lineWidth: 1 // Customize grid line width
                    },
                    ticks: {
                        color: "white",
                    }
                }],
                yAxes: [{
                    gridLines: {
                        display: true, // Set to false to hide grid lines
                        color: 'rgba(255, 255, 255, 0.1)', // Customize grid line color
                        lineWidth: 1 // Customize grid line width
                    },
                    ticks: {
                        color: "white",
                    }
                }]
            },
            plugins: {
                legend: {
                    labels: {
                        color: "white",
                    }
                }
            }
        }
    });
});
