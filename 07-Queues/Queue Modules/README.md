# Queue Modules in Python

This directory explores three different ways to implement or use Queues in Python using built-in and standard library modules.

## 1. collections.deque
The `Deque.py` module demonstrates how to use `collections.deque` as a First-In-First-Out (FIFO) queue.
- **Usage**: `from collections import deque`
- **Key Features**:
  - `maxlen`: Automatically limits the size of the queue. If it's full and a new item is added, the oldest item is removed from the opposite end.
  - Efficient append and pop operations from both ends.
- **Ideal for**: Simple, fast FIFO queues where thread safety isn't the primary concern but performance is.

## 2. queue.Queue
The `QueueModule.py` demonstrates the standard `queue` module.
- **Usage**: `import queue`
- **Key Features**:
  - `maxsize`: Limits the number of items that can be placed in the queue.
  - `put()` and `get()`: Standard methods for adding and removing items.
  - `full()` and `empty()`: Check the status of the queue.
- **Ideal for**: Multi-threaded programming. This module is designed to be thread-safe, allowing multiple threads to interact with the same queue without explicit locking.

## 3. multiprocessing.Queue
The `MultiprocessingQueue.py` shows how to use queues across different processes.
- **Usage**: `from multiprocessing import Queue`
- **Key Features**:
  - Similar API to the `queue.Queue` module.
  - Designed for Inter-Process Communication (IPC).
- **Ideal for**: Parallel processing where data needs to be shared or passed between separate processes rather than just threads.

---

### Comparison Table

| Module | Thread-Safe | Process-Safe | Best For |
| :--- | :---: | :---: | :--- |
| `collections.deque` | No* | No | General purpose, performance |
| `queue.Queue` | Yes | No | Multi-threading |
| `multiprocessing.Queue` | Yes | Yes | Parallel processing / IPC |

*\*Note: `append` and `pop` operations in `deque` are atomic and thread-safe in CPython, but the class as a whole is not designed for complex multi-threaded synchronization like the `queue` module.*
