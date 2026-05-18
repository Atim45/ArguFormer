import argparse

def get_args():
    parser = argparse.ArgumentParser(description="ArguFormer V2 — AI Communication Intelligence Platform")
    parser.add_argument("--input", type=str, default="data/sample_debates.txt", help="Path to debate transcript .txt file")
    parser.add_argument("--output", type=str, default="outputs/results", help="Path to output .json or a .csv file")
    parser.add_argument("--model", type=str, default="both",choices=["lr", "transformer", "both", "all"], help="Which model(s) to run")
    parser.add_argument("--lang", type=str, default="auto", choices=("auto", "en", "hi"), help="Language of the debate (auto-detect, English, Hindi)")
    parser.add_argument("--rag", action="store_true", help="Enable Retrieval-Augmented Generation (RAG) ")
    parser.add_argument("--benchmark", action="store_true", help="Run benchmarking and log latency per module)")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    parser.add_argument("--save-report", action="store_true", help="Save full JSON + CSV report to outputs/")

    return parser.parse_args()