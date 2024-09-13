import polars as pl
from rich import print


def main():
    file_path = "transfermarkt/data/clubs.json.gz"  # Replace with your actual file path
    data = pl.read_ndjson(file_path)
    data = data.sort("season", descending=True)
    print(data)

    print(data.to_dict(as_series=False))

    # for row in data:
    #     print(row['season'])
    #     print(row['league'])
    #     for team, id in zip(row['team_name'], row['team_id']):
    #         print(f"{team}: {id}")


if __name__ == "__main__":
    main()
