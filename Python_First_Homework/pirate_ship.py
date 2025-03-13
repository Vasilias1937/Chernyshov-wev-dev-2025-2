def load_cargo(capacity, cargo_list):
    cargo_list.sort(key=lambda cargo: cargo[2] / cargo[1], reverse=True)

    loaded_cargo = []
    
    for name, weight, value in cargo_list:
        if capacity <= 0:
            break
        if weight <= capacity:
            loaded_cargo.append((name, weight, value))
            capacity -= weight
        else:
           
            loaded_cargo.append((name, capacity, value * (capacity / weight)))
            capacity = 0  

    loaded_cargo.sort(key=lambda x: x[2], reverse=True)
    
    return loaded_cargo

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    cargo_list = []

    for _ in range(m):
        line = input().strip().split()
        name = line[0]
        weight = int(line[1])
        value = int(line[2])
        cargo_list.append((name, weight, value))

    loaded_cargo = load_cargo(n, cargo_list)

    for name, weight, value in loaded_cargo:
        print(f"{name} {weight:.2f} {value:.2f}")
