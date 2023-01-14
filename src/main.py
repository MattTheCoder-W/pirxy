#!/usr/bin/env python3
import pirxy

if __name__ == "__main__":
    filename = __file__.split("/")[-1]
    print(f"[{filename}] started")
    game = pirxy.Game()
    print(f"[{filename}] game object created")
    game.start()
    print(f"[{filename}] end")

