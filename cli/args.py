import argparse

def get_args():
    parser = argparse.ArgumentParser(description="ArguFormer V2 — AI Communication Intelligence Platform")
    parser.add_argument("--input", type=str, required=True, help="Path to debate transcript .txt file")
    parser.add_argument("--output", type=str, required=True, help="Path to output .json or a .csv file")
    parser.add_argument("--model", type=str, default="both",choices=["lr", "transformer", "both", "all"], help="Which model(s) to run")
    parser.add_argument("--lang, type=str,  ")