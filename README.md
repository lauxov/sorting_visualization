# Sort Visualization

This project provides a visualization of four common sorting algorithms: bubble sort, selection sort, insertion sort, and quicksort. The user can choose which algorithm to visualize using a command line argument. The bars on the screen represent elements in an array being sorted. The height of each bar corresponds to the value of the element.

https://youtu.be/BO_GKAWSuog

# Getting Started
To use this project, first clone the repository:
```bash
git clone https://github.com/your-username/sort-visualization.git
```

Then, navigate to the project directory and install the dependencies:
```
cd sort-visualization
pip install -r requirements.txt
```
# Usage
To run the visualization, use the following command:
```python
python tests.py --sort <algorithm>
```
where <algorithm> is one of `bubble, selection, insertion, or quick`. The visualization will begin with a set of randomly generated bars representing an unsorted array. As the sorting algorithm progresses, the bars will move and change color, ultimately resulting in a sorted array.

# Examples
To visualize bubble sort, run the following command:
```python
python sort.py --sort bubble
```
# Selection Sort
To visualize selection sort, run the following command:
```
python sort.py --sort selection
```
# Insertion Sort
To visualize insertion sort, run the following command:
```
python sort.py --sort insertion
```
# Quicksort
To visualize quicksort, run the following command:
```
python sort.py --sort quick
```
# License
This project is licensed under the MIT License - see the LICENSE file for details.
# Acknowledgments
> This project was inspired by this [YouTube video](https://www.youtube.com/watch?v=kPRA0W1kECg).

> The sounds used in this project are from https://mixkit.co/.
