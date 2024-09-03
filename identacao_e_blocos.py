def draw(valor: int) -> None:
    cards_in_hand = 0
    if cards_in_hand <= valor:
        cards_in_hand = valor
        print(f"Carta comprada com sucesso. Cartas na mão: {cards_in_hand}")
        
draw(7)