import psutil
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class CloudPortal:
    def __init__(self):
        # Initialize figure and axes for plotting
        self.fig, self.axes = plt.subplots(2, 1)
        self.fig.suptitle('CPU and Memory Usage Monitor')

        # Prepare lists to store CPU and memory usage data
        self.cpu_usage = []
        self.memory_usage = []

        # Set up plot lines for CPU and memory
        self.cpu_line, = self.axes[0].plot([], [], 'r-', label='CPU Usage (%)')
        self.mem_line, = self.axes[1].plot([], [], 'b-', label='Memory Usage (%)')

        # Configure axes
        for ax in self.axes:
            ax.set_xlim(0, 100)
            ax.set_ylim(0, 100)
            ax.set_xlabel('Time (s)')
            ax.set_ylabel('Usage (%)')
            ax.legend(loc='upper right')

    def update_usage(self):
        # Get current CPU and memory usage
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent

        # Append current usage data to lists
        self.cpu_usage.append(cpu)
        self.memory_usage.append(mem)

        # Maintain a fixed window size for the data
        if len(self.cpu_usage) > 100:
            self.cpu_usage.pop(0)
        if len(self.memory_usage) > 100:
            self.memory_usage.pop(0)

    def animate(self, frame):
        # Update usage data
        self.update_usage()

        # Update plot lines with new data
        self.cpu_line.set_data(range(len(self.cpu_usage)), self.cpu_usage)
        self.mem_line.set_data(range(len(self.memory_usage)), self.memory_usage)

        # Adjust x-axis limit
        for ax in self.axes:
            ax.set_xlim(0, len(self.cpu_usage))

        # Return updated plot lines
        return self.cpu_line, self.mem_line

    def run(self):
        # Start the animation
        ani = FuncAnimation(self.fig, self.animate, blit=False, interval=1000)
        plt.show()

if __name__ == "__main__":
    portal = CloudPortal()
    portal.run()