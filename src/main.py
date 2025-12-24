from src.data.load_data import load_raw_data

if __name__ == "__main__":
    df = load_raw_data()
    print(df.shape)
    print(df.columns)