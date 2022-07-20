# Extension Quick Sort Code
# importing time module
import time


def partition(data, head, tail, draw, tick):
	border = head
	pivot = data[tail]

	draw(data, getColorArray(len(data), head, tail, border, border))
	time.sleep(tick)

	for j in range(head, tail):
		if data[j] < pivot:
			draw(data, getColorArray(
				len(data), head, tail, border, j, True))
			time.sleep(tick)

			data[border], data[j] = data[j], data[border]
			border += 1

		draw(data, getColorArray(len(data), head, tail, border, j))
		time.sleep(tick)

	# swapping pivot with border value
	draw(data, getColorArray(len(data), head, tail, border, tail, True))
	time.sleep(tick)

	data[border], data[tail] = data[tail], data[border]

	return border


# head --> Starting index,
# tail --> Ending index
def quick_sort(data, head, tail, draw, tick):
	if head < tail:
		partition_Index = partition(data, head, tail, draw, tick)

		# left partition
		quick_sort(data, head, partition_Index - 1,  draw, tick)

		# right partition
		quick_sort(data, partition_Index + 1, tail, draw, tick)

# Function to apply colors to bars while sorting:
# Grey - Unsorted elements
# Blue - Pivot point element
# White - Sorted half/partition
# Red - Starting pointer
# Yellow - Ending pointer
# Green - after all elements are sorted


def getColorArray(data_Len, head, tail, border, curr_index, isSwaping=False):
	colorArray = []
	for i in range(data_Len):
		# base coloring
		if head <= i <= tail:
			colorArray.append('Grey')
		else:
			colorArray.append('White')

		if i == tail:
			colorArray[i] = 'Blue'
		elif i == border:
			colorArray[i] = 'Red'
		elif i == curr_index:
			colorArray[i] = 'Yellow'

		if isSwaping:
			if i == border or i == curr_index:
				colorArray[i] = 'Green'
	return colorArray
