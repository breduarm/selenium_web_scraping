from log import Log
import threading

class ThreadHandler:
    
    def __init__(self, threads_name, functions) -> None:
        self.threads_name: list[str] = threads_name
        self.threads = list()
        self.__init_threads__(functions)

    def __init_threads__(self, functions) -> None:
        for thread_index, thread_name in enumerate(self.threads_name):
            thread = threading.Thread(name=thread_name.format(thread_index), target=functions[thread_index])
            self.threads.append(thread)

    def start_threads(self) -> None:
        # Start threads
        for thread in self.threads:
            thread.start()
            Log.i(f"{thread.name} STARTED!")
        
        # Wait for all threads to complete
        for thread in self.threads:
            thread.join()

        Log.i("All threads have been completed")