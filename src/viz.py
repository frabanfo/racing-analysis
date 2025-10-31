import matplotlib.pyplot as plt

def plot_speed_distance(telemetry, title="Speed vs Distance"):
    fig, ax = plt.subplots(figsize=(12,4))
    ax.plot(telemetry['Distance'], telemetry['Speed'])
    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Speed (km/h)')
    ax.set_title(title)
    return fig

def plot_throttle_distance(telemetry, title="Throttle vs Distance"):
    fig, ax = plt.subplots(figsize=(12,4))
    ax.plot(telemetry['Distance'], telemetry['Throttle'])
    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Throttle (%)')
    ax.set_title(title)
    return fig

def plot_brakes_distance(telemetry, title="Throttle vs Distance"):
    fig, ax = plt.subplots(figsize=(12,4))
    ax.plot(telemetry['Distance'], telemetry['Brake'])
    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Brakes (%)')
    ax.set_title(title)
    return fig