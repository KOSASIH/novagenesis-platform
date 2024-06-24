import * as d3 from 'd3-array';
import * as d3Scale from 'd3-scale';
import * as d3Axis from 'd3-axis';

class AnalyticsDashboard {
    constructor(container, data) {
        this.container = container;
        this.data = data;
        this.margin = { top: 20, right: 20, bottom: 30, left: 40 };
        this.width = 500 - this.margin.left - this.margin.right;
        this.height = 300 - this.margin.top - this.margin.bottom;

        this.svg = d3.select(this.container)
           .append('svg')
           .attr('width', this.width + this.margin.left + this.margin.right)
           .attr('height', this.height + this.margin.top + this.margin.bottom)
           .append('g')
           .attr('transform', `translate(${this.margin.left}, ${this.margin.top})`);

        this.xScale = d3Scale.scaleTime()
           .domain([new Date('2022-01-01'), new Date('2022-12-31')])
           .range([0, this.width]);

        this.yScale = d3Scale.scaleLinear()
           .domain([0, 100])
           .range([this.height, 0]);

        this.line = d3.line()
           .x((d) => this.xScale(d.date))
           .y((d) => this.yScale(d.value));

        this.svg.append('path')
           .datum(this.data)
           .attr('class', 'line')
           .attr('d', this.line);

        this.svg.append('g')
           .attr('class', 'axis axis--x')
           .attr('transform', `translate(0, ${this.height})`)
           .call(d3Axis.axisBottom(this.xScale));

        this.svg.append('g')
           .attr('class', 'axis axis--y')
           .call(d3Axis.axisLeft(this.yScale));
    }
}
