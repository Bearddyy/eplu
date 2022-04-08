import requests


## Electronic Parts Look Up (EPLU) From the command line

def get_eplu(mpn):
    "Fetch results from Octopart API"
    return ""


if __name__ == "__main__":
    # get arguments from command line
    import argparse
    parser = argparse.ArgumentParser(description='Fetch EPLU data')
    parser.add_argument('mpn', help='MPN to search for')
    args = parser.parse_args()
    mpn = args.mpn
    print(get_eplu(mpn))
