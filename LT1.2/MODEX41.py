def encontrar_soma_sete():
    for dado1 in range(1, 7):
        for dado2 in range(1, 7):
            if dado1 + dado2 == 7:
                print(f"({dado1}, {dado2})")

def main():
    encontrar_soma_sete()

if __name__ == "__main__":
    main()
