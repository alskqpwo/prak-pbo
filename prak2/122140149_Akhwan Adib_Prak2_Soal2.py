import random

class RockPaperScissorsGame:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        print("Selamat datang di permainan Batu, Gunting, Kertas!")

    def __del__(self):
        print("Terima kasih telah bermain!")

    def play(self):
        while True:
            print("\nPilih tindakan Anda:")
            print("1. Batu")
            print("2. Gunting")
            print("3. Kertas")
            print("4. Keluar")

            player_choice = input("Masukkan pilihan Anda: ")

            if player_choice == "1":
                player_move = "batu"
            elif player_choice == "2":
                player_move = "gunting"
            elif player_choice == "3":
                player_move = "kertas"
            elif player_choice == "4":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
                continue

            computer_move = random.choice(["batu", "gunting", "kertas"])

            print(f"Anda memilih: {player_move}")
            print(f"Komputer memilih: {computer_move}")

            if player_move == computer_move:
                print("Hasil: Seri!")
            elif (player_move == "batu" and computer_move == "gunting") or \
                 (player_move == "gunting" and computer_move == "kertas") or \
                 (player_move == "kertas" and computer_move == "batu"):
                print("Hasil: Anda menang!")
                self.player_score += 1
            else:
                print("Hasil: Anda kalah!")
                self.computer_score += 1

            print(f"Skor Anda: {self.player_score}, Skor Komputer: {self.computer_score}")


if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.play()
