const ctx = document.getElementById("myChart").getContext('2d');

/*
const data = {
  labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
  datasets: [
		{
    label: 'Looping tension',
    data: [65, 59, 80, 81, 26, 55, 40],
    fill: false,
    borderColor: 'rgb(150, 192, 192)',
  	},
		{
    label: 'Looping tension',
    data: [55, 49, 70, 71, 16, 45, 30],
    fill: false,
    borderColor: 'rgb(75, 192, 192)',
  	}
	]
};
*/

const data = {
	datasets: [
		{
			label: 'Scatter 1',
			data:	[{
				x: 10,
				y: 0,
			}],
			backgroundColor: 'rgb(255, 0, 0)'
		},
		{
			label: 'Scatter 2',
			data:	[{
				x: 10,
				y: 20,
			}],
			backgroundColor: 'rgb(255, 255, 255)'
		}
	]
}

const image = new Image();
// image.src = 'https://www.chartjs.org/img/chartjs-logo.svg';
image.src = "data/Isle_beginning_map.webp";

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

/*
const config = {
  type: 'line',
  data: data,
  options: {
    animations: {
      tension: {
        duration: 1000,
        easing: 'easeInQuad',
        from: 1,
        to: 0,
        loop: true
      }
    },
    scales: {
      y: { // defining min and max so hiding the dataset does not change scale range
        min: 0,
        max: 100
      },
			xAxes: [{
            gridLines: {
							color: "rgba(0,0,0,0)",
            }
        }],
        yAxes: [{
            gridLines: {
                display:false,
            }   
        }]
    },
		responsive:false,
  },
	plugins: [plugin],
};
*/

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
