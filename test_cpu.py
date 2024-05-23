import threading

def calculate_sum_single_thread(numbers):
  total_sum = 0
  for num in numbers:
    total_sum += num
  return total_sum

def calculate_sum_multi_thread(numbers):
  threads = []
  chunk_size = len(numbers) // len(threading.activeCount())  # Divide work into chunks
  start = 0

  # Create threads with separate chunks of the list
  for i in range(len(threading.activeCount())):
    end = min(start + chunk_size, len(numbers))
    thread = threading.Thread(target=calculate_sum_chunk, args=(numbers[start:end],))
    threads.append(thread)
    thread.start()
    start = end

  # Wait for all threads to finish
  for thread in threads:
    thread.join()

  # Combine partial sums from each thread
  total_sum = 0
  for thread in threads:
    total_sum += thread.result

  return total_sum

def calculate_sum_chunk(chunk):
  chunk_sum = 0
  for num in chunk:
    chunk_sum += num
  return chunk_sum

# Sample large list of numbers
numbers = list(range(1, 10000001))

# Run both versions and measure execution time
import time

start_time = time.time()
single_thread_result = calculate_sum_single_thread(numbers.copy())
single_thread_time = time.time() - start_time

start_time = time.time()
multi_thread_result = calculate_sum_multi_thread(numbers.copy())
multi_thread_time = time.time() - start_time

# Verify both versions produce the same result
if single_thread_result != multi_thread_result:
  print("Error: Results don't match!")
else:
  print(f"Single Thread Time: {single_thread_time:.2f} seconds")
  print(f"Multi-Thread Time: {multi_thread_time:.2f} seconds")
