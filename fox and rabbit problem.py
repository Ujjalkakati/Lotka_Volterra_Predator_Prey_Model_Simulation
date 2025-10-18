import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def lotka_volterra_eqn(y, t, alpha, beta, delta, gamma):
    """
    Lotka-Volterra equations for predator-prey dynamics
    y[0] = prey population (rabbits)
    y[1] = predator population (foxes)
    """
    prey, predator = y
    
    # Prey equation: dprey/dt = α*prey - β*prey*predator
    dprey_dt = alpha * prey - beta * prey * predator
    
    # Predator equation: dpredator/dt = δ*prey*predator - γ*predator
    dpredator_dt = delta * prey * predator - gamma * predator
    
    return [dprey_dt, dpredator_dt]

def simulate_ecosystem(prey_initial=40, predator_initial=9, 
                      prey_growth=0.1, predation_rate=0.02,
                      predator_growth=0.01, predator_death=0.1,
                      duration=200, steps=1000):
    """
    Simulate the predator-prey ecosystem dynamics
    """
    # Time points for simulation
    t = np.linspace(0, duration, steps)
    
    # Initial conditions [prey, predator]
    y0 = [prey_initial, predator_initial]
    
    # Parameters: [prey_growth, predation_rate, predator_growth, predator_death]
    params = (prey_growth, predation_rate, predator_growth, predator_death)
    
    # Solve the differential equations
    solution = odeint(lotka_volterra_eqn, y0, t, args=params)
    
    # Create DataFrame with results
    df = pd.DataFrame({
        'time': t,
        'rabbits': solution[:, 0],
        'foxes': solution[:, 1]
    })
    
    return df

def analyze_ecosystem_dynamics(df):
    """
    Analyze and provide insights about the ecosystem dynamics
    """
    rabbits = df['rabbits'].values
    foxes = df['foxes'].values
    time = df['time'].values
    
    # Find peaks and troughs
    from scipy.signal import find_peaks
    
    rabbit_peaks, _ = find_peaks(rabbits)
    fox_peaks, _ = find_peaks(foxes)
    rabbit_troughs, _ = find_peaks(-rabbits)
    fox_troughs, _ = find_peaks(-foxes)
    
    # Calculate phase relationship
    if len(rabbit_peaks) > 1 and len(fox_peaks) > 1:
        rabbit_period = np.mean(np.diff(time[rabbit_peaks]))
        fox_period = np.mean(np.diff(time[fox_peaks]))
        phase_lag = (time[fox_peaks[0]] - time[rabbit_peaks[0]]) if len(rabbit_peaks) > 0 and len(fox_peaks) > 0 else 0
    else:
        rabbit_period = fox_period = phase_lag = 0
    
    insights = {
        'max_rabbits': np.max(rabbits),
        'min_rabbits': np.min(rabbits),
        'max_foxes': np.max(foxes),
        'min_foxes': np.min(foxes),
        'rabbit_peaks': len(rabbit_peaks),
        'fox_peaks': len(fox_peaks),
        'avg_rabbit_period': rabbit_period,
        'avg_fox_period': fox_period,
        'phase_lag': phase_lag,
        'final_rabbits': rabbits[-1],
        'final_foxes': foxes[-1]
    }
    
    return insights

def create_ecosystem_story(df, insights):
    """
    Create a human-readable story from the simulation data
    """
    print("🌿 FOREST ECOSYSTEM STORY 🌿")
    print("=" * 50)
    
    rabbits = df['rabbits'].values
    foxes = df['foxes'].values
    time = df['time'].values
    
    # Find major events
    rabbit_max_idx = np.argmax(rabbits)
    fox_max_idx = np.argmax(foxes)
    rabbit_min_idx = np.argmin(rabbits)
    fox_min_idx = np.argmin(foxes)
    
    print(f"\n🏞️  The forest began with {int(rabbits[0])} rabbits and {int(foxes[0])} foxes.")
    
    # Rabbit population story
    print(f"\n🐇 RABBIT TALE:")
    print(f"  • Peak population: {int(insights['max_rabbits'])} rabbits at year {int(time[rabbit_max_idx])}")
    print(f"  • Lowest point: {int(insights['min_rabbits'])} rabbits")
    print(f"  • Experienced {insights['rabbit_peaks']} major population cycles")
    
    # Fox population story
    print(f"\n🦊 FOX CHRONICLES:")
    print(f"  • Peak population: {int(insights['max_foxes'])} foxes at year {int(time[fox_max_idx])}")
    print(f"  • Lowest point: {int(insights['min_foxes'])} foxes")
    print(f"  • Experienced {insights['fox_peaks']} major population cycles")
    
    # Ecological insights
    print(f"\n🔬 ECOLOGICAL PATTERNS:")
    if insights['phase_lag'] > 0:
        print(f"  • Fox populations lag {insights['phase_lag']:.1f} years behind rabbits")
    print(f"  • Average cycle length: {insights['avg_rabbit_period']:.1f} years")
    print(f"  • Final balance: {int(insights['final_rabbits'])} rabbits, {int(insights['final_foxes'])} foxes")
    
    # Stability assessment
    rabbit_var = np.std(rabbits) / np.mean(rabbits)
    fox_var = np.std(foxes) / np.mean(foxes)
    
    if rabbit_var < 0.3 and fox_var < 0.3:
        stability = "stable equilibrium"
    elif rabbit_var < 0.5 and fox_var < 0.5:
        stability = "moderate fluctuations"
    else:
        stability = "strong cyclical patterns"
    
    print(f"  • Ecosystem shows {stability}")

def plot_ecosystem_dynamics(df, insights):
    """
    Create comprehensive plots of the ecosystem dynamics
    """
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    time = df['time'].values
    rabbits = df['rabbits'].values
    foxes = df['foxes'].values
    
    # Population over time
    axes[0,0].plot(time, rabbits, 'g-', linewidth=2, label='Rabbits', alpha=0.8)
    axes[0,0].plot(time, foxes, 'r-', linewidth=2, label='Foxes', alpha=0.8)
    axes[0,0].set_xlabel('Time (Years)')
    axes[0,0].set_ylabel('Population')
    axes[0,0].set_title('Population Dynamics: The Eternal Dance')
    axes[0,0].legend()
    axes[0,0].grid(True, alpha=0.3)
    
    # Phase portrait
    axes[0,1].plot(rabbits, foxes, 'b-', alpha=0.7, linewidth=1)
    axes[0,1].plot(rabbits[0], foxes[0], 'go', markersize=8, label='Start')
    axes[0,1].plot(rabbits[-1], foxes[-1], 'ro', markersize=8, label='End')
    axes[0,1].set_xlabel('Rabbit Population')
    axes[0,1].set_ylabel('Fox Population')
    axes[0,1].set_title('Phase Space: Predator-Prey Relationship')
    axes[0,1].legend()
    axes[0,1].grid(True, alpha=0.3)
    
    # Population distributions
    axes[1,0].hist(rabbits, bins=30, alpha=0.7, color='green', label='Rabbits')
    axes[1,0].hist(foxes, bins=30, alpha=0.7, color='red', label='Foxes')
    axes[1,0].set_xlabel('Population')
    axes[1,0].set_ylabel('Frequency')
    axes[1,0].set_title('Population Distributions')
    axes[1,0].legend()
    axes[1,0].grid(True, alpha=0.3)
    
    # Rate of change analysis
    rabbit_change = np.diff(rabbits)
    fox_change = np.diff(foxes)
    
    axes[1,1].scatter(rabbits[:-1], rabbit_change, alpha=0.5, color='green', s=1, label='Rabbit Change')
    axes[1,1].scatter(foxes[:-1], fox_change, alpha=0.5, color='red', s=1, label='Fox Change')
    axes[1,1].axhline(y=0, color='k', linestyle='--', alpha=0.5)
    axes[1,1].set_xlabel('Population')
    axes[1,1].set_ylabel('Population Change Rate')
    axes[1,1].set_title('Population Change vs Population Size')
    axes[1,1].legend()
    axes[1,1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def compare_ecosystem_scenarios():
    """
    Compare different ecosystem scenarios
    """
    scenarios = {
        'Balanced Forest': (40, 9, 0.1, 0.02, 0.01, 0.1),
        'Rabbit Paradise': (100, 5, 0.15, 0.01, 0.005, 0.1),
        'Fox Dominance': (20, 20, 0.08, 0.03, 0.02, 0.08),
        'Fragile Balance': (30, 12, 0.12, 0.025, 0.015, 0.12)
    }
    
    plt.figure(figsize=(15, 10))
    
    for i, (scenario_name, params) in enumerate(scenarios.items(), 1):
        df = simulate_ecosystem(*params)
        
        plt.subplot(2, 2, i)
        plt.plot(df['time'], df['rabbits'], 'g-', label='Rabbits', alpha=0.8)
        plt.plot(df['time'], df['foxes'], 'r-', label='Foxes', alpha=0.8)
        plt.title(f'{scenario_name}\nR:{params[0]}, F:{params[1]}')
        plt.xlabel('Years')
        plt.ylabel('Population')
        plt.legend()
        plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to run the ecosystem simulation
    """
    print("🌳 LOTKA-VOLTERRA ECOSYSTEM SIMULATION 🌳")
    print("Simulating the delicate balance between rabbits and foxes...\n")
    
    # Run main simulation
    df = simulate_ecosystem()
    insights = analyze_ecosystem_dynamics(df)
    
    # Tell the story
    create_ecosystem_story(df, insights)
    
    # Create plots
    plot_ecosystem_dynamics(df, insights)
    
    # Show comparison of different scenarios
    print("\n" + "="*50)
    print("🌍 COMPARING DIFFERENT ECOSYSTEM SCENARIOS")
    print("="*50)
    compare_ecosystem_scenarios()
    
    # Statistical summary
    print("\n📊 STATISTICAL SUMMARY")
    print("="*30)
    print(df[['rabbits', 'foxes']].describe().round(2))
    
    # Correlation analysis
    correlation = np.corrcoef(df['rabbits'], df['foxes'])[0,1]
    print(f"\n📈 Population Correlation: {correlation:.3f}")
    if correlation < 0:
        print("   (Negative correlation: typical predator-prey dynamics)")
    else:
        print("   (Positive correlation: unusual pattern)")

if __name__ == "__main__":
    main()