from pydub import AudioSegment
from pydub.playback import play

def merge_sort(data, first, last):
    if first < last:
        mid = (first + last) // 2
        merge_sort(data, first, mid)
        merge_sort(data, mid + 1, last)
        merge(data, first, mid, last)

def merge(data, first, mid, last):
    # Create temporary arrays 
    left_half = data[first:mid + 1]
    right_half = data[mid + 1:last + 1]

    left_index = 0
    right_index = 0
    merge_index = first

    # Merge back
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            data[merge_index] = left_half[left_index]
            left_index += 1
        else:
            data[merge_index] = right_half[right_index]
            right_index += 1
        merge_index += 1

    # Copy any remaining elements from the left half
    while left_index < len(left_half):
        data[merge_index] = left_half[left_index]
        left_index += 1
        merge_index += 1

    # Copy any remaining elements from the right half
    while right_index < len(right_half):
        data[merge_index] = right_half[right_index]
        right_index += 1
        merge_index += 1

def read_input():
    print("Sharubaa Kirubakaran 100744513 sorter")
    return list(map(int, input("Enter the numbers to be sorted, separated by spaces: ").split()))

# Function to play a sound
def play_sound():
    # for playing wav file
    song = AudioSegment.from_wav("note.wav")
    print('Playing sound using pydub')
    play(song)

# Ask user for input
array = read_input()

# Play sound
play_sound()

# Perform merge sort
merge_sort(array, 0, len(array) - 1)

# Print the sorted array
print("Sorted Array:", array)
