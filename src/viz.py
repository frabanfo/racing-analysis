import matplotlib.pyplot as plt

def plot_speed_distance(telemetry, title="Speed vs Distance"):
    fig, ax = plt.subplots(figsize=(12,4))
    ax.plot(telemetry['Distance'], telemetry['Speed'])
    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Speed (km/h)')
    ax.set_title(title)
    return fig
