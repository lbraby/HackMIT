const ctx = document.getElementById("myChart").getContext('2d');

const data = {
	datasets: [
		{
			data:	[{
				x: 10,
				y: 0,
			}],
			backgroundColor: 'rgb(255, 0, 0)'
		},
		{
			data:	[{
				x: 10,
				y: 20,
			}],
			backgroundColor: 'rgb(255, 255, 255)'
		}
	]
}

const image = new Image();
image.src = 'https://www.chartjs.org/img/chartjs-logo.svg';
image.src = "data/isle.webp";

const plugin = {
  id: 'custom_canvas_background_image',
  beforeDraw: (chart) => {
    if (image.complete) {
      const ctx = chart.ctx;
      const {top, left, width, height} = chart.chartArea;
      const x = left + width / 2 - image.width / 2;
      const y = top + height / 2 - image.height / 2;
      ctx.drawImage(image, x, y);
    } else {
      image.onload = () => chart.draw();
    }
  }
};

const config = {
	type: 'scatter',
	data: data,
	options: {
		responsive:false,
		scales: {
			y: {
				min:0,
				max:100,
				// grid:true
			},
			x: {
				min:0,
				max:100,
				// grid:true
			}
		}	
	},
	plugins: [plugin],
};

const Chart = require('chart.js');
Chart.defaults.plugins.legend.display = false;
const myChart = new Chart(ctx, config);

deleteData = (chart, ind) => {
	chart.data.datasets[ind].data.pop();
	chart.update();
}

addData = () => {
	var nextData = [ {x: 30, y: 30}, {x: 50, y: 50} ];
	chart = myChart;
	
	for (let i = 0; i < nextData.length; i++) {
		deleteData( chart, i );
		chart.data.datasets[i].data.push( nextData[i] );
	}
	chart.update();
}

const button = document.getElementById("myButton");
button.addEventListener('click',addData);
